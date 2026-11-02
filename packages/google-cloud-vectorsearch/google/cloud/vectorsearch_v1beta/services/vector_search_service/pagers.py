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

from google.cloud.vectorsearch_v1beta.types import vectorsearch_service


class ListCollectionsPager:
    """A pager for iterating through ``list_collections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vectorsearch_v1beta.types.ListCollectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``collections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCollections`` requests and continue to iterate
    through the ``collections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vectorsearch_v1beta.types.ListCollectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vectorsearch_service.ListCollectionsResponse],
        request: vectorsearch_service.ListCollectionsRequest,
        response: vectorsearch_service.ListCollectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vectorsearch_v1beta.types.ListCollectionsRequest):
                The initial request object.
            response (google.cloud.vectorsearch_v1beta.types.ListCollectionsResponse):
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
        self._request = vectorsearch_service.ListCollectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vectorsearch_service.ListCollectionsResponse]:
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

    def __iter__(self) -> Iterator[vectorsearch_service.Collection]:
        for page in self.pages:
            yield from page.collections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCollectionsAsyncPager:
    """A pager for iterating through ``list_collections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vectorsearch_v1beta.types.ListCollectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``collections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCollections`` requests and continue to iterate
    through the ``collections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vectorsearch_v1beta.types.ListCollectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vectorsearch_service.ListCollectionsResponse]],
        request: vectorsearch_service.ListCollectionsRequest,
        response: vectorsearch_service.ListCollectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vectorsearch_v1beta.types.ListCollectionsRequest):
                The initial request object.
            response (google.cloud.vectorsearch_v1beta.types.ListCollectionsResponse):
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
        self._request = vectorsearch_service.ListCollectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[vectorsearch_service.ListCollectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vectorsearch_service.Collection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.collections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIndexesPager:
    """A pager for iterating through ``list_indexes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vectorsearch_v1beta.types.ListIndexesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``indexes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListIndexes`` requests and continue to iterate
    through the ``indexes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vectorsearch_v1beta.types.ListIndexesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vectorsearch_service.ListIndexesResponse],
        request: vectorsearch_service.ListIndexesRequest,
        response: vectorsearch_service.ListIndexesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vectorsearch_v1beta.types.ListIndexesRequest):
                The initial request object.
            response (google.cloud.vectorsearch_v1beta.types.ListIndexesResponse):
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
        self._request = vectorsearch_service.ListIndexesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vectorsearch_service.ListIndexesResponse]:
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

    def __iter__(self) -> Iterator[vectorsearch_service.Index]:
        for page in self.pages:
            yield from page.indexes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIndexesAsyncPager:
    """A pager for iterating through ``list_indexes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vectorsearch_v1beta.types.ListIndexesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``indexes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListIndexes`` requests and continue to iterate
    through the ``indexes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vectorsearch_v1beta.types.ListIndexesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vectorsearch_service.ListIndexesResponse]],
        request: vectorsearch_service.ListIndexesRequest,
        response: vectorsearch_service.ListIndexesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vectorsearch_v1beta.types.ListIndexesRequest):
                The initial request object.
            response (google.cloud.vectorsearch_v1beta.types.ListIndexesResponse):
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
        self._request = vectorsearch_service.ListIndexesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vectorsearch_service.ListIndexesResponse]:
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

    def __aiter__(self) -> AsyncIterator[vectorsearch_service.Index]:
        async def async_generator():
            async for page in self.pages:
                for response in page.indexes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
