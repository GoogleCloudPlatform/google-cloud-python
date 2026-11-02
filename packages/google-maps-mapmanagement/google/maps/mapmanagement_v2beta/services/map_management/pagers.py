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

from google.maps.mapmanagement_v2beta.types import map_management_service


class ListMapConfigsPager:
    """A pager for iterating through ``list_map_configs`` requests.

    This class thinly wraps an initial
    :class:`google.maps.mapmanagement_v2beta.types.ListMapConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``map_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMapConfigs`` requests and continue to iterate
    through the ``map_configs`` field on the
    corresponding responses.

    All the usual :class:`google.maps.mapmanagement_v2beta.types.ListMapConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., map_management_service.ListMapConfigsResponse],
        request: map_management_service.ListMapConfigsRequest,
        response: map_management_service.ListMapConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.maps.mapmanagement_v2beta.types.ListMapConfigsRequest):
                The initial request object.
            response (google.maps.mapmanagement_v2beta.types.ListMapConfigsResponse):
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
        self._request = map_management_service.ListMapConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[map_management_service.ListMapConfigsResponse]:
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

    def __iter__(self) -> Iterator[map_management_service.MapConfig]:
        for page in self.pages:
            yield from page.map_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMapConfigsAsyncPager:
    """A pager for iterating through ``list_map_configs`` requests.

    This class thinly wraps an initial
    :class:`google.maps.mapmanagement_v2beta.types.ListMapConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``map_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMapConfigs`` requests and continue to iterate
    through the ``map_configs`` field on the
    corresponding responses.

    All the usual :class:`google.maps.mapmanagement_v2beta.types.ListMapConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[map_management_service.ListMapConfigsResponse]],
        request: map_management_service.ListMapConfigsRequest,
        response: map_management_service.ListMapConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.maps.mapmanagement_v2beta.types.ListMapConfigsRequest):
                The initial request object.
            response (google.maps.mapmanagement_v2beta.types.ListMapConfigsResponse):
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
        self._request = map_management_service.ListMapConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[map_management_service.ListMapConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[map_management_service.MapConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.map_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStyleConfigsPager:
    """A pager for iterating through ``list_style_configs`` requests.

    This class thinly wraps an initial
    :class:`google.maps.mapmanagement_v2beta.types.ListStyleConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``style_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStyleConfigs`` requests and continue to iterate
    through the ``style_configs`` field on the
    corresponding responses.

    All the usual :class:`google.maps.mapmanagement_v2beta.types.ListStyleConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., map_management_service.ListStyleConfigsResponse],
        request: map_management_service.ListStyleConfigsRequest,
        response: map_management_service.ListStyleConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.maps.mapmanagement_v2beta.types.ListStyleConfigsRequest):
                The initial request object.
            response (google.maps.mapmanagement_v2beta.types.ListStyleConfigsResponse):
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
        self._request = map_management_service.ListStyleConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[map_management_service.ListStyleConfigsResponse]:
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

    def __iter__(self) -> Iterator[map_management_service.StyleConfig]:
        for page in self.pages:
            yield from page.style_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStyleConfigsAsyncPager:
    """A pager for iterating through ``list_style_configs`` requests.

    This class thinly wraps an initial
    :class:`google.maps.mapmanagement_v2beta.types.ListStyleConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``style_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStyleConfigs`` requests and continue to iterate
    through the ``style_configs`` field on the
    corresponding responses.

    All the usual :class:`google.maps.mapmanagement_v2beta.types.ListStyleConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[map_management_service.ListStyleConfigsResponse]
        ],
        request: map_management_service.ListStyleConfigsRequest,
        response: map_management_service.ListStyleConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.maps.mapmanagement_v2beta.types.ListStyleConfigsRequest):
                The initial request object.
            response (google.maps.mapmanagement_v2beta.types.ListStyleConfigsResponse):
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
        self._request = map_management_service.ListStyleConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[map_management_service.ListStyleConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[map_management_service.StyleConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.style_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMapContextConfigsPager:
    """A pager for iterating through ``list_map_context_configs`` requests.

    This class thinly wraps an initial
    :class:`google.maps.mapmanagement_v2beta.types.ListMapContextConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``map_context_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMapContextConfigs`` requests and continue to iterate
    through the ``map_context_configs`` field on the
    corresponding responses.

    All the usual :class:`google.maps.mapmanagement_v2beta.types.ListMapContextConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., map_management_service.ListMapContextConfigsResponse],
        request: map_management_service.ListMapContextConfigsRequest,
        response: map_management_service.ListMapContextConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.maps.mapmanagement_v2beta.types.ListMapContextConfigsRequest):
                The initial request object.
            response (google.maps.mapmanagement_v2beta.types.ListMapContextConfigsResponse):
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
        self._request = map_management_service.ListMapContextConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[map_management_service.ListMapContextConfigsResponse]:
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

    def __iter__(self) -> Iterator[map_management_service.MapContextConfig]:
        for page in self.pages:
            yield from page.map_context_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMapContextConfigsAsyncPager:
    """A pager for iterating through ``list_map_context_configs`` requests.

    This class thinly wraps an initial
    :class:`google.maps.mapmanagement_v2beta.types.ListMapContextConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``map_context_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMapContextConfigs`` requests and continue to iterate
    through the ``map_context_configs`` field on the
    corresponding responses.

    All the usual :class:`google.maps.mapmanagement_v2beta.types.ListMapContextConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[map_management_service.ListMapContextConfigsResponse]
        ],
        request: map_management_service.ListMapContextConfigsRequest,
        response: map_management_service.ListMapContextConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.maps.mapmanagement_v2beta.types.ListMapContextConfigsRequest):
                The initial request object.
            response (google.maps.mapmanagement_v2beta.types.ListMapContextConfigsResponse):
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
        self._request = map_management_service.ListMapContextConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[map_management_service.ListMapContextConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[map_management_service.MapContextConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.map_context_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
