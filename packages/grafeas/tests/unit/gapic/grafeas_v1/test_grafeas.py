# -*- coding: utf-8 -*-
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
#
import asyncio
import json
import math
import os
from collections.abc import AsyncIterable, Iterable, Mapping, Sequence
from unittest import mock
from unittest.mock import AsyncMock

import grpc
import pytest
from google.api_core import api_core_version
from google.protobuf import json_format
from grpc.experimental import aio
from proto.marshal.rules import wrappers
from proto.marshal.rules.dates import DurationRule, TimestampRule
from requests import PreparedRequest, Request, Response
from requests.sessions import Session

try:
    from google.auth.aio import credentials as ga_credentials_async

    HAS_GOOGLE_AUTH_AIO = True
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

import google.auth
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
from google.api_core import (
    client_options,
    gapic_v1,
    grpc_helpers,
    grpc_helpers_async,
    path_template,
)
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.oauth2 import service_account

from grafeas.grafeas_v1.services.grafeas import (
    GrafeasAsyncClient,
    GrafeasClient,
    pagers,
    transports,
)
from grafeas.grafeas_v1.types import (
    attestation,
    build,
    common,
    compliance,
    cvss,
    deployment,
    discovery,
    dsse_attestation,
    grafeas,
    image,
    intoto_provenance,
    intoto_statement,
    package,
    provenance,
    risk,
    sbom,
    secret,
    severity,
    slsa_provenance,
    slsa_provenance_zero_two,
    upgrade,
    vex,
    vulnerability,
)

CRED_INFO_JSON = {
    "credential_source": "/path/to/file",
    "credential_type": "service account credentials",
    "principal": "service-account@example.com",
}
CRED_INFO_STRING = json.dumps(CRED_INFO_JSON)


@pytest.fixture(autouse=True)
def disable_mtls_env():
    with mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "false",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "false",
        },
    ):
        yield


async def mock_async_gen(data, chunk_size=1):
    for i in range(0, len(data)):  # pragma: NO COVER
        chunk = data[i : i + chunk_size]
        yield chunk.encode("utf-8")


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# TODO: use async auth anon credentials by default once the minimum version of google-auth is upgraded.
# See related issue: https://github.com/googleapis/gapic-generator-python/issues/2107.
def async_anonymous_credentials():
    if HAS_GOOGLE_AUTH_AIO:
        return ga_credentials_async.AnonymousCredentials()
    return ga_credentials.AnonymousCredentials()


@pytest.fixture(autouse=True)
def set_event_loop():
    try:
        asyncio.get_running_loop()
        yield
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            yield
        finally:
            loop.close()
            asyncio.set_event_loop(None)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetOccurrenceRequest(),
        {},
    ],
)
def test_get_occurrence(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence(
            name="name_value",
            resource_uri="resource_uri_value",
            note_name="note_name_value",
            kind=common.NoteKind.VULNERABILITY,
            remediation="remediation_value",
        )
        response = client.get_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.GetOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


def test_get_occurrence_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.GetOccurrenceRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_occurrence(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_occurrence_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_occurrence] = mock_rpc
        request = {}
        client.get_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_occurrence_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_occurrence
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_occurrence
        ] = mock_rpc

        request = {}
        await client.get_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetOccurrenceRequest(),
        {},
    ],
)
async def test_get_occurrence_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Occurrence(
                name="name_value",
                resource_uri="resource_uri_value",
                note_name="note_name_value",
                kind=common.NoteKind.VULNERABILITY,
                remediation="remediation_value",
            )
        )
        response = await client.get_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.GetOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


def test_get_occurrence_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.GetOccurrenceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        call.return_value = grafeas.Occurrence()
        client.get_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_occurrence_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.GetOccurrenceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Occurrence())
        await client.get_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_occurrence_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_occurrence(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_occurrence_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_occurrence(
            grafeas.GetOccurrenceRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_occurrence_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Occurrence())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_occurrence(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_occurrence_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_occurrence(
            grafeas.GetOccurrenceRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListOccurrencesRequest(),
        {},
    ],
)
def test_list_occurrences(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListOccurrencesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )
        response = client.list_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.ListOccurrencesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOccurrencesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_occurrences_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.ListOccurrencesRequest(
        parent="parent_value",
        filter="filter_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_occurrences(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListOccurrencesRequest(
            parent="parent_value",
            filter="filter_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_occurrences_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_occurrences in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_occurrences] = (
            mock_rpc
        )
        request = {}
        client.list_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_occurrences_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_occurrences
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_occurrences
        ] = mock_rpc

        request = {}
        await client.list_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListOccurrencesRequest(),
        {},
    ],
)
async def test_list_occurrences_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListOccurrencesResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.ListOccurrencesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOccurrencesAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_occurrences_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.ListOccurrencesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        call.return_value = grafeas.ListOccurrencesResponse()
        client.list_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_occurrences_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.ListOccurrencesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListOccurrencesResponse()
        )
        await client.list_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_occurrences_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListOccurrencesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_occurrences(
            parent="parent_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


def test_list_occurrences_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_occurrences(
            grafeas.ListOccurrencesRequest(),
            parent="parent_value",
            filter="filter_value",
        )


@pytest.mark.asyncio
async def test_list_occurrences_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListOccurrencesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListOccurrencesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_occurrences(
            parent="parent_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_occurrences_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_occurrences(
            grafeas.ListOccurrencesRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_occurrences_pager(transport_name: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_occurrences(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, grafeas.Occurrence) for i in results)


def test_list_occurrences_pages(transport_name: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_occurrences(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_occurrences_async_pager():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_occurrences), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_occurrences(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, grafeas.Occurrence) for i in responses)


@pytest.mark.asyncio
async def test_list_occurrences_async_pages():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_occurrences), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_occurrences(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.DeleteOccurrenceRequest(),
        {},
    ],
)
def test_delete_occurrence(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.DeleteOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_occurrence_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.DeleteOccurrenceRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_occurrence(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteOccurrenceRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_occurrence_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_occurrence] = (
            mock_rpc
        )
        request = {}
        client.delete_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_occurrence_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_occurrence
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_occurrence
        ] = mock_rpc

        request = {}
        await client.delete_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.DeleteOccurrenceRequest(),
        {},
    ],
)
async def test_delete_occurrence_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.DeleteOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_occurrence_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.DeleteOccurrenceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        call.return_value = None
        client.delete_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_occurrence_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.DeleteOccurrenceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_delete_occurrence_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_occurrence(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_occurrence_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_occurrence(
            grafeas.DeleteOccurrenceRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_occurrence_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_occurrence(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_occurrence_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_occurrence(
            grafeas.DeleteOccurrenceRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.CreateOccurrenceRequest(),
        {},
    ],
)
def test_create_occurrence(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence(
            name="name_value",
            resource_uri="resource_uri_value",
            note_name="note_name_value",
            kind=common.NoteKind.VULNERABILITY,
            remediation="remediation_value",
        )
        response = client.create_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.CreateOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


def test_create_occurrence_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.CreateOccurrenceRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_occurrence(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateOccurrenceRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_occurrence_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_occurrence] = (
            mock_rpc
        )
        request = {}
        client.create_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_occurrence_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_occurrence
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_occurrence
        ] = mock_rpc

        request = {}
        await client.create_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.CreateOccurrenceRequest(),
        {},
    ],
)
async def test_create_occurrence_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Occurrence(
                name="name_value",
                resource_uri="resource_uri_value",
                note_name="note_name_value",
                kind=common.NoteKind.VULNERABILITY,
                remediation="remediation_value",
            )
        )
        response = await client.create_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.CreateOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


def test_create_occurrence_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.CreateOccurrenceRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        call.return_value = grafeas.Occurrence()
        client.create_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_occurrence_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.CreateOccurrenceRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Occurrence())
        await client.create_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_create_occurrence_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_occurrence(
            parent="parent_value",
            occurrence=grafeas.Occurrence(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].occurrence
        mock_val = grafeas.Occurrence(name="name_value")
        assert arg == mock_val


def test_create_occurrence_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_occurrence(
            grafeas.CreateOccurrenceRequest(),
            parent="parent_value",
            occurrence=grafeas.Occurrence(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_occurrence_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Occurrence())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_occurrence(
            parent="parent_value",
            occurrence=grafeas.Occurrence(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].occurrence
        mock_val = grafeas.Occurrence(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_occurrence_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_occurrence(
            grafeas.CreateOccurrenceRequest(),
            parent="parent_value",
            occurrence=grafeas.Occurrence(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.BatchCreateOccurrencesRequest(),
        {},
    ],
)
def test_batch_create_occurrences(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.BatchCreateOccurrencesResponse()
        response = client.batch_create_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.BatchCreateOccurrencesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.BatchCreateOccurrencesResponse)


def test_batch_create_occurrences_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.BatchCreateOccurrencesRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.batch_create_occurrences(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateOccurrencesRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_batch_create_occurrences_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_occurrences
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_create_occurrences
        ] = mock_rpc
        request = {}
        client.batch_create_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_batch_create_occurrences_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.batch_create_occurrences
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.batch_create_occurrences
        ] = mock_rpc

        request = {}
        await client.batch_create_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.batch_create_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.BatchCreateOccurrencesRequest(),
        {},
    ],
)
async def test_batch_create_occurrences_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateOccurrencesResponse()
        )
        response = await client.batch_create_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.BatchCreateOccurrencesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.BatchCreateOccurrencesResponse)


def test_batch_create_occurrences_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.BatchCreateOccurrencesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        call.return_value = grafeas.BatchCreateOccurrencesResponse()
        client.batch_create_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_batch_create_occurrences_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.BatchCreateOccurrencesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateOccurrencesResponse()
        )
        await client.batch_create_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_batch_create_occurrences_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.BatchCreateOccurrencesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.batch_create_occurrences(
            parent="parent_value",
            occurrences=[grafeas.Occurrence(name="name_value")],
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].occurrences
        mock_val = [grafeas.Occurrence(name="name_value")]
        assert arg == mock_val


def test_batch_create_occurrences_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_occurrences(
            grafeas.BatchCreateOccurrencesRequest(),
            parent="parent_value",
            occurrences=[grafeas.Occurrence(name="name_value")],
        )


@pytest.mark.asyncio
async def test_batch_create_occurrences_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.BatchCreateOccurrencesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateOccurrencesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.batch_create_occurrences(
            parent="parent_value",
            occurrences=[grafeas.Occurrence(name="name_value")],
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].occurrences
        mock_val = [grafeas.Occurrence(name="name_value")]
        assert arg == mock_val


@pytest.mark.asyncio
async def test_batch_create_occurrences_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.batch_create_occurrences(
            grafeas.BatchCreateOccurrencesRequest(),
            parent="parent_value",
            occurrences=[grafeas.Occurrence(name="name_value")],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.UpdateOccurrenceRequest(),
        {},
    ],
)
def test_update_occurrence(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence(
            name="name_value",
            resource_uri="resource_uri_value",
            note_name="note_name_value",
            kind=common.NoteKind.VULNERABILITY,
            remediation="remediation_value",
        )
        response = client.update_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.UpdateOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


def test_update_occurrence_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.UpdateOccurrenceRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_occurrence(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateOccurrenceRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_update_occurrence_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_occurrence] = (
            mock_rpc
        )
        request = {}
        client.update_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_occurrence_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_occurrence
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_occurrence
        ] = mock_rpc

        request = {}
        await client.update_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.UpdateOccurrenceRequest(),
        {},
    ],
)
async def test_update_occurrence_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Occurrence(
                name="name_value",
                resource_uri="resource_uri_value",
                note_name="note_name_value",
                kind=common.NoteKind.VULNERABILITY,
                remediation="remediation_value",
            )
        )
        response = await client.update_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.UpdateOccurrenceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


def test_update_occurrence_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.UpdateOccurrenceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        call.return_value = grafeas.Occurrence()
        client.update_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_occurrence_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.UpdateOccurrenceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Occurrence())
        await client.update_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_update_occurrence_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_occurrence(
            name="name_value",
            occurrence=grafeas.Occurrence(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].occurrence
        mock_val = grafeas.Occurrence(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_occurrence_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_occurrence(
            grafeas.UpdateOccurrenceRequest(),
            name="name_value",
            occurrence=grafeas.Occurrence(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_occurrence_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Occurrence()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Occurrence())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_occurrence(
            name="name_value",
            occurrence=grafeas.Occurrence(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].occurrence
        mock_val = grafeas.Occurrence(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_occurrence_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_occurrence(
            grafeas.UpdateOccurrenceRequest(),
            name="name_value",
            occurrence=grafeas.Occurrence(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetOccurrenceNoteRequest(),
        {},
    ],
)
def test_get_occurrence_note(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )
        response = client.get_occurrence_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.GetOccurrenceNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_get_occurrence_note_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.GetOccurrenceNoteRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_occurrence_note(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceNoteRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_occurrence_note_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_occurrence_note in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_occurrence_note] = (
            mock_rpc
        )
        request = {}
        client.get_occurrence_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_occurrence_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_occurrence_note_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_occurrence_note
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_occurrence_note
        ] = mock_rpc

        request = {}
        await client.get_occurrence_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_occurrence_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetOccurrenceNoteRequest(),
        {},
    ],
)
async def test_get_occurrence_note_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        response = await client.get_occurrence_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.GetOccurrenceNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_get_occurrence_note_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.GetOccurrenceNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        call.return_value = grafeas.Note()
        client.get_occurrence_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_occurrence_note_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.GetOccurrenceNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        await client.get_occurrence_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_occurrence_note_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_occurrence_note(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_occurrence_note_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_occurrence_note(
            grafeas.GetOccurrenceNoteRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_occurrence_note_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_occurrence_note(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_occurrence_note_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_occurrence_note(
            grafeas.GetOccurrenceNoteRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetNoteRequest(),
        {},
    ],
)
def test_get_note(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )
        response = client.get_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.GetNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_get_note_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.GetNoteRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_note(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetNoteRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_note_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_note] = mock_rpc
        request = {}
        client.get_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_note_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_note
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_note
        ] = mock_rpc

        request = {}
        await client.get_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetNoteRequest(),
        {},
    ],
)
async def test_get_note_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        response = await client.get_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.GetNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_get_note_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.GetNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        call.return_value = grafeas.Note()
        client.get_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_note_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.GetNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        await client.get_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_note_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_note(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_note_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_note(
            grafeas.GetNoteRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_note_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_note(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_note_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_note(
            grafeas.GetNoteRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListNotesRequest(),
        {},
    ],
)
def test_list_notes(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListNotesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )
        response = client.list_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.ListNotesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListNotesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_notes_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.ListNotesRequest(
        parent="parent_value",
        filter="filter_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_notes(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNotesRequest(
            parent="parent_value",
            filter="filter_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_notes_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_notes in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_notes] = mock_rpc
        request = {}
        client.list_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_notes(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_notes_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_notes
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_notes
        ] = mock_rpc

        request = {}
        await client.list_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_notes(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListNotesRequest(),
        {},
    ],
)
async def test_list_notes_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNotesResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.ListNotesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListNotesAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_notes_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.ListNotesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        call.return_value = grafeas.ListNotesResponse()
        client.list_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_notes_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.ListNotesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNotesResponse()
        )
        await client.list_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_notes_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListNotesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_notes(
            parent="parent_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


def test_list_notes_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_notes(
            grafeas.ListNotesRequest(),
            parent="parent_value",
            filter="filter_value",
        )


@pytest.mark.asyncio
async def test_list_notes_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListNotesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNotesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_notes(
            parent="parent_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_notes_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_notes(
            grafeas.ListNotesRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_notes_pager(transport_name: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                    grafeas.Note(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNotesResponse(
                notes=[],
                next_page_token="def",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_notes(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, grafeas.Note) for i in results)


def test_list_notes_pages(transport_name: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                    grafeas.Note(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNotesResponse(
                notes=[],
                next_page_token="def",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_notes(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_notes_async_pager():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_notes), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                    grafeas.Note(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNotesResponse(
                notes=[],
                next_page_token="def",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_notes(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, grafeas.Note) for i in responses)


@pytest.mark.asyncio
async def test_list_notes_async_pages():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_notes), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                    grafeas.Note(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNotesResponse(
                notes=[],
                next_page_token="def",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_notes(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.DeleteNoteRequest(),
        {},
    ],
)
def test_delete_note(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.DeleteNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_note_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.DeleteNoteRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_note(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteNoteRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_note_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_note] = mock_rpc
        request = {}
        client.delete_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_note_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_note
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_note
        ] = mock_rpc

        request = {}
        await client.delete_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.DeleteNoteRequest(),
        {},
    ],
)
async def test_delete_note_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.DeleteNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_note_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.DeleteNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        call.return_value = None
        client.delete_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_note_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.DeleteNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_delete_note_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_note(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_note_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_note(
            grafeas.DeleteNoteRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_note_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_note(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_note_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_note(
            grafeas.DeleteNoteRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.CreateNoteRequest(),
        {},
    ],
)
def test_create_note(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )
        response = client.create_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.CreateNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_create_note_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.CreateNoteRequest(
        parent="parent_value",
        note_id="note_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_note(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateNoteRequest(
            parent="parent_value",
            note_id="note_id_value",
        )
        assert args[0] == request_msg


def test_create_note_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_note] = mock_rpc
        request = {}
        client.create_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_note_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_note
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_note
        ] = mock_rpc

        request = {}
        await client.create_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.CreateNoteRequest(),
        {},
    ],
)
async def test_create_note_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        response = await client.create_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.CreateNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_create_note_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.CreateNoteRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        call.return_value = grafeas.Note()
        client.create_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_note_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.CreateNoteRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        await client.create_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_create_note_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_note(
            parent="parent_value",
            note_id="note_id_value",
            note=grafeas.Note(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].note_id
        mock_val = "note_id_value"
        assert arg == mock_val
        arg = args[0].note
        mock_val = grafeas.Note(name="name_value")
        assert arg == mock_val


def test_create_note_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_note(
            grafeas.CreateNoteRequest(),
            parent="parent_value",
            note_id="note_id_value",
            note=grafeas.Note(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_note_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_note(
            parent="parent_value",
            note_id="note_id_value",
            note=grafeas.Note(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].note_id
        mock_val = "note_id_value"
        assert arg == mock_val
        arg = args[0].note
        mock_val = grafeas.Note(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_note_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_note(
            grafeas.CreateNoteRequest(),
            parent="parent_value",
            note_id="note_id_value",
            note=grafeas.Note(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.BatchCreateNotesRequest(),
        {},
    ],
)
def test_batch_create_notes(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.BatchCreateNotesResponse()
        response = client.batch_create_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.BatchCreateNotesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.BatchCreateNotesResponse)


def test_batch_create_notes_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.BatchCreateNotesRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.batch_create_notes(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateNotesRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_batch_create_notes_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_notes in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_create_notes] = (
            mock_rpc
        )
        request = {}
        client.batch_create_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_notes(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_batch_create_notes_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.batch_create_notes
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.batch_create_notes
        ] = mock_rpc

        request = {}
        await client.batch_create_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.batch_create_notes(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.BatchCreateNotesRequest(),
        {},
    ],
)
async def test_batch_create_notes_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateNotesResponse()
        )
        response = await client.batch_create_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.BatchCreateNotesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.BatchCreateNotesResponse)


def test_batch_create_notes_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.BatchCreateNotesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        call.return_value = grafeas.BatchCreateNotesResponse()
        client.batch_create_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_batch_create_notes_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.BatchCreateNotesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateNotesResponse()
        )
        await client.batch_create_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_batch_create_notes_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.BatchCreateNotesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.batch_create_notes(
            parent="parent_value",
            notes={"key_value": grafeas.Note(name="name_value")},
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].notes
        mock_val = {"key_value": grafeas.Note(name="name_value")}
        assert arg == mock_val


def test_batch_create_notes_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_notes(
            grafeas.BatchCreateNotesRequest(),
            parent="parent_value",
            notes={"key_value": grafeas.Note(name="name_value")},
        )


@pytest.mark.asyncio
async def test_batch_create_notes_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.BatchCreateNotesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateNotesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.batch_create_notes(
            parent="parent_value",
            notes={"key_value": grafeas.Note(name="name_value")},
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].notes
        mock_val = {"key_value": grafeas.Note(name="name_value")}
        assert arg == mock_val


@pytest.mark.asyncio
async def test_batch_create_notes_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.batch_create_notes(
            grafeas.BatchCreateNotesRequest(),
            parent="parent_value",
            notes={"key_value": grafeas.Note(name="name_value")},
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.UpdateNoteRequest(),
        {},
    ],
)
def test_update_note(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )
        response = client.update_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.UpdateNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_update_note_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.UpdateNoteRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_note(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateNoteRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_update_note_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_note] = mock_rpc
        request = {}
        client.update_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_note_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_note
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_note
        ] = mock_rpc

        request = {}
        await client.update_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.UpdateNoteRequest(),
        {},
    ],
)
async def test_update_note_async(request_type, transport: str = "grpc_asyncio"):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        response = await client.update_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.UpdateNoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


def test_update_note_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.UpdateNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        call.return_value = grafeas.Note()
        client.update_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_note_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.UpdateNoteRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        await client.update_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_update_note_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_note(
            name="name_value",
            note=grafeas.Note(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].note
        mock_val = grafeas.Note(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_note_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_note(
            grafeas.UpdateNoteRequest(),
            name="name_value",
            note=grafeas.Note(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_note_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.Note()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(grafeas.Note())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_note(
            name="name_value",
            note=grafeas.Note(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].note
        mock_val = grafeas.Note(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_note_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_note(
            grafeas.UpdateNoteRequest(),
            name="name_value",
            note=grafeas.Note(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListNoteOccurrencesRequest(),
        {},
    ],
)
def test_list_note_occurrences(request_type, transport: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListNoteOccurrencesResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_note_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = grafeas.ListNoteOccurrencesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListNoteOccurrencesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_note_occurrences_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = grafeas.ListNoteOccurrencesRequest(
        name="name_value",
        filter="filter_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_note_occurrences(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNoteOccurrencesRequest(
            name="name_value",
            filter="filter_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_note_occurrences_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_note_occurrences
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_note_occurrences] = (
            mock_rpc
        )
        request = {}
        client.list_note_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_note_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_note_occurrences_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GrafeasAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_note_occurrences
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_note_occurrences
        ] = mock_rpc

        request = {}
        await client.list_note_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_note_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListNoteOccurrencesRequest(),
        {},
    ],
)
async def test_list_note_occurrences_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNoteOccurrencesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_note_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = grafeas.ListNoteOccurrencesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListNoteOccurrencesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_note_occurrences_field_headers():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.ListNoteOccurrencesRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        call.return_value = grafeas.ListNoteOccurrencesResponse()
        client.list_note_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_note_occurrences_field_headers_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = grafeas.ListNoteOccurrencesRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNoteOccurrencesResponse()
        )
        await client.list_note_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_list_note_occurrences_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListNoteOccurrencesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_note_occurrences(
            name="name_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


def test_list_note_occurrences_flattened_error():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_note_occurrences(
            grafeas.ListNoteOccurrencesRequest(),
            name="name_value",
            filter="filter_value",
        )


@pytest.mark.asyncio
async def test_list_note_occurrences_flattened_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grafeas.ListNoteOccurrencesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNoteOccurrencesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_note_occurrences(
            name="name_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_note_occurrences_flattened_error_async():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_note_occurrences(
            grafeas.ListNoteOccurrencesRequest(),
            name="name_value",
            filter="filter_value",
        )


def test_list_note_occurrences_pager(transport_name: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", ""),)),
        )
        pager = client.list_note_occurrences(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, grafeas.Occurrence) for i in results)


def test_list_note_occurrences_pages(transport_name: str = "grpc"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_note_occurrences(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_note_occurrences_async_pager():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_note_occurrences(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, grafeas.Occurrence) for i in responses)


@pytest.mark.asyncio
async def test_list_note_occurrences_async_pages():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_note_occurrences(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_occurrence_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_occurrence] = mock_rpc

        request = {}
        client.get_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_occurrence_rest_required_fields(request_type=grafeas.GetOccurrenceRequest):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetOccurrence,
        "_BaseGetOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.Occurrence()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.Occurrence.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_occurrence(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_occurrence_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Occurrence()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/occurrences/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.Occurrence.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_occurrence(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/occurrences/*}" % client.transport._host, args[1]
        )


def test_get_occurrence_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_occurrence(
            grafeas.GetOccurrenceRequest(),
            name="name_value",
        )


def test_list_occurrences_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_occurrences in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_occurrences] = (
            mock_rpc
        )

        request = {}
        client.list_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_occurrences_rest_required_fields(
    request_type=grafeas.ListOccurrencesRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListOccurrences,
        "_BaseListOccurrences__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "pageSize",
            "pageToken",
            "returnPartialSuccess",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.ListOccurrencesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.ListOccurrencesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_occurrences(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_occurrences_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.ListOccurrencesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            filter="filter_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.ListOccurrencesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_occurrences(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*}/occurrences" % client.transport._host, args[1]
        )


def test_list_occurrences_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_occurrences(
            grafeas.ListOccurrencesRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_occurrences_rest_pager(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(grafeas.ListOccurrencesResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1"}

        pager = client.list_occurrences(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, grafeas.Occurrence) for i in results)

        pages = list(client.list_occurrences(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_delete_occurrence_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_occurrence] = (
            mock_rpc
        )

        request = {}
        client.delete_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_occurrence_rest_required_fields(
    request_type=grafeas.DeleteOccurrenceRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteOccurrence,
        "_BaseDeleteOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = None
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = ""

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_occurrence(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_occurrence_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/occurrences/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = ""
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_occurrence(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/occurrences/*}" % client.transport._host, args[1]
        )


def test_delete_occurrence_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_occurrence(
            grafeas.DeleteOccurrenceRequest(),
            name="name_value",
        )


def test_create_occurrence_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_occurrence] = (
            mock_rpc
        )

        request = {}
        client.create_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_occurrence_rest_required_fields(
    request_type=grafeas.CreateOccurrenceRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateOccurrence,
        "_BaseCreateOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.Occurrence()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.Occurrence.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_occurrence(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_occurrence_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Occurrence()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            occurrence=grafeas.Occurrence(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.Occurrence.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_occurrence(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*}/occurrences" % client.transport._host, args[1]
        )


def test_create_occurrence_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_occurrence(
            grafeas.CreateOccurrenceRequest(),
            parent="parent_value",
            occurrence=grafeas.Occurrence(name="name_value"),
        )


def test_batch_create_occurrences_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_occurrences
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_create_occurrences
        ] = mock_rpc

        request = {}
        client.batch_create_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_create_occurrences_rest_required_fields(
    request_type=grafeas.BatchCreateOccurrencesRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchCreateOccurrences,
        "_BaseBatchCreateOccurrences__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.BatchCreateOccurrencesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.BatchCreateOccurrencesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_create_occurrences(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_create_occurrences_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.BatchCreateOccurrencesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            occurrences=[grafeas.Occurrence(name="name_value")],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.BatchCreateOccurrencesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_create_occurrences(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*}/occurrences:batchCreate"
            % client.transport._host,
            args[1],
        )


def test_batch_create_occurrences_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_occurrences(
            grafeas.BatchCreateOccurrencesRequest(),
            parent="parent_value",
            occurrences=[grafeas.Occurrence(name="name_value")],
        )


def test_update_occurrence_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_occurrence in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_occurrence] = (
            mock_rpc
        )

        request = {}
        client.update_occurrence(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_occurrence(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_occurrence_rest_required_fields(
    request_type=grafeas.UpdateOccurrenceRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateOccurrence,
        "_BaseUpdateOccurrence__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("updateMask",))

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.Occurrence()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.Occurrence.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_occurrence(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_occurrence_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Occurrence()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/occurrences/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            occurrence=grafeas.Occurrence(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.Occurrence.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_occurrence(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/occurrences/*}" % client.transport._host, args[1]
        )


def test_update_occurrence_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_occurrence(
            grafeas.UpdateOccurrenceRequest(),
            name="name_value",
            occurrence=grafeas.Occurrence(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_get_occurrence_note_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_occurrence_note in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_occurrence_note] = (
            mock_rpc
        )

        request = {}
        client.get_occurrence_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_occurrence_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_occurrence_note_rest_required_fields(
    request_type=grafeas.GetOccurrenceNoteRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetOccurrenceNote,
        "_BaseGetOccurrenceNote__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.Note()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.Note.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_occurrence_note(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_occurrence_note_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/occurrences/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_occurrence_note(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/occurrences/*}/notes" % client.transport._host,
            args[1],
        )


def test_get_occurrence_note_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_occurrence_note(
            grafeas.GetOccurrenceNoteRequest(),
            name="name_value",
        )


def test_get_note_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_note] = mock_rpc

        request = {}
        client.get_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_note_rest_required_fields(request_type=grafeas.GetNoteRequest):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetNote,
        "_BaseGetNote__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.Note()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.Note.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_note(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_note_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/notes/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_note(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/notes/*}" % client.transport._host, args[1]
        )


def test_get_note_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_note(
            grafeas.GetNoteRequest(),
            name="name_value",
        )


def test_list_notes_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_notes in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_notes] = mock_rpc

        request = {}
        client.list_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_notes(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_notes_rest_required_fields(request_type=grafeas.ListNotesRequest):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListNotes,
        "_BaseListNotes__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "pageSize",
            "pageToken",
            "returnPartialSuccess",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.ListNotesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.ListNotesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_notes(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_notes_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.ListNotesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            filter="filter_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.ListNotesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_notes(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*}/notes" % client.transport._host, args[1]
        )


def test_list_notes_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_notes(
            grafeas.ListNotesRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_notes_rest_pager(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                    grafeas.Note(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNotesResponse(
                notes=[],
                next_page_token="def",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNotesResponse(
                notes=[
                    grafeas.Note(),
                    grafeas.Note(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(grafeas.ListNotesResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1"}

        pager = client.list_notes(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, grafeas.Note) for i in results)

        pages = list(client.list_notes(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_delete_note_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_note] = mock_rpc

        request = {}
        client.delete_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_note_rest_required_fields(request_type=grafeas.DeleteNoteRequest):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteNote,
        "_BaseDeleteNote__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = None
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = ""

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_note(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_note_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/notes/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = ""
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_note(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/notes/*}" % client.transport._host, args[1]
        )


def test_delete_note_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_note(
            grafeas.DeleteNoteRequest(),
            name="name_value",
        )


def test_create_note_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_note] = mock_rpc

        request = {}
        client.create_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_note_rest_required_fields(request_type=grafeas.CreateNoteRequest):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["note_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "noteId" not in jsonified_request

    default_values = getattr(
        transport_class._BaseCreateNote,
        "_BaseCreateNote__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "noteId" in jsonified_request
    assert jsonified_request["noteId"] == request_init["note_id"]

    jsonified_request["parent"] = "parent_value"
    jsonified_request["noteId"] = "note_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("noteId",))

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "noteId" in jsonified_request
    assert jsonified_request["noteId"] == "note_id_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.Note()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.Note.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_note(request)

            expected_params = [
                (
                    "noteId",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_note_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            note_id="note_id_value",
            note=grafeas.Note(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_note(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*}/notes" % client.transport._host, args[1]
        )


def test_create_note_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_note(
            grafeas.CreateNoteRequest(),
            parent="parent_value",
            note_id="note_id_value",
            note=grafeas.Note(name="name_value"),
        )


def test_batch_create_notes_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_notes in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_create_notes] = (
            mock_rpc
        )

        request = {}
        client.batch_create_notes(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_notes(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_create_notes_rest_required_fields(
    request_type=grafeas.BatchCreateNotesRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchCreateNotes,
        "_BaseBatchCreateNotes__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.BatchCreateNotesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.BatchCreateNotesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_create_notes(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_create_notes_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.BatchCreateNotesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            notes={"key_value": grafeas.Note(name="name_value")},
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.BatchCreateNotesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_create_notes(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*}/notes:batchCreate" % client.transport._host,
            args[1],
        )


def test_batch_create_notes_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_notes(
            grafeas.BatchCreateNotesRequest(),
            parent="parent_value",
            notes={"key_value": grafeas.Note(name="name_value")},
        )


def test_update_note_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_note in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_note] = mock_rpc

        request = {}
        client.update_note(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_note(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_note_rest_required_fields(request_type=grafeas.UpdateNoteRequest):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateNote,
        "_BaseUpdateNote__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("updateMask",))

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.Note()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.Note.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_note(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_note_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/notes/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            note=grafeas.Note(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_note(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/notes/*}" % client.transport._host, args[1]
        )


def test_update_note_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_note(
            grafeas.UpdateNoteRequest(),
            name="name_value",
            note=grafeas.Note(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_list_note_occurrences_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_note_occurrences
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_note_occurrences] = (
            mock_rpc
        )

        request = {}
        client.list_note_occurrences(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_note_occurrences(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_note_occurrences_rest_required_fields(
    request_type=grafeas.ListNoteOccurrencesRequest,
):
    transport_class = transports.GrafeasRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListNoteOccurrences,
        "_BaseListNoteOccurrences__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = grafeas.ListNoteOccurrencesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = grafeas.ListNoteOccurrencesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_note_occurrences(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_note_occurrences_rest_flattened():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.ListNoteOccurrencesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/notes/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            filter="filter_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = grafeas.ListNoteOccurrencesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_note_occurrences(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/notes/*}/occurrences" % client.transport._host,
            args[1],
        )


def test_list_note_occurrences_rest_flattened_error(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_note_occurrences(
            grafeas.ListNoteOccurrencesRequest(),
            name="name_value",
            filter="filter_value",
        )


def test_list_note_occurrences_rest_pager(transport: str = "rest"):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
                next_page_token="abc",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[],
                next_page_token="def",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                ],
                next_page_token="ghi",
            ),
            grafeas.ListNoteOccurrencesResponse(
                occurrences=[
                    grafeas.Occurrence(),
                    grafeas.Occurrence(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            grafeas.ListNoteOccurrencesResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"name": "projects/sample1/notes/sample2"}

        pager = client.list_note_occurrences(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, grafeas.Occurrence) for i in results)

        pages = list(client.list_note_occurrences(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GrafeasGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = GrafeasClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GrafeasGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.GrafeasGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GrafeasGrpcTransport,
        transports.GrafeasGrpcAsyncIOTransport,
        transports.GrafeasRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = GrafeasClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_occurrence_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        call.return_value = grafeas.Occurrence()
        client.get_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_occurrences_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        call.return_value = grafeas.ListOccurrencesResponse()
        client.list_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListOccurrencesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_occurrence_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        call.return_value = None
        client.delete_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_occurrence_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        call.return_value = grafeas.Occurrence()
        client.create_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_occurrences_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        call.return_value = grafeas.BatchCreateOccurrencesResponse()
        client.batch_create_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateOccurrencesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_occurrence_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        call.return_value = grafeas.Occurrence()
        client.update_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_occurrence_note_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        call.return_value = grafeas.Note()
        client.get_occurrence_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_note_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        call.return_value = grafeas.Note()
        client.get_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_notes_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        call.return_value = grafeas.ListNotesResponse()
        client.list_notes(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNotesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_note_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        call.return_value = None
        client.delete_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_note_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        call.return_value = grafeas.Note()
        client.create_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_notes_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        call.return_value = grafeas.BatchCreateNotesResponse()
        client.batch_create_notes(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateNotesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_note_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        call.return_value = grafeas.Note()
        client.update_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_note_occurrences_empty_call_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        call.return_value = grafeas.ListNoteOccurrencesResponse()
        client.list_note_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNoteOccurrencesRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = GrafeasAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_occurrence_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Occurrence(
                name="name_value",
                resource_uri="resource_uri_value",
                note_name="note_name_value",
                kind=common.NoteKind.VULNERABILITY,
                remediation="remediation_value",
            )
        )
        await client.get_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_occurrences_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListOccurrencesResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        await client.list_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListOccurrencesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_occurrence_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_occurrence_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Occurrence(
                name="name_value",
                resource_uri="resource_uri_value",
                note_name="note_name_value",
                kind=common.NoteKind.VULNERABILITY,
                remediation="remediation_value",
            )
        )
        await client.create_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_batch_create_occurrences_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateOccurrencesResponse()
        )
        await client.batch_create_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateOccurrencesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_occurrence_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Occurrence(
                name="name_value",
                resource_uri="resource_uri_value",
                note_name="note_name_value",
                kind=common.NoteKind.VULNERABILITY,
                remediation="remediation_value",
            )
        )
        await client.update_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_occurrence_note_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        await client.get_occurrence_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_note_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        await client.get_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_notes_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNotesResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        await client.list_notes(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNotesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_note_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_note_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        await client.create_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_batch_create_notes_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.BatchCreateNotesResponse()
        )
        await client.batch_create_notes(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateNotesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_note_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.Note(
                name="name_value",
                short_description="short_description_value",
                long_description="long_description_value",
                kind=common.NoteKind.VULNERABILITY,
                related_note_names=["related_note_names_value"],
            )
        )
        await client.update_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_note_occurrences_empty_call_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            grafeas.ListNoteOccurrencesResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_note_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNoteOccurrencesRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = GrafeasClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_occurrence_rest_bad_request(request_type=grafeas.GetOccurrenceRequest):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_occurrence(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetOccurrenceRequest,
        dict,
    ],
)
def test_get_occurrence_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Occurrence(
            name="name_value",
            resource_uri="resource_uri_value",
            note_name="note_name_value",
            kind=common.NoteKind.VULNERABILITY,
            remediation="remediation_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.Occurrence.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_occurrence(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_occurrence_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_get_occurrence"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_get_occurrence_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_get_occurrence"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.GetOccurrenceRequest.pb(grafeas.GetOccurrenceRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.Occurrence.to_json(grafeas.Occurrence())
        req.return_value.content = return_value

        request = grafeas.GetOccurrenceRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.Occurrence()
        post_with_metadata.return_value = grafeas.Occurrence(), metadata

        client.get_occurrence(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_occurrences_rest_bad_request(request_type=grafeas.ListOccurrencesRequest):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_occurrences(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListOccurrencesRequest,
        dict,
    ],
)
def test_list_occurrences_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.ListOccurrencesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.ListOccurrencesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_occurrences(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOccurrencesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_occurrences_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_list_occurrences"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_list_occurrences_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_list_occurrences"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.ListOccurrencesRequest.pb(grafeas.ListOccurrencesRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.ListOccurrencesResponse.to_json(
            grafeas.ListOccurrencesResponse()
        )
        req.return_value.content = return_value

        request = grafeas.ListOccurrencesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.ListOccurrencesResponse()
        post_with_metadata.return_value = grafeas.ListOccurrencesResponse(), metadata

        client.list_occurrences(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_occurrence_rest_bad_request(
    request_type=grafeas.DeleteOccurrenceRequest,
):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_occurrence(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.DeleteOccurrenceRequest,
        dict,
    ],
)
def test_delete_occurrence_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ""
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_occurrence(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_occurrence_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_delete_occurrence"
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = grafeas.DeleteOccurrenceRequest.pb(
            grafeas.DeleteOccurrenceRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        request = grafeas.DeleteOccurrenceRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_occurrence(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_create_occurrence_rest_bad_request(
    request_type=grafeas.CreateOccurrenceRequest,
):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.create_occurrence(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.CreateOccurrenceRequest,
        dict,
    ],
)
def test_create_occurrence_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request_init["occurrence"] = {
        "name": "name_value",
        "resource_uri": "resource_uri_value",
        "note_name": "note_name_value",
        "kind": 1,
        "remediation": "remediation_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "vulnerability": {
            "type_": "type__value",
            "severity": 1,
            "cvss_score": 0.1082,
            "cvssv3": {
                "base_score": 0.1046,
                "exploitability_score": 0.21580000000000002,
                "impact_score": 0.1273,
                "attack_vector": 1,
                "attack_complexity": 1,
                "authentication": 1,
                "privileges_required": 1,
                "user_interaction": 1,
                "scope": 1,
                "confidentiality_impact": 1,
                "integrity_impact": 1,
                "availability_impact": 1,
                "attack_requirements": 1,
                "vulnerable_system_confidentiality_impact": 1,
                "vulnerable_system_integrity_impact": 1,
                "vulnerable_system_availability_impact": 1,
                "subsequent_system_confidentiality_impact": 1,
                "subsequent_system_integrity_impact": 1,
                "subsequent_system_availability_impact": 1,
                "exploit_maturity": 1,
            },
            "package_issue": [
                {
                    "affected_cpe_uri": "affected_cpe_uri_value",
                    "affected_package": "affected_package_value",
                    "affected_version": {
                        "epoch": 527,
                        "name": "name_value",
                        "revision": "revision_value",
                        "inclusive": True,
                        "kind": 1,
                        "full_name": "full_name_value",
                    },
                    "fixed_cpe_uri": "fixed_cpe_uri_value",
                    "fixed_package": "fixed_package_value",
                    "fixed_version": {},
                    "fix_available": True,
                    "package_type": "package_type_value",
                    "effective_severity": 1,
                    "file_location": [
                        {
                            "file_path": "file_path_value",
                            "layer_details": {
                                "index": 536,
                                "diff_id": "diff_id_value",
                                "chain_id": "chain_id_value",
                                "command": "command_value",
                                "base_images": [
                                    {
                                        "name": "name_value",
                                        "repository": "repository_value",
                                        "layer_count": 1189,
                                        "registry": "registry_value",
                                    }
                                ],
                            },
                            "line_number": 1168,
                        }
                    ],
                }
            ],
            "short_description": "short_description_value",
            "long_description": "long_description_value",
            "related_urls": [{"url": "url_value", "label": "label_value"}],
            "effective_severity": 1,
            "fix_available": True,
            "cvss_version": 1,
            "cvss_v2": {},
            "vex_assessment": {
                "cve": "cve_value",
                "vulnerability_id": "vulnerability_id_value",
                "related_uris": {},
                "note_name": "note_name_value",
                "state": 1,
                "impacts": ["impacts_value1", "impacts_value2"],
                "remediations": [
                    {
                        "remediation_type": 1,
                        "details": "details_value",
                        "remediation_uri": {},
                    }
                ],
                "justification": {"justification_type": 1, "details": "details_value"},
            },
            "extra_details": "extra_details_value",
            "risk": {
                "cisa_kev": {
                    "known_ransomware_campaign_use": "known_ransomware_campaign_use_value"
                },
                "epss": {"percentile": 0.1067, "score": 0.54},
            },
            "cvss_v4": {},
        },
        "build": {
            "provenance": {
                "id": "id_value",
                "project_id": "project_id_value",
                "commands": [
                    {
                        "name": "name_value",
                        "env": ["env_value1", "env_value2"],
                        "args": ["args_value1", "args_value2"],
                        "dir_": "dir__value",
                        "id": "id_value",
                        "wait_for": ["wait_for_value1", "wait_for_value2"],
                    }
                ],
                "built_artifacts": [
                    {
                        "checksum": "checksum_value",
                        "id": "id_value",
                        "names": ["names_value1", "names_value2"],
                    }
                ],
                "create_time": {},
                "start_time": {},
                "end_time": {},
                "creator": "creator_value",
                "logs_uri": "logs_uri_value",
                "source_provenance": {
                    "artifact_storage_source_uri": "artifact_storage_source_uri_value",
                    "file_hashes": {},
                    "context": {
                        "cloud_repo": {
                            "repo_id": {
                                "project_repo_id": {
                                    "project_id": "project_id_value",
                                    "repo_name": "repo_name_value",
                                },
                                "uid": "uid_value",
                            },
                            "revision_id": "revision_id_value",
                            "alias_context": {"kind": 1, "name": "name_value"},
                        },
                        "gerrit": {
                            "host_uri": "host_uri_value",
                            "gerrit_project": "gerrit_project_value",
                            "revision_id": "revision_id_value",
                            "alias_context": {},
                        },
                        "git": {"url": "url_value", "revision_id": "revision_id_value"},
                        "labels": {},
                    },
                    "additional_contexts": {},
                },
                "trigger_id": "trigger_id_value",
                "build_options": {},
                "builder_version": "builder_version_value",
            },
            "provenance_bytes": "provenance_bytes_value",
            "intoto_provenance": {
                "builder_config": {"id": "id_value"},
                "recipe": {
                    "type_": "type__value",
                    "defined_in_material": 1971,
                    "entry_point": "entry_point_value",
                    "arguments": [
                        {
                            "type_url": "type.googleapis.com/google.protobuf.Duration",
                            "value": b"\x08\x0c\x10\xdb\x07",
                        }
                    ],
                    "environment": {},
                },
                "metadata": {
                    "build_invocation_id": "build_invocation_id_value",
                    "build_started_on": {},
                    "build_finished_on": {},
                    "completeness": {
                        "arguments": True,
                        "environment": True,
                        "materials": True,
                    },
                    "reproducible": True,
                },
                "materials": ["materials_value1", "materials_value2"],
            },
            "intoto_statement": {
                "type_": "type__value",
                "subject": [{"name": "name_value", "digest": {}}],
                "predicate_type": "predicate_type_value",
                "provenance": {},
                "slsa_provenance": {
                    "builder": {"id": "id_value"},
                    "recipe": {
                        "type_": "type__value",
                        "defined_in_material": 1971,
                        "entry_point": "entry_point_value",
                        "arguments": {},
                        "environment": {},
                    },
                    "metadata": {
                        "build_invocation_id": "build_invocation_id_value",
                        "build_started_on": {},
                        "build_finished_on": {},
                        "completeness": {
                            "arguments": True,
                            "environment": True,
                            "materials": True,
                        },
                        "reproducible": True,
                    },
                    "materials": [{"uri": "uri_value", "digest": {}}],
                },
                "slsa_provenance_zero_two": {
                    "builder": {"id": "id_value"},
                    "build_type": "build_type_value",
                    "invocation": {
                        "config_source": {
                            "uri": "uri_value",
                            "digest": {},
                            "entry_point": "entry_point_value",
                        },
                        "parameters": {"fields": {}},
                        "environment": {},
                    },
                    "build_config": {},
                    "metadata": {
                        "build_invocation_id": "build_invocation_id_value",
                        "build_started_on": {},
                        "build_finished_on": {},
                        "completeness": {
                            "parameters": True,
                            "environment": True,
                            "materials": True,
                        },
                        "reproducible": True,
                    },
                    "materials": [{"uri": "uri_value", "digest": {}}],
                },
            },
            "in_toto_slsa_provenance_v1": {
                "type_": "type__value",
                "subject": {},
                "predicate_type": "predicate_type_value",
                "predicate": {
                    "build_definition": {
                        "build_type": "build_type_value",
                        "external_parameters": {},
                        "internal_parameters": {},
                        "resolved_dependencies": [
                            {
                                "name": "name_value",
                                "uri": "uri_value",
                                "digest": {},
                                "content": b"content_blob",
                                "download_location": "download_location_value",
                                "media_type": "media_type_value",
                                "annotations": {},
                            }
                        ],
                    },
                    "run_details": {
                        "builder": {
                            "id": "id_value",
                            "version": {},
                            "builder_dependencies": {},
                        },
                        "metadata": {
                            "invocation_id": "invocation_id_value",
                            "started_on": {},
                            "finished_on": {},
                        },
                        "byproducts": {},
                    },
                },
            },
        },
        "image": {
            "fingerprint": {
                "v1_name": "v1_name_value",
                "v2_blob": ["v2_blob_value1", "v2_blob_value2"],
                "v2_name": "v2_name_value",
            },
            "distance": 843,
            "layer_info": [
                {"directive": "directive_value", "arguments": "arguments_value"}
            ],
            "base_resource_url": "base_resource_url_value",
        },
        "package": {
            "name": "name_value",
            "location": [
                {"cpe_uri": "cpe_uri_value", "version": {}, "path": "path_value"}
            ],
            "package_type": "package_type_value",
            "cpe_uri": "cpe_uri_value",
            "architecture": 1,
            "license_": {
                "expression": "expression_value",
                "comments": "comments_value",
            },
            "version": {},
        },
        "deployment": {
            "user_email": "user_email_value",
            "deploy_time": {},
            "undeploy_time": {},
            "config": "config_value",
            "address": "address_value",
            "resource_uri": ["resource_uri_value1", "resource_uri_value2"],
            "platform": 1,
        },
        "discovery": {
            "continuous_analysis": 1,
            "analysis_status": 1,
            "analysis_completed": {
                "analysis_type": ["analysis_type_value1", "analysis_type_value2"]
            },
            "analysis_error": [
                {"code": 411, "message": "message_value", "details": {}}
            ],
            "analysis_status_error": {},
            "cpe": "cpe_value",
            "last_scan_time": {},
            "archive_time": {},
            "sbom_status": {"sbom_state": 1, "error": "error_value"},
            "vulnerability_attestation": {
                "last_attempt_time": {},
                "state": 1,
                "error": "error_value",
            },
            "files": [{"name": "name_value", "digest": {}}],
            "last_vulnerability_update_time": {},
        },
        "attestation": {
            "serialized_payload": b"serialized_payload_blob",
            "signatures": [
                {"signature": b"signature_blob", "public_key_id": "public_key_id_value"}
            ],
            "jwts": [{"compact_jwt": "compact_jwt_value"}],
        },
        "upgrade": {
            "package": "package_value",
            "parsed_version": {},
            "distribution": {
                "cpe_uri": "cpe_uri_value",
                "classification": "classification_value",
                "severity": "severity_value",
                "cve": ["cve_value1", "cve_value2"],
            },
            "windows_update": {
                "identity": {"update_id": "update_id_value", "revision": 879},
                "title": "title_value",
                "description": "description_value",
                "categories": [
                    {"category_id": "category_id_value", "name": "name_value"}
                ],
                "kb_article_ids": ["kb_article_ids_value1", "kb_article_ids_value2"],
                "support_url": "support_url_value",
                "last_published_timestamp": {},
            },
        },
        "compliance": {
            "non_compliant_files": [
                {
                    "path": "path_value",
                    "display_command": "display_command_value",
                    "reason": "reason_value",
                }
            ],
            "non_compliance_reason": "non_compliance_reason_value",
            "version": {
                "cpe_uri": "cpe_uri_value",
                "benchmark_document": "benchmark_document_value",
                "version": "version_value",
            },
        },
        "dsse_attestation": {
            "envelope": {
                "payload": b"payload_blob",
                "payload_type": "payload_type_value",
                "signatures": [{"sig": b"sig_blob", "keyid": "keyid_value"}],
            },
            "statement": {},
        },
        "sbom_reference": {
            "payload": {
                "type_": "type__value",
                "predicate_type": "predicate_type_value",
                "subject": {},
                "predicate": {
                    "referrer_id": "referrer_id_value",
                    "location": "location_value",
                    "mime_type": "mime_type_value",
                    "digest": {},
                },
            },
            "payload_type": "payload_type_value",
            "signatures": {},
        },
        "secret": {
            "kind": 1,
            "locations": [{"file_location": {}}],
            "statuses": [{"status": 1, "update_time": {}, "message": "message_value"}],
            "data": {},
            "digest": {"algo": "algo_value", "digest_bytes": b"digest_bytes_blob"},
        },
        "envelope": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = grafeas.CreateOccurrenceRequest.meta.fields["occurrence"]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init["occurrence"].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["occurrence"][field])):
                    del request_init["occurrence"][field][i][subfield]
            else:
                del request_init["occurrence"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Occurrence(
            name="name_value",
            resource_uri="resource_uri_value",
            note_name="note_name_value",
            kind=common.NoteKind.VULNERABILITY,
            remediation="remediation_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.Occurrence.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_occurrence(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_occurrence_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_create_occurrence"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_create_occurrence_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_create_occurrence"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.CreateOccurrenceRequest.pb(
            grafeas.CreateOccurrenceRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.Occurrence.to_json(grafeas.Occurrence())
        req.return_value.content = return_value

        request = grafeas.CreateOccurrenceRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.Occurrence()
        post_with_metadata.return_value = grafeas.Occurrence(), metadata

        client.create_occurrence(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_create_occurrences_rest_bad_request(
    request_type=grafeas.BatchCreateOccurrencesRequest,
):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.batch_create_occurrences(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.BatchCreateOccurrencesRequest,
        dict,
    ],
)
def test_batch_create_occurrences_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.BatchCreateOccurrencesResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.BatchCreateOccurrencesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_create_occurrences(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.BatchCreateOccurrencesResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_create_occurrences_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_batch_create_occurrences"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor,
            "post_batch_create_occurrences_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_batch_create_occurrences"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.BatchCreateOccurrencesRequest.pb(
            grafeas.BatchCreateOccurrencesRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.BatchCreateOccurrencesResponse.to_json(
            grafeas.BatchCreateOccurrencesResponse()
        )
        req.return_value.content = return_value

        request = grafeas.BatchCreateOccurrencesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.BatchCreateOccurrencesResponse()
        post_with_metadata.return_value = (
            grafeas.BatchCreateOccurrencesResponse(),
            metadata,
        )

        client.batch_create_occurrences(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_occurrence_rest_bad_request(
    request_type=grafeas.UpdateOccurrenceRequest,
):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.update_occurrence(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.UpdateOccurrenceRequest,
        dict,
    ],
)
def test_update_occurrence_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request_init["occurrence"] = {
        "name": "name_value",
        "resource_uri": "resource_uri_value",
        "note_name": "note_name_value",
        "kind": 1,
        "remediation": "remediation_value",
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "vulnerability": {
            "type_": "type__value",
            "severity": 1,
            "cvss_score": 0.1082,
            "cvssv3": {
                "base_score": 0.1046,
                "exploitability_score": 0.21580000000000002,
                "impact_score": 0.1273,
                "attack_vector": 1,
                "attack_complexity": 1,
                "authentication": 1,
                "privileges_required": 1,
                "user_interaction": 1,
                "scope": 1,
                "confidentiality_impact": 1,
                "integrity_impact": 1,
                "availability_impact": 1,
                "attack_requirements": 1,
                "vulnerable_system_confidentiality_impact": 1,
                "vulnerable_system_integrity_impact": 1,
                "vulnerable_system_availability_impact": 1,
                "subsequent_system_confidentiality_impact": 1,
                "subsequent_system_integrity_impact": 1,
                "subsequent_system_availability_impact": 1,
                "exploit_maturity": 1,
            },
            "package_issue": [
                {
                    "affected_cpe_uri": "affected_cpe_uri_value",
                    "affected_package": "affected_package_value",
                    "affected_version": {
                        "epoch": 527,
                        "name": "name_value",
                        "revision": "revision_value",
                        "inclusive": True,
                        "kind": 1,
                        "full_name": "full_name_value",
                    },
                    "fixed_cpe_uri": "fixed_cpe_uri_value",
                    "fixed_package": "fixed_package_value",
                    "fixed_version": {},
                    "fix_available": True,
                    "package_type": "package_type_value",
                    "effective_severity": 1,
                    "file_location": [
                        {
                            "file_path": "file_path_value",
                            "layer_details": {
                                "index": 536,
                                "diff_id": "diff_id_value",
                                "chain_id": "chain_id_value",
                                "command": "command_value",
                                "base_images": [
                                    {
                                        "name": "name_value",
                                        "repository": "repository_value",
                                        "layer_count": 1189,
                                        "registry": "registry_value",
                                    }
                                ],
                            },
                            "line_number": 1168,
                        }
                    ],
                }
            ],
            "short_description": "short_description_value",
            "long_description": "long_description_value",
            "related_urls": [{"url": "url_value", "label": "label_value"}],
            "effective_severity": 1,
            "fix_available": True,
            "cvss_version": 1,
            "cvss_v2": {},
            "vex_assessment": {
                "cve": "cve_value",
                "vulnerability_id": "vulnerability_id_value",
                "related_uris": {},
                "note_name": "note_name_value",
                "state": 1,
                "impacts": ["impacts_value1", "impacts_value2"],
                "remediations": [
                    {
                        "remediation_type": 1,
                        "details": "details_value",
                        "remediation_uri": {},
                    }
                ],
                "justification": {"justification_type": 1, "details": "details_value"},
            },
            "extra_details": "extra_details_value",
            "risk": {
                "cisa_kev": {
                    "known_ransomware_campaign_use": "known_ransomware_campaign_use_value"
                },
                "epss": {"percentile": 0.1067, "score": 0.54},
            },
            "cvss_v4": {},
        },
        "build": {
            "provenance": {
                "id": "id_value",
                "project_id": "project_id_value",
                "commands": [
                    {
                        "name": "name_value",
                        "env": ["env_value1", "env_value2"],
                        "args": ["args_value1", "args_value2"],
                        "dir_": "dir__value",
                        "id": "id_value",
                        "wait_for": ["wait_for_value1", "wait_for_value2"],
                    }
                ],
                "built_artifacts": [
                    {
                        "checksum": "checksum_value",
                        "id": "id_value",
                        "names": ["names_value1", "names_value2"],
                    }
                ],
                "create_time": {},
                "start_time": {},
                "end_time": {},
                "creator": "creator_value",
                "logs_uri": "logs_uri_value",
                "source_provenance": {
                    "artifact_storage_source_uri": "artifact_storage_source_uri_value",
                    "file_hashes": {},
                    "context": {
                        "cloud_repo": {
                            "repo_id": {
                                "project_repo_id": {
                                    "project_id": "project_id_value",
                                    "repo_name": "repo_name_value",
                                },
                                "uid": "uid_value",
                            },
                            "revision_id": "revision_id_value",
                            "alias_context": {"kind": 1, "name": "name_value"},
                        },
                        "gerrit": {
                            "host_uri": "host_uri_value",
                            "gerrit_project": "gerrit_project_value",
                            "revision_id": "revision_id_value",
                            "alias_context": {},
                        },
                        "git": {"url": "url_value", "revision_id": "revision_id_value"},
                        "labels": {},
                    },
                    "additional_contexts": {},
                },
                "trigger_id": "trigger_id_value",
                "build_options": {},
                "builder_version": "builder_version_value",
            },
            "provenance_bytes": "provenance_bytes_value",
            "intoto_provenance": {
                "builder_config": {"id": "id_value"},
                "recipe": {
                    "type_": "type__value",
                    "defined_in_material": 1971,
                    "entry_point": "entry_point_value",
                    "arguments": [
                        {
                            "type_url": "type.googleapis.com/google.protobuf.Duration",
                            "value": b"\x08\x0c\x10\xdb\x07",
                        }
                    ],
                    "environment": {},
                },
                "metadata": {
                    "build_invocation_id": "build_invocation_id_value",
                    "build_started_on": {},
                    "build_finished_on": {},
                    "completeness": {
                        "arguments": True,
                        "environment": True,
                        "materials": True,
                    },
                    "reproducible": True,
                },
                "materials": ["materials_value1", "materials_value2"],
            },
            "intoto_statement": {
                "type_": "type__value",
                "subject": [{"name": "name_value", "digest": {}}],
                "predicate_type": "predicate_type_value",
                "provenance": {},
                "slsa_provenance": {
                    "builder": {"id": "id_value"},
                    "recipe": {
                        "type_": "type__value",
                        "defined_in_material": 1971,
                        "entry_point": "entry_point_value",
                        "arguments": {},
                        "environment": {},
                    },
                    "metadata": {
                        "build_invocation_id": "build_invocation_id_value",
                        "build_started_on": {},
                        "build_finished_on": {},
                        "completeness": {
                            "arguments": True,
                            "environment": True,
                            "materials": True,
                        },
                        "reproducible": True,
                    },
                    "materials": [{"uri": "uri_value", "digest": {}}],
                },
                "slsa_provenance_zero_two": {
                    "builder": {"id": "id_value"},
                    "build_type": "build_type_value",
                    "invocation": {
                        "config_source": {
                            "uri": "uri_value",
                            "digest": {},
                            "entry_point": "entry_point_value",
                        },
                        "parameters": {"fields": {}},
                        "environment": {},
                    },
                    "build_config": {},
                    "metadata": {
                        "build_invocation_id": "build_invocation_id_value",
                        "build_started_on": {},
                        "build_finished_on": {},
                        "completeness": {
                            "parameters": True,
                            "environment": True,
                            "materials": True,
                        },
                        "reproducible": True,
                    },
                    "materials": [{"uri": "uri_value", "digest": {}}],
                },
            },
            "in_toto_slsa_provenance_v1": {
                "type_": "type__value",
                "subject": {},
                "predicate_type": "predicate_type_value",
                "predicate": {
                    "build_definition": {
                        "build_type": "build_type_value",
                        "external_parameters": {},
                        "internal_parameters": {},
                        "resolved_dependencies": [
                            {
                                "name": "name_value",
                                "uri": "uri_value",
                                "digest": {},
                                "content": b"content_blob",
                                "download_location": "download_location_value",
                                "media_type": "media_type_value",
                                "annotations": {},
                            }
                        ],
                    },
                    "run_details": {
                        "builder": {
                            "id": "id_value",
                            "version": {},
                            "builder_dependencies": {},
                        },
                        "metadata": {
                            "invocation_id": "invocation_id_value",
                            "started_on": {},
                            "finished_on": {},
                        },
                        "byproducts": {},
                    },
                },
            },
        },
        "image": {
            "fingerprint": {
                "v1_name": "v1_name_value",
                "v2_blob": ["v2_blob_value1", "v2_blob_value2"],
                "v2_name": "v2_name_value",
            },
            "distance": 843,
            "layer_info": [
                {"directive": "directive_value", "arguments": "arguments_value"}
            ],
            "base_resource_url": "base_resource_url_value",
        },
        "package": {
            "name": "name_value",
            "location": [
                {"cpe_uri": "cpe_uri_value", "version": {}, "path": "path_value"}
            ],
            "package_type": "package_type_value",
            "cpe_uri": "cpe_uri_value",
            "architecture": 1,
            "license_": {
                "expression": "expression_value",
                "comments": "comments_value",
            },
            "version": {},
        },
        "deployment": {
            "user_email": "user_email_value",
            "deploy_time": {},
            "undeploy_time": {},
            "config": "config_value",
            "address": "address_value",
            "resource_uri": ["resource_uri_value1", "resource_uri_value2"],
            "platform": 1,
        },
        "discovery": {
            "continuous_analysis": 1,
            "analysis_status": 1,
            "analysis_completed": {
                "analysis_type": ["analysis_type_value1", "analysis_type_value2"]
            },
            "analysis_error": [
                {"code": 411, "message": "message_value", "details": {}}
            ],
            "analysis_status_error": {},
            "cpe": "cpe_value",
            "last_scan_time": {},
            "archive_time": {},
            "sbom_status": {"sbom_state": 1, "error": "error_value"},
            "vulnerability_attestation": {
                "last_attempt_time": {},
                "state": 1,
                "error": "error_value",
            },
            "files": [{"name": "name_value", "digest": {}}],
            "last_vulnerability_update_time": {},
        },
        "attestation": {
            "serialized_payload": b"serialized_payload_blob",
            "signatures": [
                {"signature": b"signature_blob", "public_key_id": "public_key_id_value"}
            ],
            "jwts": [{"compact_jwt": "compact_jwt_value"}],
        },
        "upgrade": {
            "package": "package_value",
            "parsed_version": {},
            "distribution": {
                "cpe_uri": "cpe_uri_value",
                "classification": "classification_value",
                "severity": "severity_value",
                "cve": ["cve_value1", "cve_value2"],
            },
            "windows_update": {
                "identity": {"update_id": "update_id_value", "revision": 879},
                "title": "title_value",
                "description": "description_value",
                "categories": [
                    {"category_id": "category_id_value", "name": "name_value"}
                ],
                "kb_article_ids": ["kb_article_ids_value1", "kb_article_ids_value2"],
                "support_url": "support_url_value",
                "last_published_timestamp": {},
            },
        },
        "compliance": {
            "non_compliant_files": [
                {
                    "path": "path_value",
                    "display_command": "display_command_value",
                    "reason": "reason_value",
                }
            ],
            "non_compliance_reason": "non_compliance_reason_value",
            "version": {
                "cpe_uri": "cpe_uri_value",
                "benchmark_document": "benchmark_document_value",
                "version": "version_value",
            },
        },
        "dsse_attestation": {
            "envelope": {
                "payload": b"payload_blob",
                "payload_type": "payload_type_value",
                "signatures": [{"sig": b"sig_blob", "keyid": "keyid_value"}],
            },
            "statement": {},
        },
        "sbom_reference": {
            "payload": {
                "type_": "type__value",
                "predicate_type": "predicate_type_value",
                "subject": {},
                "predicate": {
                    "referrer_id": "referrer_id_value",
                    "location": "location_value",
                    "mime_type": "mime_type_value",
                    "digest": {},
                },
            },
            "payload_type": "payload_type_value",
            "signatures": {},
        },
        "secret": {
            "kind": 1,
            "locations": [{"file_location": {}}],
            "statuses": [{"status": 1, "update_time": {}, "message": "message_value"}],
            "data": {},
            "digest": {"algo": "algo_value", "digest_bytes": b"digest_bytes_blob"},
        },
        "envelope": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = grafeas.UpdateOccurrenceRequest.meta.fields["occurrence"]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init["occurrence"].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["occurrence"][field])):
                    del request_init["occurrence"][field][i][subfield]
            else:
                del request_init["occurrence"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Occurrence(
            name="name_value",
            resource_uri="resource_uri_value",
            note_name="note_name_value",
            kind=common.NoteKind.VULNERABILITY,
            remediation="remediation_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.Occurrence.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_occurrence(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Occurrence)
    assert response.name == "name_value"
    assert response.resource_uri == "resource_uri_value"
    assert response.note_name == "note_name_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.remediation == "remediation_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_occurrence_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_update_occurrence"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_update_occurrence_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_update_occurrence"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.UpdateOccurrenceRequest.pb(
            grafeas.UpdateOccurrenceRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.Occurrence.to_json(grafeas.Occurrence())
        req.return_value.content = return_value

        request = grafeas.UpdateOccurrenceRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.Occurrence()
        post_with_metadata.return_value = grafeas.Occurrence(), metadata

        client.update_occurrence(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_occurrence_note_rest_bad_request(
    request_type=grafeas.GetOccurrenceNoteRequest,
):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_occurrence_note(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetOccurrenceNoteRequest,
        dict,
    ],
)
def test_get_occurrence_note_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/occurrences/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_occurrence_note(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_occurrence_note_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_get_occurrence_note"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_get_occurrence_note_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_get_occurrence_note"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.GetOccurrenceNoteRequest.pb(
            grafeas.GetOccurrenceNoteRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.Note.to_json(grafeas.Note())
        req.return_value.content = return_value

        request = grafeas.GetOccurrenceNoteRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.Note()
        post_with_metadata.return_value = grafeas.Note(), metadata

        client.get_occurrence_note(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_note_rest_bad_request(request_type=grafeas.GetNoteRequest):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_note(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.GetNoteRequest,
        dict,
    ],
)
def test_get_note_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_note(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_note_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(transports.GrafeasRestInterceptor, "post_get_note") as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_get_note_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.GrafeasRestInterceptor, "pre_get_note") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.GetNoteRequest.pb(grafeas.GetNoteRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.Note.to_json(grafeas.Note())
        req.return_value.content = return_value

        request = grafeas.GetNoteRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.Note()
        post_with_metadata.return_value = grafeas.Note(), metadata

        client.get_note(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_notes_rest_bad_request(request_type=grafeas.ListNotesRequest):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_notes(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListNotesRequest,
        dict,
    ],
)
def test_list_notes_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.ListNotesResponse(
            next_page_token="next_page_token_value",
            unreachable=["unreachable_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.ListNotesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_notes(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListNotesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_notes_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(transports.GrafeasRestInterceptor, "post_list_notes") as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_list_notes_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.GrafeasRestInterceptor, "pre_list_notes") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.ListNotesRequest.pb(grafeas.ListNotesRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.ListNotesResponse.to_json(grafeas.ListNotesResponse())
        req.return_value.content = return_value

        request = grafeas.ListNotesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.ListNotesResponse()
        post_with_metadata.return_value = grafeas.ListNotesResponse(), metadata

        client.list_notes(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_note_rest_bad_request(request_type=grafeas.DeleteNoteRequest):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_note(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.DeleteNoteRequest,
        dict,
    ],
)
def test_delete_note_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ""
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_note(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_note_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(transports.GrafeasRestInterceptor, "pre_delete_note") as pre,
    ):
        pre.assert_not_called()
        pb_message = grafeas.DeleteNoteRequest.pb(grafeas.DeleteNoteRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        request = grafeas.DeleteNoteRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_note(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_create_note_rest_bad_request(request_type=grafeas.CreateNoteRequest):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.create_note(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.CreateNoteRequest,
        dict,
    ],
)
def test_create_note_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request_init["note"] = {
        "name": "name_value",
        "short_description": "short_description_value",
        "long_description": "long_description_value",
        "kind": 1,
        "related_url": [{"url": "url_value", "label": "label_value"}],
        "expiration_time": {"seconds": 751, "nanos": 543},
        "create_time": {},
        "update_time": {},
        "related_note_names": [
            "related_note_names_value1",
            "related_note_names_value2",
        ],
        "vulnerability": {
            "cvss_score": 0.1082,
            "severity": 1,
            "details": [
                {
                    "severity_name": "severity_name_value",
                    "description": "description_value",
                    "package_type": "package_type_value",
                    "affected_cpe_uri": "affected_cpe_uri_value",
                    "affected_package": "affected_package_value",
                    "affected_version_start": {
                        "epoch": 527,
                        "name": "name_value",
                        "revision": "revision_value",
                        "inclusive": True,
                        "kind": 1,
                        "full_name": "full_name_value",
                    },
                    "affected_version_end": {},
                    "fixed_cpe_uri": "fixed_cpe_uri_value",
                    "fixed_package": "fixed_package_value",
                    "fixed_version": {},
                    "is_obsolete": True,
                    "source_update_time": {},
                    "source": "source_value",
                    "vendor": "vendor_value",
                }
            ],
            "cvss_v3": {
                "base_score": 0.1046,
                "exploitability_score": 0.21580000000000002,
                "impact_score": 0.1273,
                "attack_vector": 1,
                "attack_complexity": 1,
                "privileges_required": 1,
                "user_interaction": 1,
                "scope": 1,
                "confidentiality_impact": 1,
                "integrity_impact": 1,
                "availability_impact": 1,
            },
            "windows_details": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "name": "name_value",
                    "description": "description_value",
                    "fixing_kbs": [{"name": "name_value", "url": "url_value"}],
                }
            ],
            "source_update_time": {},
            "cvss_version": 1,
            "cvss_v2": {
                "base_score": 0.1046,
                "exploitability_score": 0.21580000000000002,
                "impact_score": 0.1273,
                "attack_vector": 1,
                "attack_complexity": 1,
                "authentication": 1,
                "privileges_required": 1,
                "user_interaction": 1,
                "scope": 1,
                "confidentiality_impact": 1,
                "integrity_impact": 1,
                "availability_impact": 1,
                "attack_requirements": 1,
                "vulnerable_system_confidentiality_impact": 1,
                "vulnerable_system_integrity_impact": 1,
                "vulnerable_system_availability_impact": 1,
                "subsequent_system_confidentiality_impact": 1,
                "subsequent_system_integrity_impact": 1,
                "subsequent_system_availability_impact": 1,
                "exploit_maturity": 1,
            },
            "advisory_publish_time": {},
            "cvss_v4": {},
        },
        "build": {"builder_version": "builder_version_value"},
        "image": {
            "resource_url": "resource_url_value",
            "fingerprint": {
                "v1_name": "v1_name_value",
                "v2_blob": ["v2_blob_value1", "v2_blob_value2"],
                "v2_name": "v2_name_value",
            },
        },
        "package": {
            "name": "name_value",
            "distribution": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "architecture": 1,
                    "latest_version": {},
                    "maintainer": "maintainer_value",
                    "url": "url_value",
                    "description": "description_value",
                }
            ],
            "package_type": "package_type_value",
            "cpe_uri": "cpe_uri_value",
            "architecture": 1,
            "version": {},
            "maintainer": "maintainer_value",
            "url": "url_value",
            "description": "description_value",
            "license_": {
                "expression": "expression_value",
                "comments": "comments_value",
            },
            "digest": [{"algo": "algo_value", "digest_bytes": b"digest_bytes_blob"}],
        },
        "deployment": {"resource_uri": ["resource_uri_value1", "resource_uri_value2"]},
        "discovery": {"analysis_kind": 1},
        "attestation": {"hint": {"human_readable_name": "human_readable_name_value"}},
        "upgrade": {
            "package": "package_value",
            "version": {},
            "distributions": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "classification": "classification_value",
                    "severity": "severity_value",
                    "cve": ["cve_value1", "cve_value2"],
                }
            ],
            "windows_update": {
                "identity": {"update_id": "update_id_value", "revision": 879},
                "title": "title_value",
                "description": "description_value",
                "categories": [
                    {"category_id": "category_id_value", "name": "name_value"}
                ],
                "kb_article_ids": ["kb_article_ids_value1", "kb_article_ids_value2"],
                "support_url": "support_url_value",
                "last_published_timestamp": {},
            },
        },
        "compliance": {
            "title": "title_value",
            "description": "description_value",
            "version": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "benchmark_document": "benchmark_document_value",
                    "version": "version_value",
                }
            ],
            "rationale": "rationale_value",
            "remediation": "remediation_value",
            "cis_benchmark": {"profile_level": 1384, "severity": 1},
            "scan_instructions": b"scan_instructions_blob",
            "impact": "impact_value",
        },
        "dsse_attestation": {
            "hint": {"human_readable_name": "human_readable_name_value"}
        },
        "vulnerability_assessment": {
            "title": "title_value",
            "short_description": "short_description_value",
            "long_description": "long_description_value",
            "language_code": "language_code_value",
            "publisher": {
                "name": "name_value",
                "issuing_authority": "issuing_authority_value",
                "publisher_namespace": "publisher_namespace_value",
            },
            "product": {
                "name": "name_value",
                "id": "id_value",
                "generic_uri": "generic_uri_value",
            },
            "assessment": {
                "cve": "cve_value",
                "vulnerability_id": "vulnerability_id_value",
                "short_description": "short_description_value",
                "long_description": "long_description_value",
                "related_uris": {},
                "state": 1,
                "impacts": ["impacts_value1", "impacts_value2"],
                "justification": {"justification_type": 1, "details": "details_value"},
                "remediations": [
                    {
                        "remediation_type": 1,
                        "details": "details_value",
                        "remediation_uri": {},
                    }
                ],
            },
        },
        "sbom_reference": {"format_": "format__value", "version": "version_value"},
        "secret": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = grafeas.CreateNoteRequest.meta.fields["note"]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init["note"].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["note"][field])):
                    del request_init["note"][field][i][subfield]
            else:
                del request_init["note"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_note(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_note_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_create_note"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_create_note_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.GrafeasRestInterceptor, "pre_create_note") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.CreateNoteRequest.pb(grafeas.CreateNoteRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.Note.to_json(grafeas.Note())
        req.return_value.content = return_value

        request = grafeas.CreateNoteRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.Note()
        post_with_metadata.return_value = grafeas.Note(), metadata

        client.create_note(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_create_notes_rest_bad_request(
    request_type=grafeas.BatchCreateNotesRequest,
):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.batch_create_notes(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.BatchCreateNotesRequest,
        dict,
    ],
)
def test_batch_create_notes_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.BatchCreateNotesResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.BatchCreateNotesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_create_notes(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.BatchCreateNotesResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_create_notes_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_batch_create_notes"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_batch_create_notes_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_batch_create_notes"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.BatchCreateNotesRequest.pb(
            grafeas.BatchCreateNotesRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.BatchCreateNotesResponse.to_json(
            grafeas.BatchCreateNotesResponse()
        )
        req.return_value.content = return_value

        request = grafeas.BatchCreateNotesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.BatchCreateNotesResponse()
        post_with_metadata.return_value = grafeas.BatchCreateNotesResponse(), metadata

        client.batch_create_notes(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_note_rest_bad_request(request_type=grafeas.UpdateNoteRequest):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.update_note(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.UpdateNoteRequest,
        dict,
    ],
)
def test_update_note_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request_init["note"] = {
        "name": "name_value",
        "short_description": "short_description_value",
        "long_description": "long_description_value",
        "kind": 1,
        "related_url": [{"url": "url_value", "label": "label_value"}],
        "expiration_time": {"seconds": 751, "nanos": 543},
        "create_time": {},
        "update_time": {},
        "related_note_names": [
            "related_note_names_value1",
            "related_note_names_value2",
        ],
        "vulnerability": {
            "cvss_score": 0.1082,
            "severity": 1,
            "details": [
                {
                    "severity_name": "severity_name_value",
                    "description": "description_value",
                    "package_type": "package_type_value",
                    "affected_cpe_uri": "affected_cpe_uri_value",
                    "affected_package": "affected_package_value",
                    "affected_version_start": {
                        "epoch": 527,
                        "name": "name_value",
                        "revision": "revision_value",
                        "inclusive": True,
                        "kind": 1,
                        "full_name": "full_name_value",
                    },
                    "affected_version_end": {},
                    "fixed_cpe_uri": "fixed_cpe_uri_value",
                    "fixed_package": "fixed_package_value",
                    "fixed_version": {},
                    "is_obsolete": True,
                    "source_update_time": {},
                    "source": "source_value",
                    "vendor": "vendor_value",
                }
            ],
            "cvss_v3": {
                "base_score": 0.1046,
                "exploitability_score": 0.21580000000000002,
                "impact_score": 0.1273,
                "attack_vector": 1,
                "attack_complexity": 1,
                "privileges_required": 1,
                "user_interaction": 1,
                "scope": 1,
                "confidentiality_impact": 1,
                "integrity_impact": 1,
                "availability_impact": 1,
            },
            "windows_details": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "name": "name_value",
                    "description": "description_value",
                    "fixing_kbs": [{"name": "name_value", "url": "url_value"}],
                }
            ],
            "source_update_time": {},
            "cvss_version": 1,
            "cvss_v2": {
                "base_score": 0.1046,
                "exploitability_score": 0.21580000000000002,
                "impact_score": 0.1273,
                "attack_vector": 1,
                "attack_complexity": 1,
                "authentication": 1,
                "privileges_required": 1,
                "user_interaction": 1,
                "scope": 1,
                "confidentiality_impact": 1,
                "integrity_impact": 1,
                "availability_impact": 1,
                "attack_requirements": 1,
                "vulnerable_system_confidentiality_impact": 1,
                "vulnerable_system_integrity_impact": 1,
                "vulnerable_system_availability_impact": 1,
                "subsequent_system_confidentiality_impact": 1,
                "subsequent_system_integrity_impact": 1,
                "subsequent_system_availability_impact": 1,
                "exploit_maturity": 1,
            },
            "advisory_publish_time": {},
            "cvss_v4": {},
        },
        "build": {"builder_version": "builder_version_value"},
        "image": {
            "resource_url": "resource_url_value",
            "fingerprint": {
                "v1_name": "v1_name_value",
                "v2_blob": ["v2_blob_value1", "v2_blob_value2"],
                "v2_name": "v2_name_value",
            },
        },
        "package": {
            "name": "name_value",
            "distribution": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "architecture": 1,
                    "latest_version": {},
                    "maintainer": "maintainer_value",
                    "url": "url_value",
                    "description": "description_value",
                }
            ],
            "package_type": "package_type_value",
            "cpe_uri": "cpe_uri_value",
            "architecture": 1,
            "version": {},
            "maintainer": "maintainer_value",
            "url": "url_value",
            "description": "description_value",
            "license_": {
                "expression": "expression_value",
                "comments": "comments_value",
            },
            "digest": [{"algo": "algo_value", "digest_bytes": b"digest_bytes_blob"}],
        },
        "deployment": {"resource_uri": ["resource_uri_value1", "resource_uri_value2"]},
        "discovery": {"analysis_kind": 1},
        "attestation": {"hint": {"human_readable_name": "human_readable_name_value"}},
        "upgrade": {
            "package": "package_value",
            "version": {},
            "distributions": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "classification": "classification_value",
                    "severity": "severity_value",
                    "cve": ["cve_value1", "cve_value2"],
                }
            ],
            "windows_update": {
                "identity": {"update_id": "update_id_value", "revision": 879},
                "title": "title_value",
                "description": "description_value",
                "categories": [
                    {"category_id": "category_id_value", "name": "name_value"}
                ],
                "kb_article_ids": ["kb_article_ids_value1", "kb_article_ids_value2"],
                "support_url": "support_url_value",
                "last_published_timestamp": {},
            },
        },
        "compliance": {
            "title": "title_value",
            "description": "description_value",
            "version": [
                {
                    "cpe_uri": "cpe_uri_value",
                    "benchmark_document": "benchmark_document_value",
                    "version": "version_value",
                }
            ],
            "rationale": "rationale_value",
            "remediation": "remediation_value",
            "cis_benchmark": {"profile_level": 1384, "severity": 1},
            "scan_instructions": b"scan_instructions_blob",
            "impact": "impact_value",
        },
        "dsse_attestation": {
            "hint": {"human_readable_name": "human_readable_name_value"}
        },
        "vulnerability_assessment": {
            "title": "title_value",
            "short_description": "short_description_value",
            "long_description": "long_description_value",
            "language_code": "language_code_value",
            "publisher": {
                "name": "name_value",
                "issuing_authority": "issuing_authority_value",
                "publisher_namespace": "publisher_namespace_value",
            },
            "product": {
                "name": "name_value",
                "id": "id_value",
                "generic_uri": "generic_uri_value",
            },
            "assessment": {
                "cve": "cve_value",
                "vulnerability_id": "vulnerability_id_value",
                "short_description": "short_description_value",
                "long_description": "long_description_value",
                "related_uris": {},
                "state": 1,
                "impacts": ["impacts_value1", "impacts_value2"],
                "justification": {"justification_type": 1, "details": "details_value"},
                "remediations": [
                    {
                        "remediation_type": 1,
                        "details": "details_value",
                        "remediation_uri": {},
                    }
                ],
            },
        },
        "sbom_reference": {"format_": "format__value", "version": "version_value"},
        "secret": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = grafeas.UpdateNoteRequest.meta.fields["note"]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init["note"].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["note"][field])):
                    del request_init["note"][field][i][subfield]
            else:
                del request_init["note"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.Note(
            name="name_value",
            short_description="short_description_value",
            long_description="long_description_value",
            kind=common.NoteKind.VULNERABILITY,
            related_note_names=["related_note_names_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.Note.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_note(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, grafeas.Note)
    assert response.name == "name_value"
    assert response.short_description == "short_description_value"
    assert response.long_description == "long_description_value"
    assert response.kind == common.NoteKind.VULNERABILITY
    assert response.related_note_names == ["related_note_names_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_note_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_update_note"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_update_note_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.GrafeasRestInterceptor, "pre_update_note") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.UpdateNoteRequest.pb(grafeas.UpdateNoteRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.Note.to_json(grafeas.Note())
        req.return_value.content = return_value

        request = grafeas.UpdateNoteRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.Note()
        post_with_metadata.return_value = grafeas.Note(), metadata

        client.update_note(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_note_occurrences_rest_bad_request(
    request_type=grafeas.ListNoteOccurrencesRequest,
):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_note_occurrences(request)


@pytest.mark.parametrize(
    "request_type",
    [
        grafeas.ListNoteOccurrencesRequest,
        dict,
    ],
)
def test_list_note_occurrences_rest_call_success(request_type):
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/notes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = grafeas.ListNoteOccurrencesResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = grafeas.ListNoteOccurrencesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_note_occurrences(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListNoteOccurrencesPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_note_occurrences_rest_interceptors(null_interceptor):
    transport = transports.GrafeasRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.GrafeasRestInterceptor(),
    )
    client = GrafeasClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "post_list_note_occurrences"
        ) as post,
        mock.patch.object(
            transports.GrafeasRestInterceptor,
            "post_list_note_occurrences_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GrafeasRestInterceptor, "pre_list_note_occurrences"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = grafeas.ListNoteOccurrencesRequest.pb(
            grafeas.ListNoteOccurrencesRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = grafeas.ListNoteOccurrencesResponse.to_json(
            grafeas.ListNoteOccurrencesResponse()
        )
        req.return_value.content = return_value

        request = grafeas.ListNoteOccurrencesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = grafeas.ListNoteOccurrencesResponse()
        post_with_metadata.return_value = (
            grafeas.ListNoteOccurrencesResponse(),
            metadata,
        )

        client.list_note_occurrences(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_initialize_client_w_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_occurrence_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_occurrence), "__call__") as call:
        client.get_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_occurrences_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_occurrences), "__call__") as call:
        client.list_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListOccurrencesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_occurrence_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_occurrence), "__call__"
    ) as call:
        client.delete_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_occurrence_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_occurrence), "__call__"
    ) as call:
        client.create_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_occurrences_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_occurrences), "__call__"
    ) as call:
        client.batch_create_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateOccurrencesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_occurrence_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_occurrence), "__call__"
    ) as call:
        client.update_occurrence(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateOccurrenceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_occurrence_note_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_occurrence_note), "__call__"
    ) as call:
        client.get_occurrence_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetOccurrenceNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_note_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_note), "__call__") as call:
        client.get_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.GetNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_notes_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_notes), "__call__") as call:
        client.list_notes(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNotesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_note_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_note), "__call__") as call:
        client.delete_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.DeleteNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_note_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_note), "__call__") as call:
        client.create_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.CreateNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_notes_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_notes), "__call__"
    ) as call:
        client.batch_create_notes(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.BatchCreateNotesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_note_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_note), "__call__") as call:
        client.update_note(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.UpdateNoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_note_occurrences_empty_call_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_note_occurrences), "__call__"
    ) as call:
        client.list_note_occurrences(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = grafeas.ListNoteOccurrencesRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.GrafeasGrpcTransport,
    )


def test_grafeas_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "grafeas.grafeas_v1.services.grafeas.transports.GrafeasTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.GrafeasTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_occurrence",
        "list_occurrences",
        "delete_occurrence",
        "create_occurrence",
        "batch_create_occurrences",
        "update_occurrence",
        "get_occurrence_note",
        "get_note",
        "list_notes",
        "delete_note",
        "create_note",
        "batch_create_notes",
        "update_note",
        "list_note_occurrences",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Catch all for all remaining methods and properties
    remainder = [
        "kind",
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_grafeas_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "grafeas.grafeas_v1.services.grafeas.transports.GrafeasTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.GrafeasTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(),
            quota_project_id="octopus",
        )


def test_grafeas_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "grafeas.grafeas_v1.services.grafeas.transports.GrafeasTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.GrafeasTransport()
        adc.assert_called_once()


def test_grafeas_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        GrafeasClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GrafeasGrpcTransport,
        transports.GrafeasGrpcAsyncIOTransport,
    ],
)
def test_grafeas_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GrafeasGrpcTransport,
        transports.GrafeasGrpcAsyncIOTransport,
        transports.GrafeasRestTransport,
    ],
)
def test_grafeas_transport_auth_gdch_credentials(transport_class):
    host = "https://language.com"
    api_audience_tests = [None, "https://language2.com"]
    api_audience_expect = [host, "https://language2.com"]
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, "default", autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(
                return_value=gdch_mock
            )
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(e)


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.GrafeasGrpcTransport, grpc_helpers),
        (transports.GrafeasGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_grafeas_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch.object(
            grpc_helpers, "create_channel", autospec=True
        ) as create_channel,
    ):
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])

        create_channel.assert_called_with(
            ":443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(),
            scopes=["1", "2"],
            default_host="",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [transports.GrafeasGrpcTransport, transports.GrafeasGrpcAsyncIOTransport],
)
def test_grafeas_grpc_transport_client_cert_source_for_mtls(transport_class):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds,
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback,
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert, private_key=expected_key
            )


def test_grafeas_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.GrafeasRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


def test_grafeas_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.GrafeasGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_grafeas_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.GrafeasGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.filterwarnings("ignore::FutureWarning")
@pytest.mark.parametrize(
    "transport_class",
    [transports.GrafeasGrpcTransport, transports.GrafeasGrpcAsyncIOTransport],
)
def test_grafeas_transport_channel_mtls_with_client_cert_source(transport_class):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [transports.GrafeasGrpcTransport, transports.GrafeasGrpcAsyncIOTransport],
)
def test_grafeas_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_note_path():
    project = "squid"
    note = "clam"
    expected = "projects/{project}/notes/{note}".format(
        project=project,
        note=note,
    )
    actual = GrafeasClient.note_path(project, note)
    assert expected == actual


def test_parse_note_path():
    expected = {
        "project": "whelk",
        "note": "octopus",
    }
    path = GrafeasClient.note_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_note_path(path)
    assert expected == actual


def test_occurrence_path():
    project = "oyster"
    occurrence = "nudibranch"
    expected = "projects/{project}/occurrences/{occurrence}".format(
        project=project,
        occurrence=occurrence,
    )
    actual = GrafeasClient.occurrence_path(project, occurrence)
    assert expected == actual


def test_parse_occurrence_path():
    expected = {
        "project": "cuttlefish",
        "occurrence": "mussel",
    }
    path = GrafeasClient.occurrence_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_occurrence_path(path)
    assert expected == actual


def test_project_path():
    project = "winkle"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = GrafeasClient.project_path(project)
    assert expected == actual


def test_parse_project_path():
    expected = {
        "project": "nautilus",
    }
    path = GrafeasClient.project_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_project_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "scallop"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = GrafeasClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "abalone",
    }
    path = GrafeasClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "squid"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = GrafeasClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "clam",
    }
    path = GrafeasClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "whelk"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = GrafeasClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "octopus",
    }
    path = GrafeasClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "oyster"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = GrafeasClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nudibranch",
    }
    path = GrafeasClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = GrafeasClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = GrafeasClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = GrafeasClient.parse_common_location_path(path)
    assert expected == actual


def test_transport_close_grpc():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


@pytest.mark.asyncio
async def test_transport_close_grpc_asyncio():
    client = GrafeasAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = GrafeasClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_session")), "close"
    ) as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


def test_client_ctx():
    transports = [
        "rest",
        "grpc",
    ]
    for transport in transports:
        client = GrafeasClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()
