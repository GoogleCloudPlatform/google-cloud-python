# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from google import showcase
from google.rpc import error_details_pb2
from google.protobuf import any_pb2
from grpc_status import rpc_status
from google.api_core import exceptions


def create_status(error_details=None):
    status = rpc_status.status_pb2.Status()
    status.code = 3
    status.message = "test"
    status_detail = any_pb2.Any()
    if error_details:
        status_detail.Pack(error_details)
    status.details.append(status_detail)
    return status


def test_bad_request_details(echo):
    # TODO(dovs): reenable when transcoding requests with an "Any"
    # field is properly handled
    # See https://github.com/googleapis/proto-plus-python/issues/285
    # for background and tracking.
    if "rest" in str(echo.transport).lower():
        return

    def create_bad_request_details():
        bad_request_details = error_details_pb2.BadRequest()
        field_violation = bad_request_details.field_violations.add()
        field_violation.field = "test field"
        field_violation.description = "test description"
        return bad_request_details

    bad_request_details = create_bad_request_details()
    status = create_status(bad_request_details)

    with pytest.raises(exceptions.GoogleAPICallError) as e:
        _ = echo.echo(
            showcase.EchoRequest(
                error=status,
            )
        )

    # Note: error details are exposed as e.value.details.
    assert e.value.details == [bad_request_details]


def test_precondition_failure_details(echo):
    # TODO(dovs): reenable when transcoding requests with an "Any"
    # field is properly handled
    # See https://github.com/googleapis/proto-plus-python/issues/285
    # for background and tracking.
    if "rest" in str(echo.transport).lower():
        return

    def create_precondition_failure_details():
        pf_details = error_details_pb2.PreconditionFailure()
        violation = pf_details.violations.add()
        violation.type = "test type"
        violation.subject = "test subject"
        violation.description = "test description"
        return pf_details

    pf_details = create_precondition_failure_details()
    status = create_status(pf_details)

    with pytest.raises(exceptions.GoogleAPICallError) as e:
        _ = echo.echo(
            showcase.EchoRequest(
                error=status,
            )
        )

    # Note: error details are exposed as e.value.details.
    assert e.value.details == [pf_details]


def test_unknown_details(echo):
    # TODO(dovs): reenable when transcoding requests with an "Any"
    # field is properly handled
    # See https://github.com/googleapis/proto-plus-python/issues/285
    # for background and tracking.
    if "rest" in str(echo.transport).lower():
        return

    status = create_status()
    with pytest.raises(exceptions.GoogleAPICallError) as e:
        _ = echo.echo(
            showcase.EchoRequest(
                error=status,
            )
        )

    # Note: error details are exposed as e.value.details.
    assert e.value.details == list(status.details)
