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
import http.client as http_client
import threading
from typing import AsyncGenerator
from unittest.mock import AsyncMock, Mock, patch

import pytest  # type: ignore
from aioresponses import aioresponses  # type: ignore

import google.auth.credentials
import google.auth.transport.requests
from google.auth.aio.credentials import AnonymousCredentials, Credentials
from google.auth.aio.transport import (
    _DEFAULT_TIMEOUT_SECONDS,
    DEFAULT_MAX_RETRY_ATTEMPTS,
    DEFAULT_RETRYABLE_STATUS_CODES,
    Request,
    Response,
    sessions,
)
from google.auth.exceptions import (
    InvalidType,
    RefreshError,
    TimeoutError,
    TransportError,
)


@pytest.fixture
def simple_async_task():
    # Wrap async fixture within a synchronous fixture to suppress pytest.PytestRemovedIn9Warning
    # See https://docs.pytest.org/en/stable/deprecations.html#sync-test-depending-on-async-fixture
    async def inner_fixture():
        return True

    return inner_fixture()


class MockRequest(Request):
    def __init__(self, response=None, side_effect=None):
        self._closed = False
        self._response = response
        self._side_effect = side_effect
        self.call_count = 0

    async def __call__(
        self,
        url,
        method="GET",
        body=None,
        headers=None,
        timeout=_DEFAULT_TIMEOUT_SECONDS,
        total_attempts=DEFAULT_MAX_RETRY_ATTEMPTS,
        **kwargs,
    ):
        self.call_count += 1
        if self._side_effect:
            raise self._side_effect
        return self._response

    async def close(self):
        self._closed = True
        return None


class MockResponse(Response):
    def __init__(self, status_code, headers=None, content=None):
        self._status_code = status_code
        self._headers = headers
        self._content = content
        self._close = False

    @property
    def status_code(self):
        return self._status_code

    @property
    def headers(self):
        return self._headers

    async def read(self) -> bytes:
        content = await self.content(1024)
        return b"".join([chunk async for chunk in content])

    async def content(self, chunk_size=None) -> AsyncGenerator:
        return self._content

    async def close(self) -> None:
        self._close = True


class TestTimeoutGuard(object):
    default_timeout = 1

    def make_timeout_guard(self, timeout):
        return sessions.timeout_guard(timeout)

    @pytest.mark.asyncio
    async def test_timeout_with_simple_async_task_within_bounds(
        self, simple_async_task
    ):
        task = False
        with patch(
            "time.monotonic", side_effect=lambda it=iter([0, 0.25]): next(it, 0.75)
        ):
            with patch("asyncio.wait_for", lambda coro, _: coro):
                async with self.make_timeout_guard(
                    timeout=self.default_timeout
                ) as with_timeout:
                    task = await with_timeout(simple_async_task)

        # Task succeeds.
        assert task is True

    @pytest.mark.asyncio
    async def test_timeout_with_simple_async_task_out_of_bounds(
        self, simple_async_task
    ):
        task = False
        with patch("time.monotonic", side_effect=[0, 1, 1]):
            with pytest.raises(TimeoutError) as exc:
                async with self.make_timeout_guard(
                    timeout=self.default_timeout
                ) as with_timeout:
                    task = await with_timeout(simple_async_task)

        # Task does not succeed and the context manager times out i.e. no remaining time left.
        assert task is False
        assert exc.match(
            f"Context manager exceeded the configured timeout of {self.default_timeout}s."
        )

    @pytest.mark.asyncio
    async def test_timeout_with_async_task_timing_out_before_context(
        self, simple_async_task
    ):
        task = False
        with pytest.raises(TimeoutError) as exc:
            async with self.make_timeout_guard(
                timeout=self.default_timeout
            ) as with_timeout:
                with patch("asyncio.wait_for", side_effect=asyncio.TimeoutError):
                    task = await with_timeout(simple_async_task)

        # Task does not complete i.e. the operation times out.
        assert task is False
        assert exc.match(
            f"The operation {simple_async_task} exceeded the configured timeout of {self.default_timeout}s."
        )


class TestAsyncAuthorizedSession(object):
    TEST_URL = "http://example.com/"
    credentials = AnonymousCredentials()

    @pytest.fixture
    def mocked_content(self):
        # Wrap async fixture within a synchronous fixture to suppress pytest.PytestRemovedIn9Warning
        # See https://docs.pytest.org/en/stable/deprecations.html#sync-test-depending-on-async-fixture
        async def inner_fixture():
            content = [b"Cavefish ", b"have ", b"no ", b"sight."]
            for chunk in content:
                yield chunk

        return inner_fixture()

    @pytest.mark.asyncio
    async def test_constructor_with_default_auth_request(self):
        with patch("google.auth.aio.transport.sessions.AIOHTTP_INSTALLED", True):
            authed_session = sessions.AsyncAuthorizedSession(self.credentials)
        assert authed_session._credentials == self.credentials
        await authed_session.close()

    @pytest.mark.asyncio
    async def test_constructor_with_provided_auth_request(self):
        auth_request = MockRequest()
        authed_session = sessions.AsyncAuthorizedSession(
            self.credentials, auth_request=auth_request
        )

        assert authed_session._auth_request is auth_request
        await authed_session.close()

    @pytest.mark.asyncio
    async def test_constructor_raises_no_auth_request_error(self):
        with patch("google.auth.aio.transport.sessions.AIOHTTP_INSTALLED", False):
            with pytest.raises(TransportError) as exc:
                sessions.AsyncAuthorizedSession(self.credentials)

        exc.match(
            "`auth_request` must either be configured or the external package `aiohttp` must be installed to use the default value."
        )

    @pytest.mark.asyncio
    async def test_constructor_raises_incorrect_credentials_error(self):
        credentials = Mock()
        with pytest.raises(InvalidType) as exc:
            sessions.AsyncAuthorizedSession(credentials)

        exc.match(
            f"The configured credentials of type {type(credentials)} are invalid and must be of type `google.auth.aio.credentials.Credentials` or `google.auth.credentials.Credentials`"
        )

    @pytest.mark.asyncio
    async def test_constructor_with_sync_credentials(self):
        sync_credentials = google.auth.credentials.AnonymousCredentials()
        authed_session = sessions.AsyncAuthorizedSession(
            sync_credentials, auth_request=MockRequest()
        )

        # Synchronous credentials are adapted to the asynchronous credentials interface.
        assert isinstance(authed_session._credentials, Credentials)
        assert isinstance(authed_session._credentials, sessions._SyncCredentialsAdapter)
        assert authed_session._credentials._credentials is sync_credentials
        with patch.object(
            authed_session._credentials,
            "close",
            wraps=authed_session._credentials.close,
        ) as mock_close:
            await authed_session.close()
            mock_close.assert_called_once()

    @pytest.mark.asyncio
    async def test_request_with_sync_credentials_success(self, mocked_content):
        sync_credentials = Mock(spec=google.auth.credentials.Credentials)
        mocked_response = MockResponse(
            status_code=http_client.OK,
            headers={"Content-Type": "application/json"},
            content=mocked_content,
        )
        auth_request = MockRequest(mocked_response)
        authed_session = sessions.AsyncAuthorizedSession(sync_credentials, auth_request)

        response = await authed_session.request(
            "GET", self.TEST_URL, headers={"x-test": "value"}
        )

        assert response.status_code == http_client.OK
        assert await response.read() == b"Cavefish have no sight."
        # The synchronous credentials are invoked with a synchronous transport rather
        # than the asynchronous transport of the session.
        sync_credentials.before_request.assert_called_once()
        request, method, url, headers = sync_credentials.before_request.call_args.args
        assert isinstance(request, google.auth.transport.requests.Request)
        assert method == "GET"
        assert url == self.TEST_URL
        assert headers == {"x-test": "value"}
        await authed_session.close()

    @pytest.mark.asyncio
    async def test_request_with_sync_credentials_refreshes_on_unauthorized(self):
        sync_credentials = Mock(spec=google.auth.credentials.Credentials)
        unauthorized_response = MockResponse(status_code=http_client.UNAUTHORIZED)
        ok_response = MockResponse(status_code=http_client.OK)
        auth_request = AsyncMock(side_effect=[unauthorized_response, ok_response])
        authed_session = sessions.AsyncAuthorizedSession(
            sync_credentials, auth_request=auth_request
        )

        response = await authed_session.request("GET", self.TEST_URL)

        assert response is ok_response
        assert auth_request.call_count == 2
        assert unauthorized_response._close
        sync_credentials.refresh.assert_called_once()
        (refresh_request,) = sync_credentials.refresh.call_args.args
        assert isinstance(refresh_request, google.auth.transport.requests.Request)
        # The same synchronous transport is reused for every call to the credentials.
        assert refresh_request is sync_credentials.before_request.call_args.args[0]
        await authed_session.close()

    @pytest.mark.asyncio
    async def test_request_default_auth_request_success(self):
        with aioresponses() as m:
            mocked_chunks = [b"Cavefish ", b"have ", b"no ", b"sight."]
            mocked_response = b"".join(mocked_chunks)
            m.get(self.TEST_URL, status=200, body=mocked_response)
            authed_session = sessions.AsyncAuthorizedSession(self.credentials)
            response = await authed_session.request("GET", self.TEST_URL)
            assert response.status_code == 200
            assert response.headers == {"Content-Type": "application/json"}
            assert await response.read() == b"Cavefish have no sight."
            await response.close()

        await authed_session.close()

    @pytest.mark.asyncio
    async def test_request_provided_auth_request_success(self, mocked_content):
        mocked_response = MockResponse(
            status_code=200,
            headers={"Content-Type": "application/json"},
            content=mocked_content,
        )
        auth_request = MockRequest(mocked_response)
        authed_session = sessions.AsyncAuthorizedSession(self.credentials, auth_request)
        response = await authed_session.request("GET", self.TEST_URL)
        assert response.status_code == 200
        assert response.headers == {"Content-Type": "application/json"}
        assert await response.read() == b"Cavefish have no sight."
        await response.close()
        assert response._close

        await authed_session.close()

    @pytest.mark.asyncio
    async def test_request_raises_timeout_error(self):
        auth_request = MockRequest(side_effect=asyncio.TimeoutError)
        authed_session = sessions.AsyncAuthorizedSession(self.credentials, auth_request)
        with pytest.raises(TimeoutError):
            await authed_session.request("GET", self.TEST_URL)

    @pytest.mark.asyncio
    async def test_request_raises_transport_error(self):
        auth_request = MockRequest(side_effect=TransportError)
        authed_session = sessions.AsyncAuthorizedSession(self.credentials, auth_request)
        with pytest.raises(TransportError):
            await authed_session.request("GET", self.TEST_URL)

    @pytest.mark.asyncio
    async def test_request_max_allowed_time_exceeded_error(self):
        auth_request = MockRequest(side_effect=TransportError)
        authed_session = sessions.AsyncAuthorizedSession(self.credentials, auth_request)
        with patch("time.monotonic", side_effect=[0, 0] + [2] * 10):
            with pytest.raises(TimeoutError):
                await authed_session.request("GET", self.TEST_URL, max_allowed_time=1)

    @pytest.mark.parametrize("retry_status", DEFAULT_RETRYABLE_STATUS_CODES)
    @pytest.mark.asyncio
    async def test_request_total_attempt_1(self, retry_status):
        mocked_response = MockResponse(status_code=retry_status)
        auth_request = MockRequest(mocked_response)
        with patch("asyncio.sleep", return_value=None):
            authed_session = sessions.AsyncAuthorizedSession(
                self.credentials, auth_request
            )
            await authed_session.request(
                "GET", self.TEST_URL, max_allowed_time=float("inf"), total_attempts=1
            )
            assert auth_request.call_count == 1

    @pytest.mark.parametrize("retry_status", DEFAULT_RETRYABLE_STATUS_CODES)
    @pytest.mark.asyncio
    async def test_request_max_retries(self, retry_status):
        mocked_response = MockResponse(status_code=retry_status)
        auth_request = MockRequest(mocked_response)
        with patch("asyncio.sleep", return_value=None):
            authed_session = sessions.AsyncAuthorizedSession(
                self.credentials, auth_request
            )
            await authed_session.request("GET", self.TEST_URL)
            assert auth_request.call_count == DEFAULT_MAX_RETRY_ATTEMPTS

    @pytest.mark.asyncio
    async def test_request_closes_previous_response_before_retry(self):
        retry_response = MockResponse(status_code=503)
        success_response = MockResponse(status_code=200)

        class _SequenceMockRequest(MockRequest):
            def __init__(self, responses):
                super().__init__(response=None)
                self._responses = responses

            async def __call__(self, *args, **kwargs):
                self.call_count += 1
                return self._responses[self.call_count - 1]

        auth_request = _SequenceMockRequest([retry_response, success_response])
        with patch("asyncio.sleep", return_value=None):
            authed_session = sessions.AsyncAuthorizedSession(
                self.credentials, auth_request
            )
            response = await authed_session.request(
                "GET",
                self.TEST_URL,
                max_allowed_time=float("inf"),
                total_attempts=2,
            )
            assert response is success_response
            assert auth_request.call_count == 2
            # The initial retryable response must be closed before the retry
            # so its connection is released back to the pool.
            assert retry_response._close
            # The final response is left open for the caller to close.
            assert not success_response._close

        await authed_session.close()

    @pytest.mark.asyncio
    async def test_http_get_method_success(self):
        expected_payload = b"content is retrieved."
        authed_session = sessions.AsyncAuthorizedSession(self.credentials)
        with aioresponses() as m:
            m.get(self.TEST_URL, status=200, body=expected_payload)
            response = await authed_session.get(self.TEST_URL)
            assert await response.read() == expected_payload
            response = await authed_session.close()

    @pytest.mark.asyncio
    async def test_http_post_method_success(self):
        expected_payload = b"content is posted."
        authed_session = sessions.AsyncAuthorizedSession(self.credentials)
        with aioresponses() as m:
            m.post(self.TEST_URL, status=200, body=expected_payload)
            response = await authed_session.post(self.TEST_URL)
            assert await response.read() == expected_payload
            response = await authed_session.close()

    @pytest.mark.asyncio
    async def test_http_put_method_success(self):
        expected_payload = b"content is retrieved."
        authed_session = sessions.AsyncAuthorizedSession(self.credentials)
        with aioresponses() as m:
            m.put(self.TEST_URL, status=200, body=expected_payload)
            response = await authed_session.put(self.TEST_URL)
            assert await response.read() == expected_payload
            response = await authed_session.close()

    @pytest.mark.asyncio
    async def test_http_patch_method_success(self):
        expected_payload = b"content is retrieved."
        authed_session = sessions.AsyncAuthorizedSession(self.credentials)
        with aioresponses() as m:
            m.patch(self.TEST_URL, status=200, body=expected_payload)
            response = await authed_session.patch(self.TEST_URL)
            assert await response.read() == expected_payload
            response = await authed_session.close()

    @pytest.mark.asyncio
    async def test_http_delete_method_success(self):
        expected_payload = b"content is deleted."
        authed_session = sessions.AsyncAuthorizedSession(self.credentials)
        with aioresponses() as m:
            m.delete(self.TEST_URL, status=200, body=expected_payload)
            response = await authed_session.delete(self.TEST_URL)
            assert await response.read() == expected_payload
            response = await authed_session.close()

    @pytest.mark.asyncio
    async def test_configure_mtls_channel_with_custom_transport_and_broken_cert(self):
        auth_request = MockRequest()
        authed_session = sessions.AsyncAuthorizedSession(
            self.credentials, auth_request=auth_request
        )

        with patch(
            "google.auth.transport._mtls_helper.check_use_client_cert",
            return_value=True,
        ):

            def callback():
                return b"invalid-cert", b"invalid-key"

            with pytest.warns(
                UserWarning,
                match="Attempted to establish mTLS, but a custom async transport was provided",
            ):
                await authed_session.configure_mtls_channel(callback)

            assert authed_session._is_mtls is False
            assert authed_session._cached_cert is None

        await authed_session.close()


def test_mock_request_clone():
    request = MockRequest()
    cloned = request._clone()
    assert cloned is request


class BlockingRefreshCredentials(google.auth.credentials.Credentials):
    """Synchronous credentials whose refresh blocks until released by the test."""

    def __init__(self):
        super().__init__()
        self.refresh_calls = 0
        self.in_flight_refreshes = 0
        self.max_in_flight_refreshes = 0
        self.refresh_started = threading.Event()
        self.release_refresh = threading.Event()

    def refresh(self, request):
        self.refresh_calls += 1
        self.in_flight_refreshes += 1
        self.max_in_flight_refreshes = max(
            self.max_in_flight_refreshes, self.in_flight_refreshes
        )
        self.refresh_started.set()
        self.release_refresh.wait(timeout=5)
        self.in_flight_refreshes -= 1
        self.token = "token"


class TestSyncCredentialsAdapter(object):
    TEST_URL = "http://example.com/"

    @pytest.mark.asyncio
    async def test_delegates_to_sync_credentials(self):
        sync_credentials = Mock(spec=google.auth.credentials.Credentials)
        sync_credentials.token = "sync-token"
        sync_credentials.expiry = Mock()
        sync_credentials.valid = True
        sync_credentials.expired = False
        adapter = sessions._SyncCredentialsAdapter(sync_credentials)
        headers = {}

        await adapter.before_request(Mock(), "GET", self.TEST_URL, headers)
        await adapter.refresh(Mock())
        await adapter.apply(headers, token="token")

        assert adapter.token == "sync-token"
        assert adapter.expiry is sync_credentials.expiry
        assert adapter.valid is True
        assert adapter.expired is False

        # The same synchronous transport is used for every call.
        sync_request = sync_credentials.before_request.call_args.args[0]
        assert isinstance(sync_request, google.auth.transport.requests.Request)
        sync_credentials.before_request.assert_called_once_with(
            sync_request, "GET", self.TEST_URL, headers
        )
        sync_credentials.refresh.assert_called_once_with(sync_request)
        sync_credentials.apply.assert_called_once_with(headers, token="token")
        with patch.object(sync_request.session, "close") as mock_close:
            adapter.close()
            mock_close.assert_called_once()

    @pytest.mark.asyncio
    async def test_blocking_calls_run_off_the_event_loop_thread(self):
        sync_credentials = Mock(spec=google.auth.credentials.Credentials)
        thread_ids = []
        sync_credentials.before_request.side_effect = lambda *args: thread_ids.append(
            threading.get_ident()
        )
        sync_credentials.refresh.side_effect = lambda *args: thread_ids.append(
            threading.get_ident()
        )
        adapter = sessions._SyncCredentialsAdapter(sync_credentials)

        await adapter.before_request(Mock(), "GET", self.TEST_URL, {})
        await adapter.refresh(Mock())

        assert len(thread_ids) == 2
        assert threading.get_ident() not in thread_ids

    @pytest.mark.asyncio
    async def test_concurrent_before_request_refreshes_once(self):
        sync_credentials = BlockingRefreshCredentials()
        adapter = sessions._SyncCredentialsAdapter(sync_credentials)
        headers = [{} for _ in range(5)]

        tasks = [
            asyncio.create_task(adapter.before_request(Mock(), "GET", self.TEST_URL, h))
            for h in headers
        ]
        await asyncio.to_thread(sync_credentials.refresh_started.wait, 5)
        # Yield to the event loop so all tasks run until they await the refresh.
        await asyncio.sleep(0)
        sync_credentials.release_refresh.set()
        await asyncio.gather(*tasks)

        assert sync_credentials.refresh_calls == 1
        assert all(h["authorization"] == "Bearer token" for h in headers)

    @pytest.mark.asyncio
    async def test_refresh_and_before_request_share_one_refresh(self):
        sync_credentials = BlockingRefreshCredentials()
        adapter = sessions._SyncCredentialsAdapter(sync_credentials)
        headers = {}

        refresh_task = asyncio.create_task(adapter.refresh(Mock()))
        await asyncio.to_thread(sync_credentials.refresh_started.wait, 5)
        before_request_task = asyncio.create_task(
            adapter.before_request(Mock(), "GET", self.TEST_URL, headers)
        )
        # Yield to the event loop so before_request_task reaches the refresh.
        await asyncio.sleep(0)
        sync_credentials.release_refresh.set()
        await asyncio.gather(refresh_task, before_request_task)

        assert sync_credentials.max_in_flight_refreshes == 1
        assert sync_credentials.refresh_calls == 1
        assert headers["authorization"] == "Bearer token"

    @pytest.mark.asyncio
    async def test_cancelled_caller_does_not_abandon_refresh(self):
        sync_credentials = BlockingRefreshCredentials()
        adapter = sessions._SyncCredentialsAdapter(sync_credentials)

        cancelled_task = asyncio.create_task(
            adapter.before_request(Mock(), "GET", self.TEST_URL, {})
        )
        await asyncio.to_thread(sync_credentials.refresh_started.wait, 5)
        cancelled_task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await cancelled_task

        # The refresh started on behalf of the cancelled request is still running:
        # a new request must wait for it rather than start a second refresh.
        headers = {}
        waiting_task = asyncio.create_task(
            adapter.before_request(Mock(), "GET", self.TEST_URL, headers)
        )
        await asyncio.sleep(0)
        assert not waiting_task.done()
        sync_credentials.release_refresh.set()
        await waiting_task

        assert sync_credentials.refresh_calls == 1
        assert sync_credentials.max_in_flight_refreshes == 1
        assert headers["authorization"] == "Bearer token"

    @pytest.mark.asyncio
    async def test_failed_refresh_is_not_reused(self):
        sync_credentials = Mock(spec=google.auth.credentials.Credentials)
        sync_credentials.refresh.side_effect = [RefreshError("refresh failed"), None]
        adapter = sessions._SyncCredentialsAdapter(sync_credentials)

        with pytest.raises(RefreshError):
            await adapter.refresh(Mock())
        await adapter.refresh(Mock())

        assert sync_credentials.refresh.call_count == 2

    @pytest.mark.asyncio
    async def test_before_request_with_valid_credentials_does_not_wait_for_refresh(
        self,
    ):
        sync_credentials = BlockingRefreshCredentials()
        sync_credentials.token = "token"
        adapter = sessions._SyncCredentialsAdapter(sync_credentials)
        headers = {}

        refresh_task = asyncio.create_task(adapter.refresh(Mock()))
        await asyncio.to_thread(sync_credentials.refresh_started.wait, 5)
        # Requests that already have a valid token must not wait for the refresh.
        await asyncio.wait_for(
            adapter.before_request(Mock(), "GET", self.TEST_URL, headers), timeout=5
        )
        assert headers["authorization"] == "Bearer token"

        sync_credentials.release_refresh.set()
        await refresh_task
        assert sync_credentials.refresh_calls == 1
