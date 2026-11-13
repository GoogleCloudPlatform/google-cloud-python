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

import multiprocessing
import os
import queue
import shutil
import signal
import time
import uuid

from google.cloud.bigtable.data._accelerator import _daemon
from google.cloud.bigtable.data._cross_sync import CrossSync
from google.cloud.bigtable.data.mutations import DeleteAllFromRow, SetCell

from . import _harness

if CrossSync.is_async:
    from ._base_async import AcceleratorTestBaseAsync as AcceleratorTestBase
else:
    from ._base_autogen import AcceleratorTestBase

__CROSS_SYNC_OUTPUT__ = "tests.system.data.accelerator.test_lifecycle_autogen"


def _daemon_owner_process(project, instance_id, table_id, app_profile_id, result_queue):
    from google.cloud.bigtable.data import BigtableDataClient

    override = os.environ.get(_harness.BIN_ENV_VAR)
    if override:
        _daemon._resolve_binary_path = lambda: override
    with BigtableDataClient(project=project, use_accelerator=True) as client:
        table_kwargs = {"app_profile_id": app_profile_id} if app_profile_id else {}
        with client.get_table(instance_id, table_id, **table_kwargs) as table:
            key = f"crash-{uuid.uuid4().hex}".encode()
            ts = 1000 * _harness.MS
            table.mutate_row(
                key, SetCell(_harness.TEST_FAMILY, b"q", b"v", timestamp_micros=ts)
            )
            table.mutate_row(key, DeleteAllFromRow())
            result_queue.put(
                (_harness.daemon_pid(table), table._accelerator_daemon._tempdir)
            )
            while True:
                time.sleep(3600)


@CrossSync.convert_class(sync_name="TestLifecycle")
class TestLifecycleAsync(AcceleratorTestBase):
    @CrossSync.convert
    async def _one_lifecycle(self, instance_id, table_id):
        async with self._make_client(use_accelerator=True) as client:
            async with client.get_table(instance_id, table_id) as table:
                self.assert_accelerator_active(table)
                key = f"life-{uuid.uuid4().hex}".encode()
                await table.mutate_row(
                    key,
                    SetCell(
                        _harness.TEST_FAMILY,
                        b"q",
                        b"v",
                        timestamp_micros=1000 * _harness.MS,
                    ),
                )
                assert (await table.read_row(key)) is not None
                await table.mutate_row(key, DeleteAllFromRow())

    @CrossSync.pytest
    async def test_close_reaps_daemon_and_tempdir(self, instance_id, table_id):
        async with self._make_client(use_accelerator=True) as client:
            async with client.get_table(instance_id, table_id) as table:
                self.assert_accelerator_active(table)
                pid = _harness.daemon_pid(table)
                tempdir = table._accelerator_daemon._tempdir
                assert pid is not None and _harness.pid_alive(pid)
                assert tempdir is not None and os.path.exists(tempdir)
        assert not _harness.pid_alive(pid), "daemon still alive after client close"
        assert not os.path.exists(tempdir), "UDS tempdir not cleaned up"

    @CrossSync.pytest
    async def test_no_leaks_over_repeated_lifecycles(self, instance_id, table_id):
        introspector = _harness.ProcessIntrospector()
        await self._one_lifecycle(instance_id, table_id)
        before = introspector.snapshot()
        for _ in range(8):
            await self._one_lifecycle(instance_id, table_id)
        introspector.assert_no_leaks(before, label="8x accelerator lifecycle")

    @CrossSync.pytest
    async def test_close_reclaims_resources_after_daemon_crash(
        self, instance_id, table_id
    ):
        introspector = _harness.ProcessIntrospector()
        before = introspector.snapshot()
        async with self._make_client(use_accelerator=True) as client:
            async with client.get_table(instance_id, table_id) as table:
                self.assert_accelerator_active(table)
                pid = _harness.daemon_pid(table)
                tempdir = table._accelerator_daemon._tempdir
                assert pid is not None and _harness.pid_alive(pid)
                assert tempdir is not None and os.path.exists(tempdir)
                os.kill(pid, signal.SIGKILL)
                deadline = time.monotonic() + 10.0
                while _harness.pid_alive(pid) and time.monotonic() < deadline:
                    time.sleep(0.05)
                assert not _harness.pid_alive(pid), "daemon did not die after SIGKILL"
        assert not os.path.exists(tempdir), "client.close() did not reclaim tempdir"
        introspector.assert_no_leaks(before, label="daemon-crash teardown")

    @CrossSync.pytest
    async def test_no_daemon_leak_when_owner_process_is_killed(
        self, instance_id, table_id
    ):
        project = self._project_id()
        app_profile_id = os.getenv("BIGTABLE_TEST_APP_PROFILE") or os.getenv(
            "CBT_APP_PROFILE_ID"
        )
        ctx = multiprocessing.get_context("spawn")
        result_queue = ctx.Queue()
        owner = ctx.Process(
            target=_daemon_owner_process,
            args=(project, instance_id, table_id, app_profile_id, result_queue),
        )
        owner.start()
        daemon_pid = tempdir = None
        try:
            deadline = time.monotonic() + 60.0
            while time.monotonic() < deadline:
                try:
                    daemon_pid, tempdir = result_queue.get(timeout=0.2)
                    break
                except queue.Empty:
                    assert owner.is_alive(), "owner exited before starting daemon"
            assert daemon_pid is not None, "accelerator fell back to native"
            assert _harness.pid_alive(daemon_pid), "daemon not alive after owner start"
            owner.kill()
            owner.join(timeout=10)
            assert not owner.is_alive(), "owner process not reaped after SIGKILL"
            deadline = time.monotonic() + 30.0
            while _harness.pid_alive(daemon_pid) and time.monotonic() < deadline:
                time.sleep(0.1)
            assert not _harness.pid_alive(daemon_pid), f"orphaned daemon {daemon_pid}"
        finally:
            if owner.is_alive():
                owner.kill()
                owner.join()
            if tempdir and os.path.isdir(tempdir):
                shutil.rmtree(tempdir, ignore_errors=True)
