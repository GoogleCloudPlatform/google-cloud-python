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

from google.cloud.chronicle_v1.types import feed


class ListFeedsPager:
    """A pager for iterating through ``list_feeds`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListFeedsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``feeds`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFeeds`` requests and continue to iterate
    through the ``feeds`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListFeedsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., feed.ListFeedsResponse],
        request: feed.ListFeedsRequest,
        response: feed.ListFeedsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListFeedsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListFeedsResponse):
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
        self._request = feed.ListFeedsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[feed.ListFeedsResponse]:
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

    def __iter__(self) -> Iterator[feed.Feed]:
        for page in self.pages:
            yield from page.feeds

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeedsAsyncPager:
    """A pager for iterating through ``list_feeds`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListFeedsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``feeds`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFeeds`` requests and continue to iterate
    through the ``feeds`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListFeedsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[feed.ListFeedsResponse]],
        request: feed.ListFeedsRequest,
        response: feed.ListFeedsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListFeedsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListFeedsResponse):
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
        self._request = feed.ListFeedsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[feed.ListFeedsResponse]:
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

    def __aiter__(self) -> AsyncIterator[feed.Feed]:
        async def async_generator():
            async for page in self.pages:
                for response in page.feeds:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeedPacksPager:
    """A pager for iterating through ``list_feed_packs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListFeedPacksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``feed_packs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFeedPacks`` requests and continue to iterate
    through the ``feed_packs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListFeedPacksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., feed.ListFeedPacksResponse],
        request: feed.ListFeedPacksRequest,
        response: feed.ListFeedPacksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListFeedPacksRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListFeedPacksResponse):
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
        self._request = feed.ListFeedPacksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[feed.ListFeedPacksResponse]:
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

    def __iter__(self) -> Iterator[feed.FeedPack]:
        for page in self.pages:
            yield from page.feed_packs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeedPacksAsyncPager:
    """A pager for iterating through ``list_feed_packs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListFeedPacksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``feed_packs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFeedPacks`` requests and continue to iterate
    through the ``feed_packs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListFeedPacksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[feed.ListFeedPacksResponse]],
        request: feed.ListFeedPacksRequest,
        response: feed.ListFeedPacksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListFeedPacksRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListFeedPacksResponse):
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
        self._request = feed.ListFeedPacksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[feed.ListFeedPacksResponse]:
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

    def __aiter__(self) -> AsyncIterator[feed.FeedPack]:
        async def async_generator():
            async for page in self.pages:
                for response in page.feed_packs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeedSourceTypeSchemasPager:
    """A pager for iterating through ``list_feed_source_type_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``feed_source_type_schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFeedSourceTypeSchemas`` requests and continue to iterate
    through the ``feed_source_type_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., feed.ListFeedSourceTypeSchemasResponse],
        request: feed.ListFeedSourceTypeSchemasRequest,
        response: feed.ListFeedSourceTypeSchemasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasResponse):
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
        self._request = feed.ListFeedSourceTypeSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[feed.ListFeedSourceTypeSchemasResponse]:
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

    def __iter__(self) -> Iterator[feed.FeedSourceTypeSchema]:
        for page in self.pages:
            yield from page.feed_source_type_schemas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeedSourceTypeSchemasAsyncPager:
    """A pager for iterating through ``list_feed_source_type_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``feed_source_type_schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFeedSourceTypeSchemas`` requests and continue to iterate
    through the ``feed_source_type_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[feed.ListFeedSourceTypeSchemasResponse]],
        request: feed.ListFeedSourceTypeSchemasRequest,
        response: feed.ListFeedSourceTypeSchemasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListFeedSourceTypeSchemasResponse):
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
        self._request = feed.ListFeedSourceTypeSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[feed.ListFeedSourceTypeSchemasResponse]:
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

    def __aiter__(self) -> AsyncIterator[feed.FeedSourceTypeSchema]:
        async def async_generator():
            async for page in self.pages:
                for response in page.feed_source_type_schemas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLogTypeSchemasPager:
    """A pager for iterating through ``list_log_type_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListLogTypeSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``log_type_schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLogTypeSchemas`` requests and continue to iterate
    through the ``log_type_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListLogTypeSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., feed.ListLogTypeSchemasResponse],
        request: feed.ListLogTypeSchemasRequest,
        response: feed.ListLogTypeSchemasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListLogTypeSchemasRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListLogTypeSchemasResponse):
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
        self._request = feed.ListLogTypeSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[feed.ListLogTypeSchemasResponse]:
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

    def __iter__(self) -> Iterator[feed.LogTypeSchema]:
        for page in self.pages:
            yield from page.log_type_schemas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLogTypeSchemasAsyncPager:
    """A pager for iterating through ``list_log_type_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListLogTypeSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``log_type_schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLogTypeSchemas`` requests and continue to iterate
    through the ``log_type_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListLogTypeSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[feed.ListLogTypeSchemasResponse]],
        request: feed.ListLogTypeSchemasRequest,
        response: feed.ListLogTypeSchemasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListLogTypeSchemasRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListLogTypeSchemasResponse):
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
        self._request = feed.ListLogTypeSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[feed.ListLogTypeSchemasResponse]:
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

    def __aiter__(self) -> AsyncIterator[feed.LogTypeSchema]:
        async def async_generator():
            async for page in self.pages:
                for response in page.log_type_schemas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
