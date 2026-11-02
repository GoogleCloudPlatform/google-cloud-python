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

from google.cloud.agentidentity_v1.types import auth_provider_service


class ListAuthProvidersPager:
    """A pager for iterating through ``list_auth_providers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.ListAuthProvidersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``auth_providers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuthProviders`` requests and continue to iterate
    through the ``auth_providers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.ListAuthProvidersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auth_provider_service.ListAuthProvidersResponse],
        request: auth_provider_service.ListAuthProvidersRequest,
        response: auth_provider_service.ListAuthProvidersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.ListAuthProvidersRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.ListAuthProvidersResponse):
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
        self._request = auth_provider_service.ListAuthProvidersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auth_provider_service.ListAuthProvidersResponse]:
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

    def __iter__(self) -> Iterator[auth_provider_service.AuthProvider]:
        for page in self.pages:
            yield from page.auth_providers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthProvidersAsyncPager:
    """A pager for iterating through ``list_auth_providers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.ListAuthProvidersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``auth_providers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuthProviders`` requests and continue to iterate
    through the ``auth_providers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.ListAuthProvidersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[auth_provider_service.ListAuthProvidersResponse]
        ],
        request: auth_provider_service.ListAuthProvidersRequest,
        response: auth_provider_service.ListAuthProvidersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.ListAuthProvidersRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.ListAuthProvidersResponse):
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
        self._request = auth_provider_service.ListAuthProvidersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[auth_provider_service.ListAuthProvidersResponse]:
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

    def __aiter__(self) -> AsyncIterator[auth_provider_service.AuthProvider]:
        async def async_generator():
            async for page in self.pages:
                for response in page.auth_providers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryAuthProvidersPager:
    """A pager for iterating through ``query_auth_providers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``auth_provider_names`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryAuthProviders`` requests and continue to iterate
    through the ``auth_provider_names`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auth_provider_service.QueryAuthProvidersResponse],
        request: auth_provider_service.QueryAuthProvidersRequest,
        response: auth_provider_service.QueryAuthProvidersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.QueryAuthProvidersRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse):
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
        self._request = auth_provider_service.QueryAuthProvidersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auth_provider_service.QueryAuthProvidersResponse]:
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

    def __iter__(self) -> Iterator[str]:
        for page in self.pages:
            yield from page.auth_provider_names

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryAuthProvidersAsyncPager:
    """A pager for iterating through ``query_auth_providers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``auth_provider_names`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryAuthProviders`` requests and continue to iterate
    through the ``auth_provider_names`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[auth_provider_service.QueryAuthProvidersResponse]
        ],
        request: auth_provider_service.QueryAuthProvidersRequest,
        response: auth_provider_service.QueryAuthProvidersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.QueryAuthProvidersRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse):
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
        self._request = auth_provider_service.QueryAuthProvidersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[auth_provider_service.QueryAuthProvidersResponse]:
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

    def __aiter__(self) -> AsyncIterator[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.auth_provider_names:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryWorkloadsPager:
    """A pager for iterating through ``query_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.QueryWorkloadsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workload_ids`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryWorkloads`` requests and continue to iterate
    through the ``workload_ids`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.QueryWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auth_provider_service.QueryWorkloadsResponse],
        request: auth_provider_service.QueryWorkloadsRequest,
        response: auth_provider_service.QueryWorkloadsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.QueryWorkloadsRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.QueryWorkloadsResponse):
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
        self._request = auth_provider_service.QueryWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auth_provider_service.QueryWorkloadsResponse]:
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

    def __iter__(self) -> Iterator[str]:
        for page in self.pages:
            yield from page.workload_ids

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryWorkloadsAsyncPager:
    """A pager for iterating through ``query_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.QueryWorkloadsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workload_ids`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryWorkloads`` requests and continue to iterate
    through the ``workload_ids`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.QueryWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[auth_provider_service.QueryWorkloadsResponse]],
        request: auth_provider_service.QueryWorkloadsRequest,
        response: auth_provider_service.QueryWorkloadsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.QueryWorkloadsRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.QueryWorkloadsResponse):
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
        self._request = auth_provider_service.QueryWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[auth_provider_service.QueryWorkloadsResponse]:
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

    def __aiter__(self) -> AsyncIterator[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workload_ids:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthorizationsPager:
    """A pager for iterating through ``list_authorizations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.ListAuthorizationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``authorizations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuthorizations`` requests and continue to iterate
    through the ``authorizations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.ListAuthorizationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auth_provider_service.ListAuthorizationsResponse],
        request: auth_provider_service.ListAuthorizationsRequest,
        response: auth_provider_service.ListAuthorizationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.ListAuthorizationsRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.ListAuthorizationsResponse):
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
        self._request = auth_provider_service.ListAuthorizationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auth_provider_service.ListAuthorizationsResponse]:
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

    def __iter__(self) -> Iterator[auth_provider_service.Authorization]:
        for page in self.pages:
            yield from page.authorizations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthorizationsAsyncPager:
    """A pager for iterating through ``list_authorizations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.ListAuthorizationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``authorizations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuthorizations`` requests and continue to iterate
    through the ``authorizations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.ListAuthorizationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[auth_provider_service.ListAuthorizationsResponse]
        ],
        request: auth_provider_service.ListAuthorizationsRequest,
        response: auth_provider_service.ListAuthorizationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.ListAuthorizationsRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.ListAuthorizationsResponse):
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
        self._request = auth_provider_service.ListAuthorizationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[auth_provider_service.ListAuthorizationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[auth_provider_service.Authorization]:
        async def async_generator():
            async for page in self.pages:
                for response in page.authorizations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccessSummariesPager:
    """A pager for iterating through ``list_access_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.ListAccessSummariesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``access_summaries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccessSummaries`` requests and continue to iterate
    through the ``access_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.ListAccessSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auth_provider_service.ListAccessSummariesResponse],
        request: auth_provider_service.ListAccessSummariesRequest,
        response: auth_provider_service.ListAccessSummariesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.ListAccessSummariesRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.ListAccessSummariesResponse):
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
        self._request = auth_provider_service.ListAccessSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auth_provider_service.ListAccessSummariesResponse]:
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

    def __iter__(self) -> Iterator[auth_provider_service.AccessSummary]:
        for page in self.pages:
            yield from page.access_summaries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccessSummariesAsyncPager:
    """A pager for iterating through ``list_access_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentidentity_v1.types.ListAccessSummariesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``access_summaries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccessSummaries`` requests and continue to iterate
    through the ``access_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentidentity_v1.types.ListAccessSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[auth_provider_service.ListAccessSummariesResponse]
        ],
        request: auth_provider_service.ListAccessSummariesRequest,
        response: auth_provider_service.ListAccessSummariesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentidentity_v1.types.ListAccessSummariesRequest):
                The initial request object.
            response (google.cloud.agentidentity_v1.types.ListAccessSummariesResponse):
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
        self._request = auth_provider_service.ListAccessSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[auth_provider_service.ListAccessSummariesResponse]:
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

    def __aiter__(self) -> AsyncIterator[auth_provider_service.AccessSummary]:
        async def async_generator():
            async for page in self.pages:
                for response in page.access_summaries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
