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

import os
import pytest
import grpc
from google.auth import exceptions


def test_client(echo):
    with echo as c:
        resp = c.echo({"content": "hello"})
        assert resp.content == "hello"


def test_client_destroyed(echo):
    # The REST session is fine with being closed multiple times.
    if "rest" in str(echo.transport).lower():
        return

    echo.__exit__(None, None, None)
    with pytest.raises(ValueError):
        echo.echo({"content": "hello"})


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_client_async(async_echo):
        async with async_echo:
            response = await async_echo.echo({"content": "hello"})
            assert response.content == "hello"

    @pytest.mark.asyncio
    async def test_client_destroyed_async(async_echo):
        await async_echo.__aexit__(None, None, None)
        with pytest.raises((grpc._cython.cygrpc.UsageError, exceptions.TransportError)):
            await async_echo.echo({"content": "hello"})
