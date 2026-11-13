# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Crash correctness, fallback, and error parity tests for the accelerator."""

import concurrent.futures
import functools
import uuid

import pytest
from google.api_core import exceptions as core_exceptions

from google.cloud.bigtable.data._cross_sync import CrossSync
from google.cloud.bigtable.data.mutations import AddToCell, SetCell

from . import _harness

if CrossSync.is_async:
    from ._base_async import AcceleratorTestBaseAsync as AcceleratorTestBase
else:
    from ._base_autogen import AcceleratorTestBase

__CROSS_SYNC_OUTPUT__ = "tests.system.data.accelerator.test_error_handling_autogen"


@CrossSync.convert_class(sync_name="TestErrorHandling")
class TestErrorHandlingAsync(AcceleratorTestBase):
    CRASH_WORKERS = 8
    OPS_PER_CRASH_WORKER = 40

    @CrossSync.convert
    async def _crash_worker(self, table, worker_id, kill_at_op):
        prefix = f"crash-w{worker_id}-{uuid.uuid4().hex[:8]}-".encode()
        ops = _harness.RandomOps(
            100 + worker_id, key_prefix=prefix, include_aggregate=False
        )
        expected_state = _harness.ExpectedState()
        touched = set()
        for i in range(self.OPS_PER_CRASH_WORKER):
            if i == kill_at_op:
                _harness.force_kill_daemon(table._accelerator_daemon)
            key, mutation = ops.build_mutation(expected_state)
            await table.mutate_row(key, mutation, operation_timeout=30)
            touched.add(key)
            if i % 4 == 3:
                row = await table.read_row(key, operation_timeout=30)
                _harness.assert_rows_equivalent(
                    f"crash-worker-{worker_id}-op-{i}",
                    _harness.normalize_row(row),
                    "model",
                    expected_state.expected_cells(key),
                )
        return sorted(touched), expected_state

    @CrossSync.pytest
    async def test_daemon_killed_during_active_idempotent_workload_preserves_correctness(
        self, instance_id, table_id, native_table, janitor
    ):
        """Killing the Go daemon mid-flight under concurrent idempotent load must
        trip the breaker, fall back to native without failing any call, and keep
        all rows identical to ExpectedState and native reads."""
        async with self._make_client(use_accelerator=True) as client:
            async with client.get_table(instance_id, table_id) as table:
                self.assert_accelerator_active(table)
                assert not table._accelerator_breaker.bypass()

                executor = (
                    concurrent.futures.ThreadPoolExecutor(
                        max_workers=self.CRASH_WORKERS
                    )
                    if not CrossSync.is_async
                    else None
                )
                try:
                    partials = [
                        functools.partial(
                            self._crash_worker,
                            table,
                            w,
                            self.OPS_PER_CRASH_WORKER // 3 if w == 0 else -1,
                        )
                        for w in range(self.CRASH_WORKERS)
                    ]
                    results = await CrossSync.gather_partials(
                        partials, return_exceptions=True, sync_executor=executor
                    )
                finally:
                    if executor is not None:
                        executor.shutdown(wait=True)

                assert not table._accelerator_daemon.is_running
                assert table._accelerator_breaker.bypass()
                assert table._use_accelerator("read_row") is False
                assert table._use_accelerator("mutate_row") is False

                for w, res in enumerate(results):
                    assert not isinstance(res, BaseException), (
                        f"worker {w} failed during mid-flight daemon crash: {res!r}"
                    )
                    keys, expected_state = res
                    for key in keys:
                        janitor.track(key)
                        accel_row = await table.read_row(key)
                        native_row = await native_table.read_row(key)
                        expected = expected_state.expected_cells(key)
                        _harness.assert_rows_equivalent(
                            "fallback-table",
                            _harness.normalize_row(accel_row),
                            "expected",
                            expected,
                        )
                        _harness.assert_rows_equivalent(
                            "native-table",
                            _harness.normalize_row(native_row),
                            "expected",
                            expected,
                        )

    @CrossSync.pytest
    async def test_non_idempotent_mutate_row_on_daemon_crash_does_not_double_apply(
        self, instance_id, table_id, native_table, janitor
    ):
        """When the daemon crashes on a non-idempotent AddToCell or server-timestamp
        SetCell, the call must raise rather than retrying on native, trip the
        breaker, and route subsequent increments through native with exact totals."""
        agg_key = janitor.track(f"crash-agg-{uuid.uuid4().hex}".encode())
        srv_key = janitor.track(f"crash-srv-{uuid.uuid4().hex}".encode())
        ts = 1000 * _harness.MS
        expected_state = _harness.ExpectedState()

        async with self._make_client(use_accelerator=True) as client:
            async with client.get_table(instance_id, table_id) as table:
                self.assert_accelerator_active(table)

                # 1. Apply an initial increment (+10) through the live accelerator.
                await table.mutate_row(
                    agg_key, expected_state.add_to_cell(agg_key, b"counter", 10, ts)
                )
                row = await table.read_row(agg_key)
                _harness.assert_rows_equivalent(
                    "initial-agg",
                    _harness.normalize_row(row),
                    "expected",
                    expected_state.expected_cells(agg_key),
                )

                # 2. Kill the daemon before a non-idempotent AddToCell (+100).
                # It must raise and trip the breaker rather than falling back to
                # native (which on a true mid-flight crash could double-increment).
                _harness.force_kill_daemon(table._accelerator_daemon)
                assert not table._accelerator_daemon.is_running

                with pytest.raises(core_exceptions.GoogleAPICallError):
                    await table.mutate_row(
                        agg_key,
                        AddToCell(
                            _harness.TEST_AGGREGATE_FAMILY,
                            b"counter",
                            100,
                            timestamp_micros=ts,
                        ),
                    )
                assert table._accelerator_breaker.is_tripped
                assert table._use_accelerator("mutate_row") is False

                # 3. Subsequent AddToCell (+25) routes directly to native and
                # produces the exact expected total (10 + 25 = 35, never 135).
                await table.mutate_row(
                    agg_key, expected_state.add_to_cell(agg_key, b"counter", 25, ts)
                )
                final_row = await native_table.read_row(agg_key)
                _harness.assert_rows_equivalent(
                    "final-agg",
                    _harness.normalize_row(final_row),
                    "expected",
                    expected_state.expected_cells(agg_key),
                )

        # Also verify server-assigned timestamp SetCell (timestamp_micros=-1)
        # raises on daemon death rather than falling back.
        async with self._make_client(use_accelerator=True) as client2:
            async with client2.get_table(instance_id, table_id) as table2:
                self.assert_accelerator_active(table2)
                _harness.force_kill_daemon(table2._accelerator_daemon)
                with pytest.raises(core_exceptions.GoogleAPICallError):
                    await table2.mutate_row(
                        srv_key,
                        SetCell(
                            _harness.TEST_FAMILY,
                            b"q",
                            b"server-ts",
                            timestamp_micros=-1,
                        ),
                    )
                assert table2._accelerator_breaker.is_tripped
                assert (await native_table.read_row(srv_key)) is None

    @CrossSync.pytest
    async def test_shared_daemon_crash_falls_back_across_all_client_tables(
        self, instance_id, table_id, native_table, janitor
    ):
        async with self._make_client(use_accelerator=True) as client:
            async with (
                client.get_table(instance_id, table_id) as table_a,
                client.get_table(instance_id, table_id) as table_b,
            ):
                self.assert_accelerator_active(table_a)
                self.assert_accelerator_active(table_b)
                key_a = janitor.track(f"multi-a-{uuid.uuid4().hex}".encode())
                key_b = janitor.track(f"multi-b-{uuid.uuid4().hex}".encode())
                ts = 1000 * _harness.MS

                await table_a.mutate_row(
                    key_a,
                    SetCell(_harness.TEST_FAMILY, b"q", b"a1", timestamp_micros=ts),
                )
                _harness.force_kill_daemon(client._accelerator_daemon)

                # First call on table_a trips the shared client breaker and falls back;
                # table_b immediately sees the tripped breaker and also uses native.
                row_a = await table_a.read_row(key_a, operation_timeout=30)
                assert row_a is not None and row_a.cells[0].value == b"a1"
                assert table_a._use_accelerator("read_row") is False
                assert table_b._use_accelerator("mutate_row") is False

                await table_b.mutate_row(
                    key_b,
                    SetCell(_harness.TEST_FAMILY, b"q", b"b1", timestamp_micros=ts),
                )
                row_b = await native_table.read_row(key_b)
                assert row_b is not None and row_b.cells[0].value == b"b1"

    @CrossSync.pytest
    async def test_operation_timeout_enforced_as_deadline(
        self, accel_table, native_table
    ):
        key = f"errtest-{uuid.uuid4().hex}".encode()
        with pytest.raises(core_exceptions.DeadlineExceeded):
            await accel_table.read_row(key, operation_timeout=0.001)
        with pytest.raises(core_exceptions.DeadlineExceeded):
            await native_table.read_row(key, operation_timeout=0.001)
        assert not accel_table._accelerator_breaker.bypass()
        assert accel_table._accelerator_client is not None

    @CrossSync.pytest
    async def test_backend_error_type_matches_native(self, accel_table, native_table):
        key = f"errtest-{uuid.uuid4().hex}".encode()
        bad = SetCell("no-such-family", b"q", b"v", timestamp_micros=1000 * _harness.MS)
        with pytest.raises(Exception) as accel_ei:
            await accel_table.mutate_row(key, bad)
        with pytest.raises(Exception) as native_ei:
            await native_table.mutate_row(key, bad)
        assert type(accel_ei.value) is type(native_ei.value)
