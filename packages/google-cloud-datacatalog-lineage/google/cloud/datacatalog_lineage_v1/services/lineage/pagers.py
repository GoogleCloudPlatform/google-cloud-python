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

from google.cloud.datacatalog_lineage_v1.types import lineage


class ListProcessesPager:
    """A pager for iterating through ``list_processes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.ListProcessesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``processes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProcesses`` requests and continue to iterate
    through the ``processes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.ListProcessesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lineage.ListProcessesResponse],
        request: lineage.ListProcessesRequest,
        response: lineage.ListProcessesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.ListProcessesRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.ListProcessesResponse):
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
        self._request = lineage.ListProcessesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lineage.ListProcessesResponse]:
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

    def __iter__(self) -> Iterator[lineage.Process]:
        for page in self.pages:
            yield from page.processes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessesAsyncPager:
    """A pager for iterating through ``list_processes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.ListProcessesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``processes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProcesses`` requests and continue to iterate
    through the ``processes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.ListProcessesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lineage.ListProcessesResponse]],
        request: lineage.ListProcessesRequest,
        response: lineage.ListProcessesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.ListProcessesRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.ListProcessesResponse):
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
        self._request = lineage.ListProcessesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lineage.ListProcessesResponse]:
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

    def __aiter__(self) -> AsyncIterator[lineage.Process]:
        async def async_generator():
            async for page in self.pages:
                for response in page.processes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRunsPager:
    """A pager for iterating through ``list_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.ListRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRuns`` requests and continue to iterate
    through the ``runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.ListRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lineage.ListRunsResponse],
        request: lineage.ListRunsRequest,
        response: lineage.ListRunsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.ListRunsRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.ListRunsResponse):
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
        self._request = lineage.ListRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lineage.ListRunsResponse]:
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

    def __iter__(self) -> Iterator[lineage.Run]:
        for page in self.pages:
            yield from page.runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRunsAsyncPager:
    """A pager for iterating through ``list_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.ListRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRuns`` requests and continue to iterate
    through the ``runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.ListRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lineage.ListRunsResponse]],
        request: lineage.ListRunsRequest,
        response: lineage.ListRunsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.ListRunsRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.ListRunsResponse):
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
        self._request = lineage.ListRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lineage.ListRunsResponse]:
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

    def __aiter__(self) -> AsyncIterator[lineage.Run]:
        async def async_generator():
            async for page in self.pages:
                for response in page.runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLineageEventsPager:
    """A pager for iterating through ``list_lineage_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.ListLineageEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``lineage_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLineageEvents`` requests and continue to iterate
    through the ``lineage_events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.ListLineageEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lineage.ListLineageEventsResponse],
        request: lineage.ListLineageEventsRequest,
        response: lineage.ListLineageEventsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.ListLineageEventsRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.ListLineageEventsResponse):
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
        self._request = lineage.ListLineageEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lineage.ListLineageEventsResponse]:
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

    def __iter__(self) -> Iterator[lineage.LineageEvent]:
        for page in self.pages:
            yield from page.lineage_events

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLineageEventsAsyncPager:
    """A pager for iterating through ``list_lineage_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.ListLineageEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``lineage_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLineageEvents`` requests and continue to iterate
    through the ``lineage_events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.ListLineageEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lineage.ListLineageEventsResponse]],
        request: lineage.ListLineageEventsRequest,
        response: lineage.ListLineageEventsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.ListLineageEventsRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.ListLineageEventsResponse):
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
        self._request = lineage.ListLineageEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lineage.ListLineageEventsResponse]:
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

    def __aiter__(self) -> AsyncIterator[lineage.LineageEvent]:
        async def async_generator():
            async for page in self.pages:
                for response in page.lineage_events:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchLinksPager:
    """A pager for iterating through ``search_links`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.SearchLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchLinks`` requests and continue to iterate
    through the ``links`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.SearchLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lineage.SearchLinksResponse],
        request: lineage.SearchLinksRequest,
        response: lineage.SearchLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.SearchLinksRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.SearchLinksResponse):
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
        self._request = lineage.SearchLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lineage.SearchLinksResponse]:
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

    def __iter__(self) -> Iterator[lineage.Link]:
        for page in self.pages:
            yield from page.links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchLinksAsyncPager:
    """A pager for iterating through ``search_links`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.SearchLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchLinks`` requests and continue to iterate
    through the ``links`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.SearchLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lineage.SearchLinksResponse]],
        request: lineage.SearchLinksRequest,
        response: lineage.SearchLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.SearchLinksRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.SearchLinksResponse):
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
        self._request = lineage.SearchLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lineage.SearchLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[lineage.Link]:
        async def async_generator():
            async for page in self.pages:
                for response in page.links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class BatchSearchLinkProcessesPager:
    """A pager for iterating through ``batch_search_link_processes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``process_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``BatchSearchLinkProcesses`` requests and continue to iterate
    through the ``process_links`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lineage.BatchSearchLinkProcessesResponse],
        request: lineage.BatchSearchLinkProcessesRequest,
        response: lineage.BatchSearchLinkProcessesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesResponse):
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
        self._request = lineage.BatchSearchLinkProcessesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lineage.BatchSearchLinkProcessesResponse]:
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

    def __iter__(self) -> Iterator[lineage.ProcessLinks]:
        for page in self.pages:
            yield from page.process_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class BatchSearchLinkProcessesAsyncPager:
    """A pager for iterating through ``batch_search_link_processes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``process_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``BatchSearchLinkProcesses`` requests and continue to iterate
    through the ``process_links`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lineage.BatchSearchLinkProcessesResponse]],
        request: lineage.BatchSearchLinkProcessesRequest,
        response: lineage.BatchSearchLinkProcessesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesRequest):
                The initial request object.
            response (google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesResponse):
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
        self._request = lineage.BatchSearchLinkProcessesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lineage.BatchSearchLinkProcessesResponse]:
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

    def __aiter__(self) -> AsyncIterator[lineage.ProcessLinks]:
        async def async_generator():
            async for page in self.pages:
                for response in page.process_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
