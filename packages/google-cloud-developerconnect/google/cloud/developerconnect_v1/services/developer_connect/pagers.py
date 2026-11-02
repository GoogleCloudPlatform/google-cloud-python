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

from google.cloud.developerconnect_v1.types import developer_connect


class ListConnectionsPager:
    """A pager for iterating through ``list_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., developer_connect.ListConnectionsResponse],
        request: developer_connect.ListConnectionsRequest,
        response: developer_connect.ListConnectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListConnectionsRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListConnectionsResponse):
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
        self._request = developer_connect.ListConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[developer_connect.ListConnectionsResponse]:
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

    def __iter__(self) -> Iterator[developer_connect.Connection]:
        for page in self.pages:
            yield from page.connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionsAsyncPager:
    """A pager for iterating through ``list_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[developer_connect.ListConnectionsResponse]],
        request: developer_connect.ListConnectionsRequest,
        response: developer_connect.ListConnectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListConnectionsRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListConnectionsResponse):
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
        self._request = developer_connect.ListConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[developer_connect.ListConnectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[developer_connect.Connection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGitRepositoryLinksPager:
    """A pager for iterating through ``list_git_repository_links`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``git_repository_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGitRepositoryLinks`` requests and continue to iterate
    through the ``git_repository_links`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., developer_connect.ListGitRepositoryLinksResponse],
        request: developer_connect.ListGitRepositoryLinksRequest,
        response: developer_connect.ListGitRepositoryLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListGitRepositoryLinksRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse):
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
        self._request = developer_connect.ListGitRepositoryLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[developer_connect.ListGitRepositoryLinksResponse]:
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

    def __iter__(self) -> Iterator[developer_connect.GitRepositoryLink]:
        for page in self.pages:
            yield from page.git_repository_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGitRepositoryLinksAsyncPager:
    """A pager for iterating through ``list_git_repository_links`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``git_repository_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGitRepositoryLinks`` requests and continue to iterate
    through the ``git_repository_links`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[developer_connect.ListGitRepositoryLinksResponse]
        ],
        request: developer_connect.ListGitRepositoryLinksRequest,
        response: developer_connect.ListGitRepositoryLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListGitRepositoryLinksRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse):
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
        self._request = developer_connect.ListGitRepositoryLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[developer_connect.ListGitRepositoryLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[developer_connect.GitRepositoryLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.git_repository_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchLinkableGitRepositoriesPager:
    """A pager for iterating through ``fetch_linkable_git_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``linkable_git_repositories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchLinkableGitRepositories`` requests and continue to iterate
    through the ``linkable_git_repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., developer_connect.FetchLinkableGitRepositoriesResponse],
        request: developer_connect.FetchLinkableGitRepositoriesRequest,
        response: developer_connect.FetchLinkableGitRepositoriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse):
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
        self._request = developer_connect.FetchLinkableGitRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[developer_connect.FetchLinkableGitRepositoriesResponse]:
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

    def __iter__(self) -> Iterator[developer_connect.LinkableGitRepository]:
        for page in self.pages:
            yield from page.linkable_git_repositories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchLinkableGitRepositoriesAsyncPager:
    """A pager for iterating through ``fetch_linkable_git_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``linkable_git_repositories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchLinkableGitRepositories`` requests and continue to iterate
    through the ``linkable_git_repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[developer_connect.FetchLinkableGitRepositoriesResponse]
        ],
        request: developer_connect.FetchLinkableGitRepositoriesRequest,
        response: developer_connect.FetchLinkableGitRepositoriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse):
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
        self._request = developer_connect.FetchLinkableGitRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[developer_connect.FetchLinkableGitRepositoriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[developer_connect.LinkableGitRepository]:
        async def async_generator():
            async for page in self.pages:
                for response in page.linkable_git_repositories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchGitRefsPager:
    """A pager for iterating through ``fetch_git_refs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.FetchGitRefsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``ref_names`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchGitRefs`` requests and continue to iterate
    through the ``ref_names`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.FetchGitRefsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., developer_connect.FetchGitRefsResponse],
        request: developer_connect.FetchGitRefsRequest,
        response: developer_connect.FetchGitRefsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.FetchGitRefsRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.FetchGitRefsResponse):
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
        self._request = developer_connect.FetchGitRefsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[developer_connect.FetchGitRefsResponse]:
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
            yield from page.ref_names

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchGitRefsAsyncPager:
    """A pager for iterating through ``fetch_git_refs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.FetchGitRefsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``ref_names`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchGitRefs`` requests and continue to iterate
    through the ``ref_names`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.FetchGitRefsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[developer_connect.FetchGitRefsResponse]],
        request: developer_connect.FetchGitRefsRequest,
        response: developer_connect.FetchGitRefsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.FetchGitRefsRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.FetchGitRefsResponse):
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
        self._request = developer_connect.FetchGitRefsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[developer_connect.FetchGitRefsResponse]:
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
                for response in page.ref_names:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccountConnectorsPager:
    """A pager for iterating through ``list_account_connectors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``account_connectors`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccountConnectors`` requests and continue to iterate
    through the ``account_connectors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., developer_connect.ListAccountConnectorsResponse],
        request: developer_connect.ListAccountConnectorsRequest,
        response: developer_connect.ListAccountConnectorsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListAccountConnectorsRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse):
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
        self._request = developer_connect.ListAccountConnectorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[developer_connect.ListAccountConnectorsResponse]:
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

    def __iter__(self) -> Iterator[developer_connect.AccountConnector]:
        for page in self.pages:
            yield from page.account_connectors

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccountConnectorsAsyncPager:
    """A pager for iterating through ``list_account_connectors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``account_connectors`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccountConnectors`` requests and continue to iterate
    through the ``account_connectors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[developer_connect.ListAccountConnectorsResponse]
        ],
        request: developer_connect.ListAccountConnectorsRequest,
        response: developer_connect.ListAccountConnectorsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListAccountConnectorsRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse):
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
        self._request = developer_connect.ListAccountConnectorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[developer_connect.ListAccountConnectorsResponse]:
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

    def __aiter__(self) -> AsyncIterator[developer_connect.AccountConnector]:
        async def async_generator():
            async for page in self.pages:
                for response in page.account_connectors:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUsersPager:
    """A pager for iterating through ``list_users`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListUsersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``users`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUsers`` requests and continue to iterate
    through the ``users`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListUsersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., developer_connect.ListUsersResponse],
        request: developer_connect.ListUsersRequest,
        response: developer_connect.ListUsersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListUsersRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListUsersResponse):
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
        self._request = developer_connect.ListUsersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[developer_connect.ListUsersResponse]:
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

    def __iter__(self) -> Iterator[developer_connect.User]:
        for page in self.pages:
            yield from page.users

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUsersAsyncPager:
    """A pager for iterating through ``list_users`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.developerconnect_v1.types.ListUsersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``users`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUsers`` requests and continue to iterate
    through the ``users`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.developerconnect_v1.types.ListUsersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[developer_connect.ListUsersResponse]],
        request: developer_connect.ListUsersRequest,
        response: developer_connect.ListUsersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.developerconnect_v1.types.ListUsersRequest):
                The initial request object.
            response (google.cloud.developerconnect_v1.types.ListUsersResponse):
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
        self._request = developer_connect.ListUsersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[developer_connect.ListUsersResponse]:
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

    def __aiter__(self) -> AsyncIterator[developer_connect.User]:
        async def async_generator():
            async for page in self.pages:
                for response in page.users:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
