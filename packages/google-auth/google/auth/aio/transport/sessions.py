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
import collections.abc
import functools
import http.client as http_client
import inspect
import logging
import time
import warnings
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Mapping, Optional, Union

import google.auth.credentials
import google.auth.transport._mtls_helper
from google.auth import _exponential_backoff, _helpers, exceptions
from google.auth.aio import transport
from google.auth.aio.credentials import Credentials
from google.auth.aio.transport import mtls
from google.auth.exceptions import TimeoutError

if TYPE_CHECKING:  # pragma: NO COVER
    import aiohttp
    from aiohttp import ClientTimeout  # type: ignore

else:
    try:
        import aiohttp
        from aiohttp import ClientTimeout
    except (ImportError, AttributeError):
        ClientTimeout = None

_LOGGER = logging.getLogger(__name__)

# Tracks the internal aiohttp installation and usage
try:
    from google.auth.aio.transport.aiohttp import Request as AiohttpRequest

    AIOHTTP_INSTALLED = True
except ImportError:  # pragma: NO COVER
    AIOHTTP_INSTALLED = False


@asynccontextmanager
async def timeout_guard(timeout):
    """
    timeout_guard is an asynchronous context manager to apply a timeout to an asynchronous block of code.

    Args:
        timeout (float): The time in seconds before the context manager times out.

    Raises:
        google.auth.exceptions.TimeoutError: If the code within the context exceeds the provided timeout.

    Usage:
        async with timeout_guard(10) as with_timeout:
            await with_timeout(async_function())
    """
    start = time.monotonic()
    total_timeout = timeout

    def _remaining_time():
        if total_timeout is None:
            return None
        elapsed = time.monotonic() - start
        remaining = total_timeout - elapsed
        if remaining <= 0:
            raise TimeoutError(
                f"Context manager exceeded the configured timeout of {total_timeout}s."
            )
        return remaining

    async def with_timeout(coro):
        try:
            remaining = _remaining_time()
            response = await asyncio.wait_for(coro, remaining)
            return response
        except (asyncio.TimeoutError, TimeoutError) as e:
            raise TimeoutError(
                f"The operation {coro} exceeded the configured timeout of {total_timeout}s."
            ) from e

    try:
        yield with_timeout

    finally:
        _remaining_time()


class _SyncCredentialsAdapter(Credentials):
    """Adapts synchronous credentials to the asynchronous credentials interface.

    :class:`AsyncAuthorizedSession` wraps :class:`google.auth.credentials.Credentials`
    (e.g. application default credentials) with this adapter so that they can be
    used with an asynchronous transport. Calls are delegated to the wrapped
    credentials using a synchronous transport, and blocking calls such as
    refreshing the access token run in a worker thread so that the event loop
    is not blocked.

    Args:
        credentials (google.auth.credentials.Credentials): The synchronous
            credentials to adapt.
    """

    def __init__(self, credentials: google.auth.credentials.Credentials):
        self._credentials = credentials
        # Synchronous credentials cannot use the asynchronous transport of the
        # session, so they are called with a synchronous transport instead.
        self._sync_request_instance = None
        # Synchronous credentials are not safe to refresh concurrently, which
        # concurrent requests would otherwise do from multiple worker threads.
        # Instead, at most one refresh is in flight and concurrent callers share it.
        self._pending_refresh: Optional["asyncio.Task[None]"] = None

    @property
    def _sync_request(self):
        if self._sync_request_instance is None:
            # Imported here because `requests` is an optional dependency of
            # google-auth. It is installed alongside `aiohttp` by the `aiohttp` extra.
            from google.auth.transport import requests as sync_requests

            self._sync_request_instance = sync_requests.Request()
        return self._sync_request_instance

    def close(self):
        if (
            self._sync_request_instance is not None
            and hasattr(self._sync_request_instance, "session")
            and self._sync_request_instance.session is not None
        ):
            self._sync_request_instance.session.close()

    @property
    def token(self):
        """Optional[str]: The bearer token that can be used in HTTP headers to make
        authenticated requests."""
        return self._credentials.token

    @property
    def expiry(self):
        """Optional[datetime]: When the token expires and is no longer valid.
        If this is None, the token is assumed to never expire."""
        return self._credentials.expiry

    @property
    @_helpers.copy_docstring(google.auth.credentials.Credentials)
    def valid(self):
        return self._credentials.valid

    @property
    @_helpers.copy_docstring(google.auth.credentials.Credentials)
    def expired(self):
        return self._credentials.expired

    async def _refresh_shared(self):
        """Refreshes the wrapped credentials, joining a refresh already in flight.

        The refresh is shielded from cancellation: a caller that is cancelled
        while waiting (e.g. because of a timeout) stops waiting, but the refresh
        completes so that the next caller joins it rather than starting a
        second, concurrent refresh.
        """
        if self._pending_refresh is None or self._pending_refresh.done():
            self._pending_refresh = asyncio.create_task(
                asyncio.to_thread(self._credentials.refresh, self._sync_request)
            )
        await asyncio.shield(self._pending_refresh)

    @_helpers.copy_docstring(Credentials)
    async def apply(self, headers, token=None):
        self._credentials.apply(headers, token=token)

    @_helpers.copy_docstring(Credentials)
    async def refresh(self, request):
        await self._refresh_shared()

    @_helpers.copy_docstring(Credentials)
    async def before_request(self, request, method, url, headers):
        if not self._credentials.valid:
            await self._refresh_shared()
        await asyncio.to_thread(
            self._credentials.before_request,
            self._sync_request,
            method,
            url,
            headers,
        )


class AsyncAuthorizedSession:
    """This is an asynchronous implementation of :class:`google.auth.requests.AuthorizedSession` class.
    We utilize an instance of a class that implements :class:`google.auth.aio.transport.Request` configured
    by the caller or otherwise default to `google.auth.aio.transport.aiohttp.Request` if the external aiohttp
    package is installed.

    A Requests Session class with credentials.

    This class is used to perform asynchronous requests to API endpoints that require
    authorization::

        import aiohttp
        from google.auth.aio.transport import sessions

        async with sessions.AsyncAuthorizedSession(credentials) as authed_session:
            response = await authed_session.request(
                'GET', 'https://www.googleapis.com/storage/v1/b')

    The underlying :meth:`request` implementation handles adding the
    credentials' headers to the request and refreshing credentials as needed.

    Args:
        credentials (Union[google.auth.aio.credentials.Credentials, google.auth.credentials.Credentials]):
            The credentials to add to the request. Synchronous credentials
            (e.g. application default credentials) are also supported.
        auth_request (Optional[google.auth.aio.transport.Request]):
            An instance of a class that implements
            :class:`~google.auth.aio.transport.Request` used to make requests
            and refresh credentials. If not passed,
            an instance of :class:`~google.auth.aio.transport.aiohttp.Request`
            is created.

    Raises:
        - google.auth.exceptions.TransportError: If `auth_request` is `None`
            and the external package `aiohttp` is not installed.
        - google.auth.exceptions.InvalidType: If the provided credentials are
            not of type `google.auth.aio.credentials.Credentials` or
            `google.auth.credentials.Credentials`.
    """

    def __init__(
        self,
        credentials: Union[Credentials, google.auth.credentials.Credentials],
        auth_request: Optional[transport.Request] = None,
    ):
        if isinstance(credentials, google.auth.credentials.Credentials):
            credentials = _SyncCredentialsAdapter(credentials)
        elif not isinstance(credentials, Credentials):
            raise exceptions.InvalidType(
                f"The configured credentials of type {type(credentials)} are invalid and must be of type `google.auth.aio.credentials.Credentials` or `google.auth.credentials.Credentials`"
            )
        self._credentials: Credentials = credentials
        _auth_request = auth_request
        if not _auth_request and AIOHTTP_INSTALLED:
            _auth_request = AiohttpRequest()
        self._is_mtls = False
        self._mtls_init_task = None
        self._cached_cert = None
        self._client_cert_callback = None
        self._old_auth_requests: list[transport.Request] = []
        if _auth_request is None:
            raise exceptions.TransportError(
                "`auth_request` must either be configured or the external package `aiohttp` must be installed to use the default value."
            )
        self._auth_request = _auth_request
        self._mtls_rotation_lock: Optional[asyncio.Lock] = None
        self._mtls_check_counter = 0
        self._mtls_reconfig_counter = 0
        self._refresh_lock: Optional[asyncio.Lock] = None
        self._refresh_counter = 0

    async def configure_mtls_channel(self, client_cert_callback=None):
        """Configure the client certificate and key for SSL connection.

        This method configures mTLS if client certificates are explicitly enabled
        (via GOOGLE_API_USE_CLIENT_CERTIFICATE=true) or auto-enabled (when the env
        variable is unset and workload certificates are discovered). In these cases,
        the underlying transport will be reconfigured to use mTLS.

        Note: This function does nothing if the `aiohttp` library is not
        installed.
        Important: Calling this method will close any ongoing API requests associated
        with the current session. To ensure a smooth transition, it is recommended
        to call this during session initialization.

        Args:
            client_cert_callback (Optional[Callable[[], (bytes, bytes)]]):
                The optional callback returns the client certificate and private
                key bytes both in PEM format.
                If the callback is None, application default SSL credentials
                will be used.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS channel
                creation failed for any reason.
        """
        if self._mtls_init_task is None:
            self._client_cert_callback = client_cert_callback

            async def _do_configure():
                # Run the blocking check in an executor
                use_client_cert = await mtls._run_in_executor(
                    google.auth.transport._mtls_helper.check_use_client_cert
                )
                if not use_client_cert:
                    return

                try:
                    (
                        is_mtls,
                        cert,
                        key,
                    ) = await mtls.get_client_cert_and_key(client_cert_callback)

                    if is_mtls:
                        # Re-create the auth request with the new SSL context
                        if AIOHTTP_INSTALLED and isinstance(
                            self._auth_request, AiohttpRequest
                        ):
                            ssl_context = await mtls._run_in_executor(
                                mtls.make_client_cert_ssl_context, cert, key
                            )
                            connector = aiohttp.TCPConnector(ssl=ssl_context)
                            new_session = aiohttp.ClientSession(connector=connector)

                            old_auth_request = self._auth_request
                            self._auth_request = AiohttpRequest(session=new_session)
                            self._old_auth_requests.append(old_auth_request)

                            while len(self._old_auth_requests) > 2:
                                oldest_auth_request = self._old_auth_requests[0]
                                try:
                                    if hasattr(oldest_auth_request, "close"):
                                        res = oldest_auth_request.close()
                                        if inspect.isawaitable(res):
                                            await res
                                except Exception:
                                    pass
                                self._old_auth_requests.pop(0)

                        else:
                            is_mtls = False
                            warnings.warn(
                                "Attempted to establish mTLS, but a custom async transport was provided. "
                                "google-auth cannot automatically configure custom transports for mTLS. "
                                "Falling back to standard TLS. If your custom transport is not manually "
                                "configured for mTLS, you may encounter 401 Unauthorized errors when "
                                "using Certificate-Bound Tokens.",
                                UserWarning,
                            )

                    self._is_mtls = is_mtls
                    if is_mtls:
                        self._cached_cert = cert
                    else:
                        self._cached_cert = None

                except Exception as caught_exc:
                    new_exc = exceptions.MutualTLSChannelError(caught_exc)
                    raise new_exc from caught_exc

            self._mtls_init_task = asyncio.create_task(_do_configure())

        try:
            return await self._mtls_init_task
        except BaseException:
            self._mtls_init_task = None
            raise

    async def request(
        self,
        method: str,
        url: str,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, str]] = None,
        max_allowed_time: float = transport._DEFAULT_TIMEOUT_SECONDS,
        timeout: Union[float, ClientTimeout] = transport._DEFAULT_TIMEOUT_SECONDS,
        total_attempts: Optional[int] = transport.DEFAULT_MAX_RETRY_ATTEMPTS,
        **kwargs,
    ) -> transport.Response:
        """
        Args:
                method (str): The http method used to make the request.
                url (str): The URI to be requested.
                data (Optional[bytes]): The payload or body in HTTP request.
                headers (Optional[Mapping[str, str]]): Request headers.
                timeout (float, aiohttp.ClientTimeout):
                The amount of time in seconds to wait for the server response
                with each individual request.
                max_allowed_time (float):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.
                total_attempts (int):
                The total number of retry attempts.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timeout error will be raised after such
                request completes.

        Returns:
                google.auth.aio.transport.Response: The HTTP response.

        Raises:
                google.auth.exceptions.TimeoutError: If the method does not complete within
                the configured `max_allowed_time` or the request exceeds the configured
                `timeout`.
                google.auth.exceptions.MutualTLSChannelError: If mutual TLS
                channel reconfiguration fails for any reason during certificate rotation.
        """
        _auth_retry_count = kwargs.pop("_auth_retry_count", 0)
        if self._mtls_init_task and not self._mtls_init_task.done():
            try:
                await asyncio.shield(self._mtls_init_task)
            except Exception:
                # Suppress all exceptions from the background mTLS initialization task,
                # allowing the request to fail naturally elsewhere.
                pass
        retries = _exponential_backoff.AsyncExponentialBackoff(
            total_attempts=total_attempts,
        )
        request_headers = dict(headers) if headers is not None else {}
        start_time = time.monotonic()
        refresh_counter_at_error = self._refresh_counter
        check_counter_at_error = self._mtls_check_counter
        reconfig_counter_at_error = self._mtls_reconfig_counter
        async with timeout_guard(max_allowed_time) as with_timeout:
            await with_timeout(
                # Note: before_request will attempt to refresh credentials if expired.
                self._credentials.before_request(
                    self._auth_request, method, url, request_headers
                )
            )
            actual_timeout: float = 0.0
            if ClientTimeout is not None and isinstance(timeout, ClientTimeout):
                actual_timeout = timeout.total if timeout.total is not None else 0.0
            elif isinstance(timeout, (int, float)):
                actual_timeout = float(timeout)
            # Workaround issue in python 3.9 related to code coverage by adding `# pragma: no branch`
            # See https://github.com/googleapis/gapic-generator-python/pull/1174#issuecomment-1025132372
            async for _ in retries:  # pragma: no branch
                response = await with_timeout(
                    self._auth_request(
                        url, method, data, request_headers, actual_timeout, **kwargs
                    )
                )

                if response.status_code not in transport.DEFAULT_RETRYABLE_STATUS_CODES:
                    break

        if response.status_code == http_client.UNAUTHORIZED:
            if _auth_retry_count < 2:
                try:
                    if max_allowed_time is not None:
                        elapsed = time.monotonic() - start_time
                        remaining_time = max(0.0, max_allowed_time - elapsed)
                        if remaining_time == 0.0:
                            raise google.auth.exceptions.TimeoutError(
                                "Timeout exceeded before credential refresh could begin"
                            )
                    else:
                        remaining_time = None
                    is_streaming = data is not None and (
                        isinstance(
                            data,
                            (collections.abc.Iterator, collections.abc.AsyncIterable),
                        )
                        or hasattr(data, "read")
                    )

                    async def _recover_auth_state():
                        is_mtls_endpoint = False
                        if self._is_mtls:
                            is_mtls_endpoint = (
                                google.auth.transport._mtls_helper.is_mtls_endpoint(url)
                            )
                            # Snapshot the stale certificate state BEFORE acquiring the lock.
                            # This represents the cert that caused the 401 rejection.
                            if is_mtls_endpoint:
                                if self._mtls_rotation_lock is None:
                                    self._mtls_rotation_lock = asyncio.Lock()
                                async with self._mtls_rotation_lock:
                                    # Check if another coroutine already reconfigured mTLS or
                                    # ran the validation check.
                                    if (
                                        self._mtls_check_counter
                                        > check_counter_at_error
                                    ):
                                        pass
                                    else:
                                        try:
                                            (
                                                call_cert_bytes,
                                                call_key_bytes,
                                                cached_fingerprint,
                                                current_cert_fingerprint,
                                            ) = await mtls.check_parameters_for_unauthorized_response(
                                                self._cached_cert,
                                                self._client_cert_callback,
                                            )
                                        except (
                                            exceptions.ClientCertError,
                                            exceptions.MutualTLSChannelError,
                                            OSError,
                                            ValueError,
                                            ImportError,
                                        ) as e:
                                            _LOGGER.warning(
                                                "Failed to check client certificate parameters: %s. Proceeding with original response.",
                                                e,
                                            )
                                        else:
                                            if (
                                                current_cert_fingerprint is not None
                                                and cached_fingerprint
                                                != current_cert_fingerprint
                                            ):
                                                saved_callback = (
                                                    self._client_cert_callback
                                                )
                                                try:
                                                    _LOGGER.info(
                                                        "Client certificate has changed, reconfiguring mTLS "
                                                        "channel."
                                                    )
                                                    if self._mtls_init_task is not None:
                                                        if not self._mtls_init_task.done():
                                                            try:
                                                                await (
                                                                    self._mtls_init_task
                                                                )
                                                            except Exception:
                                                                pass
                                                        self._mtls_init_task = None
                                                    await self.configure_mtls_channel(
                                                        lambda: (
                                                            call_cert_bytes,
                                                            call_key_bytes,
                                                        )
                                                    )
                                                    self._mtls_reconfig_counter += 1
                                                except Exception as e:
                                                    _LOGGER.error(
                                                        "Failed to reconfigure mTLS channel: %s",
                                                        e,
                                                    )
                                                    raise exceptions.MutualTLSChannelError(
                                                        "Failed to reconfigure mTLS channel"
                                                    ) from e
                                                finally:
                                                    self._client_cert_callback = (
                                                        saved_callback
                                                    )
                                            else:
                                                if current_cert_fingerprint is None:
                                                    _LOGGER.info(
                                                        "Skipping reconfiguration of mTLS channel because the client"
                                                        " certificate does not exist."
                                                    )
                                                else:
                                                    _LOGGER.info(
                                                        "Skipping reconfiguration of mTLS channel because the client"
                                                        " certificate has not changed."
                                                    )
                                        # Always increment so waiting tasks skip the check block
                                        self._mtls_check_counter += 1
                        if self._refresh_lock is None:
                            self._refresh_lock = asyncio.Lock()

                        async with self._refresh_lock:
                            # Check if another task already refreshed credentials while we were waiting
                            if self._refresh_counter > refresh_counter_at_error:
                                _LOGGER.debug(
                                    "Credentials were already refreshed by a concurrent task. Skipping duplicate refresh."
                                )
                            else:
                                try:
                                    await self._credentials.refresh(self._auth_request)
                                except NotImplementedError:
                                    _LOGGER.debug(
                                        "Credentials do not implement refresh()."
                                    )
                                    # A retry only helps when an mTLS reconfiguration
                                    # occurred for this mTLS endpoint. Short-circuit on
                                    # non-mTLS endpoints first so that a concurrent
                                    # rotation (which bumps the session-wide counter)
                                    # cannot trigger a spurious retry here.
                                    if (
                                        not is_mtls_endpoint
                                        or self._mtls_reconfig_counter
                                        <= reconfig_counter_at_error
                                    ):
                                        return response
                                except (
                                    exceptions.RefreshError,
                                    getattr(exceptions, "InvalidOperation", Exception),
                                ) as e:
                                    _LOGGER.debug(
                                        "Credential refresh failed, returning 401 response. Error: %s",
                                        e,
                                    )
                                    return response
                                else:
                                    self._refresh_counter += 1

                        if is_streaming:
                            return response
                        # Return None to explicitly signal successful recovery & trigger retry if needed
                        return None

                    async with timeout_guard(remaining_time) as auth_with_timeout:
                        early_return_response = await auth_with_timeout(
                            _recover_auth_state()
                        )
                except (Exception, asyncio.CancelledError):
                    if hasattr(response, "close"):
                        try:
                            res = response.close()
                            if inspect.isawaitable(res):
                                await res
                        except Exception:
                            pass
                    raise
                # If it returned a response (meaning streaming or error), bail out
                if early_return_response is not None:
                    return early_return_response
                if hasattr(response, "close"):
                    try:
                        res = response.close()
                        if inspect.isawaitable(res):
                            await res
                    except Exception:
                        pass
                if max_allowed_time is not None:
                    remaining_time = max(
                        0.0, max_allowed_time - (time.monotonic() - start_time)
                    )
                    if remaining_time == 0.0:
                        raise google.auth.exceptions.TimeoutError(
                            "Timeout exceeded before retrying the request"
                        )
                kwargs["_auth_retry_count"] = _auth_retry_count + 1
                return await self.request(
                    method,
                    url,
                    data=data,
                    headers=headers,
                    max_allowed_time=remaining_time,
                    timeout=timeout,
                    total_attempts=total_attempts,
                    **kwargs,
                )
        return response

    @functools.wraps(request)
    async def get(
        self,
        url: str,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, str]] = None,
        max_allowed_time: float = transport._DEFAULT_TIMEOUT_SECONDS,
        timeout: Union[float, ClientTimeout] = transport._DEFAULT_TIMEOUT_SECONDS,
        total_attempts: Optional[int] = transport.DEFAULT_MAX_RETRY_ATTEMPTS,
        **kwargs,
    ) -> transport.Response:
        """
        Args:
                url (str): The URI to be requested.
                data (Optional[bytes]): The payload or body in HTTP request.
                headers (Optional[Mapping[str, str]]): Request headers.
                max_allowed_time (float):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.
                timeout (float, aiohttp.ClientTimeout):
                The amount of time in seconds to wait for the server response
                with each individual request.
                total_attempts (int):
                The total number of retry attempts.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timeout error will be raised after such
                request completes.

        Returns:
                google.auth.aio.transport.Response: The HTTP response.

        Raises:
                google.auth.exceptions.TimeoutError: If the method does not complete within
                the configured `max_allowed_time` or the request exceeds the configured
                `timeout`.
        """
        return await self.request(
            "GET",
            url,
            data,
            headers,
            max_allowed_time,
            timeout,
            total_attempts,
            **kwargs,
        )

    @functools.wraps(request)
    async def post(
        self,
        url: str,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, str]] = None,
        max_allowed_time: float = transport._DEFAULT_TIMEOUT_SECONDS,
        timeout: Union[float, ClientTimeout] = transport._DEFAULT_TIMEOUT_SECONDS,
        total_attempts: Optional[int] = transport.DEFAULT_MAX_RETRY_ATTEMPTS,
        **kwargs,
    ) -> transport.Response:
        """
        Args:
                url (str): The URI to be requested.
                data (Optional[bytes]): The payload or body in HTTP request.
                headers (Optional[Mapping[str, str]]): Request headers.
                max_allowed_time (float):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.
                timeout (float, aiohttp.ClientTimeout):
                The amount of time in seconds to wait for the server response
                with each individual request.
                total_attempts (int):
                The total number of retry attempts.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timeout error will be raised after such
                request completes.

        Returns:
                google.auth.aio.transport.Response: The HTTP response.

        Raises:
                google.auth.exceptions.TimeoutError: If the method does not complete within
                the configured `max_allowed_time` or the request exceeds the configured
                `timeout`.
        """
        return await self.request(
            "POST",
            url,
            data,
            headers,
            max_allowed_time,
            timeout,
            total_attempts,
            **kwargs,
        )

    @functools.wraps(request)
    async def put(
        self,
        url: str,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, str]] = None,
        max_allowed_time: float = transport._DEFAULT_TIMEOUT_SECONDS,
        timeout: Union[float, ClientTimeout] = transport._DEFAULT_TIMEOUT_SECONDS,
        total_attempts: Optional[int] = transport.DEFAULT_MAX_RETRY_ATTEMPTS,
        **kwargs,
    ) -> transport.Response:
        """
        Args:
                url (str): The URI to be requested.
                data (Optional[bytes]): The payload or body in HTTP request.
                headers (Optional[Mapping[str, str]]): Request headers.
                max_allowed_time (float):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.
                timeout (float, aiohttp.ClientTimeout):
                The amount of time in seconds to wait for the server response
                with each individual request.
                total_attempts (int):
                The total number of retry attempts.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timeout error will be raised after such
                request completes.

        Returns:
                google.auth.aio.transport.Response: The HTTP response.

        Raises:
                google.auth.exceptions.TimeoutError: If the method does not complete within
                the configured `max_allowed_time` or the request exceeds the configured
                `timeout`.
        """
        return await self.request(
            "PUT",
            url,
            data,
            headers,
            max_allowed_time,
            timeout,
            total_attempts,
            **kwargs,
        )

    @functools.wraps(request)
    async def patch(
        self,
        url: str,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, str]] = None,
        max_allowed_time: float = transport._DEFAULT_TIMEOUT_SECONDS,
        timeout: Union[float, ClientTimeout] = transport._DEFAULT_TIMEOUT_SECONDS,
        total_attempts: Optional[int] = transport.DEFAULT_MAX_RETRY_ATTEMPTS,
        **kwargs,
    ) -> transport.Response:
        """
        Args:
                url (str): The URI to be requested.
                data (Optional[bytes]): The payload or body in HTTP request.
                headers (Optional[Mapping[str, str]]): Request headers.
                max_allowed_time (float):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.
                timeout (float, aiohttp.ClientTimeout):
                The amount of time in seconds to wait for the server response
                with each individual request.
                total_attempts (int):
                The total number of retry attempts.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timeout error will be raised after such
                request completes.

        Returns:
                google.auth.aio.transport.Response: The HTTP response.

        Raises:
                google.auth.exceptions.TimeoutError: If the method does not complete within
                the configured `max_allowed_time` or the request exceeds the configured
                `timeout`.
        """
        return await self.request(
            "PATCH",
            url,
            data,
            headers,
            max_allowed_time,
            timeout,
            total_attempts,
            **kwargs,
        )

    @functools.wraps(request)
    async def delete(
        self,
        url: str,
        data: Optional[bytes] = None,
        headers: Optional[Mapping[str, str]] = None,
        max_allowed_time: float = transport._DEFAULT_TIMEOUT_SECONDS,
        timeout: Union[float, ClientTimeout] = transport._DEFAULT_TIMEOUT_SECONDS,
        total_attempts: Optional[int] = transport.DEFAULT_MAX_RETRY_ATTEMPTS,
        **kwargs,
    ) -> transport.Response:
        """
        Args:
                url (str): The URI to be requested.
                data (Optional[bytes]): The payload or body in HTTP request.
                headers (Optional[Mapping[str, str]]): Request headers.
                max_allowed_time (float):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.
                timeout (float, aiohttp.ClientTimeout):
                The amount of time in seconds to wait for the server response
                with each individual request.
                total_attempts (int):
                The total number of retry attempts.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timeout error will be raised after such
                request completes.

        Returns:
                google.auth.aio.transport.Response: The HTTP response.

        Raises:
                google.auth.exceptions.TimeoutError: If the method does not complete within
                the configured `max_allowed_time` or the request exceeds the configured
                `timeout`.
        """
        return await self.request(
            "DELETE",
            url,
            data,
            headers,
            max_allowed_time,
            timeout,
            total_attempts,
            **kwargs,
        )

    @property
    def is_mtls(self):
        """Indicates if mutual TLS is enabled."""
        return self._is_mtls

    async def close(self) -> None:
        """
        Close the underlying auth request session.
        """
        if self._mtls_init_task and not self._mtls_init_task.done():
            self._mtls_init_task.cancel()
            try:
                await self._mtls_init_task
            except asyncio.CancelledError:
                pass
        try:
            if hasattr(self._auth_request, "close"):
                res = self._auth_request.close()
                if inspect.isawaitable(res):
                    await res
        finally:
            if hasattr(self._credentials, "close"):
                self._credentials.close()
            for old_request in self._old_auth_requests:
                try:
                    if hasattr(old_request, "close"):
                        res = old_request.close()
                        if inspect.isawaitable(res):
                            await res
                except Exception:
                    pass
            self._old_auth_requests.clear()
