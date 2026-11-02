# Copyright 2022 Google LLC
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

import dataclasses
import enum
import typing
from unittest import mock

import pytest

from google.api_core import exceptions, extended_operation, retry

TEST_OPERATION_NAME = "test/extended_operation"


@dataclasses.dataclass(frozen=True)
class CustomOperation:
    class StatusCode(enum.Enum):
        UNKNOWN = 0
        DONE = 1
        PENDING = 2

    class LROCustomErrors:
        class LROCustomError:
            def __init__(self, code: str = "", message: str = ""):
                self.code = code
                self.message = message

        def __init__(self, errors: typing.List[LROCustomError] = []):
            self.errors = errors

    name: str
    status: StatusCode
    error_code: typing.Optional[int] = None
    error_message: typing.Optional[str] = None
    armor_class: typing.Optional[int] = None
    # Note: `error` can be removed once proposal A from
    # b/284179390 is implemented.
    error: typing.Optional[LROCustomErrors] = None

    # Note: in generated clients, this property must be generated for each
    # extended operation message type.
    # The status may be an enum, a string, or a bool. If it's a string or enum,
    # its text is compared to the string "DONE".
    @property
    def done(self):
        return self.status.name == "DONE"


def make_extended_operation(responses=None):
    client_operations_responses = responses or [
        CustomOperation(
            name=TEST_OPERATION_NAME, status=CustomOperation.StatusCode.PENDING
        )
    ]

    refresh = mock.Mock(spec=["__call__"], side_effect=client_operations_responses)
    refresh.responses = client_operations_responses
    cancel = mock.Mock(spec=["__call__"])
    extended_operation_future = extended_operation.ExtendedOperation.make(
        refresh,
        cancel,
        client_operations_responses[0],
    )

    return extended_operation_future, refresh, cancel


def test_constructor():
    ex_op, refresh, _ = make_extended_operation()
    assert ex_op._extended_operation == refresh.responses[0]
    assert not ex_op.cancelled()
    assert not ex_op.done()
    assert ex_op.name == TEST_OPERATION_NAME
    assert ex_op.status == CustomOperation.StatusCode.PENDING
    assert ex_op.error_code is None
    assert ex_op.error_message is None


def test_done():
    responses = [
        CustomOperation(
            name=TEST_OPERATION_NAME, status=CustomOperation.StatusCode.PENDING
        ),
        # Second response indicates that the operation has finished.
        CustomOperation(
            name=TEST_OPERATION_NAME, status=CustomOperation.StatusCode.DONE
        ),
        # Bumper to make sure we stop polling on DONE.
        CustomOperation(
            name=TEST_OPERATION_NAME,
            status=CustomOperation.StatusCode.DONE,
            error_message="Gone too far!",
        ),
    ]
    ex_op, refresh, _ = make_extended_operation(responses)

    # Start out not done.
    assert not ex_op.done()
    assert refresh.call_count == 1

    # Refresh brings us to the done state.
    assert ex_op.done()
    assert refresh.call_count == 2
    assert not ex_op.error_message

    # Make sure that subsequent checks are no-ops.
    assert ex_op.done()
    assert refresh.call_count == 2
    assert not ex_op.error_message


def test_cancellation():
    responses = [
        CustomOperation(
            name=TEST_OPERATION_NAME, status=CustomOperation.StatusCode.PENDING
        ),
        # Second response indicates that the operation was cancelled.
        CustomOperation(
            name=TEST_OPERATION_NAME, status=CustomOperation.StatusCode.DONE
        ),
    ]
    ex_op, _, cancel = make_extended_operation(responses)

    assert not ex_op.cancelled()

    assert ex_op.cancel()
    assert ex_op.cancelled()
    cancel.assert_called_once_with()

    # Cancelling twice should have no effect.
    assert not ex_op.cancel()
    cancel.assert_called_once_with()


def test_done_w_retry():
    # Not sure what's going on here with the coverage, so just ignore it.
    test_retry = retry.Retry(predicate=lambda x: True)  # pragma: NO COVER

    responses = [
        CustomOperation(
            name=TEST_OPERATION_NAME, status=CustomOperation.StatusCode.PENDING
        ),
        CustomOperation(
            name=TEST_OPERATION_NAME, status=CustomOperation.StatusCode.DONE
        ),
    ]

    ex_op, refresh, _ = make_extended_operation(responses)

    ex_op.done(retry=test_retry)

    refresh.assert_called_once_with(retry=test_retry)


def test_error():
    responses = [
        CustomOperation(
            name=TEST_OPERATION_NAME,
            status=CustomOperation.StatusCode.DONE,
            error_code=400,
            error_message="Bad request",
        ),
    ]

    ex_op, _, _ = make_extended_operation(responses)

    # Defaults to CallError when grpc is not installed
    with pytest.raises(exceptions.BadRequest):
        ex_op.result()

    # Test GCE custom LRO Error. See b/284179390
    # Note: This test case can be removed once proposal A from
    # b/284179390 is implemented.
    _EXCEPTION_CODE = "INCOMPATIBLE_BACKEND_SERVICES"
    _EXCEPTION_MESSAGE = "Validation failed for instance group"
    responses = [
        CustomOperation(
            name=TEST_OPERATION_NAME,
            status=CustomOperation.StatusCode.DONE,
            error_code=400,
            error_message="Bad request",
            error=CustomOperation.LROCustomErrors(
                errors=[
                    CustomOperation.LROCustomErrors.LROCustomError(
                        code=_EXCEPTION_CODE, message=_EXCEPTION_MESSAGE
                    )
                ]
            ),
        ),
    ]

    ex_op, _, _ = make_extended_operation(responses)

    # Defaults to CallError when grpc is not installed
    with pytest.raises(
        exceptions.BadRequest, match=f"{_EXCEPTION_CODE}: {_EXCEPTION_MESSAGE}"
    ):
        ex_op.result()

    # Inconsistent result
    responses = [
        CustomOperation(
            name=TEST_OPERATION_NAME,
            status=CustomOperation.StatusCode.DONE,
            error_code=2112,
        ),
    ]

    ex_op, _, _ = make_extended_operation(responses)

    with pytest.raises(exceptions.GoogleAPICallError):
        ex_op.result()


def test_pass_through():
    responses = [
        CustomOperation(
            name=TEST_OPERATION_NAME,
            status=CustomOperation.StatusCode.PENDING,
            armor_class=10,
        ),
        CustomOperation(
            name=TEST_OPERATION_NAME,
            status=CustomOperation.StatusCode.DONE,
            armor_class=20,
        ),
    ]
    ex_op, _, _ = make_extended_operation(responses)

    assert ex_op.armor_class == 10
    ex_op.result()
    assert ex_op.armor_class == 20
