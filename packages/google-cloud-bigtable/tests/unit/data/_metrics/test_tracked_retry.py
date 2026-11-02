# Copyright 2025 Google LLC
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

import inspect
import sys

import google.api_core.retry as retry_module
import mock
import pytest
from google.api_core import exceptions as core_exceptions
from google.api_core.retry import RetryFailureReason
from grpc import StatusCode


class TestTrackRetryableError:
    def _call_fut(self, operation):
        from google.cloud.bigtable.data._metrics.tracked_retry import (
            _track_retryable_error,
        )

        return _track_retryable_error(operation)

    def test_basic_exception(self):
        """should call operation.end_attempt_with_status with the exception for basic exceptions."""
        operation = mock.Mock()
        wrapper = self._call_fut(operation)

        exc = RuntimeError("test")
        wrapper(exc)

        operation.end_attempt_with_status.assert_called_once_with(exc)

    def test_mutate_rows_incomplete(self):
        """should call operation.end_attempt_with_status with StatusCode.OK for _MutateRowsIncomplete exceptions."""
        from google.cloud.bigtable.data.exceptions import _MutateRowsIncomplete

        operation = mock.Mock()
        wrapper = self._call_fut(operation)

        exc = _MutateRowsIncomplete("test")
        wrapper(exc)

        operation.end_attempt_with_status.assert_called_once_with(StatusCode.OK)

    def test_rpc_error_metadata(self):
        """should extract and add metadata from GoogleAPICallError."""
        operation = mock.Mock()
        wrapper = self._call_fut(operation)

        rpc_error = mock.Mock()
        rpc_error.trailing_metadata.return_value = (("key1", "val1"),)
        rpc_error.initial_metadata.return_value = (("key2", "val2"),)

        exc = core_exceptions.GoogleAPICallError("test", errors=[rpc_error])
        wrapper(exc)

        operation.add_response_metadata.assert_called_once_with(
            {"key1": "val1", "key2": "val2"}
        )
        operation.end_attempt_with_status.assert_called_once_with(exc)

    def test_metadata_error_ignored(self):
        """should ignore errors during metadata collection."""
        operation = mock.Mock()
        operation.add_response_metadata.side_effect = RuntimeError("metadata error")
        wrapper = self._call_fut(operation)

        rpc_error = mock.Mock()
        rpc_error.trailing_metadata.return_value = ()
        rpc_error.initial_metadata.return_value = ()
        exc = core_exceptions.GoogleAPICallError("test", errors=[rpc_error])

        # should not raise
        wrapper(exc)

        operation.end_attempt_with_status.assert_called_once_with(exc)


class TestTrackTerminalError:
    def _call_fut(self, operation, factory):
        from google.cloud.bigtable.data._metrics.tracked_retry import (
            _track_terminal_error,
        )

        return _track_terminal_error(operation, factory)

    def test_basic_pass_through(self):
        """should call the exception_factory and end the operation with its result."""
        operation = mock.Mock()
        factory = mock.Mock()
        expected_exc = RuntimeError("source")
        expected_cause = RuntimeError("cause")
        factory.return_value = (expected_exc, expected_cause)

        wrapper = self._call_fut(operation, factory)

        exc_list = [RuntimeError("attempt1")]
        reason = RetryFailureReason.TIMEOUT
        timeout_val = 1.0

        result = wrapper(exc_list, reason, timeout_val)

        assert result == (expected_exc, expected_cause)
        factory.assert_called_once_with(exc_list, reason, timeout_val)
        operation.end_with_status.assert_called_once_with(expected_exc)

    def test_timeout_active_attempt(self):
        """should end attempt if fails on timeout."""
        from google.cloud.bigtable.data._metrics import OperationState

        operation = mock.Mock()
        operation.state = OperationState.ACTIVE_ATTEMPT
        factory = mock.Mock()
        factory.return_value = (RuntimeError("timeout"), None)

        wrapper = self._call_fut(operation, factory)

        last_exc = RuntimeError("last attempt error")
        exc_list = [last_exc]

        wrapper(exc_list, RetryFailureReason.TIMEOUT, 1.0)

        # expect call to end_attempt_with_status via the _track_retryable_error logic
        operation.end_attempt_with_status.assert_called_once_with(last_exc)
        operation.end_with_status.assert_called_once()

    def test_rpc_error_metadata(self):
        """should extract and add metadata from GoogleAPICallError in terminal errors."""
        operation = mock.Mock()
        factory = mock.Mock()

        rpc_error = mock.Mock()
        rpc_error.trailing_metadata.return_value = (("k", "v"),)
        rpc_error.initial_metadata.return_value = ()
        source_exc = core_exceptions.GoogleAPICallError("test", errors=[rpc_error])

        factory.return_value = (source_exc, None)

        wrapper = self._call_fut(operation, factory)
        wrapper([], RetryFailureReason.NON_RETRYABLE_ERROR, None)

        operation.add_response_metadata.assert_called_once_with({"k": "v"})
        operation.end_with_status.assert_called_once_with(source_exc)


class TestTrackedRetry:
    def _call_fut(self, **kwargs):
        from google.cloud.bigtable.data._metrics.tracked_retry import tracked_retry

        return tracked_retry(**kwargs)

    def test_call_args(self):
        """should correctly pass arguments to the retry_fn."""
        operation = mock.Mock()
        retry_fn = mock.Mock()
        retry_fn.return_value = "result"

        result = self._call_fut(retry_fn=retry_fn, operation=operation, other_arg=123)

        assert result == "result"
        retry_fn.assert_called_once()
        call_kwargs = retry_fn.call_args[1]

        assert call_kwargs["sleep_generator"] == operation.backoff_generator
        assert "on_error" in call_kwargs
        assert "exception_factory" in call_kwargs
        assert call_kwargs["other_arg"] == 123

    def test_tracked_retry_wraps_components(self):
        """should wrap on_error and exception_factory with tracking logic."""
        from google.cloud.bigtable.data._metrics import tracked_retry

        module = sys.modules[tracked_retry.__module__]

        with mock.patch.object(module, "_track_retryable_error") as mock_track_retry:
            with mock.patch.object(
                module, "_track_terminal_error"
            ) as mock_track_terminal:
                operation = mock.Mock()
                retry_fn = mock.Mock()
                custom_factory = mock.Mock()

                self._call_fut(
                    retry_fn=retry_fn,
                    operation=operation,
                    exception_factory=custom_factory,
                    arg=1,
                )

                mock_track_retry.assert_called_once_with(operation)
                mock_track_terminal.assert_called_once_with(operation, custom_factory)

                retry_fn.assert_called_once_with(
                    sleep_generator=operation.backoff_generator,
                    on_error=mock_track_retry.return_value,
                    exception_factory=mock_track_terminal.return_value,
                    arg=1,
                )

    @pytest.mark.parametrize(
        "fn_name,type_verifier",
        [
            ("retry_target", callable),
            ("retry_target_stream", inspect.isgenerator),
            ("retry_target_async", inspect.iscoroutine),
            ("retry_target_stream_async", inspect.isasyncgen),
        ],
    )
    def test_wrapping_api_core(self, fn_name, type_verifier):
        """Test building tracked retry from different supported retry functions"""
        from google.cloud.bigtable.data._metrics import ActiveOperationMetric

        operation = ActiveOperationMetric("type")
        fn = getattr(retry_module, fn_name)
        tracked_retry = self._call_fut(
            retry_fn=fn,
            operation=operation,
            target=mock.Mock(),
            timeout=None,
            predicate=lambda x: False,
        )
        assert type_verifier(tracked_retry)
