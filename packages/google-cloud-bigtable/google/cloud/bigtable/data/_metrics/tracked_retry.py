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
"""
Methods for instrumenting an google.api_core.retry.retry_target or
google.api_core.retry.retry_target_stream method

`tracked_retry` will intercept `on_error` and `exception_factory`
methods to update the associated ActiveOperationMetric when exceptions
are encountered through the retryable rpc.
"""

from __future__ import annotations

from typing import Callable, List, Optional, Tuple, TypeVar

from google.api_core.exceptions import GoogleAPICallError
from google.api_core.retry import RetryFailureReason
from grpc import StatusCode

from google.cloud.bigtable.data._helpers import _retry_exception_factory
from google.cloud.bigtable.data._metrics.data_model import (
    ActiveOperationMetric,
    OperationState,
)
from google.cloud.bigtable.data.exceptions import _MutateRowsIncomplete

T = TypeVar("T")


ExceptionFactoryType = Callable[
    [List[Exception], RetryFailureReason, Optional[float]],
    Tuple[Exception, Optional[Exception]],
]


def _track_retryable_error(
    operation: ActiveOperationMetric,
) -> Callable[[Exception], None]:
    """
    Used as input to api_core.Retry classes, to track when retryable errors are encountered

    Should be passed as on_error callback
    """

    def wrapper(exc: Exception) -> None:
        try:
            # record metadata from failed rpc
            if isinstance(exc, GoogleAPICallError) and exc.errors:
                rpc_error = exc.errors[-1]
                metadata = list(rpc_error.trailing_metadata()) + list(
                    rpc_error.initial_metadata()
                )
                operation.add_response_metadata({k: v for k, v in metadata})
        except Exception:
            # ignore errors in metadata collection
            pass
        if isinstance(exc, _MutateRowsIncomplete):
            # _MutateRowsIncomplete represents a successful rpc with some failed mutations
            # mark the attempt as successful
            operation.end_attempt_with_status(StatusCode.OK)
        else:
            operation.end_attempt_with_status(exc)

    return wrapper


def _track_terminal_error(
    operation: ActiveOperationMetric, exception_factory: ExceptionFactoryType
) -> ExceptionFactoryType:
    """
    Used as input to api_core.Retry classes, to track when terminal errors are encountered

    Should be used as a wrapper over an exception_factory callback
    """

    def wrapper(
        exc_list: List[Exception],
        reason: RetryFailureReason,
        timeout_val: float | None,
    ) -> tuple[Exception, Exception | None]:
        source_exc, cause_exc = exception_factory(exc_list, reason, timeout_val)
        try:
            # record metadata from failed rpc
            if isinstance(source_exc, GoogleAPICallError) and source_exc.errors:
                rpc_error = source_exc.errors[-1]
                metadata = list(rpc_error.trailing_metadata()) + list(
                    rpc_error.initial_metadata()
                )
                operation.add_response_metadata({k: v for k, v in metadata})
        except Exception:
            # ignore errors in metadata collection
            pass
        if (
            reason == RetryFailureReason.TIMEOUT
            and operation.state == OperationState.ACTIVE_ATTEMPT
            and exc_list
        ):
            # record ending attempt for timeout failures
            attempt_exc = exc_list[-1]
            _track_retryable_error(operation)(attempt_exc)
        operation.end_with_status(source_exc)
        return source_exc, cause_exc

    return wrapper


def tracked_retry(
    *,
    retry_fn: Callable[..., T],
    operation: ActiveOperationMetric,
    **kwargs,
) -> T:
    """
    Wrapper for retry_rarget or retry_target_stream, which injects methods to
    track the lifecycle of the retry using the provided ActiveOperationMetric
    """
    in_exception_factory = kwargs.pop("exception_factory", _retry_exception_factory)
    kwargs.pop("on_error", None)
    kwargs.pop("sleep_generator", None)
    return retry_fn(
        sleep_generator=operation.backoff_generator,
        on_error=_track_retryable_error(operation),
        exception_factory=_track_terminal_error(operation, in_exception_factory),
        **kwargs,
    )
