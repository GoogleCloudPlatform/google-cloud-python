# -*- coding: utf-8 -*-
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
#

from unittest import mock

import pytest
from grpc.experimental import aio

try:
    from google.auth.aio import credentials as ga_credentials_async

    HAS_GOOGLE_AUTH_AIO = True
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

from google.api_core import gapic_v1, grpc_helpers_async
from google.auth import credentials as ga_credentials

from google.cloud.bigtable_v2.services.bigtable.async_client import BigtableAsyncClient
from google.cloud.bigtable_v2.services.bigtable.client import BigtableClient
from google.cloud.bigtable_v2.types import bigtable

# This test file duplicates the gapic request header tests so that the temporary fix
# for SQL app_profile_id header handling can not be override by GAPIC.
# TODO: remove this once the fix is upstreamed


def async_anonymous_credentials():
    if HAS_GOOGLE_AUTH_AIO:
        return ga_credentials_async.AnonymousCredentials()
    return ga_credentials.AnonymousCredentials()


def test_prepare_query_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        call.return_value = bigtable.PrepareQueryResponse()
        client.prepare_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )

        assert args[0] == request_msg

        # expect app_profile_id while temporary patch is in place: https://github.com/googleapis/python-bigtable/pull/1109
        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_prepare_query_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PrepareQueryResponse(
                prepared_query=b"prepared_query_blob",
            )
        )
        await client.prepare_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )

        assert args[0] == request_msg

        # expect app_profile_id while temporary patch is in place: https://github.com/googleapis/python-bigtable/pull/1109
        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_execute_query_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        call.return_value = iter([bigtable.ExecuteQueryResponse()])
        client.execute_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )

        assert args[0] == request_msg

        # expect app_profile_id while temporary patch is in place: https://github.com/googleapis/python-bigtable/pull/1109
        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_execute_query_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ExecuteQueryResponse()]
        )
        await client.execute_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )

        assert args[0] == request_msg

        # expect app_profile_id while temporary patch is in place: https://github.com/googleapis/python-bigtable/pull/1109
        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )
