# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest  # type: ignore
import pytest_asyncio  # type: ignore
from aioresponses import aioresponses  # type: ignore

import google.auth.aio.transport.aiohttp as auth_aiohttp
from google.auth import exceptions
from google.auth.aio import _helpers as _helpers_async

try:
    import aiohttp  # type: ignore
except ImportError as caught_exc:  # pragma: NO COVER
    raise ImportError(
        "The aiohttp library is not installed from please install the aiohttp package to use the aiohttp transport."
    ) from caught_exc


@pytest.fixture
def mock_response():
    response = Mock()
    response.status = 200
    response.headers = {"Content-Type": "application/json", "Content-Length": "100"}
    mock_iterator = AsyncMock()
    mock_iterator.__aiter__.return_value = iter(
        [b"Cavefish ", b"have ", b"no ", b"sight."]
    )
    response.content.iter_chunked = lambda chunk_size: mock_iterator
    response.read = AsyncMock(return_value=b"Cavefish have no sight.")
    response.close = AsyncMock()

    return auth_aiohttp.Response(response)


class TestResponse(object):
    @pytest.mark.asyncio
    async def test_response_status_code(self, mock_response):
        assert mock_response.status_code == 200

    @pytest.mark.asyncio
    async def test_response_headers(self, mock_response):
        assert mock_response.headers["Content-Type"] == "application/json"
        assert mock_response.headers["Content-Length"] == "100"

    @pytest.mark.asyncio
    async def test_response_content(self, mock_response):
        content = b"".join([chunk async for chunk in mock_response.content()])
        assert content == b"Cavefish have no sight."

    @pytest.mark.asyncio
    async def test_response_content_raises_error(self, mock_response):
        with patch.object(
            mock_response._response.content,
            "iter_chunked",
            side_effect=aiohttp.ClientPayloadError,
        ):
            with pytest.raises(exceptions.ResponseError) as exc:
                [chunk async for chunk in mock_response.content()]
            exc.match("Failed to read from the payload stream")

    @pytest.mark.asyncio
    async def test_response_read(self, mock_response):
        content = await mock_response.read()
        assert content == b"Cavefish have no sight."

    @pytest.mark.asyncio
    async def test_response_read_raises_error(self, mock_response):
        with patch.object(
            mock_response._response,
            "read",
            side_effect=aiohttp.ClientResponseError(None, None),
        ):
            with pytest.raises(exceptions.ResponseError) as exc:
                await mock_response.read()
            exc.match("Failed to read the response body.")

    @pytest.mark.asyncio
    async def test_response_close(self, mock_response):
        await mock_response.close()
        mock_response._response.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_response_content_stream(self, mock_response):
        itr = mock_response.content().__aiter__()
        content = []
        try:
            while True:
                chunk = await itr.__anext__()
                content.append(chunk)
        except StopAsyncIteration:
            pass
        assert b"".join(content) == b"Cavefish have no sight."


@pytest.mark.asyncio
class TestRequest:
    @pytest_asyncio.fixture
    async def aiohttp_request(self):
        request = auth_aiohttp.Request()
        yield request
        await request.close()

    async def test_request_call_success(self, aiohttp_request):
        with aioresponses() as m:
            mocked_chunks = [b"Cavefish ", b"have ", b"no ", b"sight."]
            mocked_response = b"".join(mocked_chunks)
            m.get("http://example.com", status=200, body=mocked_response)
            response = await aiohttp_request("http://example.com")
            assert response.status_code == 200
            assert response.headers == {"Content-Type": "application/json"}
            content = b"".join([chunk async for chunk in response.content()])
            assert content == b"Cavefish have no sight."

    async def test_request_call_success_with_provided_session(self):
        mock_session = aiohttp.ClientSession()
        request = auth_aiohttp.Request(mock_session)
        with aioresponses() as m:
            mocked_chunks = [b"Cavefish ", b"have ", b"no ", b"sight."]
            mocked_response = b"".join(mocked_chunks)
            m.get("http://example.com", status=200, body=mocked_response)
            response = await request("http://example.com")
            assert response.status_code == 200
            assert response.headers == {"Content-Type": "application/json"}
            content = b"".join([chunk async for chunk in response.content()])
            assert content == b"Cavefish have no sight."

    async def test_request_call_raises_client_error(self, aiohttp_request):
        with aioresponses() as m:
            m.get("http://example.com", exception=aiohttp.ClientError)

            with pytest.raises(exceptions.TransportError) as exc:
                await aiohttp_request("http://example.com/api")

            exc.match("Failed to send request to http://example.com/api.")

    async def test_request_call_raises_timeout_error(self, aiohttp_request):
        with aioresponses() as m:
            m.get("http://example.com", exception=asyncio.TimeoutError)

            with pytest.raises(exceptions.TimeoutError) as exc:
                await aiohttp_request(
                    "http://example.com", timeout=aiohttp.ClientTimeout(total=120)
                )

            exc.match("Request timed out after 120 seconds.")

    async def test_request_call_raises_transport_error_for_closed_session(
        self, aiohttp_request
    ):
        with aioresponses() as m:
            m.get("http://example.com", exception=asyncio.TimeoutError)
            aiohttp_request._closed = True
            with pytest.raises(exceptions.TransportError) as exc:
                await aiohttp_request("http://example.com")

            exc.match("session is closed.")
            aiohttp_request._closed = False

    async def test_request_clone(self):
        request = auth_aiohttp.Request()
        cloned = request._clone()
        assert cloned is not request
        assert isinstance(cloned, auth_aiohttp.Request)
        assert cloned._session is not request._session
        await request.close()
        await cloned.close()

    async def test_request_close(self):
        request = auth_aiohttp.Request()
        assert not getattr(request, "_closed", False)
        await request.close()
        assert request._closed
        # Second call should be idempotent
        await request.close()
        assert request._closed

    async def test_request_clone_closed_session_raises(self):
        request = auth_aiohttp.Request()
        await request.close()
        with pytest.raises(exceptions.TransportError) as exc:
            request._clone()
        exc.match("Cannot clone a closed transport.")

    async def test_request_clone_with_active_session(self):
        import ssl

        from aiohttp import BasicAuth, ClientTimeout, TCPConnector

        custom_ssl = ssl.create_default_context()
        custom_connector = TCPConnector(
            ssl=custom_ssl,
            limit=42,
            limit_per_host=12,
            force_close=True,
            local_addr=("127.0.0.2", 0),
        )

        mock_session = aiohttp.ClientSession(
            connector=custom_connector,
            headers={"x-corporate-firewall": "open"},
            cookies={"enterprise_session": "active"},
            auth=BasicAuth("admin", "secret"),
            timeout=ClientTimeout(total=84.0),
            trust_env=True,
            trace_configs=[aiohttp.TraceConfig()],
        )
        request = auth_aiohttp.Request(session=mock_session)

        cloned = request._clone()

        assert cloned is not request
        assert cloned._session is not mock_session
        assert cloned._session is not None

        # Verify underlying TCPConnector configuration
        cloned_connector = cloned._session._connector
        assert isinstance(cloned_connector, TCPConnector)
        assert cloned_connector is not custom_connector
        assert cloned_connector._resolver is not custom_connector._resolver
        assert cloned_connector._ssl is custom_ssl
        assert cloned_connector._limit == 42
        assert cloned_connector._limit_per_host == 12
        assert cloned_connector._force_close is True
        assert _helpers_async._get_local_addr(cloned_connector) == (
            "127.0.0.2",
            0,
        )

        # Verify session-level configuration
        assert cloned._session._trust_env is True
        assert len(cloned._session._trace_configs) == 1
        assert cloned._session._default_headers == {"x-corporate-firewall": "open"}
        assert cloned._session._cookie_jar is mock_session._cookie_jar
        assert cloned._session._default_auth == mock_session._default_auth
        assert cloned._session._timeout == ClientTimeout(total=84.0)

        await request.close()
        await cloned.close()

    async def test_request_clone_unix_socket(self):
        try:
            from aiohttp import UnixConnector
        except ImportError:
            return  # Windows or environment without Unix Domain Sockets

        connector = UnixConnector(path="/var/run/enterprise.sock", limit=42)
        mock_session = aiohttp.ClientSession(connector=connector)
        request = auth_aiohttp.Request(session=mock_session)

        cloned = request._clone()

        assert cloned._session is not None
        cloned_connector = cloned._session._connector
        assert isinstance(cloned_connector, UnixConnector)
        assert cloned_connector._path == "/var/run/enterprise.sock"
        assert cloned_connector._limit == 42

        await request.close()
        await cloned.close()

    async def test_request_call_raises_timeout_error_int(self, aiohttp_request):
        with aioresponses() as m:
            m.get("http://example.com", exception=asyncio.TimeoutError)
            with pytest.raises(exceptions.TimeoutError) as exc:
                await aiohttp_request("http://example.com", timeout=120)
            exc.match("Request timed out after 120 seconds.")

    async def test_request_clone_with_closed_connector(self):
        session = aiohttp.ClientSession()
        request = auth_aiohttp.Request(session=session)
        await session.close()

        cloned = request._clone()
        assert cloned is not request
        assert cloned._session is not None
        await request.close()
        await cloned.close()

    async def test_request_clone_with_custom_connector(self):
        session = aiohttp.ClientSession()
        custom_connector = AsyncMock()
        custom_connector.closed = False
        custom_connector.close = AsyncMock()
        session._connector = custom_connector

        request = auth_aiohttp.Request(session=session)
        with pytest.raises(
            exceptions.TransportError, match="Unsupported connector type for cloning"
        ):
            request._clone()
        await request.close()

    async def test_request_clone_unix_socket_no_path(self):
        try:
            from aiohttp import UnixConnector
        except ImportError:
            return

        session = aiohttp.ClientSession()
        connector = UnixConnector(path="/tmp/test.sock")
        connector._path = None
        session._connector = connector

        request = auth_aiohttp.Request(session=session)
        cloned = request._clone()
        assert cloned is not request
        assert cloned._session is not None
        assert cloned._session._connector is not connector
        await request.close()
        await cloned.close()
