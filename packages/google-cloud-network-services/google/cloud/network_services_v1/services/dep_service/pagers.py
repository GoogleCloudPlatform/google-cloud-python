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

from google.cloud.network_services_v1.types import dep


class ListLbTrafficExtensionsPager:
    """A pager for iterating through ``list_lb_traffic_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListLbTrafficExtensionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``lb_traffic_extensions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLbTrafficExtensions`` requests and continue to iterate
    through the ``lb_traffic_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListLbTrafficExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dep.ListLbTrafficExtensionsResponse],
        request: dep.ListLbTrafficExtensionsRequest,
        response: dep.ListLbTrafficExtensionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListLbTrafficExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListLbTrafficExtensionsResponse):
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
        self._request = dep.ListLbTrafficExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dep.ListLbTrafficExtensionsResponse]:
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

    def __iter__(self) -> Iterator[dep.LbTrafficExtension]:
        for page in self.pages:
            yield from page.lb_traffic_extensions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLbTrafficExtensionsAsyncPager:
    """A pager for iterating through ``list_lb_traffic_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListLbTrafficExtensionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``lb_traffic_extensions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLbTrafficExtensions`` requests and continue to iterate
    through the ``lb_traffic_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListLbTrafficExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dep.ListLbTrafficExtensionsResponse]],
        request: dep.ListLbTrafficExtensionsRequest,
        response: dep.ListLbTrafficExtensionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListLbTrafficExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListLbTrafficExtensionsResponse):
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
        self._request = dep.ListLbTrafficExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dep.ListLbTrafficExtensionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dep.LbTrafficExtension]:
        async def async_generator():
            async for page in self.pages:
                for response in page.lb_traffic_extensions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLbRouteExtensionsPager:
    """A pager for iterating through ``list_lb_route_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListLbRouteExtensionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``lb_route_extensions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLbRouteExtensions`` requests and continue to iterate
    through the ``lb_route_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListLbRouteExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dep.ListLbRouteExtensionsResponse],
        request: dep.ListLbRouteExtensionsRequest,
        response: dep.ListLbRouteExtensionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListLbRouteExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListLbRouteExtensionsResponse):
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
        self._request = dep.ListLbRouteExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dep.ListLbRouteExtensionsResponse]:
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

    def __iter__(self) -> Iterator[dep.LbRouteExtension]:
        for page in self.pages:
            yield from page.lb_route_extensions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLbRouteExtensionsAsyncPager:
    """A pager for iterating through ``list_lb_route_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListLbRouteExtensionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``lb_route_extensions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLbRouteExtensions`` requests and continue to iterate
    through the ``lb_route_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListLbRouteExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dep.ListLbRouteExtensionsResponse]],
        request: dep.ListLbRouteExtensionsRequest,
        response: dep.ListLbRouteExtensionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListLbRouteExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListLbRouteExtensionsResponse):
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
        self._request = dep.ListLbRouteExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dep.ListLbRouteExtensionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dep.LbRouteExtension]:
        async def async_generator():
            async for page in self.pages:
                for response in page.lb_route_extensions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLbEdgeExtensionsPager:
    """A pager for iterating through ``list_lb_edge_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListLbEdgeExtensionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``lb_edge_extensions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLbEdgeExtensions`` requests and continue to iterate
    through the ``lb_edge_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListLbEdgeExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dep.ListLbEdgeExtensionsResponse],
        request: dep.ListLbEdgeExtensionsRequest,
        response: dep.ListLbEdgeExtensionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListLbEdgeExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListLbEdgeExtensionsResponse):
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
        self._request = dep.ListLbEdgeExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dep.ListLbEdgeExtensionsResponse]:
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

    def __iter__(self) -> Iterator[dep.LbEdgeExtension]:
        for page in self.pages:
            yield from page.lb_edge_extensions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLbEdgeExtensionsAsyncPager:
    """A pager for iterating through ``list_lb_edge_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListLbEdgeExtensionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``lb_edge_extensions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLbEdgeExtensions`` requests and continue to iterate
    through the ``lb_edge_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListLbEdgeExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dep.ListLbEdgeExtensionsResponse]],
        request: dep.ListLbEdgeExtensionsRequest,
        response: dep.ListLbEdgeExtensionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListLbEdgeExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListLbEdgeExtensionsResponse):
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
        self._request = dep.ListLbEdgeExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dep.ListLbEdgeExtensionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dep.LbEdgeExtension]:
        async def async_generator():
            async for page in self.pages:
                for response in page.lb_edge_extensions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthzExtensionsPager:
    """A pager for iterating through ``list_authz_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListAuthzExtensionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``authz_extensions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuthzExtensions`` requests and continue to iterate
    through the ``authz_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListAuthzExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dep.ListAuthzExtensionsResponse],
        request: dep.ListAuthzExtensionsRequest,
        response: dep.ListAuthzExtensionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListAuthzExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListAuthzExtensionsResponse):
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
        self._request = dep.ListAuthzExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dep.ListAuthzExtensionsResponse]:
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

    def __iter__(self) -> Iterator[dep.AuthzExtension]:
        for page in self.pages:
            yield from page.authz_extensions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthzExtensionsAsyncPager:
    """A pager for iterating through ``list_authz_extensions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_services_v1.types.ListAuthzExtensionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``authz_extensions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuthzExtensions`` requests and continue to iterate
    through the ``authz_extensions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_services_v1.types.ListAuthzExtensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dep.ListAuthzExtensionsResponse]],
        request: dep.ListAuthzExtensionsRequest,
        response: dep.ListAuthzExtensionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_services_v1.types.ListAuthzExtensionsRequest):
                The initial request object.
            response (google.cloud.network_services_v1.types.ListAuthzExtensionsResponse):
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
        self._request = dep.ListAuthzExtensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dep.ListAuthzExtensionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dep.AuthzExtension]:
        async def async_generator():
            async for page in self.pages:
                for response in page.authz_extensions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
