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

from google.cloud.dataform_v1.types import dataform


class QueryTeamFolderContentsPager:
    """A pager for iterating through ``query_team_folder_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryTeamFolderContentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryTeamFolderContents`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryTeamFolderContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.QueryTeamFolderContentsResponse],
        request: dataform.QueryTeamFolderContentsRequest,
        response: dataform.QueryTeamFolderContentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryTeamFolderContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryTeamFolderContentsResponse):
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
        self._request = dataform.QueryTeamFolderContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.QueryTeamFolderContentsResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[dataform.QueryTeamFolderContentsResponse.TeamFolderContentsEntry]:
        for page in self.pages:
            yield from page.entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryTeamFolderContentsAsyncPager:
    """A pager for iterating through ``query_team_folder_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryTeamFolderContentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryTeamFolderContents`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryTeamFolderContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.QueryTeamFolderContentsResponse]],
        request: dataform.QueryTeamFolderContentsRequest,
        response: dataform.QueryTeamFolderContentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryTeamFolderContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryTeamFolderContentsResponse):
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
        self._request = dataform.QueryTeamFolderContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.QueryTeamFolderContentsResponse]:
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

    def __aiter__(
        self,
    ) -> AsyncIterator[
        dataform.QueryTeamFolderContentsResponse.TeamFolderContentsEntry
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchTeamFoldersPager:
    """A pager for iterating through ``search_team_folders`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.SearchTeamFoldersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchTeamFolders`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.SearchTeamFoldersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.SearchTeamFoldersResponse],
        request: dataform.SearchTeamFoldersRequest,
        response: dataform.SearchTeamFoldersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.SearchTeamFoldersRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.SearchTeamFoldersResponse):
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
        self._request = dataform.SearchTeamFoldersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.SearchTeamFoldersResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[dataform.SearchTeamFoldersResponse.TeamFolderSearchResult]:
        for page in self.pages:
            yield from page.results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchTeamFoldersAsyncPager:
    """A pager for iterating through ``search_team_folders`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.SearchTeamFoldersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchTeamFolders`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.SearchTeamFoldersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.SearchTeamFoldersResponse]],
        request: dataform.SearchTeamFoldersRequest,
        response: dataform.SearchTeamFoldersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.SearchTeamFoldersRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.SearchTeamFoldersResponse):
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
        self._request = dataform.SearchTeamFoldersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.SearchTeamFoldersResponse]:
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

    def __aiter__(
        self,
    ) -> AsyncIterator[dataform.SearchTeamFoldersResponse.TeamFolderSearchResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryFolderContentsPager:
    """A pager for iterating through ``query_folder_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryFolderContentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryFolderContents`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryFolderContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.QueryFolderContentsResponse],
        request: dataform.QueryFolderContentsRequest,
        response: dataform.QueryFolderContentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryFolderContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryFolderContentsResponse):
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
        self._request = dataform.QueryFolderContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.QueryFolderContentsResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[dataform.QueryFolderContentsResponse.FolderContentsEntry]:
        for page in self.pages:
            yield from page.entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryFolderContentsAsyncPager:
    """A pager for iterating through ``query_folder_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryFolderContentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryFolderContents`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryFolderContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.QueryFolderContentsResponse]],
        request: dataform.QueryFolderContentsRequest,
        response: dataform.QueryFolderContentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryFolderContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryFolderContentsResponse):
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
        self._request = dataform.QueryFolderContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.QueryFolderContentsResponse]:
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

    def __aiter__(
        self,
    ) -> AsyncIterator[dataform.QueryFolderContentsResponse.FolderContentsEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryUserRootContentsPager:
    """A pager for iterating through ``query_user_root_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryUserRootContentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryUserRootContents`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryUserRootContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.QueryUserRootContentsResponse],
        request: dataform.QueryUserRootContentsRequest,
        response: dataform.QueryUserRootContentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryUserRootContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryUserRootContentsResponse):
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
        self._request = dataform.QueryUserRootContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.QueryUserRootContentsResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[dataform.QueryUserRootContentsResponse.RootContentsEntry]:
        for page in self.pages:
            yield from page.entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryUserRootContentsAsyncPager:
    """A pager for iterating through ``query_user_root_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryUserRootContentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryUserRootContents`` requests and continue to iterate
    through the ``entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryUserRootContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.QueryUserRootContentsResponse]],
        request: dataform.QueryUserRootContentsRequest,
        response: dataform.QueryUserRootContentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryUserRootContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryUserRootContentsResponse):
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
        self._request = dataform.QueryUserRootContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.QueryUserRootContentsResponse]:
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

    def __aiter__(
        self,
    ) -> AsyncIterator[dataform.QueryUserRootContentsResponse.RootContentsEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRepositoriesPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListRepositoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.ListRepositoriesResponse],
        request: dataform.ListRepositoriesRequest,
        response: dataform.ListRepositoriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListRepositoriesResponse):
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
        self._request = dataform.ListRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.ListRepositoriesResponse]:
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

    def __iter__(self) -> Iterator[dataform.Repository]:
        for page in self.pages:
            yield from page.repositories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRepositoriesAsyncPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListRepositoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.ListRepositoriesResponse]],
        request: dataform.ListRepositoriesRequest,
        response: dataform.ListRepositoriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListRepositoriesResponse):
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
        self._request = dataform.ListRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.ListRepositoriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.Repository]:
        async def async_generator():
            async for page in self.pages:
                for response in page.repositories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryRepositoryDirectoryContentsPager:
    """A pager for iterating through ``query_repository_directory_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``directory_entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryRepositoryDirectoryContents`` requests and continue to iterate
    through the ``directory_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.QueryRepositoryDirectoryContentsResponse],
        request: dataform.QueryRepositoryDirectoryContentsRequest,
        response: dataform.QueryRepositoryDirectoryContentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsResponse):
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
        self._request = dataform.QueryRepositoryDirectoryContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.QueryRepositoryDirectoryContentsResponse]:
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

    def __iter__(self) -> Iterator[dataform.DirectoryEntry]:
        for page in self.pages:
            yield from page.directory_entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryRepositoryDirectoryContentsAsyncPager:
    """A pager for iterating through ``query_repository_directory_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``directory_entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryRepositoryDirectoryContents`` requests and continue to iterate
    through the ``directory_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[dataform.QueryRepositoryDirectoryContentsResponse]
        ],
        request: dataform.QueryRepositoryDirectoryContentsRequest,
        response: dataform.QueryRepositoryDirectoryContentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryRepositoryDirectoryContentsResponse):
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
        self._request = dataform.QueryRepositoryDirectoryContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[dataform.QueryRepositoryDirectoryContentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.DirectoryEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.directory_entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchRepositoryHistoryPager:
    """A pager for iterating through ``fetch_repository_history`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.FetchRepositoryHistoryResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``commits`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchRepositoryHistory`` requests and continue to iterate
    through the ``commits`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.FetchRepositoryHistoryResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.FetchRepositoryHistoryResponse],
        request: dataform.FetchRepositoryHistoryRequest,
        response: dataform.FetchRepositoryHistoryResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.FetchRepositoryHistoryRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.FetchRepositoryHistoryResponse):
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
        self._request = dataform.FetchRepositoryHistoryRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.FetchRepositoryHistoryResponse]:
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

    def __iter__(self) -> Iterator[dataform.CommitLogEntry]:
        for page in self.pages:
            yield from page.commits

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchRepositoryHistoryAsyncPager:
    """A pager for iterating through ``fetch_repository_history`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.FetchRepositoryHistoryResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``commits`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchRepositoryHistory`` requests and continue to iterate
    through the ``commits`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.FetchRepositoryHistoryResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.FetchRepositoryHistoryResponse]],
        request: dataform.FetchRepositoryHistoryRequest,
        response: dataform.FetchRepositoryHistoryResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.FetchRepositoryHistoryRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.FetchRepositoryHistoryResponse):
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
        self._request = dataform.FetchRepositoryHistoryRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.FetchRepositoryHistoryResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.CommitLogEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.commits:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkspacesPager:
    """A pager for iterating through ``list_workspaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListWorkspacesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workspaces`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkspaces`` requests and continue to iterate
    through the ``workspaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListWorkspacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.ListWorkspacesResponse],
        request: dataform.ListWorkspacesRequest,
        response: dataform.ListWorkspacesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListWorkspacesRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListWorkspacesResponse):
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
        self._request = dataform.ListWorkspacesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.ListWorkspacesResponse]:
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

    def __iter__(self) -> Iterator[dataform.Workspace]:
        for page in self.pages:
            yield from page.workspaces

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkspacesAsyncPager:
    """A pager for iterating through ``list_workspaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListWorkspacesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workspaces`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkspaces`` requests and continue to iterate
    through the ``workspaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListWorkspacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.ListWorkspacesResponse]],
        request: dataform.ListWorkspacesRequest,
        response: dataform.ListWorkspacesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListWorkspacesRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListWorkspacesResponse):
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
        self._request = dataform.ListWorkspacesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.ListWorkspacesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.Workspace]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workspaces:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryDirectoryContentsPager:
    """A pager for iterating through ``query_directory_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryDirectoryContentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``directory_entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryDirectoryContents`` requests and continue to iterate
    through the ``directory_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryDirectoryContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.QueryDirectoryContentsResponse],
        request: dataform.QueryDirectoryContentsRequest,
        response: dataform.QueryDirectoryContentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryDirectoryContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryDirectoryContentsResponse):
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
        self._request = dataform.QueryDirectoryContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.QueryDirectoryContentsResponse]:
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

    def __iter__(self) -> Iterator[dataform.DirectoryEntry]:
        for page in self.pages:
            yield from page.directory_entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryDirectoryContentsAsyncPager:
    """A pager for iterating through ``query_directory_contents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryDirectoryContentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``directory_entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryDirectoryContents`` requests and continue to iterate
    through the ``directory_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryDirectoryContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.QueryDirectoryContentsResponse]],
        request: dataform.QueryDirectoryContentsRequest,
        response: dataform.QueryDirectoryContentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryDirectoryContentsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryDirectoryContentsResponse):
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
        self._request = dataform.QueryDirectoryContentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.QueryDirectoryContentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.DirectoryEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.directory_entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchFilesPager:
    """A pager for iterating through ``search_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.SearchFilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchFiles`` requests and continue to iterate
    through the ``search_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.SearchFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.SearchFilesResponse],
        request: dataform.SearchFilesRequest,
        response: dataform.SearchFilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.SearchFilesRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.SearchFilesResponse):
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
        self._request = dataform.SearchFilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.SearchFilesResponse]:
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

    def __iter__(self) -> Iterator[dataform.SearchResult]:
        for page in self.pages:
            yield from page.search_results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchFilesAsyncPager:
    """A pager for iterating through ``search_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.SearchFilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchFiles`` requests and continue to iterate
    through the ``search_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.SearchFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.SearchFilesResponse]],
        request: dataform.SearchFilesRequest,
        response: dataform.SearchFilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.SearchFilesRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.SearchFilesResponse):
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
        self._request = dataform.SearchFilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.SearchFilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.SearchResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.search_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleaseConfigsPager:
    """A pager for iterating through ``list_release_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListReleaseConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``release_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReleaseConfigs`` requests and continue to iterate
    through the ``release_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListReleaseConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.ListReleaseConfigsResponse],
        request: dataform.ListReleaseConfigsRequest,
        response: dataform.ListReleaseConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListReleaseConfigsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListReleaseConfigsResponse):
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
        self._request = dataform.ListReleaseConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.ListReleaseConfigsResponse]:
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

    def __iter__(self) -> Iterator[dataform.ReleaseConfig]:
        for page in self.pages:
            yield from page.release_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleaseConfigsAsyncPager:
    """A pager for iterating through ``list_release_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListReleaseConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``release_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReleaseConfigs`` requests and continue to iterate
    through the ``release_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListReleaseConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.ListReleaseConfigsResponse]],
        request: dataform.ListReleaseConfigsRequest,
        response: dataform.ListReleaseConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListReleaseConfigsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListReleaseConfigsResponse):
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
        self._request = dataform.ListReleaseConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.ListReleaseConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.ReleaseConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.release_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCompilationResultsPager:
    """A pager for iterating through ``list_compilation_results`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListCompilationResultsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``compilation_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCompilationResults`` requests and continue to iterate
    through the ``compilation_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListCompilationResultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.ListCompilationResultsResponse],
        request: dataform.ListCompilationResultsRequest,
        response: dataform.ListCompilationResultsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListCompilationResultsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListCompilationResultsResponse):
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
        self._request = dataform.ListCompilationResultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.ListCompilationResultsResponse]:
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

    def __iter__(self) -> Iterator[dataform.CompilationResult]:
        for page in self.pages:
            yield from page.compilation_results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCompilationResultsAsyncPager:
    """A pager for iterating through ``list_compilation_results`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListCompilationResultsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``compilation_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCompilationResults`` requests and continue to iterate
    through the ``compilation_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListCompilationResultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.ListCompilationResultsResponse]],
        request: dataform.ListCompilationResultsRequest,
        response: dataform.ListCompilationResultsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListCompilationResultsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListCompilationResultsResponse):
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
        self._request = dataform.ListCompilationResultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.ListCompilationResultsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.CompilationResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.compilation_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryCompilationResultActionsPager:
    """A pager for iterating through ``query_compilation_result_actions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryCompilationResultActionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``compilation_result_actions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryCompilationResultActions`` requests and continue to iterate
    through the ``compilation_result_actions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryCompilationResultActionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.QueryCompilationResultActionsResponse],
        request: dataform.QueryCompilationResultActionsRequest,
        response: dataform.QueryCompilationResultActionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryCompilationResultActionsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryCompilationResultActionsResponse):
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
        self._request = dataform.QueryCompilationResultActionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.QueryCompilationResultActionsResponse]:
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

    def __iter__(self) -> Iterator[dataform.CompilationResultAction]:
        for page in self.pages:
            yield from page.compilation_result_actions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryCompilationResultActionsAsyncPager:
    """A pager for iterating through ``query_compilation_result_actions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryCompilationResultActionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``compilation_result_actions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryCompilationResultActions`` requests and continue to iterate
    through the ``compilation_result_actions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryCompilationResultActionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[dataform.QueryCompilationResultActionsResponse]
        ],
        request: dataform.QueryCompilationResultActionsRequest,
        response: dataform.QueryCompilationResultActionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryCompilationResultActionsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryCompilationResultActionsResponse):
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
        self._request = dataform.QueryCompilationResultActionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[dataform.QueryCompilationResultActionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.CompilationResultAction]:
        async def async_generator():
            async for page in self.pages:
                for response in page.compilation_result_actions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkflowConfigsPager:
    """A pager for iterating through ``list_workflow_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListWorkflowConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workflow_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkflowConfigs`` requests and continue to iterate
    through the ``workflow_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListWorkflowConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.ListWorkflowConfigsResponse],
        request: dataform.ListWorkflowConfigsRequest,
        response: dataform.ListWorkflowConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListWorkflowConfigsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListWorkflowConfigsResponse):
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
        self._request = dataform.ListWorkflowConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.ListWorkflowConfigsResponse]:
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

    def __iter__(self) -> Iterator[dataform.WorkflowConfig]:
        for page in self.pages:
            yield from page.workflow_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkflowConfigsAsyncPager:
    """A pager for iterating through ``list_workflow_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListWorkflowConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workflow_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkflowConfigs`` requests and continue to iterate
    through the ``workflow_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListWorkflowConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.ListWorkflowConfigsResponse]],
        request: dataform.ListWorkflowConfigsRequest,
        response: dataform.ListWorkflowConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListWorkflowConfigsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListWorkflowConfigsResponse):
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
        self._request = dataform.ListWorkflowConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.ListWorkflowConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.WorkflowConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workflow_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkflowInvocationsPager:
    """A pager for iterating through ``list_workflow_invocations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListWorkflowInvocationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workflow_invocations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkflowInvocations`` requests and continue to iterate
    through the ``workflow_invocations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListWorkflowInvocationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.ListWorkflowInvocationsResponse],
        request: dataform.ListWorkflowInvocationsRequest,
        response: dataform.ListWorkflowInvocationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListWorkflowInvocationsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListWorkflowInvocationsResponse):
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
        self._request = dataform.ListWorkflowInvocationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.ListWorkflowInvocationsResponse]:
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

    def __iter__(self) -> Iterator[dataform.WorkflowInvocation]:
        for page in self.pages:
            yield from page.workflow_invocations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkflowInvocationsAsyncPager:
    """A pager for iterating through ``list_workflow_invocations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.ListWorkflowInvocationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workflow_invocations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkflowInvocations`` requests and continue to iterate
    through the ``workflow_invocations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.ListWorkflowInvocationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dataform.ListWorkflowInvocationsResponse]],
        request: dataform.ListWorkflowInvocationsRequest,
        response: dataform.ListWorkflowInvocationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.ListWorkflowInvocationsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.ListWorkflowInvocationsResponse):
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
        self._request = dataform.ListWorkflowInvocationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dataform.ListWorkflowInvocationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.WorkflowInvocation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workflow_invocations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryWorkflowInvocationActionsPager:
    """A pager for iterating through ``query_workflow_invocation_actions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workflow_invocation_actions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``QueryWorkflowInvocationActions`` requests and continue to iterate
    through the ``workflow_invocation_actions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dataform.QueryWorkflowInvocationActionsResponse],
        request: dataform.QueryWorkflowInvocationActionsRequest,
        response: dataform.QueryWorkflowInvocationActionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsResponse):
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
        self._request = dataform.QueryWorkflowInvocationActionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dataform.QueryWorkflowInvocationActionsResponse]:
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

    def __iter__(self) -> Iterator[dataform.WorkflowInvocationAction]:
        for page in self.pages:
            yield from page.workflow_invocation_actions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class QueryWorkflowInvocationActionsAsyncPager:
    """A pager for iterating through ``query_workflow_invocation_actions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workflow_invocation_actions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``QueryWorkflowInvocationActions`` requests and continue to iterate
    through the ``workflow_invocation_actions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[dataform.QueryWorkflowInvocationActionsResponse]
        ],
        request: dataform.QueryWorkflowInvocationActionsRequest,
        response: dataform.QueryWorkflowInvocationActionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsRequest):
                The initial request object.
            response (google.cloud.dataform_v1.types.QueryWorkflowInvocationActionsResponse):
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
        self._request = dataform.QueryWorkflowInvocationActionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[dataform.QueryWorkflowInvocationActionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataform.WorkflowInvocationAction]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workflow_invocation_actions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
