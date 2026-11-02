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
#
"""
Helper functions used in various places in the library.
"""

from __future__ import annotations

import enum
import time
from collections import namedtuple
from typing import (
    TYPE_CHECKING,
    Callable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core.retry import RetryFailureReason, exponential_sleep_generator
from google.protobuf import any_pb2, message
from google.rpc import code_pb2, status_pb2

from google.cloud.bigtable.data.exceptions import (
    MutationsExceptionGroup,
    RetryExceptionGroup,
)
from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

if TYPE_CHECKING:
    import grpc

    from google.cloud.bigtable.data._async.client import _DataApiTargetAsync
    from google.cloud.bigtable.data._sync_autogen.client import _DataApiTarget

"""
Helper functions used in various places in the library.
"""

# Type alias for the output of sample_keys
RowKeySamples = List[Tuple[bytes, int]]

# type alias for the output of query.shard()
ShardedQuery = List[ReadRowsQuery]

# used by read_rows_sharded to limit how many requests are attempted in parallel
_CONCURRENCY_LIMIT = 10

# used by every data client as a default project name for testing on Bigtable emulator.
_DEFAULT_BIGTABLE_EMULATOR_CLIENT = "google-cloud-bigtable-emulator"

# Internal error messages that can be retried during ReadRows. Internal error messages with this error
# text should be treated as Unavailable error messages with the same error text, and will therefore be
# treated as Unavailable errors rather than Internal errors.
_RETRYABLE_INTERNAL_ERROR_MESSAGES = (
    "rst_stream",
    "rst stream",
    "received unexpected eos on data frame from server",
)

# used to identify an active bigtable resource that needs to be warmed through PingAndWarm
# each instance/app_profile_id pair needs to be individually tracked
_WarmedInstanceKey = namedtuple(
    "_WarmedInstanceKey", ["instance_name", "app_profile_id"]
)


# enum used on method calls when table defaults should be used
class TABLE_DEFAULT(enum.Enum):
    # default for mutate_row, sample_row_keys, check_and_mutate_row, and read_modify_write_row
    DEFAULT = "DEFAULT"
    # default for read_rows, read_rows_stream, read_rows_sharded, row_exists, and read_row
    READ_ROWS = "READ_ROWS_DEFAULT"
    # default for bulk_mutate_rows and mutations_batcher
    MUTATE_ROWS = "MUTATE_ROWS_DEFAULT"


def _attempt_timeout_generator(
    per_request_timeout: float | None, operation_timeout: float
):
    """
    Generator that yields the timeout value for each attempt of a retry loop.

    Will return per_request_timeout until the operation_timeout is approached,
    at which point it will return the remaining time in the operation_timeout.

    Args:
        per_request_timeout: The timeout value to use for each request, in seconds.
            If None, the operation_timeout will be used for each request.
        operation_timeout: The timeout value to use for the entire operationm in seconds.
    Yields:
        float: The timeout value to use for the next request, in seonds
    """
    per_request_timeout = (
        per_request_timeout if per_request_timeout is not None else operation_timeout
    )
    deadline = operation_timeout + time.monotonic()
    while True:
        yield max(0, min(per_request_timeout, deadline - time.monotonic()))


def _retry_exception_factory(
    exc_list: list[Exception],
    reason: RetryFailureReason,
    timeout_val: float | None,
) -> tuple[Exception, Exception | None]:
    """
    Build retry error based on exceptions encountered during operation

    Args:
        exc_list: list of exceptions encountered during operation
        is_timeout: whether the operation failed due to timeout
        timeout_val: the operation timeout value in seconds, for constructing
            the error message
    Returns:
        tuple[Exception, Exception|None]:
            tuple of the exception to raise, and a cause exception if applicable
    """
    exc_list = exc_list.copy()
    if reason == RetryFailureReason.TIMEOUT:
        timeout_val_str = f"of {timeout_val:0.1f}s " if timeout_val is not None else ""
        # if failed due to timeout, raise deadline exceeded as primary exception
        source_exc: Exception = core_exceptions.DeadlineExceeded(
            f"operation_timeout{timeout_val_str} exceeded"
        )
    elif exc_list:
        # otherwise, raise non-retryable error as primary exception
        source_exc = exc_list.pop()
    else:
        source_exc = RuntimeError("failed with unspecified exception")
    # use the retry exception group as the cause of the exception
    cause_exc: Exception | None = RetryExceptionGroup(exc_list) if exc_list else None
    source_exc.__cause__ = cause_exc
    return source_exc, cause_exc


def _rst_stream_aware_predicate(
    *exception_types: type[Exception],
) -> Callable[[Exception], bool]:
    """A custom retry predicate.

    This predicate treats Internal error messages with RST_STREAM errors as
    ServiceUnavailable errors and will retry them if the Unavailable exception is retryable.

    Args:
        exception_types: Exception types to be retried during operation

    Returns:
        Callable[[Exception], bool]: A retry predicate that takes in an exception and
            returns whether or not that exception is retryable
    """
    # predicate to check for retryable error types
    if_exception_type = retries.if_exception_type(*exception_types)

    # special case: treat InternalServerError with rst_stream error message as ServiceUnavailable
    def rst_check(e):
        return (
            core_exceptions.ServiceUnavailable in exception_types
            and isinstance(e, core_exceptions.InternalServerError)
            and isinstance(e.message, str)
            and any(m in e.message.lower() for m in _RETRYABLE_INTERNAL_ERROR_MESSAGES)
        )

    return lambda e: if_exception_type(e) or rst_check(e)


def _get_timeouts(
    operation: float | TABLE_DEFAULT,
    attempt: float | None | TABLE_DEFAULT,
    table: "_DataApiTargetAsync" | "_DataApiTarget",
) -> tuple[float, float]:
    """
    Convert passed in timeout values to floats, using table defaults if necessary.

    attempt will use operation value if None, or if larger than operation.

    Will call _validate_timeouts on the outputs, and raise ValueError if the
    resulting timeouts are invalid.

    Args:
        operation: The timeout value to use for the entire operation, in seconds.
        attempt: The timeout value to use for each attempt, in seconds.
        table: The table to use for default values.
    Returns:
        tuple[float, float]: A tuple of (operation_timeout, attempt_timeout)
    """
    # load table defaults if necessary
    if operation == TABLE_DEFAULT.DEFAULT:
        final_operation = table.default_operation_timeout
    elif operation == TABLE_DEFAULT.READ_ROWS:
        final_operation = table.default_read_rows_operation_timeout
    elif operation == TABLE_DEFAULT.MUTATE_ROWS:
        final_operation = table.default_mutate_rows_operation_timeout
    else:
        final_operation = operation
    if attempt == TABLE_DEFAULT.DEFAULT:
        attempt = table.default_attempt_timeout
    elif attempt == TABLE_DEFAULT.READ_ROWS:
        attempt = table.default_read_rows_attempt_timeout
    elif attempt == TABLE_DEFAULT.MUTATE_ROWS:
        attempt = table.default_mutate_rows_attempt_timeout

    return _align_timeouts(final_operation, attempt)


def _align_timeouts(operation: float, attempt: float | None) -> tuple[float, float]:
    """
    Convert passed in timeout values to floats.

    attempt will use operation value if None, or if larger than operation.

    Will call _validate_timeouts on the outputs, and raise ValueError if the
    resulting timeouts are invalid.

    Args:
        operation: The timeout value to use for the entire operation, in seconds.
        attempt: The timeout value to use for each attempt, in seconds.
    Returns:
        tuple[float, float]: A tuple of (operation_timeout, attempt_timeout)
    """
    if attempt is None:
        # no timeout specified, use operation timeout for both
        final_attempt = operation
    else:
        # cap attempt timeout at operation timeout
        final_attempt = min(attempt, operation) if operation else attempt

    _validate_timeouts(operation, final_attempt, allow_none=False)
    return operation, final_attempt


def _get_statuses_from_mutations_exception_group(
    exc_group: MutationsExceptionGroup, batch_size: int
) -> list[status_pb2.Status]:
    """
    Helper function that populates a list of Status objects with exception information from
    the exception group.

    Args:
        exc_group: The exception group from a mutate rows operation
        batch_size: How many RowMutationGroups were provided to the batch
    Returns:
        list[status_pb2.Status]: A list of Status proto objects
    """
    # We exception handle as follows:
    #
    # 1. Each exception in the error group is a FailedMutationEntryError, and its
    #    cause is either a singular exception or a RetryExceptionGroup consisting of
    #    multiple exceptions.
    #
    # 2. In the case of a singular exception, if the error does not have a gRPC status
    #    code, we return a status code of UNKNOWN.
    #
    # 3. In the case of a RetryExceptionGroup, we use terminal exception in the exception
    #    group and process that.
    statuses = [status_pb2.Status(code=code_pb2.OK) for _ in range(batch_size)]
    for error in exc_group.exceptions:
        if isinstance(error.index, int) and 0 <= error.index < len(statuses):
            cause = error.__cause__
            if isinstance(cause, RetryExceptionGroup):
                statuses[error.index] = _get_status(cause.exceptions[-1])
            else:
                statuses[error.index] = _get_status(cause)
    return statuses


def _get_status(exc: Optional[Exception]) -> status_pb2.Status:
    """
    Helper function that returns a Status object corresponding to the given exception.

    Args:
        exc: An exception to be converted into a Status.
    Returns:
        status_pb2.Status: A Status proto object.
    """
    if isinstance(exc, core_exceptions.GoogleAPICallError):
        grpc_code = exc.grpc_status_code
        if grpc_code is not None:
            try:
                details: list[any_pb2.Any] = []
                for detail in exc.details or ():
                    try:
                        if isinstance(detail, any_pb2.Any):
                            details.append(detail)
                        elif isinstance(detail, message.Message):
                            packed = any_pb2.Any()
                            packed.Pack(detail)
                            details.append(packed)
                        elif isinstance(getattr(detail, "_pb", None), message.Message):
                            packed = any_pb2.Any()
                            packed.Pack(detail._pb)
                            details.append(packed)
                    except Exception:
                        continue
                return status_pb2.Status(
                    code=grpc_code.value[0],
                    message=exc.message or "",
                    details=details,
                )
            except Exception:
                pass

    return status_pb2.Status(
        code=code_pb2.UNKNOWN,
        message=_exc_message(exc),
    )


def _exc_message(exc: Optional[Exception]) -> str:
    """
    Helper function that renders an exception as a string, without raising.

    ``GoogleAPICallError.__str__`` reads ``exc.details``, which raises if the
    exception was built with a malformed ``details`` value, so fall back to the
    raw message when that happens.

    Args:
        exc: The exception to render.
    Returns:
        str: A description of the exception.
    """
    if exc is None:
        return "An unknown error has occurred"
    try:
        return str(exc)
    except Exception:
        raw_message = getattr(exc, "message", None)
        return raw_message if isinstance(raw_message, str) else type(exc).__name__


def _validate_timeouts(
    operation_timeout: float, attempt_timeout: float | None, allow_none: bool = False
):
    """
    Helper function that will verify that timeout values are valid, and raise
    an exception if they are not.

    Args:
        operation_timeout: The timeout value to use for the entire operation, in seconds.
        attempt_timeout: The timeout value to use for each attempt, in seconds.
        allow_none: If True, attempt_timeout can be None. If False, None values will raise an exception.
    Raises:
        ValueError: if operation_timeout or attempt_timeout are invalid.
    """
    if operation_timeout is None:
        raise ValueError("operation_timeout cannot be None")
    if operation_timeout <= 0:
        raise ValueError("operation_timeout must be greater than 0")
    if not allow_none and attempt_timeout is None:
        raise ValueError("attempt_timeout must not be None")
    elif attempt_timeout is not None:
        if attempt_timeout <= 0:
            raise ValueError("attempt_timeout must be greater than 0")


def _get_error_type(
    call_code: Union["grpc.StatusCode", int, type[Exception]],
) -> type[Exception]:
    """Helper function for ensuring the object is an exception type.
    If it is not, the proper GoogleAPICallError type is infered from the status
    code.

    Args:
      - call_code: Exception type or gRPC status code.
    Raises:
      - ValueError: if call_code is not a valid retryable gRPC error status code
        or exception type.
    """
    if isinstance(call_code, type):
        return call_code
    if isinstance(call_code, bool):
        raise ValueError(f"Invalid gRPC error status code: {call_code!r}")
    error_type = type(core_exceptions.from_grpc_status(call_code, ""))
    # from_grpc_status falls back to the base GoogleAPICallError for codes it
    # doesn't recognize (including OK / 0). Returning the base class here would
    # make retries.if_exception_type match every GoogleAPICallError subclass,
    # silently turning all errors into retryable ones, so reject it instead.
    if error_type is core_exceptions.GoogleAPICallError:
        raise ValueError(f"Invalid gRPC error status code: {call_code!r}")
    return error_type


def _get_retryable_errors(
    call_codes: Sequence["grpc.StatusCode" | int | type[Exception]] | TABLE_DEFAULT,
    table: "_DataApiTargetAsync" | "_DataApiTarget",
) -> list[type[Exception]]:
    """
    Convert passed in retryable error codes to a list of exception types.

    Args:
        call_codes: The error codes to convert. Can be a list of grpc.StatusCode values,
            int values, or Exception types, or a TABLE_DEFAULT value.
        table: The table to use for default values.
    Returns:
        list[type[Exception]]: A list of exception types to retry on.
    """
    # load table defaults if necessary
    if call_codes == TABLE_DEFAULT.DEFAULT:
        call_codes = table.default_retryable_errors
    elif call_codes == TABLE_DEFAULT.READ_ROWS:
        call_codes = table.default_read_rows_retryable_errors
    elif call_codes == TABLE_DEFAULT.MUTATE_ROWS:
        call_codes = table.default_mutate_rows_retryable_errors

    return [_get_error_type(e) for e in call_codes]


class TrackedBackoffGenerator:
    """
    Generator class for exponential backoff sleep times.
    This implementation builds on top of api_core.retries.exponential_sleep_generator,
    adding the ability to retrieve previous values using get_attempt_backoff(idx).
    This is used by the Metrics class to track the sleep times used for each attempt.
    """

    def __init__(self, initial=0.01, maximum=60, multiplier=2):
        self.history = []
        self.subgenerator = exponential_sleep_generator(
            initial=initial, maximum=maximum, multiplier=multiplier
        )
        self._next_override: float | None = None

    def __iter__(self):
        return self

    def set_next(self, next_value: float):
        """
        Set the next backoff value, instead of generating one from subgenerator.
        After the value is yielded, it will go back to using self.subgenerator.

        If set_next is called twice before the next() is called, only the latest
        value will be used and others discarded

        Args:
            next_value: the upcomming value to yield when next() is called
        Raises:
            ValueError: if next_value is negative
        """
        if next_value < 0:
            raise ValueError("backoff value cannot be less than 0")
        self._next_override = next_value

    def __next__(self) -> float:
        if self._next_override is not None:
            next_backoff = self._next_override
            self._next_override = None
        else:
            next_backoff = next(self.subgenerator)
        self.history.append(next_backoff)
        return next_backoff

    def get_attempt_backoff(self, attempt_idx) -> float:
        """
        returns the backoff time for a specific attempt index, starting at 0.

        Args:
            attempt_idx: the index of the attempt to return backoff for
        Raises:
            IndexError: if attempt_idx is negative, or not in history
        """
        if attempt_idx < 0:
            raise IndexError("received negative attempt number")
        return self.history[attempt_idx]
