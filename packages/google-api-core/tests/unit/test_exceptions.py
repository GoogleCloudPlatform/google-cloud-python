# Copyright 2014 Google LLC
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

import http.client
import json
from unittest import mock

import pytest
import requests

try:
    import grpc
    from grpc_status import rpc_status
except ImportError:  # pragma: NO COVER
    grpc = rpc_status = None

from google.protobuf import any_pb2, json_format
from google.rpc import error_details_pb2, status_pb2

from google.api_core import exceptions


def test_create_google_cloud_error():
    exception = exceptions.GoogleAPICallError("Testing")
    exception.code = 600
    assert str(exception) == "600 Testing"
    assert exception.message == "Testing"
    assert exception.errors == []
    assert exception.response is None


def test_create_google_cloud_error_with_args():
    error = {
        "code": 600,
        "message": "Testing",
    }
    response = mock.sentinel.response
    exception = exceptions.GoogleAPICallError("Testing", [error], response=response)
    exception.code = 600
    assert str(exception) == "600 Testing"
    assert exception.message == "Testing"
    assert exception.errors == [error]
    assert exception.response == response


def test_from_http_status():
    message = "message"
    exception = exceptions.from_http_status(http.client.NOT_FOUND, message)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == message
    assert exception.errors == []


def test_from_http_status_with_errors_and_response():
    message = "message"
    errors = ["1", "2"]
    response = mock.sentinel.response
    exception = exceptions.from_http_status(
        http.client.NOT_FOUND, message, errors=errors, response=response
    )

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == message
    assert exception.errors == errors
    assert exception.response == response


def test_from_http_status_unknown_code():
    message = "message"
    status_code = 156
    exception = exceptions.from_http_status(status_code, message)
    assert exception.code == status_code
    assert exception.message == message


def make_response(content):
    response = requests.Response()
    response._content = content
    response.status_code = http.client.NOT_FOUND
    response.request = requests.Request(
        method="POST", url="https://example.com"
    ).prepare()
    return response


def test_from_http_response_no_content():
    response = make_response(None)

    exception = exceptions.from_http_response(response)

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == "POST https://example.com/: unknown error"
    assert exception.response == response


def test_from_http_response_text_content():
    response = make_response(b"message")
    response.encoding = "UTF8"  # suppress charset_normalizer warning

    exception = exceptions.from_http_response(response)

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == "POST https://example.com/: message"


def test_from_http_response_json_content():
    response = make_response(
        json.dumps({"error": {"message": "json message", "errors": ["1", "2"]}}).encode(
            "utf-8"
        )
    )

    exception = exceptions.from_http_response(response)

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == "POST https://example.com/: json message"
    assert exception.errors == ["1", "2"]


def test_from_http_response_json_list_content():
    response = make_response(
        json.dumps(
            [{"error": {"message": "json message", "errors": ["1", "2"]}}]
        ).encode("utf-8")
    )

    exception = exceptions.from_http_response(response)

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == "POST https://example.com/: json message"
    assert exception.errors == ["1", "2"]


def test_from_http_response_json_list_content_without_error_dict():
    response = make_response(json.dumps(["error message"]).encode("utf-8"))

    exception = exceptions.from_http_response(response)

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == "POST https://example.com/: unknown error"


def test_from_http_response_bad_json_content():
    response = make_response(json.dumps({"meep": "moop"}).encode("utf-8"))

    exception = exceptions.from_http_response(response)

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == "POST https://example.com/: unknown error"


def test_from_http_response_json_unicode_content():
    response = make_response(
        json.dumps(
            {"error": {"message": "\u2019 message", "errors": ["1", "2"]}}
        ).encode("utf-8")
    )

    exception = exceptions.from_http_response(response)

    assert isinstance(exception, exceptions.NotFound)
    assert exception.code == http.client.NOT_FOUND
    assert exception.message == "POST https://example.com/: \u2019 message"
    assert exception.errors == ["1", "2"]


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_status():
    message = "message"
    exception = exceptions.from_grpc_status(grpc.StatusCode.OUT_OF_RANGE, message)
    assert isinstance(exception, exceptions.BadRequest)
    assert isinstance(exception, exceptions.OutOfRange)
    assert exception.code == http.client.BAD_REQUEST
    assert exception.grpc_status_code == grpc.StatusCode.OUT_OF_RANGE
    assert exception.message == message
    assert exception.errors == []


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_status_as_int():
    message = "message"
    exception = exceptions.from_grpc_status(11, message)
    assert isinstance(exception, exceptions.BadRequest)
    assert isinstance(exception, exceptions.OutOfRange)
    assert exception.code == http.client.BAD_REQUEST
    assert exception.grpc_status_code == grpc.StatusCode.OUT_OF_RANGE
    assert exception.message == message
    assert exception.errors == []


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_status_with_errors_and_response():
    message = "message"
    response = mock.sentinel.response
    errors = ["1", "2"]
    exception = exceptions.from_grpc_status(
        grpc.StatusCode.OUT_OF_RANGE, message, errors=errors, response=response
    )

    assert isinstance(exception, exceptions.OutOfRange)
    assert exception.message == message
    assert exception.errors == errors
    assert exception.response == response


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_status_unknown_code():
    message = "message"
    exception = exceptions.from_grpc_status(grpc.StatusCode.OK, message)
    assert exception.grpc_status_code == grpc.StatusCode.OK
    assert exception.message == message


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_error():
    message = "message"
    error = mock.create_autospec(grpc.Call, instance=True)
    error.code.return_value = grpc.StatusCode.INVALID_ARGUMENT
    error.details.return_value = message

    exception = exceptions.from_grpc_error(error)

    assert isinstance(exception, exceptions.BadRequest)
    assert isinstance(exception, exceptions.InvalidArgument)
    assert exception.code == http.client.BAD_REQUEST
    assert exception.grpc_status_code == grpc.StatusCode.INVALID_ARGUMENT
    assert exception.message == message
    assert exception.errors == [error]
    assert exception.response == error


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_error_non_call():
    message = "message"
    error = mock.create_autospec(grpc.RpcError, instance=True)
    error.__str__.return_value = message

    exception = exceptions.from_grpc_error(error)

    assert isinstance(exception, exceptions.GoogleAPICallError)
    assert exception.code is None
    assert exception.grpc_status_code is None
    assert exception.message == message
    assert exception.errors == [error]
    assert exception.response == error


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_error_bare_call():
    message = "Testing"

    class TestingError(grpc.Call, grpc.RpcError):
        def __init__(self, exception):
            self.exception = exception

        def code(self):
            return self.exception.grpc_status_code

        def details(self):
            return message

    nested_message = "message"
    error = TestingError(exceptions.GoogleAPICallError(nested_message))

    exception = exceptions.from_grpc_error(error)

    assert isinstance(exception, exceptions.GoogleAPICallError)
    assert exception.code is None
    assert exception.grpc_status_code is None
    assert exception.message == message
    assert exception.errors == [error]
    assert exception.response == error
    assert exception.details == []


def create_bad_request_details():
    bad_request_details = error_details_pb2.BadRequest()
    field_violation = bad_request_details.field_violations.add()
    field_violation.field = "document.content"
    field_violation.description = "Must have some text content to annotate."
    status_detail = any_pb2.Any()
    status_detail.Pack(bad_request_details)
    return status_detail


def create_error_info_details():
    info = error_details_pb2.ErrorInfo(
        reason="SERVICE_DISABLED",
        domain="googleapis.com",
        metadata={
            "consumer": "projects/455411330361",
            "service": "translate.googleapis.com",
        },
    )
    status_detail = any_pb2.Any()
    status_detail.Pack(info)
    return status_detail


def test_error_details_from_rest_response():
    bad_request_detail = create_bad_request_details()
    error_info_detail = create_error_info_details()
    status = status_pb2.Status()
    status.code = 3
    status.message = (
        "3 INVALID_ARGUMENT: One of content, or gcs_content_uri must be set."
    )
    status.details.append(bad_request_detail)
    status.details.append(error_info_detail)

    # See JSON schema in https://cloud.google.com/apis/design/errors#http_mapping
    http_response = make_response(
        json.dumps(
            {"error": json.loads(json_format.MessageToJson(status, sort_keys=True))}
        ).encode("utf-8")
    )
    exception = exceptions.from_http_response(http_response)
    want_error_details = [
        json.loads(json_format.MessageToJson(bad_request_detail)),
        json.loads(json_format.MessageToJson(error_info_detail)),
    ]
    assert want_error_details == exception.details

    # 404 POST comes from make_response.
    assert str(exception) == (
        "404 POST https://example.com/: 3 INVALID_ARGUMENT:"
        " One of content, or gcs_content_uri must be set."
        " [{'@type': 'type.googleapis.com/google.rpc.BadRequest',"
        " 'fieldViolations': [{'description': 'Must have some text content to annotate.',"
        " 'field': 'document.content'}]},"
        " {'@type': 'type.googleapis.com/google.rpc.ErrorInfo',"
        " 'domain': 'googleapis.com',"
        " 'metadata': {'consumer': 'projects/455411330361',"
        " 'service': 'translate.googleapis.com'},"
        " 'reason': 'SERVICE_DISABLED'}]"
    )


def test_error_details_from_v1_rest_response():
    response = make_response(
        json.dumps(
            {"error": {"message": "\u2019 message", "errors": ["1", "2"]}}
        ).encode("utf-8")
    )
    exception = exceptions.from_http_response(response)
    assert exception.details == []
    assert (
        exception.reason is None
        and exception.domain is None
        and exception.metadata is None
    )


@pytest.mark.skipif(grpc is None, reason="gRPC not importable")
def test_error_details_from_grpc_response():
    status = rpc_status.status_pb2.Status()
    status.code = 3
    status.message = (
        "3 INVALID_ARGUMENT: One of content, or gcs_content_uri must be set."
    )
    status_br_detail = create_bad_request_details()
    status_ei_detail = create_error_info_details()
    status.details.append(status_br_detail)
    status.details.append(status_ei_detail)

    # The actual error doesn't matter as long as its grpc.Call,
    # because from_call is mocked.
    error = mock.create_autospec(grpc.Call, instance=True)
    with mock.patch("grpc_status.rpc_status.from_call") as m:
        m.return_value = status
        exception = exceptions.from_grpc_error(error)

    bad_request_detail = error_details_pb2.BadRequest()
    error_info_detail = error_details_pb2.ErrorInfo()
    status_br_detail.Unpack(bad_request_detail)
    status_ei_detail.Unpack(error_info_detail)
    assert exception.details == [bad_request_detail, error_info_detail]
    assert exception.reason == error_info_detail.reason
    assert exception.domain == error_info_detail.domain
    assert exception.metadata == error_info_detail.metadata


@pytest.mark.skipif(grpc is None, reason="gRPC not importable")
def test_error_details_from_grpc_response_unknown_error():
    status_detail = any_pb2.Any()

    status = rpc_status.status_pb2.Status()
    status.code = 3
    status.message = (
        "3 INVALID_ARGUMENT: One of content, or gcs_content_uri must be set."
    )
    status.details.append(status_detail)

    error = mock.create_autospec(grpc.Call, instance=True)
    with mock.patch("grpc_status.rpc_status.from_call") as m:
        m.return_value = status
        exception = exceptions.from_grpc_error(error)
    assert exception.details == [status_detail]
    assert (
        exception.reason is None
        and exception.domain is None
        and exception.metadata is None
    )


@pytest.mark.skipif(grpc is None, reason="No grpc")
def test_from_grpc_error_misleading_404():
    message = "Received http2 header with status: 404"
    error = mock.create_autospec(grpc.Call, instance=True)
    error.code.return_value = grpc.StatusCode.UNIMPLEMENTED
    error.details.return_value = message

    exception = exceptions.from_grpc_error(error)

    assert isinstance(exception, exceptions.MethodNotImplemented)
    assert exception.grpc_status_code == grpc.StatusCode.UNIMPLEMENTED
    assert "Received http2 header with status: 404" in exception.message
    assert "api_endpoint" in exception.message
