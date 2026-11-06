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
"""Unit tests for accelerator request routing/failover and _start_accelerator
lifecycle. Tests cover:
  - _use_accelerator() routing predicate
  - _read_row_via_accelerator() and _mutate_row_via_accelerator() call paths
  - read_row() / mutate_row() fallback to native when accelerator raises
  - _start_accelerator() success and failure with cleanup
"""

from __future__ import annotations

import asyncio
from types import SimpleNamespace
from unittest import mock

import grpc as _grpc
import pytest
from google.api_core import exceptions as core_exceptions
from grpc import StatusCode

from google.cloud.bigtable.data._accelerator._fallback import (
    AcceleratorBreaker,
    _AcceleratorFallback,
)
from google.cloud.bigtable.data._accelerator._routing import is_supported
from google.cloud.bigtable.data._async.client import (
    _AcceleratorIdentityError,
    _DataApiTargetAsync,
)


class _FakeRpcError(_grpc.RpcError):
    """grpc.RpcError subclass that exposes code()/details()/trailing_metadata()."""

    def __init__(self, status_code, details=""):
        self._code = status_code
        self._details = details

    def code(self):
        return self._code

    def details(self):
        return self._details

    def trailing_metadata(self):
        return None


# ---------------------------------------------------------------------------
# Minimal concrete _DataApiTargetAsync that skips __init__
# ---------------------------------------------------------------------------


class _ConcreteTarget(_DataApiTargetAsync):
    """Minimal subclass to make the abstract class instantiable."""

    @property
    def _request_path(self):
        return {"table_name": "projects/p/instances/i/tables/t"}


def _bare_target(
    *,
    accel_client=None,
    accel_daemon=None,
    breaker=None,
):
    """Build a _DataApiTargetAsync that skips __init__.

    Wired with mock client, metrics, and configurable accelerator state.
    """
    from google.cloud.bigtable.data._metrics import BigtableClientSideMetricsController

    t = object.__new__(_ConcreteTarget)
    t.client = SimpleNamespace(
        project="p",
        _emulator_host=None,
        _accelerator_blocked_reason=None,
        _accelerator_flags=[],
        _accelerator_env={},
        _use_accelerator=None,
        _metrics=BigtableClientSideMetricsController(handlers=[]),
        _gapic_client=mock.Mock(),
    )
    t.instance_id = "i"
    t.app_profile_id = None
    t.default_operation_timeout = 60.0
    t.default_attempt_timeout = 20.0
    t.default_read_rows_operation_timeout = 600.0
    t.default_read_rows_attempt_timeout = 20.0
    t.default_mutate_rows_operation_timeout = 600.0
    t.default_mutate_rows_attempt_timeout = 60.0
    t.default_read_rows_retryable_errors = ()
    t.default_mutate_rows_retryable_errors = ()
    t.default_retryable_errors = ()
    t._accelerator_client = accel_client
    t._accelerator_daemon = accel_daemon
    t._accelerator_breaker = breaker if breaker is not None else AcceleratorBreaker()
    return t


# ---------------------------------------------------------------------------
# _use_accelerator predicate
# ---------------------------------------------------------------------------


class TestUseAccelerator:
    def test_returns_true_when_all_conditions_met(self):
        t = _bare_target(accel_client=mock.Mock())
        assert t._use_accelerator("read_row") is True
        assert t._use_accelerator("mutate_row") is True

    def test_returns_false_when_client_is_none(self):
        t = _bare_target(accel_client=None)
        assert t._use_accelerator("read_row") is False

    def test_returns_false_for_unsupported_method(self):
        t = _bare_target(accel_client=mock.Mock())
        assert t._use_accelerator("read_rows") is False
        assert t._use_accelerator("mutate_rows") is False
        assert t._use_accelerator("sample_row_keys") is False

    def test_returns_false_when_breaker_tripped(self):
        breaker = AcceleratorBreaker()
        breaker.trip()
        t = _bare_target(accel_client=mock.Mock(), breaker=breaker)
        assert t._use_accelerator("read_row") is False

    def test_becomes_false_after_trip(self):
        t = _bare_target(accel_client=mock.Mock())
        assert t._use_accelerator("read_row") is True
        t._accelerator_breaker.trip()
        assert t._use_accelerator("read_row") is False

    def test_close_trips_breaker_before_teardown(self):
        t = _bare_target(accel_client=mock.AsyncMock(), accel_daemon=mock.Mock())
        t._accelerator_health = None
        t._register_instance_future = None
        t.client._remove_instance_registration = mock.Mock()
        assert t._accelerator_breaker.is_tripped is False
        asyncio.get_event_loop().run_until_complete(t.close())
        assert t._accelerator_breaker.is_tripped is True


# ---------------------------------------------------------------------------
# _mutate_row_via_accelerator
# ---------------------------------------------------------------------------


class TestMutateRowViaAccelerator:
    def _run(self, coro):
        return asyncio.get_event_loop().run_until_complete(coro)

    def test_raises_fallback_when_client_is_none(self):
        t = _bare_target()
        # accel_client is None by default

        from google.cloud.bigtable_v2.types.bigtable import MutateRowRequest

        req = MutateRowRequest()
        with pytest.raises(_AcceleratorFallback):
            self._run(t._mutate_row_via_accelerator(req, 30.0))

    def test_returns_response_on_success(self):
        from google.cloud.bigtable_v2.types.bigtable import (
            MutateRowRequest,
            MutateRowResponse,
        )

        resp = MutateRowResponse()
        client_mock = mock.AsyncMock()
        client_mock.mutate_row.return_value = resp
        t = _bare_target(
            accel_client=client_mock, accel_daemon=mock.Mock(is_running=True)
        )

        req = MutateRowRequest()
        result = self._run(t._mutate_row_via_accelerator(req, 30.0))
        assert result == resp
        client_mock.mutate_row.assert_awaited_once_with(req, timeout=30.0)

    def test_unimplemented_trips_breaker_and_raises_fallback(self):
        from google.cloud.bigtable_v2.types.bigtable import MutateRowRequest

        rpc_exc = _FakeRpcError(StatusCode.UNIMPLEMENTED, "no sessions")
        client_mock = mock.AsyncMock()
        client_mock.mutate_row.side_effect = rpc_exc
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        req = MutateRowRequest()
        with pytest.raises(_AcceleratorFallback):
            self._run(t._mutate_row_via_accelerator(req, 30.0))
        assert t._accelerator_breaker.bypass()

    def test_dead_daemon_trips_breaker_and_raises_fallback(self):
        from google.cloud.bigtable_v2.types.bigtable import MutateRowRequest

        rpc_exc = _FakeRpcError(StatusCode.INTERNAL, "channel closed")
        client_mock = mock.AsyncMock()
        client_mock.mutate_row.side_effect = rpc_exc
        daemon = mock.Mock(is_running=False)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        req = MutateRowRequest()
        with pytest.raises(_AcceleratorFallback):
            self._run(t._mutate_row_via_accelerator(req, 30.0))
        assert t._accelerator_breaker.bypass()

    def test_not_found_translates_and_raises(self):
        from google.cloud.bigtable_v2.types.bigtable import MutateRowRequest

        rpc_exc = _FakeRpcError(StatusCode.NOT_FOUND, "row not found")
        client_mock = mock.AsyncMock()
        client_mock.mutate_row.side_effect = rpc_exc
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        req = MutateRowRequest()
        with pytest.raises(core_exceptions.GoogleAPICallError):
            self._run(t._mutate_row_via_accelerator(req, 30.0))
        # NOT_FOUND is a real server result, not a fallback — breaker stays clear.
        assert not t._accelerator_breaker.bypass()

    def test_non_grpc_exception_reraises(self):
        from google.cloud.bigtable_v2.types.bigtable import MutateRowRequest

        client_mock = mock.AsyncMock()
        client_mock.mutate_row.side_effect = RuntimeError("unexpected")
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        req = MutateRowRequest()
        with pytest.raises(RuntimeError, match="unexpected"):
            self._run(t._mutate_row_via_accelerator(req, 30.0))
        assert not t._accelerator_breaker.bypass()


# ---------------------------------------------------------------------------
# _read_row_via_accelerator
# ---------------------------------------------------------------------------


class TestReadRowViaAccelerator:
    def _run(self, coro):
        return asyncio.get_event_loop().run_until_complete(coro)

    def test_raises_fallback_when_client_is_none(self):
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

        t = _bare_target()
        query = ReadRowsQuery(row_keys=b"key1", limit=1)

        with pytest.raises(_AcceleratorFallback):
            self._run(t._read_row_via_accelerator(query, 30.0))

    def test_returns_row_on_success(self):
        from google.protobuf import wrappers_pb2

        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery
        from google.cloud.bigtable_v2.types.bigtable import ReadRowsResponse

        async def _stream():
            yield ReadRowsResponse(
                chunks=[
                    ReadRowsResponse.CellChunk(
                        row_key=b"key1",
                        family_name=wrappers_pb2.StringValue(value="cf1"),
                        qualifier=wrappers_pb2.BytesValue(value=b"q1"),
                        timestamp_micros=1000,
                        value=b"v1",
                        commit_row=True,
                    )
                ]
            )

        client_mock = mock.AsyncMock()
        client_mock.read_rows.return_value = _stream()
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        query = ReadRowsQuery(row_keys=b"key1", limit=1)
        row = self._run(t._read_row_via_accelerator(query, 30.0))
        assert row is not None
        assert row.row_key == b"key1"
        assert row.get_cells("cf1", b"q1")[0].value == b"v1"
        client_mock.read_rows.assert_awaited_once()

    def test_returns_none_when_stream_is_empty(self):
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

        async def _empty_stream():
            if False:
                yield

        client_mock = mock.AsyncMock()
        client_mock.read_rows.return_value = _empty_stream()
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        query = ReadRowsQuery(row_keys=b"key1", limit=1)
        row = self._run(t._read_row_via_accelerator(query, 30.0))
        assert row is None
        client_mock.read_rows.assert_awaited_once()

    def test_unimplemented_trips_breaker_and_raises_fallback(self):
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

        rpc_exc = _FakeRpcError(StatusCode.UNIMPLEMENTED, "no sessions")
        client_mock = mock.AsyncMock()
        client_mock.read_rows.side_effect = rpc_exc
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        query = ReadRowsQuery(row_keys=b"key1", limit=1)
        with pytest.raises(_AcceleratorFallback):
            self._run(t._read_row_via_accelerator(query, 30.0))
        assert t._accelerator_breaker.bypass()

    def test_dead_daemon_trips_breaker_and_raises_fallback(self):
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

        rpc_exc = _FakeRpcError(StatusCode.UNAVAILABLE, "channel dead")
        client_mock = mock.AsyncMock()
        client_mock.read_rows.side_effect = rpc_exc
        daemon = mock.Mock(is_running=False)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        query = ReadRowsQuery(row_keys=b"key1", limit=1)
        with pytest.raises(_AcceleratorFallback):
            self._run(t._read_row_via_accelerator(query, 30.0))
        assert t._accelerator_breaker.bypass()

    def test_permission_denied_translates_and_raises(self):
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

        rpc_exc = _FakeRpcError(StatusCode.PERMISSION_DENIED, "caller lacks permission")
        client_mock = mock.AsyncMock()
        client_mock.read_rows.side_effect = rpc_exc
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        query = ReadRowsQuery(row_keys=b"key1", limit=1)
        with pytest.raises(core_exceptions.GoogleAPICallError):
            self._run(t._read_row_via_accelerator(query, 30.0))
        assert not t._accelerator_breaker.bypass()

    def test_non_grpc_exception_reraises(self):
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

        client_mock = mock.AsyncMock()
        client_mock.read_rows.side_effect = RuntimeError("unexpected")
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        query = ReadRowsQuery(row_keys=b"key1", limit=1)
        with pytest.raises(RuntimeError, match="unexpected"):
            self._run(t._read_row_via_accelerator(query, 30.0))
        assert not t._accelerator_breaker.bypass()

    def test_invalid_chunk_trips_breaker_and_raises_fallback(self):
        from google.protobuf import wrappers_pb2

        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery
        from google.cloud.bigtable_v2.types.bigtable import ReadRowsResponse

        async def _malformed_stream():
            yield ReadRowsResponse(
                chunks=[
                    ReadRowsResponse.CellChunk(
                        row_key=b"",
                        family_name=wrappers_pb2.StringValue(value="cf1"),
                        qualifier=wrappers_pb2.BytesValue(value=b"q1"),
                        timestamp_micros=1000,
                        value=b"v1",
                        commit_row=True,
                    )
                ]
            )

        client_mock = mock.AsyncMock()
        client_mock.read_rows.return_value = _malformed_stream()
        daemon = mock.Mock(is_running=True)
        t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

        query = ReadRowsQuery(row_keys=b"", limit=1)
        with pytest.raises(_AcceleratorFallback):
            self._run(t._read_row_via_accelerator(query, 30.0))
        assert t._accelerator_breaker.bypass()


# ---------------------------------------------------------------------------
# read_row: accelerator dispatch and fallback to native
# ---------------------------------------------------------------------------


class TestReadRowAcceleratorDispatch:
    """Test read_row() routing without spinning up a real client.

    We patch _use_accelerator and _read_row_via_accelerator so these tests are
    decoupled from gRPC and the row-merging machinery.
    """

    def _run(self, coro):
        return asyncio.get_event_loop().run_until_complete(coro)

    def test_routes_to_accelerator_when_enabled(self):
        from google.cloud.bigtable.data.row import Row

        t = _bare_target()
        expected_row = Row(b"key1", cells={})

        async def fake_accel(query, op_timeout):
            return expected_row

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_read_row_via_accelerator", side_effect=fake_accel
            ) as accel_mock,
        ):
            result = self._run(t.read_row(b"key1"))

        assert result == expected_row
        accel_mock.assert_called_once()

    def test_falls_back_to_native_on_accelerator_fallback(self):
        from google.cloud.bigtable.data.row import Row

        t = _bare_target()
        expected_row = Row(b"key1", cells={})

        async def fake_accel_fallback(query, op_timeout):
            raise _AcceleratorFallback()

        async def _row_gen():
            yield expected_row

        # start_operation must return the async generator directly (not a coroutine).
        native_row_merger = mock.Mock()
        native_row_merger.start_operation.return_value = _row_gen()

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_read_row_via_accelerator", side_effect=fake_accel_fallback
            ),
            mock.patch(
                "google.cloud.bigtable.data._async.client.CrossSync._ReadRowsOperation",
                return_value=native_row_merger,
            ),
        ):
            result = self._run(t.read_row(b"key1"))

        assert result == expected_row

    def test_fallback_subtracts_elapsed_time_and_clamps_attempt_timeout(self):
        from google.cloud.bigtable.data.row import Row

        t = _bare_target()
        expected_row = Row(b"key1", cells={})
        fake_clock = mock.Mock(monotonic=mock.Mock(return_value=100.0))

        async def fake_accel_fallback(query, op_timeout):
            fake_clock.monotonic.return_value = 107.0
            raise _AcceleratorFallback()

        async def _row_gen():
            yield expected_row

        native_row_merger = mock.Mock()
        native_row_merger.start_operation.return_value = _row_gen()

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_read_row_via_accelerator", side_effect=fake_accel_fallback
            ),
            mock.patch("google.cloud.bigtable.data._async.client.time", fake_clock),
            mock.patch(
                "google.cloud.bigtable.data._async.client.CrossSync._ReadRowsOperation",
                return_value=native_row_merger,
            ) as op_mock,
        ):
            result = self._run(
                t.read_row(b"key1", operation_timeout=10.0, attempt_timeout=5.0)
            )

        assert result == expected_row
        op_mock.assert_called_once()
        _, kwargs = op_mock.call_args
        assert kwargs["operation_timeout"] == pytest.approx(3.0)
        assert kwargs["attempt_timeout"] == pytest.approx(3.0)

    def test_fallback_raises_deadline_exceeded_when_budget_exhausted(self):
        t = _bare_target()
        fake_clock = mock.Mock(monotonic=mock.Mock(return_value=100.0))

        async def fake_accel_fallback(query, op_timeout):
            fake_clock.monotonic.return_value = 110.0
            raise _AcceleratorFallback()

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_read_row_via_accelerator", side_effect=fake_accel_fallback
            ),
            mock.patch("google.cloud.bigtable.data._async.client.time", fake_clock),
            mock.patch(
                "google.cloud.bigtable.data._async.client.CrossSync._ReadRowsOperation"
            ) as op_mock,
        ):
            with pytest.raises(core_exceptions.DeadlineExceeded):
                self._run(
                    t.read_row(b"key1", operation_timeout=10.0, attempt_timeout=5.0)
                )
            op_mock.assert_not_called()

    def test_uses_native_directly_when_accelerator_disabled(self):
        from google.cloud.bigtable.data.row import Row

        t = (
            _bare_target()
        )  # _accelerator_client is None → _use_accelerator returns False
        expected_row = Row(b"key1", cells={})

        async def _row_gen():
            yield expected_row

        native_row_merger = mock.Mock()
        native_row_merger.start_operation.return_value = _row_gen()

        with (
            mock.patch.object(t, "_use_accelerator", return_value=False),
            mock.patch(
                "google.cloud.bigtable.data._async.client.CrossSync._ReadRowsOperation",
                return_value=native_row_merger,
            ),
        ):
            result = self._run(t.read_row(b"key1"))

        assert result == expected_row

    def test_raises_value_error_for_none_key(self):
        t = _bare_target()
        with pytest.raises(ValueError, match="row_key must be string or bytes"):
            self._run(t.read_row(None))

    def test_returns_none_for_missing_row(self):
        t = _bare_target()

        async def _empty_gen():
            return
            yield  # make it a proper async generator

        native_row_merger = mock.Mock()
        native_row_merger.start_operation.return_value = _empty_gen()

        with (
            mock.patch.object(t, "_use_accelerator", return_value=False),
            mock.patch(
                "google.cloud.bigtable.data._async.client.CrossSync._ReadRowsOperation",
                return_value=native_row_merger,
            ),
        ):
            result = self._run(t.read_row(b"missing"))

        assert result is None


# ---------------------------------------------------------------------------
# mutate_row: accelerator dispatch and fallback to native
# ---------------------------------------------------------------------------


class TestMutateRowAcceleratorDispatch:
    def _run(self, coro):
        return asyncio.get_event_loop().run_until_complete(coro)

    def test_routes_to_accelerator_when_enabled(self):
        from google.cloud.bigtable.data.mutations import SetCell
        from google.cloud.bigtable_v2.types.bigtable import MutateRowResponse

        t = _bare_target()
        resp = MutateRowResponse()

        async def fake_accel(request, op_timeout):
            return resp

        mutations = [SetCell("cf", "col", b"val", timestamp_micros=1000)]

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_mutate_row_via_accelerator", side_effect=fake_accel
            ) as accel_mock,
        ):
            result = self._run(t.mutate_row(b"key1", mutations))

        assert result == resp
        accel_mock.assert_called_once()

    def test_falls_back_to_native_on_accelerator_fallback(self):
        from google.cloud.bigtable.data.mutations import SetCell
        from google.cloud.bigtable_v2.types.bigtable import MutateRowResponse

        t = _bare_target()
        native_resp = MutateRowResponse()

        async def fake_accel_fallback(request, op_timeout):
            raise _AcceleratorFallback()

        async def fake_native_mutate(*args, **kwargs):
            return native_resp

        mutations = [SetCell("cf", "col", b"val", timestamp_micros=1000)]

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_mutate_row_via_accelerator", side_effect=fake_accel_fallback
            ),
            mock.patch(
                "google.cloud.bigtable.data._async.client.tracked_retry",
                side_effect=fake_native_mutate,
            ),
        ):
            result = self._run(t.mutate_row(b"key1", mutations))

        assert result == native_resp

    def test_fallback_subtracts_elapsed_time_and_clamps_attempt_timeout(self):
        from google.cloud.bigtable.data.mutations import SetCell
        from google.cloud.bigtable_v2.types.bigtable import MutateRowResponse

        t = _bare_target()
        native_resp = MutateRowResponse()
        fake_clock = mock.Mock(monotonic=mock.Mock(return_value=100.0))

        async def fake_accel_fallback(request, op_timeout):
            fake_clock.monotonic.return_value = 107.0
            raise _AcceleratorFallback()

        async def fake_native_mutate(*args, **kwargs):
            return native_resp

        mutations = [SetCell("cf", "col", b"val", timestamp_micros=1000)]

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_mutate_row_via_accelerator", side_effect=fake_accel_fallback
            ),
            mock.patch("google.cloud.bigtable.data._async.client.time", fake_clock),
            mock.patch(
                "google.cloud.bigtable.data._async.client.tracked_retry",
                side_effect=fake_native_mutate,
            ) as retry_mock,
        ):
            result = self._run(
                t.mutate_row(
                    b"key1", mutations, operation_timeout=10.0, attempt_timeout=5.0
                )
            )

        assert result == native_resp
        retry_mock.assert_called_once()
        _, kwargs = retry_mock.call_args
        assert kwargs["timeout"] == pytest.approx(3.0)
        assert kwargs["target"].keywords["timeout"] == pytest.approx(3.0)

    def test_fallback_raises_deadline_exceeded_when_budget_exhausted(self):
        from google.cloud.bigtable.data.mutations import SetCell

        t = _bare_target()
        fake_clock = mock.Mock(monotonic=mock.Mock(return_value=100.0))

        async def fake_accel_fallback(request, op_timeout):
            fake_clock.monotonic.return_value = 110.0
            raise _AcceleratorFallback()

        mutations = [SetCell("cf", "col", b"val", timestamp_micros=1000)]

        with (
            mock.patch.object(t, "_use_accelerator", return_value=True),
            mock.patch.object(
                t, "_mutate_row_via_accelerator", side_effect=fake_accel_fallback
            ),
            mock.patch("google.cloud.bigtable.data._async.client.time", fake_clock),
            mock.patch(
                "google.cloud.bigtable.data._async.client.tracked_retry"
            ) as retry_mock,
        ):
            with pytest.raises(core_exceptions.DeadlineExceeded):
                self._run(
                    t.mutate_row(
                        b"key1", mutations, operation_timeout=10.0, attempt_timeout=5.0
                    )
                )
            retry_mock.assert_not_called()

    def test_uses_native_directly_when_accelerator_disabled(self):
        from google.cloud.bigtable.data.mutations import SetCell
        from google.cloud.bigtable_v2.types.bigtable import MutateRowResponse

        t = _bare_target()
        native_resp = MutateRowResponse()
        mutations = [SetCell("cf", "col", b"val", timestamp_micros=1000)]

        async def fake_native_mutate(*args, **kwargs):
            return native_resp

        with (
            mock.patch.object(t, "_use_accelerator", return_value=False),
            mock.patch(
                "google.cloud.bigtable.data._async.client.tracked_retry",
                side_effect=fake_native_mutate,
            ),
        ):
            result = self._run(t.mutate_row(b"key1", mutations))

        assert result == native_resp

    def test_raises_value_error_for_empty_mutations(self):
        t = _bare_target()
        with pytest.raises(ValueError, match="No mutations provided"):
            self._run(t.mutate_row(b"key1", []))

    def test_non_idempotent_mutate_row_routes_to_accelerator(self):
        from google.cloud.bigtable.data.mutations import AddToCell, SetCell
        from google.cloud.bigtable_v2.types.bigtable import MutateRowResponse

        resp = MutateRowResponse()
        for mut in (
            SetCell("cf", "col", b"val", timestamp_micros=-1),
            AddToCell("cf", "col", 1, timestamp_micros=1000),
        ):
            client_mock = mock.AsyncMock()
            client_mock.mutate_row.return_value = resp
            daemon = mock.Mock(is_running=True)
            t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

            result = self._run(t.mutate_row(b"key1", [mut]))
            assert result == resp
            client_mock.mutate_row.assert_awaited_once()

    def test_non_idempotent_midflight_daemon_death_raises_without_fallback(self):
        from google.cloud.bigtable.data.mutations import AddToCell, SetCell

        for mut in (
            SetCell("cf", "col", b"val", timestamp_micros=-1),
            AddToCell("cf", "col", 1, timestamp_micros=1000),
        ):
            daemon = mock.NonCallableMock()
            is_running_prop = mock.PropertyMock(return_value=True)
            type(daemon).is_running = is_running_prop

            async def crash_midflight(*args, **kwargs):
                is_running_prop.return_value = False
                raise _FakeRpcError(StatusCode.UNAVAILABLE, "socket closed")

            client_mock = mock.AsyncMock()
            client_mock.mutate_row.side_effect = crash_midflight
            t = _bare_target(accel_client=client_mock, accel_daemon=daemon)

            with mock.patch(
                "google.cloud.bigtable.data._async.client.tracked_retry"
            ) as native_mock:
                with pytest.raises(core_exceptions.ServiceUnavailable):
                    self._run(t.mutate_row(b"key1", [mut]))
                native_mock.assert_not_called()

            assert t._accelerator_breaker.is_tripped
            assert is_running_prop.call_count == 1


# ---------------------------------------------------------------------------
# _start_accelerator: startup lifecycle
# ---------------------------------------------------------------------------


class TestStartAccelerator:
    """Tests for _start_accelerator() — the method that spawns the daemon and
    wires up the AcceleratorClient. These use mocks to avoid real subprocesses."""

    def test_success_sets_daemon_and_client(self):
        from google.cloud.bigtable.data._accelerator._daemon import AcceleratorDaemon

        t = _bare_target()
        t._accelerator_daemon = None
        t._accelerator_client = None

        fake_daemon = mock.Mock(spec=AcceleratorDaemon)
        fake_daemon.uds_path = "/tmp/fake-sock"
        fake_daemon.auth_secret = "secret-token"
        fake_client = mock.Mock()

        with (
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorDaemon",
                return_value=fake_daemon,
            ),
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorClientType",
                return_value=fake_client,
            ),
            mock.patch.object(t, "_verify_daemon_identity"),
        ):
            t._start_accelerator()

        fake_daemon.start.assert_called_once()
        assert t._accelerator_daemon is fake_daemon
        assert t._accelerator_client is fake_client

    def test_daemon_start_failure_calls_close_and_reraises(self):
        from google.cloud.bigtable.data._accelerator._daemon import AcceleratorDaemon

        t = _bare_target()
        t._accelerator_daemon = None
        t._accelerator_client = None

        fake_daemon = mock.Mock(spec=AcceleratorDaemon)
        fake_daemon.start.side_effect = RuntimeError("binary missing")

        with (
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorDaemon",
                return_value=fake_daemon,
            ),
            pytest.raises(RuntimeError, match="binary missing"),
        ):
            t._start_accelerator()

        fake_daemon.close.assert_called_once()
        assert t._accelerator_daemon is None
        assert t._accelerator_client is None

    def test_identity_verify_failure_closes_daemon_and_propagates(self):
        """Identity mismatches propagate from _start_accelerator so
        _maybe_start_accelerator can decide whether to warn (auto) or raise
        (explicit). The daemon is closed before the error surfaces.
        """
        from google.cloud.bigtable.data._accelerator._daemon import AcceleratorDaemon

        t = _bare_target()
        t._accelerator_daemon = None
        t._accelerator_client = None

        fake_daemon = mock.Mock(spec=AcceleratorDaemon)
        fake_daemon.uds_path = "/tmp/fake-sock"
        fake_daemon.auth_secret = "secret-token"

        with (
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorDaemon",
                return_value=fake_daemon,
            ),
            mock.patch.object(
                t,
                "_verify_daemon_identity",
                side_effect=_AcceleratorIdentityError("mismatch"),
            ),
            pytest.raises(_AcceleratorIdentityError, match="mismatch"),
        ):
            t._start_accelerator()

        fake_daemon.close.assert_called_once()

    def test_passes_project_instance_flags(self):
        from google.cloud.bigtable.data._accelerator._daemon import AcceleratorDaemon

        t = _bare_target()
        t.client.project = "my-project"
        t.instance_id = "my-instance"
        t.app_profile_id = None
        t.client._accelerator_flags = []
        t.client._accelerator_env = {}
        t._accelerator_daemon = None
        t._accelerator_client = None

        fake_daemon = mock.Mock(spec=AcceleratorDaemon)
        fake_daemon.uds_path = "/tmp/fake-sock"
        captured = {}

        def capture_daemon(cli_flags=(), **kwargs):
            captured["cli_flags"] = list(cli_flags)
            captured["extra_env"] = kwargs.get("extra_env", {})
            return fake_daemon

        with (
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorDaemon",
                side_effect=capture_daemon,
            ),
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorClientType",
            ),
            mock.patch.object(t, "_verify_daemon_identity"),
        ):
            t._start_accelerator()

        flags = captured["cli_flags"]
        assert "--project" in flags
        assert flags[flags.index("--project") + 1] == "my-project"
        assert "--instance" in flags
        assert flags[flags.index("--instance") + 1] == "my-instance"

    def test_passes_app_profile_flag_when_set(self):
        from google.cloud.bigtable.data._accelerator._daemon import AcceleratorDaemon

        t = _bare_target()
        t.client.project = "p"
        t.instance_id = "i"
        t.app_profile_id = "my-app-profile"
        t.client._accelerator_flags = []
        t.client._accelerator_env = {}
        t._accelerator_daemon = None
        t._accelerator_client = None

        fake_daemon = mock.Mock(spec=AcceleratorDaemon)
        fake_daemon.uds_path = "/tmp/fake-sock"
        captured = {}

        def capture_daemon(cli_flags=(), **kwargs):
            captured["cli_flags"] = list(cli_flags)
            return fake_daemon

        with (
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorDaemon",
                side_effect=capture_daemon,
            ),
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorClientType",
            ),
            mock.patch.object(t, "_verify_daemon_identity"),
        ):
            t._start_accelerator()

        flags = captured["cli_flags"]
        assert "--app-profile" in flags
        assert flags[flags.index("--app-profile") + 1] == "my-app-profile"

    def test_no_app_profile_flag_when_none(self):
        from google.cloud.bigtable.data._accelerator._daemon import AcceleratorDaemon

        t = _bare_target()
        t.client.project = "p"
        t.instance_id = "i"
        t.app_profile_id = None
        t.client._accelerator_flags = []
        t.client._accelerator_env = {}
        t._accelerator_daemon = None
        t._accelerator_client = None

        fake_daemon = mock.Mock(spec=AcceleratorDaemon)
        fake_daemon.uds_path = "/tmp/fake-sock"
        captured = {}

        def capture_daemon(cli_flags=(), **kwargs):
            captured["cli_flags"] = list(cli_flags)
            return fake_daemon

        with (
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorDaemon",
                side_effect=capture_daemon,
            ),
            mock.patch(
                "google.cloud.bigtable.data._async.client.AcceleratorClientType",
            ),
            mock.patch.object(t, "_verify_daemon_identity"),
        ):
            t._start_accelerator()

        assert "--app-profile" not in captured["cli_flags"]


# ---------------------------------------------------------------------------
# Event loop fixture so run_until_complete works
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        loop.close()
        asyncio.set_event_loop(None)
