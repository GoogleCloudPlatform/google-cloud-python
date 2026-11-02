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
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import retry_async as retries_async

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
    OptionalAsyncRetry = Union[
        retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None
    ]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, object, None]  # type: ignore

from google.cloud.network_security_v1.types import (
    authorization_policy,
    authz_policy,
    backend_authentication_config,
    client_tls_policy,
    gateway_security_policy,
    gateway_security_policy_rule,
    server_tls_policy,
    tls_inspection_policy,
    url_list,
)


class ListAuthorizationPoliciesPager:
    """A pager for iterating through ``list_authorization_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListAuthorizationPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``authorization_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuthorizationPolicies`` requests and continue to iterate
    through the ``authorization_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListAuthorizationPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., authorization_policy.ListAuthorizationPoliciesResponse],
        request: authorization_policy.ListAuthorizationPoliciesRequest,
        response: authorization_policy.ListAuthorizationPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListAuthorizationPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListAuthorizationPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = authorization_policy.ListAuthorizationPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[authorization_policy.ListAuthorizationPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[authorization_policy.AuthorizationPolicy]:
        for page in self.pages:
            yield from page.authorization_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthorizationPoliciesAsyncPager:
    """A pager for iterating through ``list_authorization_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListAuthorizationPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``authorization_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuthorizationPolicies`` requests and continue to iterate
    through the ``authorization_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListAuthorizationPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[authorization_policy.ListAuthorizationPoliciesResponse]
        ],
        request: authorization_policy.ListAuthorizationPoliciesRequest,
        response: authorization_policy.ListAuthorizationPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListAuthorizationPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListAuthorizationPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = authorization_policy.ListAuthorizationPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[authorization_policy.ListAuthorizationPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[authorization_policy.AuthorizationPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.authorization_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackendAuthenticationConfigsPager:
    """A pager for iterating through ``list_backend_authentication_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backend_authentication_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackendAuthenticationConfigs`` requests and continue to iterate
    through the ``backend_authentication_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., backend_authentication_config.ListBackendAuthenticationConfigsResponse
        ],
        request: backend_authentication_config.ListBackendAuthenticationConfigsRequest,
        response: backend_authentication_config.ListBackendAuthenticationConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = (
            backend_authentication_config.ListBackendAuthenticationConfigsRequest(
                request
            )
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[
        backend_authentication_config.ListBackendAuthenticationConfigsResponse
    ]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(
        self,
    ) -> Iterator[backend_authentication_config.BackendAuthenticationConfig]:
        for page in self.pages:
            yield from page.backend_authentication_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackendAuthenticationConfigsAsyncPager:
    """A pager for iterating through ``list_backend_authentication_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backend_authentication_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackendAuthenticationConfigs`` requests and continue to iterate
    through the ``backend_authentication_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                backend_authentication_config.ListBackendAuthenticationConfigsResponse
            ],
        ],
        request: backend_authentication_config.ListBackendAuthenticationConfigsRequest,
        response: backend_authentication_config.ListBackendAuthenticationConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListBackendAuthenticationConfigsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = (
            backend_authentication_config.ListBackendAuthenticationConfigsRequest(
                request
            )
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        backend_authentication_config.ListBackendAuthenticationConfigsResponse
    ]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(
        self,
    ) -> AsyncIterator[backend_authentication_config.BackendAuthenticationConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backend_authentication_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServerTlsPoliciesPager:
    """A pager for iterating through ``list_server_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListServerTlsPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``server_tls_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServerTlsPolicies`` requests and continue to iterate
    through the ``server_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListServerTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., server_tls_policy.ListServerTlsPoliciesResponse],
        request: server_tls_policy.ListServerTlsPoliciesRequest,
        response: server_tls_policy.ListServerTlsPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListServerTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListServerTlsPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = server_tls_policy.ListServerTlsPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[server_tls_policy.ListServerTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[server_tls_policy.ServerTlsPolicy]:
        for page in self.pages:
            yield from page.server_tls_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServerTlsPoliciesAsyncPager:
    """A pager for iterating through ``list_server_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListServerTlsPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``server_tls_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServerTlsPolicies`` requests and continue to iterate
    through the ``server_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListServerTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[server_tls_policy.ListServerTlsPoliciesResponse]
        ],
        request: server_tls_policy.ListServerTlsPoliciesRequest,
        response: server_tls_policy.ListServerTlsPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListServerTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListServerTlsPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = server_tls_policy.ListServerTlsPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[server_tls_policy.ListServerTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[server_tls_policy.ServerTlsPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.server_tls_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListClientTlsPoliciesPager:
    """A pager for iterating through ``list_client_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListClientTlsPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``client_tls_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListClientTlsPolicies`` requests and continue to iterate
    through the ``client_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListClientTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., client_tls_policy.ListClientTlsPoliciesResponse],
        request: client_tls_policy.ListClientTlsPoliciesRequest,
        response: client_tls_policy.ListClientTlsPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListClientTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListClientTlsPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = client_tls_policy.ListClientTlsPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[client_tls_policy.ListClientTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[client_tls_policy.ClientTlsPolicy]:
        for page in self.pages:
            yield from page.client_tls_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListClientTlsPoliciesAsyncPager:
    """A pager for iterating through ``list_client_tls_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListClientTlsPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``client_tls_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListClientTlsPolicies`` requests and continue to iterate
    through the ``client_tls_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListClientTlsPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[client_tls_policy.ListClientTlsPoliciesResponse]
        ],
        request: client_tls_policy.ListClientTlsPoliciesRequest,
        response: client_tls_policy.ListClientTlsPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListClientTlsPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListClientTlsPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = client_tls_policy.ListClientTlsPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[client_tls_policy.ListClientTlsPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[client_tls_policy.ClientTlsPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.client_tls_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewaySecurityPoliciesPager:
    """A pager for iterating through ``list_gateway_security_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``gateway_security_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGatewaySecurityPolicies`` requests and continue to iterate
    through the ``gateway_security_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., gateway_security_policy.ListGatewaySecurityPoliciesResponse
        ],
        request: gateway_security_policy.ListGatewaySecurityPoliciesRequest,
        response: gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = gateway_security_policy.ListGatewaySecurityPoliciesRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[gateway_security_policy.ListGatewaySecurityPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[gateway_security_policy.GatewaySecurityPolicy]:
        for page in self.pages:
            yield from page.gateway_security_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewaySecurityPoliciesAsyncPager:
    """A pager for iterating through ``list_gateway_security_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``gateway_security_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGatewaySecurityPolicies`` requests and continue to iterate
    through the ``gateway_security_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[gateway_security_policy.ListGatewaySecurityPoliciesResponse]
        ],
        request: gateway_security_policy.ListGatewaySecurityPoliciesRequest,
        response: gateway_security_policy.ListGatewaySecurityPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListGatewaySecurityPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = gateway_security_policy.ListGatewaySecurityPoliciesRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[gateway_security_policy.ListGatewaySecurityPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[gateway_security_policy.GatewaySecurityPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.gateway_security_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewaySecurityPolicyRulesPager:
    """A pager for iterating through ``list_gateway_security_policy_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``gateway_security_policy_rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGatewaySecurityPolicyRules`` requests and continue to iterate
    through the ``gateway_security_policy_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse
        ],
        request: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest,
        response: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = (
            gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest(request)
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(
        self,
    ) -> Iterator[gateway_security_policy_rule.GatewaySecurityPolicyRule]:
        for page in self.pages:
            yield from page.gateway_security_policy_rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewaySecurityPolicyRulesAsyncPager:
    """A pager for iterating through ``list_gateway_security_policy_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``gateway_security_policy_rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGatewaySecurityPolicyRules`` requests and continue to iterate
    through the ``gateway_security_policy_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse
            ],
        ],
        request: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest,
        response: gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListGatewaySecurityPolicyRulesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = (
            gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest(request)
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse
    ]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(
        self,
    ) -> AsyncIterator[gateway_security_policy_rule.GatewaySecurityPolicyRule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.gateway_security_policy_rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUrlListsPager:
    """A pager for iterating through ``list_url_lists`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListUrlListsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``url_lists`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUrlLists`` requests and continue to iterate
    through the ``url_lists`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListUrlListsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., url_list.ListUrlListsResponse],
        request: url_list.ListUrlListsRequest,
        response: url_list.ListUrlListsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListUrlListsRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListUrlListsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = url_list.ListUrlListsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[url_list.ListUrlListsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[url_list.UrlList]:
        for page in self.pages:
            yield from page.url_lists

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUrlListsAsyncPager:
    """A pager for iterating through ``list_url_lists`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListUrlListsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``url_lists`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUrlLists`` requests and continue to iterate
    through the ``url_lists`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListUrlListsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[url_list.ListUrlListsResponse]],
        request: url_list.ListUrlListsRequest,
        response: url_list.ListUrlListsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListUrlListsRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListUrlListsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = url_list.ListUrlListsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[url_list.ListUrlListsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[url_list.UrlList]:
        async def async_generator():
            async for page in self.pages:
                for response in page.url_lists:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTlsInspectionPoliciesPager:
    """A pager for iterating through ``list_tls_inspection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListTlsInspectionPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tls_inspection_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTlsInspectionPolicies`` requests and continue to iterate
    through the ``tls_inspection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListTlsInspectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., tls_inspection_policy.ListTlsInspectionPoliciesResponse],
        request: tls_inspection_policy.ListTlsInspectionPoliciesRequest,
        response: tls_inspection_policy.ListTlsInspectionPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListTlsInspectionPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListTlsInspectionPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = tls_inspection_policy.ListTlsInspectionPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[tls_inspection_policy.ListTlsInspectionPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[tls_inspection_policy.TlsInspectionPolicy]:
        for page in self.pages:
            yield from page.tls_inspection_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTlsInspectionPoliciesAsyncPager:
    """A pager for iterating through ``list_tls_inspection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListTlsInspectionPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tls_inspection_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTlsInspectionPolicies`` requests and continue to iterate
    through the ``tls_inspection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListTlsInspectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[tls_inspection_policy.ListTlsInspectionPoliciesResponse]
        ],
        request: tls_inspection_policy.ListTlsInspectionPoliciesRequest,
        response: tls_inspection_policy.ListTlsInspectionPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListTlsInspectionPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListTlsInspectionPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = tls_inspection_policy.ListTlsInspectionPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[tls_inspection_policy.ListTlsInspectionPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[tls_inspection_policy.TlsInspectionPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tls_inspection_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthzPoliciesPager:
    """A pager for iterating through ``list_authz_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListAuthzPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``authz_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuthzPolicies`` requests and continue to iterate
    through the ``authz_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListAuthzPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., authz_policy.ListAuthzPoliciesResponse],
        request: authz_policy.ListAuthzPoliciesRequest,
        response: authz_policy.ListAuthzPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListAuthzPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListAuthzPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = authz_policy.ListAuthzPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[authz_policy.ListAuthzPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[authz_policy.AuthzPolicy]:
        for page in self.pages:
            yield from page.authz_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthzPoliciesAsyncPager:
    """A pager for iterating through ``list_authz_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1.types.ListAuthzPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``authz_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuthzPolicies`` requests and continue to iterate
    through the ``authz_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1.types.ListAuthzPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[authz_policy.ListAuthzPoliciesResponse]],
        request: authz_policy.ListAuthzPoliciesRequest,
        response: authz_policy.ListAuthzPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1.types.ListAuthzPoliciesRequest):
                The initial request object.
            response (google.cloud.network_security_v1.types.ListAuthzPoliciesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = authz_policy.ListAuthzPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[authz_policy.ListAuthzPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[authz_policy.AuthzPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.authz_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
