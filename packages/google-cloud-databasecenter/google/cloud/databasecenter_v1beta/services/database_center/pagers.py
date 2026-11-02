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

from google.cloud.databasecenter_v1beta.types import product, service


class QueryProductsPager:
    """A pager for iterating through ``query_products`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.QueryProductsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``products`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryProducts`` requests and continue to iterate
    through the ``products`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.QueryProductsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.QueryProductsResponse],
        request: service.QueryProductsRequest,
        response: service.QueryProductsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.QueryProductsRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.QueryProductsResponse):
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
        self._request = service.QueryProductsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.QueryProductsResponse]:
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

    def __iter__(self) -> Iterator[product.Product]:
        for page in self.pages:
            yield from page.products

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryProductsAsyncPager:
    """A pager for iterating through ``query_products`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.QueryProductsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``products`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryProducts`` requests and continue to iterate
    through the ``products`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.QueryProductsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.QueryProductsResponse]],
        request: service.QueryProductsRequest,
        response: service.QueryProductsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.QueryProductsRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.QueryProductsResponse):
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
        self._request = service.QueryProductsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.QueryProductsResponse]:
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

    def __aiter__(self) -> AsyncIterator[product.Product]:
        async def async_generator():
            async for page in self.pages:
                for response in page.products:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AggregateFleetPager:
    """A pager for iterating through ``aggregate_fleet`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.AggregateFleetResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rows`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``AggregateFleet`` requests and continue to iterate
    through the ``rows`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.AggregateFleetResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.AggregateFleetResponse],
        request: service.AggregateFleetRequest,
        response: service.AggregateFleetResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.AggregateFleetRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.AggregateFleetResponse):
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
        self._request = service.AggregateFleetRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.AggregateFleetResponse]:
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

    def __iter__(self) -> Iterator[service.AggregateFleetRow]:
        for page in self.pages:
            yield from page.rows

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AggregateFleetAsyncPager:
    """A pager for iterating through ``aggregate_fleet`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.AggregateFleetResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rows`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``AggregateFleet`` requests and continue to iterate
    through the ``rows`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.AggregateFleetResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.AggregateFleetResponse]],
        request: service.AggregateFleetRequest,
        response: service.AggregateFleetResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.AggregateFleetRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.AggregateFleetResponse):
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
        self._request = service.AggregateFleetRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.AggregateFleetResponse]:
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

    def __aiter__(self) -> AsyncIterator[service.AggregateFleetRow]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rows:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryDatabaseResourceGroupsPager:
    """A pager for iterating through ``query_database_resource_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resource_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryDatabaseResourceGroups`` requests and continue to iterate
    through the ``resource_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.QueryDatabaseResourceGroupsResponse],
        request: service.QueryDatabaseResourceGroupsRequest,
        response: service.QueryDatabaseResourceGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsResponse):
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
        self._request = service.QueryDatabaseResourceGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.QueryDatabaseResourceGroupsResponse]:
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

    def __iter__(self) -> Iterator[service.DatabaseResourceGroup]:
        for page in self.pages:
            yield from page.resource_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryDatabaseResourceGroupsAsyncPager:
    """A pager for iterating through ``query_database_resource_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resource_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryDatabaseResourceGroups`` requests and continue to iterate
    through the ``resource_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.QueryDatabaseResourceGroupsResponse]],
        request: service.QueryDatabaseResourceGroupsRequest,
        response: service.QueryDatabaseResourceGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.QueryDatabaseResourceGroupsResponse):
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
        self._request = service.QueryDatabaseResourceGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.QueryDatabaseResourceGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[service.DatabaseResourceGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resource_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AggregateQueryStatsPager:
    """A pager for iterating through ``aggregate_query_stats`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.AggregateQueryStatsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``query_stats`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``AggregateQueryStats`` requests and continue to iterate
    through the ``query_stats`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.AggregateQueryStatsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.AggregateQueryStatsResponse],
        request: service.AggregateQueryStatsRequest,
        response: service.AggregateQueryStatsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.AggregateQueryStatsRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.AggregateQueryStatsResponse):
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
        self._request = service.AggregateQueryStatsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.AggregateQueryStatsResponse]:
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

    def __iter__(self) -> Iterator[service.QueryStatsInfo]:
        for page in self.pages:
            yield from page.query_stats

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AggregateQueryStatsAsyncPager:
    """A pager for iterating through ``aggregate_query_stats`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.AggregateQueryStatsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``query_stats`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``AggregateQueryStats`` requests and continue to iterate
    through the ``query_stats`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.AggregateQueryStatsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.AggregateQueryStatsResponse]],
        request: service.AggregateQueryStatsRequest,
        response: service.AggregateQueryStatsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.AggregateQueryStatsRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.AggregateQueryStatsResponse):
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
        self._request = service.AggregateQueryStatsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.AggregateQueryStatsResponse]:
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

    def __aiter__(self) -> AsyncIterator[service.QueryStatsInfo]:
        async def async_generator():
            async for page in self.pages:
                for response in page.query_stats:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryIssuesPager:
    """A pager for iterating through ``query_issues`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.QueryIssuesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resource_issues`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryIssues`` requests and continue to iterate
    through the ``resource_issues`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.QueryIssuesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.QueryIssuesResponse],
        request: service.QueryIssuesRequest,
        response: service.QueryIssuesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.QueryIssuesRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.QueryIssuesResponse):
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
        self._request = service.QueryIssuesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.QueryIssuesResponse]:
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

    def __iter__(self) -> Iterator[service.DatabaseResourceIssue]:
        for page in self.pages:
            yield from page.resource_issues

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryIssuesAsyncPager:
    """A pager for iterating through ``query_issues`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.databasecenter_v1beta.types.QueryIssuesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resource_issues`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryIssues`` requests and continue to iterate
    through the ``resource_issues`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.databasecenter_v1beta.types.QueryIssuesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.QueryIssuesResponse]],
        request: service.QueryIssuesRequest,
        response: service.QueryIssuesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.databasecenter_v1beta.types.QueryIssuesRequest):
                The initial request object.
            response (google.cloud.databasecenter_v1beta.types.QueryIssuesResponse):
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
        self._request = service.QueryIssuesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.QueryIssuesResponse]:
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

    def __aiter__(self) -> AsyncIterator[service.DatabaseResourceIssue]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resource_issues:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
