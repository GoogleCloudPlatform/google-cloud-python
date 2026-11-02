# Copyright 2018 Google LLC
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

import os
import pytest
import re

from google.api_core import exceptions
from google.rpc import code_pb2

from google import showcase

UUID4_RE = r"[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}"


def test_unary_with_request_object(echo):
    response = echo.echo(
        showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails.",
            request_id="some_value",
            other_request_id="",
        )
    )
    assert response.content == "The hail in Wales falls mainly on the snails."
    assert response.request_id == "some_value"
    assert response.other_request_id == ""

    # Repeat the same test but this time without `request_id`` set
    # The `request_id` field should be automatically populated with
    # a UUID4 value if it is not set.
    # See https://google.aip.dev/client-libraries/4235
    response = echo.echo(
        showcase.EchoRequest(
            content="The hail in Wales falls mainly on the snails.",
        )
    )
    assert response.content == "The hail in Wales falls mainly on the snails."
    # Ensure that the uuid4 field is set according to AIP 4235
    assert re.match(UUID4_RE, response.request_id)
    assert len(response.request_id) == 36
    # Ensure that the uuid4 field is set according to AIP 4235
    assert re.match(UUID4_RE, response.other_request_id)
    assert len(response.other_request_id) == 36


def test_unary_with_dict(echo):
    response = echo.echo(
        {
            "content": "The hail in Wales falls mainly on the snails.",
            "request_id": "some_value",
            "other_request_id": "",
        }
    )
    assert response.content == "The hail in Wales falls mainly on the snails."
    assert response.request_id == "some_value"
    assert response.other_request_id == ""

    # Repeat the same test but this time without `request_id`` set
    # The `request_id` field should be automatically populated with
    # a UUID4 value if it is not set.
    # See https://google.aip.dev/client-libraries/4235
    response = echo.echo(
        {
            "content": "The hail in Wales falls mainly on the snails.",
        }
    )
    assert response.content == "The hail in Wales falls mainly on the snails."
    assert re.match(UUID4_RE, response.request_id)
    assert len(response.request_id) == 36
    # Ensure that the uuid4 field is set according to AIP 4235
    assert re.match(UUID4_RE, response.other_request_id)
    assert len(response.other_request_id) == 36


def test_unary_error(echo):
    message = "Bad things! Bad things!"
    http_message = f"POST http://localhost:7469/v1beta1/echo:echo: {message}"
    # Note: InvalidArgument is from gRPC, BadRequest from http (no MTLS), InternalServerError from http (MTLS)
    # TODO: Reduce number of different exception types here.
    with pytest.raises(
        (
            exceptions.InvalidArgument,
            exceptions.BadRequest,
            exceptions.InternalServerError,
        )
    ) as exc:
        echo.echo(
            {
                "error": {
                    "code": code_pb2.Code.Value("INVALID_ARGUMENT"),
                    "message": message,
                },
            }
        )
    err_message = message if "grpc" in str(echo.transport) else http_message
    assert exc.value.code == 400
    assert exc.value.message == err_message

    if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
        # Under gRPC, we raise exceptions.InvalidArgument, which is a
        # sub-class of exceptions.BadRequest.
        with pytest.raises(exceptions.InvalidArgument) as exc:
            echo.echo(
                {
                    "error": {
                        "code": code_pb2.Code.Value("INVALID_ARGUMENT"),
                        "message": message,
                    },
                }
            )
        assert exc.value.code == 400
        assert exc.value.message == message


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":
    import asyncio

    @pytest.mark.asyncio
    async def test_async_unary_with_request_object(async_echo):
        response = await async_echo.echo(
            showcase.EchoRequest(
                content="The hail in Wales falls mainly on the snails.",
            ),
            timeout=1,
        )
        assert response.content == "The hail in Wales falls mainly on the snails."

    @pytest.mark.asyncio
    async def test_async_unary_with_dict(async_echo):
        response = await async_echo.echo(
            {
                "content": "The hail in Wales falls mainly on the snails.",
            }
        )
        assert response.content == "The hail in Wales falls mainly on the snails."

    @pytest.mark.asyncio
    async def test_async_unary_error(async_echo):
        message = "Bad things! Bad things!"
        expected_err_message = (
            message
            if "grpc_asyncio" in str(async_echo.transport)
            else f"POST http://localhost:7469/v1beta1/echo:echo: {message}"
        )
        # Note: InvalidArgument is from gRPC, BadRequest from http (no MTLS)
        with pytest.raises((exceptions.InvalidArgument, exceptions.BadRequest)) as exc:
            await async_echo.echo(
                {
                    "error": {
                        "code": code_pb2.Code.Value(
                            "INVALID_ARGUMENT",
                        ),
                        "message": message,
                    },
                }
            )
        assert exc.value.code == 400
        assert exc.value.message == expected_err_message
