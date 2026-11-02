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

from google.cloud.networkconnectivity_v1beta.types import hub


class ListHubsPager:
    """A pager for iterating through ``list_hubs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListHubsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``hubs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHubs`` requests and continue to iterate
    through the ``hubs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListHubsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.ListHubsResponse],
        request: hub.ListHubsRequest,
        response: hub.ListHubsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListHubsRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListHubsResponse):
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
        self._request = hub.ListHubsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.ListHubsResponse]:
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

    def __iter__(self) -> Iterator[hub.Hub]:
        for page in self.pages:
            yield from page.hubs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHubsAsyncPager:
    """A pager for iterating through ``list_hubs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListHubsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``hubs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHubs`` requests and continue to iterate
    through the ``hubs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListHubsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.ListHubsResponse]],
        request: hub.ListHubsRequest,
        response: hub.ListHubsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListHubsRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListHubsResponse):
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
        self._request = hub.ListHubsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.ListHubsResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.Hub]:
        async def async_generator():
            async for page in self.pages:
                for response in page.hubs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHubSpokesPager:
    """A pager for iterating through ``list_hub_spokes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``spokes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHubSpokes`` requests and continue to iterate
    through the ``spokes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.ListHubSpokesResponse],
        request: hub.ListHubSpokesRequest,
        response: hub.ListHubSpokesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListHubSpokesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse):
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
        self._request = hub.ListHubSpokesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.ListHubSpokesResponse]:
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

    def __iter__(self) -> Iterator[hub.Spoke]:
        for page in self.pages:
            yield from page.spokes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHubSpokesAsyncPager:
    """A pager for iterating through ``list_hub_spokes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``spokes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHubSpokes`` requests and continue to iterate
    through the ``spokes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.ListHubSpokesResponse]],
        request: hub.ListHubSpokesRequest,
        response: hub.ListHubSpokesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListHubSpokesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse):
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
        self._request = hub.ListHubSpokesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.ListHubSpokesResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.Spoke]:
        async def async_generator():
            async for page in self.pages:
                for response in page.spokes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryHubStatusPager:
    """A pager for iterating through ``query_hub_status`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.QueryHubStatusResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``hub_status_entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryHubStatus`` requests and continue to iterate
    through the ``hub_status_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.QueryHubStatusResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.QueryHubStatusResponse],
        request: hub.QueryHubStatusRequest,
        response: hub.QueryHubStatusResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.QueryHubStatusRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.QueryHubStatusResponse):
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
        self._request = hub.QueryHubStatusRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.QueryHubStatusResponse]:
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

    def __iter__(self) -> Iterator[hub.HubStatusEntry]:
        for page in self.pages:
            yield from page.hub_status_entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryHubStatusAsyncPager:
    """A pager for iterating through ``query_hub_status`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.QueryHubStatusResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``hub_status_entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryHubStatus`` requests and continue to iterate
    through the ``hub_status_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.QueryHubStatusResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.QueryHubStatusResponse]],
        request: hub.QueryHubStatusRequest,
        response: hub.QueryHubStatusResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.QueryHubStatusRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.QueryHubStatusResponse):
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
        self._request = hub.QueryHubStatusRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.QueryHubStatusResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.HubStatusEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.hub_status_entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSpokesPager:
    """A pager for iterating through ``list_spokes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListSpokesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``spokes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSpokes`` requests and continue to iterate
    through the ``spokes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListSpokesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.ListSpokesResponse],
        request: hub.ListSpokesRequest,
        response: hub.ListSpokesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListSpokesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListSpokesResponse):
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
        self._request = hub.ListSpokesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.ListSpokesResponse]:
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

    def __iter__(self) -> Iterator[hub.Spoke]:
        for page in self.pages:
            yield from page.spokes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSpokesAsyncPager:
    """A pager for iterating through ``list_spokes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListSpokesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``spokes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSpokes`` requests and continue to iterate
    through the ``spokes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListSpokesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.ListSpokesResponse]],
        request: hub.ListSpokesRequest,
        response: hub.ListSpokesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListSpokesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListSpokesResponse):
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
        self._request = hub.ListSpokesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.ListSpokesResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.Spoke]:
        async def async_generator():
            async for page in self.pages:
                for response in page.spokes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutesPager:
    """A pager for iterating through ``list_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRoutes`` requests and continue to iterate
    through the ``routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.ListRoutesResponse],
        request: hub.ListRoutesRequest,
        response: hub.ListRoutesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListRoutesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListRoutesResponse):
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
        self._request = hub.ListRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.ListRoutesResponse]:
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

    def __iter__(self) -> Iterator[hub.Route]:
        for page in self.pages:
            yield from page.routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutesAsyncPager:
    """A pager for iterating through ``list_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRoutes`` requests and continue to iterate
    through the ``routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.ListRoutesResponse]],
        request: hub.ListRoutesRequest,
        response: hub.ListRoutesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListRoutesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListRoutesResponse):
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
        self._request = hub.ListRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.ListRoutesResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.Route]:
        async def async_generator():
            async for page in self.pages:
                for response in page.routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRouteTablesPager:
    """A pager for iterating through ``list_route_tables`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListRouteTablesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``route_tables`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRouteTables`` requests and continue to iterate
    through the ``route_tables`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListRouteTablesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.ListRouteTablesResponse],
        request: hub.ListRouteTablesRequest,
        response: hub.ListRouteTablesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListRouteTablesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListRouteTablesResponse):
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
        self._request = hub.ListRouteTablesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.ListRouteTablesResponse]:
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

    def __iter__(self) -> Iterator[hub.RouteTable]:
        for page in self.pages:
            yield from page.route_tables

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRouteTablesAsyncPager:
    """A pager for iterating through ``list_route_tables`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListRouteTablesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``route_tables`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRouteTables`` requests and continue to iterate
    through the ``route_tables`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListRouteTablesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.ListRouteTablesResponse]],
        request: hub.ListRouteTablesRequest,
        response: hub.ListRouteTablesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListRouteTablesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListRouteTablesResponse):
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
        self._request = hub.ListRouteTablesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.ListRouteTablesResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.RouteTable]:
        async def async_generator():
            async for page in self.pages:
                for response in page.route_tables:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGroupsPager:
    """A pager for iterating through ``list_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGroups`` requests and continue to iterate
    through the ``groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.ListGroupsResponse],
        request: hub.ListGroupsRequest,
        response: hub.ListGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListGroupsRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListGroupsResponse):
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
        self._request = hub.ListGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.ListGroupsResponse]:
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

    def __iter__(self) -> Iterator[hub.Group]:
        for page in self.pages:
            yield from page.groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGroupsAsyncPager:
    """A pager for iterating through ``list_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGroups`` requests and continue to iterate
    through the ``groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.ListGroupsResponse]],
        request: hub.ListGroupsRequest,
        response: hub.ListGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListGroupsRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListGroupsResponse):
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
        self._request = hub.ListGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.ListGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.Group]:
        async def async_generator():
            async for page in self.pages:
                for response in page.groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewayAdvertisedRoutesPager:
    """A pager for iterating through ``list_gateway_advertised_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``gateway_advertised_routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGatewayAdvertisedRoutes`` requests and continue to iterate
    through the ``gateway_advertised_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hub.ListGatewayAdvertisedRoutesResponse],
        request: hub.ListGatewayAdvertisedRoutesRequest,
        response: hub.ListGatewayAdvertisedRoutesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesResponse):
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
        self._request = hub.ListGatewayAdvertisedRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hub.ListGatewayAdvertisedRoutesResponse]:
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

    def __iter__(self) -> Iterator[hub.GatewayAdvertisedRoute]:
        for page in self.pages:
            yield from page.gateway_advertised_routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGatewayAdvertisedRoutesAsyncPager:
    """A pager for iterating through ``list_gateway_advertised_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``gateway_advertised_routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGatewayAdvertisedRoutes`` requests and continue to iterate
    through the ``gateway_advertised_routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[hub.ListGatewayAdvertisedRoutesResponse]],
        request: hub.ListGatewayAdvertisedRoutesRequest,
        response: hub.ListGatewayAdvertisedRoutesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1beta.types.ListGatewayAdvertisedRoutesResponse):
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
        self._request = hub.ListGatewayAdvertisedRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[hub.ListGatewayAdvertisedRoutesResponse]:
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

    def __aiter__(self) -> AsyncIterator[hub.GatewayAdvertisedRoute]:
        async def async_generator():
            async for page in self.pages:
                for response in page.gateway_advertised_routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
