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

from google.cloud.netapp_v1.types import (
    active_directory,
    backup,
    backup_policy,
    backup_vault,
    host_group,
    kms,
    quota_rule,
    replication,
    snapshot,
    storage_pool,
    volume,
)


class ListStoragePoolsPager:
    """A pager for iterating through ``list_storage_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``storage_pools`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStoragePools`` requests and continue to iterate
    through the ``storage_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., storage_pool.ListStoragePoolsResponse],
        request: storage_pool.ListStoragePoolsRequest,
        response: storage_pool.ListStoragePoolsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListStoragePoolsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListStoragePoolsResponse):
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
        self._request = storage_pool.ListStoragePoolsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[storage_pool.ListStoragePoolsResponse]:
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

    def __iter__(self) -> Iterator[storage_pool.StoragePool]:
        for page in self.pages:
            yield from page.storage_pools

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStoragePoolsAsyncPager:
    """A pager for iterating through ``list_storage_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``storage_pools`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStoragePools`` requests and continue to iterate
    through the ``storage_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListStoragePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[storage_pool.ListStoragePoolsResponse]],
        request: storage_pool.ListStoragePoolsRequest,
        response: storage_pool.ListStoragePoolsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListStoragePoolsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListStoragePoolsResponse):
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
        self._request = storage_pool.ListStoragePoolsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[storage_pool.ListStoragePoolsResponse]:
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

    def __aiter__(self) -> AsyncIterator[storage_pool.StoragePool]:
        async def async_generator():
            async for page in self.pages:
                for response in page.storage_pools:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumesPager:
    """A pager for iterating through ``list_volumes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListVolumesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``volumes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVolumes`` requests and continue to iterate
    through the ``volumes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListVolumesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., volume.ListVolumesResponse],
        request: volume.ListVolumesRequest,
        response: volume.ListVolumesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListVolumesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListVolumesResponse):
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
        self._request = volume.ListVolumesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[volume.ListVolumesResponse]:
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

    def __iter__(self) -> Iterator[volume.Volume]:
        for page in self.pages:
            yield from page.volumes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumesAsyncPager:
    """A pager for iterating through ``list_volumes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListVolumesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``volumes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVolumes`` requests and continue to iterate
    through the ``volumes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListVolumesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[volume.ListVolumesResponse]],
        request: volume.ListVolumesRequest,
        response: volume.ListVolumesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListVolumesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListVolumesResponse):
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
        self._request = volume.ListVolumesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[volume.ListVolumesResponse]:
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

    def __aiter__(self) -> AsyncIterator[volume.Volume]:
        async def async_generator():
            async for page in self.pages:
                for response in page.volumes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSnapshotsPager:
    """A pager for iterating through ``list_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``snapshots`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSnapshots`` requests and continue to iterate
    through the ``snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., snapshot.ListSnapshotsResponse],
        request: snapshot.ListSnapshotsRequest,
        response: snapshot.ListSnapshotsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListSnapshotsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListSnapshotsResponse):
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
        self._request = snapshot.ListSnapshotsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[snapshot.ListSnapshotsResponse]:
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

    def __iter__(self) -> Iterator[snapshot.Snapshot]:
        for page in self.pages:
            yield from page.snapshots

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSnapshotsAsyncPager:
    """A pager for iterating through ``list_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``snapshots`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSnapshots`` requests and continue to iterate
    through the ``snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[snapshot.ListSnapshotsResponse]],
        request: snapshot.ListSnapshotsRequest,
        response: snapshot.ListSnapshotsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListSnapshotsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListSnapshotsResponse):
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
        self._request = snapshot.ListSnapshotsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[snapshot.ListSnapshotsResponse]:
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

    def __aiter__(self) -> AsyncIterator[snapshot.Snapshot]:
        async def async_generator():
            async for page in self.pages:
                for response in page.snapshots:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListActiveDirectoriesPager:
    """A pager for iterating through ``list_active_directories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``active_directories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListActiveDirectories`` requests and continue to iterate
    through the ``active_directories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., active_directory.ListActiveDirectoriesResponse],
        request: active_directory.ListActiveDirectoriesRequest,
        response: active_directory.ListActiveDirectoriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListActiveDirectoriesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListActiveDirectoriesResponse):
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
        self._request = active_directory.ListActiveDirectoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[active_directory.ListActiveDirectoriesResponse]:
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

    def __iter__(self) -> Iterator[active_directory.ActiveDirectory]:
        for page in self.pages:
            yield from page.active_directories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListActiveDirectoriesAsyncPager:
    """A pager for iterating through ``list_active_directories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``active_directories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListActiveDirectories`` requests and continue to iterate
    through the ``active_directories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListActiveDirectoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[active_directory.ListActiveDirectoriesResponse]
        ],
        request: active_directory.ListActiveDirectoriesRequest,
        response: active_directory.ListActiveDirectoriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListActiveDirectoriesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListActiveDirectoriesResponse):
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
        self._request = active_directory.ListActiveDirectoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[active_directory.ListActiveDirectoriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[active_directory.ActiveDirectory]:
        async def async_generator():
            async for page in self.pages:
                for response in page.active_directories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKmsConfigsPager:
    """A pager for iterating through ``list_kms_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``kms_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListKmsConfigs`` requests and continue to iterate
    through the ``kms_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., kms.ListKmsConfigsResponse],
        request: kms.ListKmsConfigsRequest,
        response: kms.ListKmsConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListKmsConfigsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListKmsConfigsResponse):
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
        self._request = kms.ListKmsConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[kms.ListKmsConfigsResponse]:
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

    def __iter__(self) -> Iterator[kms.KmsConfig]:
        for page in self.pages:
            yield from page.kms_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKmsConfigsAsyncPager:
    """A pager for iterating through ``list_kms_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``kms_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListKmsConfigs`` requests and continue to iterate
    through the ``kms_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListKmsConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[kms.ListKmsConfigsResponse]],
        request: kms.ListKmsConfigsRequest,
        response: kms.ListKmsConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListKmsConfigsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListKmsConfigsResponse):
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
        self._request = kms.ListKmsConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[kms.ListKmsConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[kms.KmsConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.kms_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReplicationsPager:
    """A pager for iterating through ``list_replications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListReplicationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``replications`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReplications`` requests and continue to iterate
    through the ``replications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListReplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., replication.ListReplicationsResponse],
        request: replication.ListReplicationsRequest,
        response: replication.ListReplicationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListReplicationsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListReplicationsResponse):
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
        self._request = replication.ListReplicationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[replication.ListReplicationsResponse]:
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

    def __iter__(self) -> Iterator[replication.Replication]:
        for page in self.pages:
            yield from page.replications

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReplicationsAsyncPager:
    """A pager for iterating through ``list_replications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListReplicationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``replications`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReplications`` requests and continue to iterate
    through the ``replications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListReplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[replication.ListReplicationsResponse]],
        request: replication.ListReplicationsRequest,
        response: replication.ListReplicationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListReplicationsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListReplicationsResponse):
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
        self._request = replication.ListReplicationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[replication.ListReplicationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[replication.Replication]:
        async def async_generator():
            async for page in self.pages:
                for response in page.replications:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupVaultsPager:
    """A pager for iterating through ``list_backup_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupVaultsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_vaults`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupVaults`` requests and continue to iterate
    through the ``backup_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backup_vault.ListBackupVaultsResponse],
        request: backup_vault.ListBackupVaultsRequest,
        response: backup_vault.ListBackupVaultsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupVaultsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupVaultsResponse):
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
        self._request = backup_vault.ListBackupVaultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backup_vault.ListBackupVaultsResponse]:
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

    def __iter__(self) -> Iterator[backup_vault.BackupVault]:
        for page in self.pages:
            yield from page.backup_vaults

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupVaultsAsyncPager:
    """A pager for iterating through ``list_backup_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupVaultsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_vaults`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupVaults`` requests and continue to iterate
    through the ``backup_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backup_vault.ListBackupVaultsResponse]],
        request: backup_vault.ListBackupVaultsRequest,
        response: backup_vault.ListBackupVaultsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupVaultsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupVaultsResponse):
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
        self._request = backup_vault.ListBackupVaultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backup_vault.ListBackupVaultsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backup_vault.BackupVault]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_vaults:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupsPager:
    """A pager for iterating through ``list_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backup.ListBackupsResponse],
        request: backup.ListBackupsRequest,
        response: backup.ListBackupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupsResponse):
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
        self._request = backup.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backup.ListBackupsResponse]:
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

    def __iter__(self) -> Iterator[backup.Backup]:
        for page in self.pages:
            yield from page.backups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupsAsyncPager:
    """A pager for iterating through ``list_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backup.ListBackupsResponse]],
        request: backup.ListBackupsRequest,
        response: backup.ListBackupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupsResponse):
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
        self._request = backup.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backup.ListBackupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backup.Backup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPoliciesPager:
    """A pager for iterating through ``list_backup_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupPolicies`` requests and continue to iterate
    through the ``backup_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backup_policy.ListBackupPoliciesResponse],
        request: backup_policy.ListBackupPoliciesRequest,
        response: backup_policy.ListBackupPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupPoliciesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupPoliciesResponse):
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
        self._request = backup_policy.ListBackupPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backup_policy.ListBackupPoliciesResponse]:
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

    def __iter__(self) -> Iterator[backup_policy.BackupPolicy]:
        for page in self.pages:
            yield from page.backup_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPoliciesAsyncPager:
    """A pager for iterating through ``list_backup_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupPolicies`` requests and continue to iterate
    through the ``backup_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backup_policy.ListBackupPoliciesResponse]],
        request: backup_policy.ListBackupPoliciesRequest,
        response: backup_policy.ListBackupPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupPoliciesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupPoliciesResponse):
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
        self._request = backup_policy.ListBackupPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backup_policy.ListBackupPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[backup_policy.BackupPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQuotaRulesPager:
    """A pager for iterating through ``list_quota_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListQuotaRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``quota_rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListQuotaRules`` requests and continue to iterate
    through the ``quota_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListQuotaRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., quota_rule.ListQuotaRulesResponse],
        request: quota_rule.ListQuotaRulesRequest,
        response: quota_rule.ListQuotaRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListQuotaRulesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListQuotaRulesResponse):
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
        self._request = quota_rule.ListQuotaRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[quota_rule.ListQuotaRulesResponse]:
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

    def __iter__(self) -> Iterator[quota_rule.QuotaRule]:
        for page in self.pages:
            yield from page.quota_rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQuotaRulesAsyncPager:
    """A pager for iterating through ``list_quota_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListQuotaRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``quota_rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListQuotaRules`` requests and continue to iterate
    through the ``quota_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListQuotaRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[quota_rule.ListQuotaRulesResponse]],
        request: quota_rule.ListQuotaRulesRequest,
        response: quota_rule.ListQuotaRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListQuotaRulesRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListQuotaRulesResponse):
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
        self._request = quota_rule.ListQuotaRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[quota_rule.ListQuotaRulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[quota_rule.QuotaRule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.quota_rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHostGroupsPager:
    """A pager for iterating through ``list_host_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListHostGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``host_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHostGroups`` requests and continue to iterate
    through the ``host_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListHostGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., host_group.ListHostGroupsResponse],
        request: host_group.ListHostGroupsRequest,
        response: host_group.ListHostGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListHostGroupsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListHostGroupsResponse):
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
        self._request = host_group.ListHostGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[host_group.ListHostGroupsResponse]:
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

    def __iter__(self) -> Iterator[host_group.HostGroup]:
        for page in self.pages:
            yield from page.host_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHostGroupsAsyncPager:
    """A pager for iterating through ``list_host_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListHostGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``host_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHostGroups`` requests and continue to iterate
    through the ``host_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListHostGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[host_group.ListHostGroupsResponse]],
        request: host_group.ListHostGroupsRequest,
        response: host_group.ListHostGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListHostGroupsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListHostGroupsResponse):
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
        self._request = host_group.ListHostGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[host_group.ListHostGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[host_group.HostGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.host_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupConfigsPager:
    """A pager for iterating through ``list_backup_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``volume_backup_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupConfigs`` requests and continue to iterate
    through the ``volume_backup_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., volume.ListBackupConfigsResponse],
        request: volume.ListBackupConfigsRequest,
        response: volume.ListBackupConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupConfigsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupConfigsResponse):
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
        self._request = volume.ListBackupConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[volume.ListBackupConfigsResponse]:
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

    def __iter__(self) -> Iterator[volume.VolumeBackupConfig]:
        for page in self.pages:
            yield from page.volume_backup_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupConfigsAsyncPager:
    """A pager for iterating through ``list_backup_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.netapp_v1.types.ListBackupConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``volume_backup_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupConfigs`` requests and continue to iterate
    through the ``volume_backup_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.netapp_v1.types.ListBackupConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[volume.ListBackupConfigsResponse]],
        request: volume.ListBackupConfigsRequest,
        response: volume.ListBackupConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.netapp_v1.types.ListBackupConfigsRequest):
                The initial request object.
            response (google.cloud.netapp_v1.types.ListBackupConfigsResponse):
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
        self._request = volume.ListBackupConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[volume.ListBackupConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[volume.VolumeBackupConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.volume_backup_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
