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
"""Unit tests for AcceleratorBreaker, _grpc_code, and handle_accelerator_error
in google.cloud.bigtable.data._accelerator._fallback."""

from unittest import mock

import grpc
import pytest
from google.api_core import exceptions as core_exceptions
from grpc import StatusCode

from google.cloud.bigtable.data._accelerator._fallback import (
    AcceleratorBreaker,
    _AcceleratorFallback,
    _grpc_code,
    handle_accelerator_error,
)
from google.cloud.bigtable.data.exceptions import InvalidChunk

# ---------------------------------------------------------------------------
# AcceleratorBreaker
# ---------------------------------------------------------------------------


class TestAcceleratorBreaker:
    def test_initially_not_bypassed(self):
        b = AcceleratorBreaker()
        assert not b.bypass()

    def test_trip_sets_bypass(self):
        b = AcceleratorBreaker()
        assert b.trip() is True
        assert b.bypass()

    def test_trip_is_idempotent(self):
        b = AcceleratorBreaker()
        assert b.trip() is True
        assert b.trip() is False
        assert b.bypass()

    def test_bypass_is_sticky(self):
        b = AcceleratorBreaker()
        b.trip()
        # Multiple reads are all True after tripping.
        assert b.bypass()
        assert b.bypass()

    def test_thread_safety(self):
        import threading

        b = AcceleratorBreaker()
        errors = []
        first_trips = []
        lock = threading.Lock()

        def trip_and_check():
            try:
                was_first = b.trip()
                with lock:
                    first_trips.append(was_first)
                assert b.bypass()
            except Exception as e:
                errors.append(e)

        threads = [threading.Thread(target=trip_and_check) for _ in range(20)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        assert not errors
        assert first_trips.count(True) == 1

    def test_trip_instance_is_isolated_to_that_instance(self):
        b = AcceleratorBreaker()
        assert b.trip_instance("instance-a") is True
        assert b.trip_instance("instance-a") is False
        assert b.is_instance_tripped("instance-a") is True
        assert b.is_instance_tripped("instance-b") is False
        assert b.bypass("instance-a") is True
        assert b.bypass("instance-b") is False
        assert b.bypass() is False
        assert b.is_tripped is False

    def test_client_wide_trip_overrides_all_instances(self):
        b = AcceleratorBreaker()
        b.trip_instance("instance-a")
        assert b.bypass("instance-b") is False
        assert b.trip() is True
        assert b.bypass("instance-a") is True
        assert b.bypass("instance-b") is True
        assert b.bypass() is True

    def test_set_degraded_overrides_instances_until_recovered(self):
        b = AcceleratorBreaker()
        b.trip_instance("instance-a")
        b.set_degraded(True)
        assert b.bypass("instance-a") is True
        assert b.bypass("instance-b") is True
        b.set_degraded(False)
        assert b.bypass("instance-a") is True
        assert b.bypass("instance-b") is False

    def test_trip_instance_thread_safety(self):
        import threading

        b = AcceleratorBreaker()
        errors = []
        first_trips = []
        lock = threading.Lock()

        def trip_and_check():
            try:
                was_first = b.trip_instance("instance-a")
                with lock:
                    first_trips.append(was_first)
                assert b.bypass("instance-a")
                assert not b.bypass("instance-b")
            except Exception as e:
                errors.append(e)

        threads = [threading.Thread(target=trip_and_check) for _ in range(20)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        assert not errors
        assert first_trips.count(True) == 1


# ---------------------------------------------------------------------------
# _grpc_code
# ---------------------------------------------------------------------------


class TestGrpcCode:
    def test_rpc_error_with_code_method(self):
        # grpc.RpcError doesn't define code() in its class spec, so use plain Mock.
        exc = mock.Mock()
        exc.code.return_value = StatusCode.NOT_FOUND
        assert _grpc_code(exc) == StatusCode.NOT_FOUND

    def test_google_api_call_error_with_grpc_status_code_attr(self):
        exc = mock.Mock(spec=[])
        exc.grpc_status_code = StatusCode.UNAVAILABLE
        # No callable code() method, but has grpc_status_code attribute.
        assert _grpc_code(exc) == StatusCode.UNAVAILABLE

    def test_plain_exception_returns_none(self):
        assert _grpc_code(ValueError("boom")) is None

    def test_code_method_raises_returns_none(self):
        exc = mock.Mock()
        exc.code.side_effect = RuntimeError("broken")
        assert _grpc_code(exc) is None

    def test_grpc_status_code_wrong_type_returns_none(self):
        exc = mock.Mock(spec=[])
        exc.grpc_status_code = "NOT_FOUND"  # string, not StatusCode
        assert _grpc_code(exc) is None


# ---------------------------------------------------------------------------
# handle_accelerator_error
# ---------------------------------------------------------------------------


class _FakeRpcError(grpc.RpcError):
    """Minimal grpc.RpcError subclass for tests — passes isinstance checks.

    Implements the methods that google.api_core.exceptions.from_grpc_error
    inspects when translating a gRPC error.
    """

    def __init__(self, status_code: StatusCode, details: str = ""):
        self._code = status_code
        self._details = details

    def code(self) -> StatusCode:
        return self._code

    def details(self) -> str:
        return self._details

    def trailing_metadata(self):
        return None


def _make_rpc_error(code: StatusCode) -> grpc.RpcError:
    return _FakeRpcError(code, f"mocked {code}")


class TestHandleAcceleratorError:
    # -- Dead daemon ---------------------------------------------------------

    def test_dead_daemon_trips_breaker_and_falls_back(self):
        daemon = mock.Mock()
        daemon.is_running = False
        breaker = AcceleratorBreaker()

        exc = _make_rpc_error(StatusCode.INTERNAL)
        with pytest.raises(_AcceleratorFallback):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert breaker.bypass()

    def test_dead_daemon_wins_over_unimplemented(self):
        """Daemon liveness check runs before status code check."""
        daemon = mock.Mock()
        daemon.is_running = False
        breaker = AcceleratorBreaker()

        exc = _make_rpc_error(StatusCode.UNIMPLEMENTED)
        with pytest.raises(_AcceleratorFallback):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert breaker.bypass()

    # -- UNIMPLEMENTED -------------------------------------------------------

    def test_unimplemented_trips_breaker_and_falls_back(self):
        daemon = mock.Mock()
        daemon.is_running = True
        breaker = AcceleratorBreaker()

        exc = _make_rpc_error(StatusCode.UNIMPLEMENTED)
        with pytest.raises(_AcceleratorFallback):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert breaker.bypass()

    def test_unimplemented_without_daemon_object_falls_back(self):
        """daemon=None means the client has no daemon reference; UNIMPLEMENTED still trips."""
        breaker = AcceleratorBreaker()
        exc = _make_rpc_error(StatusCode.UNIMPLEMENTED)
        with pytest.raises(_AcceleratorFallback):
            handle_accelerator_error(exc, daemon=None, breaker=breaker)
        assert breaker.bypass()

    def test_dead_daemon_logs_warning_once_without_traceback(self, caplog):
        import logging

        daemon = mock.Mock(is_running=False)
        breaker = AcceleratorBreaker()
        exc = _make_rpc_error(StatusCode.UNAVAILABLE)
        with caplog.at_level(logging.WARNING):
            for _ in range(3):
                with pytest.raises(_AcceleratorFallback):
                    handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert len(caplog.records) == 1
        assert "no longer running" in caplog.records[0].getMessage()
        assert caplog.records[0].exc_info is None

    def test_unimplemented_logs_warning_once(self, caplog):
        import logging

        daemon = mock.Mock(is_running=True)
        breaker = AcceleratorBreaker()
        exc = _make_rpc_error(StatusCode.UNIMPLEMENTED)
        with caplog.at_level(logging.WARNING):
            for _ in range(3):
                with pytest.raises(_AcceleratorFallback):
                    handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert len(caplog.records) == 1
        assert "replied UNIMPLEMENTED" in caplog.records[0].getMessage()

    def test_unimplemented_with_instance_id_trips_only_that_instance(self, caplog):
        import logging

        daemon = mock.Mock(is_running=True)
        breaker = AcceleratorBreaker()
        exc = _make_rpc_error(StatusCode.UNIMPLEMENTED)
        with caplog.at_level(logging.WARNING):
            for _ in range(3):
                with pytest.raises(_AcceleratorFallback):
                    handle_accelerator_error(
                        exc,
                        daemon=daemon,
                        breaker=breaker,
                        instance_id="instance-a",
                    )
        assert breaker.bypass("instance-a") is True
        assert breaker.bypass("instance-b") is False
        assert breaker.is_tripped is False
        assert len(caplog.records) == 1
        assert "instance-a" in caplog.records[0].getMessage()

        with caplog.at_level(logging.WARNING):
            with pytest.raises(_AcceleratorFallback):
                handle_accelerator_error(
                    exc,
                    daemon=daemon,
                    breaker=breaker,
                    instance_id="instance-b",
                )
        assert breaker.bypass("instance-b") is True
        assert len(caplog.records) == 2
        assert "instance-b" in caplog.records[1].getMessage()

    # -- Other gRPC errors are translated ------------------------------------

    def test_not_found_translated_and_raised(self):
        daemon = mock.Mock()
        daemon.is_running = True
        breaker = AcceleratorBreaker()

        exc = _make_rpc_error(StatusCode.NOT_FOUND)
        with pytest.raises(core_exceptions.GoogleAPICallError):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        # Breaker must NOT have been tripped for a real server error.
        assert not breaker.bypass()

    def test_permission_denied_translated_and_raised(self):
        daemon = mock.Mock()
        daemon.is_running = True
        breaker = AcceleratorBreaker()

        exc = _make_rpc_error(StatusCode.PERMISSION_DENIED)
        with pytest.raises(core_exceptions.GoogleAPICallError):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert not breaker.bypass()

    def test_internal_error_translated_and_raised(self):
        daemon = mock.Mock()
        daemon.is_running = True
        breaker = AcceleratorBreaker()

        exc = _make_rpc_error(StatusCode.INTERNAL)
        with pytest.raises(core_exceptions.GoogleAPICallError):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert not breaker.bypass()

    # -- InvalidChunk --------------------------------------------------------

    def test_invalid_chunk_trips_breaker_and_falls_back(self):
        daemon = mock.Mock()
        daemon.is_running = True
        breaker = AcceleratorBreaker()

        exc = InvalidChunk("first row chunk is missing key")
        with pytest.raises(_AcceleratorFallback):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert breaker.bypass()

    def test_invalid_chunk_logs_warning_once_without_traceback(self, caplog):
        import logging

        daemon = mock.Mock(is_running=True)
        breaker = AcceleratorBreaker()
        exc = InvalidChunk("first row chunk is missing key")
        with caplog.at_level(logging.WARNING):
            for _ in range(3):
                with pytest.raises(_AcceleratorFallback):
                    handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert len(caplog.records) == 1
        assert "invalid ReadRows chunk" in caplog.records[0].getMessage()
        assert caplog.records[0].exc_info is None

    # -- Non-gRPC exceptions are re-raised unchanged -------------------------

    def test_non_grpc_exception_reraises_unchanged(self):
        daemon = mock.Mock()
        daemon.is_running = True
        breaker = AcceleratorBreaker()

        exc = ValueError("bad merge")
        with pytest.raises(ValueError, match="bad merge"):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert not breaker.bypass()

    def test_runtime_error_reraises_unchanged(self):
        daemon = mock.Mock()
        daemon.is_running = True
        breaker = AcceleratorBreaker()

        exc = RuntimeError("internal logic bug")
        with pytest.raises(RuntimeError, match="internal logic bug"):
            handle_accelerator_error(exc, daemon=daemon, breaker=breaker)
        assert not breaker.bypass()

    # -- daemon=None with alive-ish context ----------------------------------

    def test_none_daemon_unavailable_translates(self):
        """When no daemon reference is supplied and the error is UNAVAILABLE,
        translate and raise (not UNIMPLEMENTED, so no fallback)."""
        breaker = AcceleratorBreaker()
        exc = _make_rpc_error(StatusCode.UNAVAILABLE)
        with pytest.raises(core_exceptions.GoogleAPICallError):
            handle_accelerator_error(exc, daemon=None, breaker=breaker)
        assert not breaker.bypass()

    def test_dead_daemon_non_idempotent_trips_breaker_without_fallback(self):
        daemon = mock.Mock(is_running=False)
        breaker = AcceleratorBreaker()
        exc = _make_rpc_error(StatusCode.UNAVAILABLE)
        with pytest.raises(core_exceptions.ServiceUnavailable):
            handle_accelerator_error(
                exc, daemon=daemon, breaker=breaker, is_idempotent=False
            )
        assert breaker.is_tripped

    def test_dead_daemon_non_idempotent_non_grpc_reraises_and_trips(self):
        daemon = mock.Mock(is_running=False)
        breaker = AcceleratorBreaker()
        exc = RuntimeError("broken pipe")
        with pytest.raises(RuntimeError, match="broken pipe"):
            handle_accelerator_error(
                exc, daemon=daemon, breaker=breaker, is_idempotent=False
            )
        assert breaker.is_tripped
