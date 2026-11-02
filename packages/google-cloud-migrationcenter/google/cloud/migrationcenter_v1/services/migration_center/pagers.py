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

from google.cloud.migrationcenter_v1.types import migrationcenter


class ListAssetsPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListAssetsResponse],
        request: migrationcenter.ListAssetsRequest,
        response: migrationcenter.ListAssetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListAssetsResponse):
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
        self._request = migrationcenter.ListAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListAssetsResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.Asset]:
        for page in self.pages:
            yield from page.assets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAssetsAsyncPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListAssetsResponse]],
        request: migrationcenter.ListAssetsRequest,
        response: migrationcenter.ListAssetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListAssetsResponse):
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
        self._request = migrationcenter.ListAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListAssetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.Asset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImportJobsPager:
    """A pager for iterating through ``list_import_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListImportJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``import_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListImportJobs`` requests and continue to iterate
    through the ``import_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListImportJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListImportJobsResponse],
        request: migrationcenter.ListImportJobsRequest,
        response: migrationcenter.ListImportJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListImportJobsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListImportJobsResponse):
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
        self._request = migrationcenter.ListImportJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListImportJobsResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.ImportJob]:
        for page in self.pages:
            yield from page.import_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImportJobsAsyncPager:
    """A pager for iterating through ``list_import_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListImportJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``import_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListImportJobs`` requests and continue to iterate
    through the ``import_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListImportJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListImportJobsResponse]],
        request: migrationcenter.ListImportJobsRequest,
        response: migrationcenter.ListImportJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListImportJobsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListImportJobsResponse):
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
        self._request = migrationcenter.ListImportJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListImportJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.ImportJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.import_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImportDataFilesPager:
    """A pager for iterating through ``list_import_data_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListImportDataFilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``import_data_files`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListImportDataFiles`` requests and continue to iterate
    through the ``import_data_files`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListImportDataFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListImportDataFilesResponse],
        request: migrationcenter.ListImportDataFilesRequest,
        response: migrationcenter.ListImportDataFilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListImportDataFilesRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListImportDataFilesResponse):
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
        self._request = migrationcenter.ListImportDataFilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListImportDataFilesResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.ImportDataFile]:
        for page in self.pages:
            yield from page.import_data_files

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImportDataFilesAsyncPager:
    """A pager for iterating through ``list_import_data_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListImportDataFilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``import_data_files`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListImportDataFiles`` requests and continue to iterate
    through the ``import_data_files`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListImportDataFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListImportDataFilesResponse]],
        request: migrationcenter.ListImportDataFilesRequest,
        response: migrationcenter.ListImportDataFilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListImportDataFilesRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListImportDataFilesResponse):
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
        self._request = migrationcenter.ListImportDataFilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListImportDataFilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.ImportDataFile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.import_data_files:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGroupsPager:
    """A pager for iterating through ``list_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGroups`` requests and continue to iterate
    through the ``groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListGroupsResponse],
        request: migrationcenter.ListGroupsRequest,
        response: migrationcenter.ListGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListGroupsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListGroupsResponse):
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
        self._request = migrationcenter.ListGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListGroupsResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.Group]:
        for page in self.pages:
            yield from page.groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGroupsAsyncPager:
    """A pager for iterating through ``list_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGroups`` requests and continue to iterate
    through the ``groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListGroupsResponse]],
        request: migrationcenter.ListGroupsRequest,
        response: migrationcenter.ListGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListGroupsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListGroupsResponse):
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
        self._request = migrationcenter.ListGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.Group]:
        async def async_generator():
            async for page in self.pages:
                for response in page.groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListErrorFramesPager:
    """A pager for iterating through ``list_error_frames`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListErrorFramesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``error_frames`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListErrorFrames`` requests and continue to iterate
    through the ``error_frames`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListErrorFramesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListErrorFramesResponse],
        request: migrationcenter.ListErrorFramesRequest,
        response: migrationcenter.ListErrorFramesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListErrorFramesRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListErrorFramesResponse):
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
        self._request = migrationcenter.ListErrorFramesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListErrorFramesResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.ErrorFrame]:
        for page in self.pages:
            yield from page.error_frames

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListErrorFramesAsyncPager:
    """A pager for iterating through ``list_error_frames`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListErrorFramesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``error_frames`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListErrorFrames`` requests and continue to iterate
    through the ``error_frames`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListErrorFramesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListErrorFramesResponse]],
        request: migrationcenter.ListErrorFramesRequest,
        response: migrationcenter.ListErrorFramesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListErrorFramesRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListErrorFramesResponse):
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
        self._request = migrationcenter.ListErrorFramesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListErrorFramesResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.ErrorFrame]:
        async def async_generator():
            async for page in self.pages:
                for response in page.error_frames:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSourcesPager:
    """A pager for iterating through ``list_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListSourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``sources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSources`` requests and continue to iterate
    through the ``sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListSourcesResponse],
        request: migrationcenter.ListSourcesRequest,
        response: migrationcenter.ListSourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListSourcesRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListSourcesResponse):
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
        self._request = migrationcenter.ListSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListSourcesResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.Source]:
        for page in self.pages:
            yield from page.sources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSourcesAsyncPager:
    """A pager for iterating through ``list_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListSourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``sources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSources`` requests and continue to iterate
    through the ``sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListSourcesResponse]],
        request: migrationcenter.ListSourcesRequest,
        response: migrationcenter.ListSourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListSourcesRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListSourcesResponse):
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
        self._request = migrationcenter.ListSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListSourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.Source]:
        async def async_generator():
            async for page in self.pages:
                for response in page.sources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPreferenceSetsPager:
    """A pager for iterating through ``list_preference_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListPreferenceSetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``preference_sets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPreferenceSets`` requests and continue to iterate
    through the ``preference_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListPreferenceSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListPreferenceSetsResponse],
        request: migrationcenter.ListPreferenceSetsRequest,
        response: migrationcenter.ListPreferenceSetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListPreferenceSetsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListPreferenceSetsResponse):
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
        self._request = migrationcenter.ListPreferenceSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListPreferenceSetsResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.PreferenceSet]:
        for page in self.pages:
            yield from page.preference_sets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPreferenceSetsAsyncPager:
    """A pager for iterating through ``list_preference_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListPreferenceSetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``preference_sets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPreferenceSets`` requests and continue to iterate
    through the ``preference_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListPreferenceSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListPreferenceSetsResponse]],
        request: migrationcenter.ListPreferenceSetsRequest,
        response: migrationcenter.ListPreferenceSetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListPreferenceSetsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListPreferenceSetsResponse):
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
        self._request = migrationcenter.ListPreferenceSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListPreferenceSetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.PreferenceSet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.preference_sets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReportConfigsPager:
    """A pager for iterating through ``list_report_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListReportConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``report_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReportConfigs`` requests and continue to iterate
    through the ``report_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListReportConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListReportConfigsResponse],
        request: migrationcenter.ListReportConfigsRequest,
        response: migrationcenter.ListReportConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListReportConfigsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListReportConfigsResponse):
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
        self._request = migrationcenter.ListReportConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListReportConfigsResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.ReportConfig]:
        for page in self.pages:
            yield from page.report_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReportConfigsAsyncPager:
    """A pager for iterating through ``list_report_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListReportConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``report_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReportConfigs`` requests and continue to iterate
    through the ``report_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListReportConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListReportConfigsResponse]],
        request: migrationcenter.ListReportConfigsRequest,
        response: migrationcenter.ListReportConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListReportConfigsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListReportConfigsResponse):
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
        self._request = migrationcenter.ListReportConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListReportConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.ReportConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.report_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReportsPager:
    """A pager for iterating through ``list_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListReportsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``reports`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReports`` requests and continue to iterate
    through the ``reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., migrationcenter.ListReportsResponse],
        request: migrationcenter.ListReportsRequest,
        response: migrationcenter.ListReportsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListReportsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListReportsResponse):
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
        self._request = migrationcenter.ListReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[migrationcenter.ListReportsResponse]:
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

    def __iter__(self) -> Iterator[migrationcenter.Report]:
        for page in self.pages:
            yield from page.reports

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReportsAsyncPager:
    """A pager for iterating through ``list_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.migrationcenter_v1.types.ListReportsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``reports`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReports`` requests and continue to iterate
    through the ``reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.migrationcenter_v1.types.ListReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[migrationcenter.ListReportsResponse]],
        request: migrationcenter.ListReportsRequest,
        response: migrationcenter.ListReportsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.migrationcenter_v1.types.ListReportsRequest):
                The initial request object.
            response (google.cloud.migrationcenter_v1.types.ListReportsResponse):
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
        self._request = migrationcenter.ListReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[migrationcenter.ListReportsResponse]:
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

    def __aiter__(self) -> AsyncIterator[migrationcenter.Report]:
        async def async_generator():
            async for page in self.pages:
                for response in page.reports:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
