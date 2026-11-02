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

from google.cloud.network_services_v1.types import (
    agent_gateway,
    endpoint_policy,
    extensibility,
    gateway,
    grpc_route,
    http_route,
    mesh,
    route_view,
    service_binding,
    service_lb_policy,
    tcp_route,
    tls_route,
)


class ListEndpointPoliciesPager:
    """A pager for iterating through ``list_endpoint_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListEndpointPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``endpoint_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEndpointPolicies`` requests and continue to iterate
    through the ``endpoint_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListEndpointPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., endpoint_policy.ListEndpointPoliciesResponse],
        request: endpoint_policy.ListEndpointPoliciesRequest,
        response: endpoint_policy.ListEndpointPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListEndpointPoliciesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListEndpointPoliciesResponse):
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
        self._request = endpoint_policy.ListEndpointPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[endpoint_policy.ListEndpointPoliciesResponse]:
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

    def __iter__(self) -> Iterator[endpoint_policy.EndpointPolicy]:
        for page in self.pages:
            yield from page.endpoint_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEndpointPoliciesAsyncPager:
    """A pager for iterating through ``list_endpoint_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListEndpointPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``endpoint_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEndpointPolicies`` requests and continue to iterate
    through the ``endpoint_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListEndpointPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[endpoint_policy.ListEndpointPoliciesResponse]],
        request: endpoint_policy.ListEndpointPoliciesRequest,
        response: endpoint_policy.ListEndpointPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListEndpointPoliciesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListEndpointPoliciesResponse):
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
        self._request = endpoint_policy.ListEndpointPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[endpoint_policy.ListEndpointPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[endpoint_policy.EndpointPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.endpoint_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWasmPluginVersionsPager:
    """A pager for iterating through ``list_wasm_plugin_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListWasmPluginVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``wasm_plugin_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWasmPluginVersions`` requests and continue to iterate
    through the ``wasm_plugin_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListWasmPluginVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., extensibility.ListWasmPluginVersionsResponse],
        request: extensibility.ListWasmPluginVersionsRequest,
        response: extensibility.ListWasmPluginVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListWasmPluginVersionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListWasmPluginVersionsResponse):
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
        self._request = extensibility.ListWasmPluginVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[extensibility.ListWasmPluginVersionsResponse]:
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

    def __iter__(self) -> Iterator[extensibility.WasmPluginVersion]:
        for page in self.pages:
            yield from page.wasm_plugin_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWasmPluginVersionsAsyncPager:
    """A pager for iterating through ``list_wasm_plugin_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListWasmPluginVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``wasm_plugin_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWasmPluginVersions`` requests and continue to iterate
    through the ``wasm_plugin_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListWasmPluginVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[extensibility.ListWasmPluginVersionsResponse]],
        request: extensibility.ListWasmPluginVersionsRequest,
        response: extensibility.ListWasmPluginVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListWasmPluginVersionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListWasmPluginVersionsResponse):
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
        self._request = extensibility.ListWasmPluginVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[extensibility.ListWasmPluginVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[extensibility.WasmPluginVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.wasm_plugin_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWasmPluginsPager:
    """A pager for iterating through ``list_wasm_plugins`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListWasmPluginsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``wasm_plugins`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWasmPlugins`` requests and continue to iterate
    through the ``wasm_plugins`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListWasmPluginsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., extensibility.ListWasmPluginsResponse],
        request: extensibility.ListWasmPluginsRequest,
        response: extensibility.ListWasmPluginsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListWasmPluginsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListWasmPluginsResponse):
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
        self._request = extensibility.ListWasmPluginsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[extensibility.ListWasmPluginsResponse]:
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

    def __iter__(self) -> Iterator[extensibility.WasmPlugin]:
        for page in self.pages:
            yield from page.wasm_plugins

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWasmPluginsAsyncPager:
    """A pager for iterating through ``list_wasm_plugins`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListWasmPluginsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``wasm_plugins`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWasmPlugins`` requests and continue to iterate
    through the ``wasm_plugins`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListWasmPluginsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[extensibility.ListWasmPluginsResponse]],
        request: extensibility.ListWasmPluginsRequest,
        response: extensibility.ListWasmPluginsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListWasmPluginsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListWasmPluginsResponse):
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
        self._request = extensibility.ListWasmPluginsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[extensibility.ListWasmPluginsResponse]:
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

    def __aiter__(self) -> AsyncIterator[extensibility.WasmPlugin]:
        async def async_generator():
            async for page in self.pages:
                for response in page.wasm_plugins:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewaysPager:
    """A pager for iterating through ``list_gateways`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListGatewaysResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``gateways`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGateways`` requests and continue to iterate
    through the ``gateways`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListGatewaysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gateway.ListGatewaysResponse],
        request: gateway.ListGatewaysRequest,
        response: gateway.ListGatewaysResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListGatewaysRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListGatewaysResponse):
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
        self._request = gateway.ListGatewaysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gateway.ListGatewaysResponse]:
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

    def __iter__(self) -> Iterator[gateway.Gateway]:
        for page in self.pages:
            yield from page.gateways

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewaysAsyncPager:
    """A pager for iterating through ``list_gateways`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListGatewaysResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``gateways`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGateways`` requests and continue to iterate
    through the ``gateways`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListGatewaysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gateway.ListGatewaysResponse]],
        request: gateway.ListGatewaysRequest,
        response: gateway.ListGatewaysResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListGatewaysRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListGatewaysResponse):
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
        self._request = gateway.ListGatewaysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gateway.ListGatewaysResponse]:
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

    def __aiter__(self) -> AsyncIterator[gateway.Gateway]:
        async def async_generator():
            async for page in self.pages:
                for response in page.gateways:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGrpcRoutesPager:
    """A pager for iterating through ``list_grpc_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListGrpcRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``grpc_routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGrpcRoutes`` requests and continue to iterate
    through the ``grpc_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListGrpcRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., grpc_route.ListGrpcRoutesResponse],
        request: grpc_route.ListGrpcRoutesRequest,
        response: grpc_route.ListGrpcRoutesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListGrpcRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListGrpcRoutesResponse):
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
        self._request = grpc_route.ListGrpcRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[grpc_route.ListGrpcRoutesResponse]:
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

    def __iter__(self) -> Iterator[grpc_route.GrpcRoute]:
        for page in self.pages:
            yield from page.grpc_routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGrpcRoutesAsyncPager:
    """A pager for iterating through ``list_grpc_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListGrpcRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``grpc_routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGrpcRoutes`` requests and continue to iterate
    through the ``grpc_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListGrpcRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[grpc_route.ListGrpcRoutesResponse]],
        request: grpc_route.ListGrpcRoutesRequest,
        response: grpc_route.ListGrpcRoutesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListGrpcRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListGrpcRoutesResponse):
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
        self._request = grpc_route.ListGrpcRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[grpc_route.ListGrpcRoutesResponse]:
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

    def __aiter__(self) -> AsyncIterator[grpc_route.GrpcRoute]:
        async def async_generator():
            async for page in self.pages:
                for response in page.grpc_routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHttpRoutesPager:
    """A pager for iterating through ``list_http_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListHttpRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``http_routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHttpRoutes`` requests and continue to iterate
    through the ``http_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListHttpRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., http_route.ListHttpRoutesResponse],
        request: http_route.ListHttpRoutesRequest,
        response: http_route.ListHttpRoutesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListHttpRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListHttpRoutesResponse):
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
        self._request = http_route.ListHttpRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[http_route.ListHttpRoutesResponse]:
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

    def __iter__(self) -> Iterator[http_route.HttpRoute]:
        for page in self.pages:
            yield from page.http_routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHttpRoutesAsyncPager:
    """A pager for iterating through ``list_http_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListHttpRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``http_routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHttpRoutes`` requests and continue to iterate
    through the ``http_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListHttpRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[http_route.ListHttpRoutesResponse]],
        request: http_route.ListHttpRoutesRequest,
        response: http_route.ListHttpRoutesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListHttpRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListHttpRoutesResponse):
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
        self._request = http_route.ListHttpRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[http_route.ListHttpRoutesResponse]:
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

    def __aiter__(self) -> AsyncIterator[http_route.HttpRoute]:
        async def async_generator():
            async for page in self.pages:
                for response in page.http_routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTcpRoutesPager:
    """A pager for iterating through ``list_tcp_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListTcpRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tcp_routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTcpRoutes`` requests and continue to iterate
    through the ``tcp_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListTcpRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., tcp_route.ListTcpRoutesResponse],
        request: tcp_route.ListTcpRoutesRequest,
        response: tcp_route.ListTcpRoutesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListTcpRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListTcpRoutesResponse):
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
        self._request = tcp_route.ListTcpRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[tcp_route.ListTcpRoutesResponse]:
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

    def __iter__(self) -> Iterator[tcp_route.TcpRoute]:
        for page in self.pages:
            yield from page.tcp_routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTcpRoutesAsyncPager:
    """A pager for iterating through ``list_tcp_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListTcpRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tcp_routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTcpRoutes`` requests and continue to iterate
    through the ``tcp_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListTcpRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[tcp_route.ListTcpRoutesResponse]],
        request: tcp_route.ListTcpRoutesRequest,
        response: tcp_route.ListTcpRoutesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListTcpRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListTcpRoutesResponse):
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
        self._request = tcp_route.ListTcpRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[tcp_route.ListTcpRoutesResponse]:
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

    def __aiter__(self) -> AsyncIterator[tcp_route.TcpRoute]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tcp_routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTlsRoutesPager:
    """A pager for iterating through ``list_tls_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListTlsRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tls_routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTlsRoutes`` requests and continue to iterate
    through the ``tls_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListTlsRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., tls_route.ListTlsRoutesResponse],
        request: tls_route.ListTlsRoutesRequest,
        response: tls_route.ListTlsRoutesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListTlsRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListTlsRoutesResponse):
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
        self._request = tls_route.ListTlsRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[tls_route.ListTlsRoutesResponse]:
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

    def __iter__(self) -> Iterator[tls_route.TlsRoute]:
        for page in self.pages:
            yield from page.tls_routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTlsRoutesAsyncPager:
    """A pager for iterating through ``list_tls_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListTlsRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tls_routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTlsRoutes`` requests and continue to iterate
    through the ``tls_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListTlsRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[tls_route.ListTlsRoutesResponse]],
        request: tls_route.ListTlsRoutesRequest,
        response: tls_route.ListTlsRoutesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListTlsRoutesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListTlsRoutesResponse):
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
        self._request = tls_route.ListTlsRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[tls_route.ListTlsRoutesResponse]:
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

    def __aiter__(self) -> AsyncIterator[tls_route.TlsRoute]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tls_routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceBindingsPager:
    """A pager for iterating through ``list_service_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListServiceBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceBindings`` requests and continue to iterate
    through the ``service_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListServiceBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service_binding.ListServiceBindingsResponse],
        request: service_binding.ListServiceBindingsRequest,
        response: service_binding.ListServiceBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListServiceBindingsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListServiceBindingsResponse):
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
        self._request = service_binding.ListServiceBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service_binding.ListServiceBindingsResponse]:
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

    def __iter__(self) -> Iterator[service_binding.ServiceBinding]:
        for page in self.pages:
            yield from page.service_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceBindingsAsyncPager:
    """A pager for iterating through ``list_service_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListServiceBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceBindings`` requests and continue to iterate
    through the ``service_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListServiceBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service_binding.ListServiceBindingsResponse]],
        request: service_binding.ListServiceBindingsRequest,
        response: service_binding.ListServiceBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListServiceBindingsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListServiceBindingsResponse):
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
        self._request = service_binding.ListServiceBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service_binding.ListServiceBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[service_binding.ServiceBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMeshesPager:
    """A pager for iterating through ``list_meshes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListMeshesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``meshes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMeshes`` requests and continue to iterate
    through the ``meshes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListMeshesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., mesh.ListMeshesResponse],
        request: mesh.ListMeshesRequest,
        response: mesh.ListMeshesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListMeshesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListMeshesResponse):
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
        self._request = mesh.ListMeshesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[mesh.ListMeshesResponse]:
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

    def __iter__(self) -> Iterator[mesh.Mesh]:
        for page in self.pages:
            yield from page.meshes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMeshesAsyncPager:
    """A pager for iterating through ``list_meshes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListMeshesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``meshes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMeshes`` requests and continue to iterate
    through the ``meshes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListMeshesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[mesh.ListMeshesResponse]],
        request: mesh.ListMeshesRequest,
        response: mesh.ListMeshesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListMeshesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListMeshesResponse):
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
        self._request = mesh.ListMeshesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[mesh.ListMeshesResponse]:
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

    def __aiter__(self) -> AsyncIterator[mesh.Mesh]:
        async def async_generator():
            async for page in self.pages:
                for response in page.meshes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceLbPoliciesPager:
    """A pager for iterating through ``list_service_lb_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListServiceLbPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_lb_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceLbPolicies`` requests and continue to iterate
    through the ``service_lb_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListServiceLbPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service_lb_policy.ListServiceLbPoliciesResponse],
        request: service_lb_policy.ListServiceLbPoliciesRequest,
        response: service_lb_policy.ListServiceLbPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListServiceLbPoliciesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListServiceLbPoliciesResponse):
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
        self._request = service_lb_policy.ListServiceLbPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service_lb_policy.ListServiceLbPoliciesResponse]:
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

    def __iter__(self) -> Iterator[service_lb_policy.ServiceLbPolicy]:
        for page in self.pages:
            yield from page.service_lb_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceLbPoliciesAsyncPager:
    """A pager for iterating through ``list_service_lb_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListServiceLbPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_lb_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceLbPolicies`` requests and continue to iterate
    through the ``service_lb_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListServiceLbPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[service_lb_policy.ListServiceLbPoliciesResponse]
        ],
        request: service_lb_policy.ListServiceLbPoliciesRequest,
        response: service_lb_policy.ListServiceLbPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListServiceLbPoliciesRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListServiceLbPoliciesResponse):
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
        self._request = service_lb_policy.ListServiceLbPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[service_lb_policy.ListServiceLbPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[service_lb_policy.ServiceLbPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_lb_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewayRouteViewsPager:
    """A pager for iterating through ``list_gateway_route_views`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListGatewayRouteViewsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``gateway_route_views`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGatewayRouteViews`` requests and continue to iterate
    through the ``gateway_route_views`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListGatewayRouteViewsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., route_view.ListGatewayRouteViewsResponse],
        request: route_view.ListGatewayRouteViewsRequest,
        response: route_view.ListGatewayRouteViewsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListGatewayRouteViewsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListGatewayRouteViewsResponse):
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
        self._request = route_view.ListGatewayRouteViewsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[route_view.ListGatewayRouteViewsResponse]:
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

    def __iter__(self) -> Iterator[route_view.GatewayRouteView]:
        for page in self.pages:
            yield from page.gateway_route_views

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewayRouteViewsAsyncPager:
    """A pager for iterating through ``list_gateway_route_views`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListGatewayRouteViewsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``gateway_route_views`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGatewayRouteViews`` requests and continue to iterate
    through the ``gateway_route_views`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListGatewayRouteViewsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[route_view.ListGatewayRouteViewsResponse]],
        request: route_view.ListGatewayRouteViewsRequest,
        response: route_view.ListGatewayRouteViewsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListGatewayRouteViewsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListGatewayRouteViewsResponse):
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
        self._request = route_view.ListGatewayRouteViewsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[route_view.ListGatewayRouteViewsResponse]:
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

    def __aiter__(self) -> AsyncIterator[route_view.GatewayRouteView]:
        async def async_generator():
            async for page in self.pages:
                for response in page.gateway_route_views:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMeshRouteViewsPager:
    """A pager for iterating through ``list_mesh_route_views`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListMeshRouteViewsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``mesh_route_views`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMeshRouteViews`` requests and continue to iterate
    through the ``mesh_route_views`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListMeshRouteViewsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., route_view.ListMeshRouteViewsResponse],
        request: route_view.ListMeshRouteViewsRequest,
        response: route_view.ListMeshRouteViewsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListMeshRouteViewsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListMeshRouteViewsResponse):
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
        self._request = route_view.ListMeshRouteViewsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[route_view.ListMeshRouteViewsResponse]:
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

    def __iter__(self) -> Iterator[route_view.MeshRouteView]:
        for page in self.pages:
            yield from page.mesh_route_views

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMeshRouteViewsAsyncPager:
    """A pager for iterating through ``list_mesh_route_views`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListMeshRouteViewsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``mesh_route_views`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMeshRouteViews`` requests and continue to iterate
    through the ``mesh_route_views`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListMeshRouteViewsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[route_view.ListMeshRouteViewsResponse]],
        request: route_view.ListMeshRouteViewsRequest,
        response: route_view.ListMeshRouteViewsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListMeshRouteViewsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListMeshRouteViewsResponse):
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
        self._request = route_view.ListMeshRouteViewsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[route_view.ListMeshRouteViewsResponse]:
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

    def __aiter__(self) -> AsyncIterator[route_view.MeshRouteView]:
        async def async_generator():
            async for page in self.pages:
                for response in page.mesh_route_views:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAgentGatewaysPager:
    """A pager for iterating through ``list_agent_gateways`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListAgentGatewaysResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``agent_gateways`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAgentGateways`` requests and continue to iterate
    through the ``agent_gateways`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListAgentGatewaysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_gateway.ListAgentGatewaysResponse],
        request: agent_gateway.ListAgentGatewaysRequest,
        response: agent_gateway.ListAgentGatewaysResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListAgentGatewaysRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListAgentGatewaysResponse):
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
        self._request = agent_gateway.ListAgentGatewaysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_gateway.ListAgentGatewaysResponse]:
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

    def __iter__(self) -> Iterator[agent_gateway.AgentGateway]:
        for page in self.pages:
            yield from page.agent_gateways

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAgentGatewaysAsyncPager:
    """A pager for iterating through ``list_agent_gateways`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListAgentGatewaysResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``agent_gateways`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAgentGateways`` requests and continue to iterate
    through the ``agent_gateways`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListAgentGatewaysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_gateway.ListAgentGatewaysResponse]],
        request: agent_gateway.ListAgentGatewaysRequest,
        response: agent_gateway.ListAgentGatewaysResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListAgentGatewaysRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListAgentGatewaysResponse):
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
        self._request = agent_gateway.ListAgentGatewaysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_gateway.ListAgentGatewaysResponse]:
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

    def __aiter__(self) -> AsyncIterator[agent_gateway.AgentGateway]:
        async def async_generator():
            async for page in self.pages:
                for response in page.agent_gateways:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
