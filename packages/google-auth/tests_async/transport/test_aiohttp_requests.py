# Copyright 2020 Google LLC
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

from unittest import mock

import aiohttp  # type: ignore
import pytest  # type: ignore
from aioresponses import aioresponses, core  # type: ignore

import google.auth._credentials_async
import google.auth.transport._mtls_helper
from google.auth.transport import _aiohttp_requests as aiohttp_requests
from tests_async.transport import async_compliance


class TestCombinedResponse:
    @pytest.mark.asyncio
    async def test__is_compressed(self):
        response = core.CallbackResult(headers={"Content-Encoding": "gzip"})
        combined_response = aiohttp_requests._CombinedResponse(response)
        compressed = combined_response._is_compressed()
        assert compressed

    def test__is_compressed_not(self):
        response = core.CallbackResult(headers={"Content-Encoding": "not"})
        combined_response = aiohttp_requests._CombinedResponse(response)
        compressed = combined_response._is_compressed()
        assert not compressed

    @pytest.mark.asyncio
    async def test_raw_content(self):
        mock_response = mock.AsyncMock()
        mock_response.content.read.return_value = mock.sentinel.read
        combined_response = aiohttp_requests._CombinedResponse(response=mock_response)
        raw_content = await combined_response.raw_content()
        assert raw_content == mock.sentinel.read

        # Second call to validate the preconfigured path.
        combined_response._raw_content = mock.sentinel.stored_raw
        raw_content = await combined_response.raw_content()
        assert raw_content == mock.sentinel.stored_raw

    @pytest.mark.asyncio
    async def test_content(self):
        mock_response = mock.AsyncMock()
        mock_response.content.read.return_value = mock.sentinel.read
        combined_response = aiohttp_requests._CombinedResponse(response=mock_response)
        content = await combined_response.content()
        assert content == mock.sentinel.read

    @mock.patch(
        "google.auth.transport._aiohttp_requests.urllib3.response.MultiDecoder.decompress",
        return_value="decompressed",
        autospec=True,
    )
    @pytest.mark.asyncio
    async def test_content_compressed(self, urllib3_mock):
        rm = core.RequestMatch(
            "url", headers={"Content-Encoding": "gzip"}, payload="compressed"
        )
        response = await rm.build_response(core.URL("url"))

        combined_response = aiohttp_requests._CombinedResponse(response=response)
        content = await combined_response.content()

        urllib3_mock.assert_called_once()
        assert content == "decompressed"


class TestResponse:
    def test_ctor(self):
        response = aiohttp_requests._Response(mock.sentinel.response)
        assert response._response == mock.sentinel.response

    @pytest.mark.asyncio
    async def test_headers_prop(self):
        rm = core.RequestMatch("url", headers={"Content-Encoding": "header prop"})
        mock_response = await rm.build_response(core.URL("url"))

        response = aiohttp_requests._Response(mock_response)
        assert response.headers["Content-Encoding"] == "header prop"

    @pytest.mark.asyncio
    async def test_status_prop(self):
        rm = core.RequestMatch("url", status=123)
        mock_response = await rm.build_response(core.URL("url"))
        response = aiohttp_requests._Response(mock_response)
        assert response.status == 123

    @pytest.mark.asyncio
    async def test_data_prop(self):
        mock_response = mock.AsyncMock()
        mock_response.content.read.return_value = mock.sentinel.read
        response = aiohttp_requests._Response(mock_response)
        data = await response.data.read()
        assert data == mock.sentinel.read


class TestRequestResponse(async_compliance.RequestResponseTests):
    def make_request(self):
        return aiohttp_requests.Request()

    def make_with_parameter_request(self):
        http = aiohttp.ClientSession(auto_decompress=False)
        return aiohttp_requests.Request(http)

    @pytest.mark.asyncio
    async def test_unsupported_session(self):
        http = aiohttp.ClientSession(auto_decompress=True)
        with pytest.raises(ValueError):
            await aiohttp_requests.Request(http)

    def test_mock_session_unspecified_auto_decompress(self):
        # A plain mock object (without spec) will return a mock on attribute access.
        # Ensure this does not trigger InvalidOperation.
        http = mock.Mock()
        request = aiohttp_requests.Request(http)
        assert request.session == http

    def test_timeout(self):
        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        request = aiohttp_requests.Request(http)
        request(url="http://example.com", method="GET", timeout=5)

    @pytest.mark.asyncio
    async def test__clone(self):
        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        http._connector = mock.Mock(spec=aiohttp.TCPConnector)
        http._connector.closed = False
        http._connector._ssl = mock.sentinel.ssl
        http._connector._limit = 50
        http._connector._limit_per_host = 10
        http._connector._force_close = True
        http._connector._resolver = mock.sentinel.resolver
        http._connector._local_addr = mock.sentinel.local_addr

        http._trust_env = False
        http._trace_configs = [mock.sentinel.trace_config]
        http._default_headers = {"test": "header"}
        http._cookie_jar = mock.sentinel.cookie_jar
        http._default_auth = mock.sentinel.auth
        http._timeout = mock.sentinel.timeout
        http._json_serialize = mock.sentinel.json_serialize

        request = aiohttp_requests.Request(http)
        with (
            mock.patch("aiohttp.ClientSession", autospec=True) as session_mock,
            mock.patch.object(
                aiohttp.TCPConnector, "__init__", autospec=True, return_value=None
            ) as connector_init_mock,
        ):
            session_mock.return_value.auto_decompress = False
            cloned = request._clone()

        assert isinstance(cloned, aiohttp_requests.Request)
        assert cloned is not request

        connector_init_mock.assert_called_once_with(
            mock.ANY,
            ssl=mock.sentinel.ssl,
            limit=50,
            limit_per_host=10,
            force_close=True,
            local_addr=mock.sentinel.local_addr,
        )

        session_mock.assert_called_once_with(
            connector=mock.ANY,
            auto_decompress=False,
            trust_env=False,
            trace_configs=[mock.sentinel.trace_config],
            headers={"test": "header"},
            cookie_jar=mock.sentinel.cookie_jar,
            auth=mock.sentinel.auth,
            timeout=mock.sentinel.timeout,
            json_serialize=mock.sentinel.json_serialize,
        )
        assert isinstance(session_mock.call_args[1]["connector"], aiohttp.TCPConnector)

    @pytest.mark.asyncio
    async def test__clone_closed(self):
        request = aiohttp_requests.Request()
        request._closed = True
        with pytest.raises(
            google.auth.exceptions.TransportError,
            match="Cannot clone a closed transport.",
        ):
            request._clone()

    @pytest.mark.asyncio
    async def test__clone_custom_connector(self):
        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        http._connector = mock.Mock()
        http._connector.closed = False
        request = aiohttp_requests.Request(http)
        with pytest.raises(
            google.auth.exceptions.TransportError,
            match="Unsupported connector type for cloning",
        ):
            request._clone()

    @pytest.mark.asyncio
    async def test_close(self):
        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        http.close = mock.AsyncMock()
        request = aiohttp_requests.Request(http)

        await request.close()
        assert request._closed is True
        http.close.assert_awaited_once()

        # Check idempotency
        await request.close()
        http.close.assert_awaited_once()  # Still only called 1 time

    @pytest.mark.asyncio
    async def test_request_call_closed(self):
        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        request = aiohttp_requests.Request(http)
        await request.close()
        with pytest.raises(
            google.auth.exceptions.TransportError, match="session is closed."
        ):
            await request("http://example.com")

    @pytest.mark.asyncio
    async def test__clone_no_session(self):
        request = aiohttp_requests.Request()
        cloned = request._clone()
        assert isinstance(cloned, aiohttp_requests.Request)
        assert cloned is not request
        assert cloned.session is not None
        await cloned.close()

    @pytest.mark.asyncio
    async def test__clone_closed_connector(self):
        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        http._connector = mock.Mock()
        http._connector.closed = True
        http._trust_env = True
        http._trace_configs = None
        http._default_headers = None
        http._cookie_jar = None
        http._default_auth = None
        http._timeout = None
        http._json_serialize = None

        request = aiohttp_requests.Request(http)
        with mock.patch("aiohttp.ClientSession", autospec=True) as session_mock:
            session_mock.return_value.auto_decompress = False
            cloned = request._clone()

        assert isinstance(cloned, aiohttp_requests.Request)
        assert cloned is not request

    @pytest.mark.asyncio
    async def test__clone_unix_socket_no_path(self):
        try:
            from aiohttp import UnixConnector
        except ImportError:
            return

        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        http._connector = mock.Mock(spec=UnixConnector)
        http._connector.closed = False
        http._connector._path = None
        http._trust_env = True
        http._trace_configs = None
        http._default_headers = None
        http._cookie_jar = None
        http._default_auth = None
        http._timeout = None
        http._json_serialize = None

        request = aiohttp_requests.Request(http)
        with mock.patch("aiohttp.ClientSession", autospec=True) as session_mock:
            session_mock.return_value.auto_decompress = False
            cloned = request._clone()

        assert isinstance(cloned, aiohttp_requests.Request)
        assert cloned is not request

    @pytest.mark.asyncio
    async def test__clone_unix_socket_with_path(self):
        try:
            from aiohttp import UnixConnector
        except ImportError:
            return

        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        http._connector = mock.Mock(spec=UnixConnector)
        http._connector.closed = False
        http._connector._path = "/tmp/test.sock"
        http._connector._limit = 42
        http._connector._force_close = True
        http._trust_env = True
        http._trace_configs = None
        http._default_headers = None
        http._cookie_jar = None
        http._default_auth = None
        http._timeout = None
        http._json_serialize = None

        request = aiohttp_requests.Request(http)
        with (
            mock.patch("aiohttp.ClientSession", autospec=True) as session_mock,
            mock.patch.object(
                UnixConnector, "__init__", autospec=True, return_value=None
            ) as connector_init_mock,
        ):
            session_mock.return_value.auto_decompress = False
            cloned = request._clone()

        assert isinstance(cloned, aiohttp_requests.Request)
        assert cloned is not request
        connector_init_mock.assert_called_once_with(
            mock.ANY,
            path="/tmp/test.sock",
            limit=42,
            force_close=True,
        )


class CredentialsStub(google.auth._credentials_async.Credentials):
    def __init__(self, token="token"):
        super(CredentialsStub, self).__init__()
        self.token = token

    def apply(self, headers, token=None):
        headers["authorization"] = self.token

    def refresh(self, request):
        self.token += "1"


class TestAuthorizedSession(object):
    TEST_URL = "http://example.com/"
    method = "GET"

    @pytest.mark.asyncio
    async def test_constructor(self):
        authed_session = aiohttp_requests.AuthorizedSession(mock.sentinel.credentials)
        assert authed_session.credentials == mock.sentinel.credentials

    @pytest.mark.asyncio
    async def test_constructor_with_auth_request(self):
        http = mock.create_autospec(
            aiohttp.ClientSession, instance=True, auto_decompress=False
        )
        auth_request = aiohttp_requests.Request(http)

        authed_session = aiohttp_requests.AuthorizedSession(
            mock.sentinel.credentials, auth_request=auth_request
        )

        assert authed_session._auth_request == auth_request

    @pytest.mark.asyncio
    async def test_request(self):
        with aioresponses() as mocked:
            credentials = mock.Mock(wraps=CredentialsStub())

            mocked.get(self.TEST_URL, status=200, body="test")
            session = aiohttp_requests.AuthorizedSession(credentials)
            resp = await session.request(
                "GET",
                "http://example.com/",
                headers={"Keep-Alive": "timeout=5, max=1000", "fake": b"bytes"},
            )

            assert resp.status == 200
            assert "test" == await resp.text()

            await session.close()

    @pytest.mark.asyncio
    async def test_ctx(self):
        with aioresponses() as mocked:
            credentials = mock.Mock(wraps=CredentialsStub())
            mocked.get("http://test.example.com", payload=dict(foo="bar"))
            session = aiohttp_requests.AuthorizedSession(credentials)
            resp = await session.request("GET", "http://test.example.com")
            data = await resp.json()

            assert dict(foo="bar") == data

            await session.close()

    @pytest.mark.asyncio
    async def test_http_headers(self):
        with aioresponses() as mocked:
            credentials = mock.Mock(wraps=CredentialsStub())
            mocked.post(
                "http://example.com",
                payload=dict(),
                headers=dict(connection="keep-alive"),
            )

            session = aiohttp_requests.AuthorizedSession(credentials)
            resp = await session.request("POST", "http://example.com")

            assert resp.headers["Connection"] == "keep-alive"

            await session.close()

    @pytest.mark.asyncio
    async def test_regexp_example(self):
        with aioresponses() as mocked:
            credentials = mock.Mock(wraps=CredentialsStub())
            mocked.get("http://example.com", status=500)
            mocked.get("http://example.com", status=200)

            session1 = aiohttp_requests.AuthorizedSession(credentials)

            resp1 = await session1.request("GET", "http://example.com")
            session2 = aiohttp_requests.AuthorizedSession(credentials)
            resp2 = await session2.request("GET", "http://example.com")

            assert resp1.status == 500
            assert resp2.status == 200

            await session1.close()
            await session2.close()

    @pytest.mark.asyncio
    async def test_request_no_refresh(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        with aioresponses() as mocked:
            mocked.get("http://example.com", status=200)
            authed_session = aiohttp_requests.AuthorizedSession(credentials)
            response = await authed_session.request("GET", "http://example.com")
            assert response.status == 200
            assert credentials.before_request.called
            assert not credentials.refresh.called

            await authed_session.close()

    @pytest.mark.asyncio
    async def test_request_refresh(self):
        credentials = mock.Mock(wraps=CredentialsStub())
        with aioresponses() as mocked:
            mocked.get("http://example.com", status=401)
            mocked.get("http://example.com", status=200)
            authed_session = aiohttp_requests.AuthorizedSession(credentials)
            response = await authed_session.request("GET", "http://example.com")
            assert credentials.refresh.called
            assert response.status == 200

            await authed_session.close()
