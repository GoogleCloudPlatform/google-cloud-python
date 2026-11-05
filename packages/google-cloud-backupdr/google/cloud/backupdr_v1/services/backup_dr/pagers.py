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

from google.cloud.backupdr_v1.types import (
    appliedautoprotectionpolicy,
    autoprotectionpolicy,
    autoprotectionpolicybinding,
    backupdr,
    backupplan,
    backupplanassociation,
    backupvault,
    bindingmatchingresource,
    datasourcereference,
    restore_template,
    restore_template_execution,
    restore_verification_plan,
    restore_verification_plan_association,
)


class ListManagementServersPager:
    """A pager for iterating through ``list_management_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListManagementServersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``management_servers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListManagementServers`` requests and continue to iterate
    through the ``management_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListManagementServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupdr.ListManagementServersResponse],
        request: backupdr.ListManagementServersRequest,
        response: backupdr.ListManagementServersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListManagementServersRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListManagementServersResponse):
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
        self._request = backupdr.ListManagementServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupdr.ListManagementServersResponse]:
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

    def __iter__(self) -> Iterator[backupdr.ManagementServer]:
        for page in self.pages:
            yield from page.management_servers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListManagementServersAsyncPager:
    """A pager for iterating through ``list_management_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListManagementServersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``management_servers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListManagementServers`` requests and continue to iterate
    through the ``management_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListManagementServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backupdr.ListManagementServersResponse]],
        request: backupdr.ListManagementServersRequest,
        response: backupdr.ListManagementServersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListManagementServersRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListManagementServersResponse):
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
        self._request = backupdr.ListManagementServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backupdr.ListManagementServersResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupdr.ManagementServer]:
        async def async_generator():
            async for page in self.pages:
                for response in page.management_servers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupVaultsPager:
    """A pager for iterating through ``list_backup_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupVaultsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_vaults`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupVaults`` requests and continue to iterate
    through the ``backup_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupvault.ListBackupVaultsResponse],
        request: backupvault.ListBackupVaultsRequest,
        response: backupvault.ListBackupVaultsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupVaultsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupVaultsResponse):
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
        self._request = backupvault.ListBackupVaultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupvault.ListBackupVaultsResponse]:
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

    def __iter__(self) -> Iterator[backupvault.BackupVault]:
        for page in self.pages:
            yield from page.backup_vaults

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupVaultsAsyncPager:
    """A pager for iterating through ``list_backup_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupVaultsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_vaults`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupVaults`` requests and continue to iterate
    through the ``backup_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backupvault.ListBackupVaultsResponse]],
        request: backupvault.ListBackupVaultsRequest,
        response: backupvault.ListBackupVaultsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupVaultsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupVaultsResponse):
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
        self._request = backupvault.ListBackupVaultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backupvault.ListBackupVaultsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupvault.BackupVault]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_vaults:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchUsableBackupVaultsPager:
    """A pager for iterating through ``fetch_usable_backup_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_vaults`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchUsableBackupVaults`` requests and continue to iterate
    through the ``backup_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupvault.FetchUsableBackupVaultsResponse],
        request: backupvault.FetchUsableBackupVaultsRequest,
        response: backupvault.FetchUsableBackupVaultsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse):
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
        self._request = backupvault.FetchUsableBackupVaultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupvault.FetchUsableBackupVaultsResponse]:
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

    def __iter__(self) -> Iterator[backupvault.BackupVault]:
        for page in self.pages:
            yield from page.backup_vaults

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchUsableBackupVaultsAsyncPager:
    """A pager for iterating through ``fetch_usable_backup_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_vaults`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchUsableBackupVaults`` requests and continue to iterate
    through the ``backup_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backupvault.FetchUsableBackupVaultsResponse]],
        request: backupvault.FetchUsableBackupVaultsRequest,
        response: backupvault.FetchUsableBackupVaultsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse):
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
        self._request = backupvault.FetchUsableBackupVaultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backupvault.FetchUsableBackupVaultsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupvault.BackupVault]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_vaults:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataSourcesPager:
    """A pager for iterating through ``list_data_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListDataSourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_sources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataSources`` requests and continue to iterate
    through the ``data_sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListDataSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupvault.ListDataSourcesResponse],
        request: backupvault.ListDataSourcesRequest,
        response: backupvault.ListDataSourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListDataSourcesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListDataSourcesResponse):
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
        self._request = backupvault.ListDataSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupvault.ListDataSourcesResponse]:
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

    def __iter__(self) -> Iterator[backupvault.DataSource]:
        for page in self.pages:
            yield from page.data_sources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataSourcesAsyncPager:
    """A pager for iterating through ``list_data_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListDataSourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_sources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataSources`` requests and continue to iterate
    through the ``data_sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListDataSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backupvault.ListDataSourcesResponse]],
        request: backupvault.ListDataSourcesRequest,
        response: backupvault.ListDataSourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListDataSourcesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListDataSourcesResponse):
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
        self._request = backupvault.ListDataSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backupvault.ListDataSourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupvault.DataSource]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_sources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupsPager:
    """A pager for iterating through ``list_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupvault.ListBackupsResponse],
        request: backupvault.ListBackupsRequest,
        response: backupvault.ListBackupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupsResponse):
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
        self._request = backupvault.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupvault.ListBackupsResponse]:
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

    def __iter__(self) -> Iterator[backupvault.Backup]:
        for page in self.pages:
            yield from page.backups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupsAsyncPager:
    """A pager for iterating through ``list_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backupvault.ListBackupsResponse]],
        request: backupvault.ListBackupsRequest,
        response: backupvault.ListBackupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupsResponse):
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
        self._request = backupvault.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backupvault.ListBackupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupvault.Backup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchBackupsForResourceTypePager:
    """A pager for iterating through ``fetch_backups_for_resource_type`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchBackupsForResourceType`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupvault.FetchBackupsForResourceTypeResponse],
        request: backupvault.FetchBackupsForResourceTypeRequest,
        response: backupvault.FetchBackupsForResourceTypeResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse):
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
        self._request = backupvault.FetchBackupsForResourceTypeRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupvault.FetchBackupsForResourceTypeResponse]:
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

    def __iter__(self) -> Iterator[backupvault.Backup]:
        for page in self.pages:
            yield from page.backups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchBackupsForResourceTypeAsyncPager:
    """A pager for iterating through ``fetch_backups_for_resource_type`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchBackupsForResourceType`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[backupvault.FetchBackupsForResourceTypeResponse]
        ],
        request: backupvault.FetchBackupsForResourceTypeRequest,
        response: backupvault.FetchBackupsForResourceTypeResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse):
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
        self._request = backupvault.FetchBackupsForResourceTypeRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[backupvault.FetchBackupsForResourceTypeResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupvault.Backup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlansPager:
    """A pager for iterating through ``list_backup_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupPlansResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_plans`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupPlans`` requests and continue to iterate
    through the ``backup_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupPlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupplan.ListBackupPlansResponse],
        request: backupplan.ListBackupPlansRequest,
        response: backupplan.ListBackupPlansResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupPlansRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupPlansResponse):
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
        self._request = backupplan.ListBackupPlansRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupplan.ListBackupPlansResponse]:
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

    def __iter__(self) -> Iterator[backupplan.BackupPlan]:
        for page in self.pages:
            yield from page.backup_plans

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlansAsyncPager:
    """A pager for iterating through ``list_backup_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupPlansResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_plans`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupPlans`` requests and continue to iterate
    through the ``backup_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupPlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backupplan.ListBackupPlansResponse]],
        request: backupplan.ListBackupPlansRequest,
        response: backupplan.ListBackupPlansResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupPlansRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupPlansResponse):
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
        self._request = backupplan.ListBackupPlansRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backupplan.ListBackupPlansResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupplan.BackupPlan]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_plans:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlanRevisionsPager:
    """A pager for iterating through ``list_backup_plan_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_plan_revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupPlanRevisions`` requests and continue to iterate
    through the ``backup_plan_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupplan.ListBackupPlanRevisionsResponse],
        request: backupplan.ListBackupPlanRevisionsRequest,
        response: backupplan.ListBackupPlanRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse):
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
        self._request = backupplan.ListBackupPlanRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[backupplan.ListBackupPlanRevisionsResponse]:
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

    def __iter__(self) -> Iterator[backupplan.BackupPlanRevision]:
        for page in self.pages:
            yield from page.backup_plan_revisions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlanRevisionsAsyncPager:
    """A pager for iterating through ``list_backup_plan_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_plan_revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupPlanRevisions`` requests and continue to iterate
    through the ``backup_plan_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[backupplan.ListBackupPlanRevisionsResponse]],
        request: backupplan.ListBackupPlanRevisionsRequest,
        response: backupplan.ListBackupPlanRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse):
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
        self._request = backupplan.ListBackupPlanRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[backupplan.ListBackupPlanRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupplan.BackupPlanRevision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_plan_revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlanAssociationsPager:
    """A pager for iterating through ``list_backup_plan_associations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_plan_associations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupPlanAssociations`` requests and continue to iterate
    through the ``backup_plan_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., backupplanassociation.ListBackupPlanAssociationsResponse],
        request: backupplanassociation.ListBackupPlanAssociationsRequest,
        response: backupplanassociation.ListBackupPlanAssociationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse):
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
        self._request = backupplanassociation.ListBackupPlanAssociationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[backupplanassociation.ListBackupPlanAssociationsResponse]:
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

    def __iter__(self) -> Iterator[backupplanassociation.BackupPlanAssociation]:
        for page in self.pages:
            yield from page.backup_plan_associations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlanAssociationsAsyncPager:
    """A pager for iterating through ``list_backup_plan_associations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_plan_associations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupPlanAssociations`` requests and continue to iterate
    through the ``backup_plan_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[backupplanassociation.ListBackupPlanAssociationsResponse]
        ],
        request: backupplanassociation.ListBackupPlanAssociationsRequest,
        response: backupplanassociation.ListBackupPlanAssociationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse):
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
        self._request = backupplanassociation.ListBackupPlanAssociationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[backupplanassociation.ListBackupPlanAssociationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backupplanassociation.BackupPlanAssociation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_plan_associations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchBackupPlanAssociationsForResourceTypePager:
    """A pager for iterating through ``fetch_backup_plan_associations_for_resource_type`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_plan_associations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchBackupPlanAssociationsForResourceType`` requests and continue to iterate
    through the ``backup_plan_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        ],
        request: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse):
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
        self._request = (
            backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest(
                request
            )
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[
        backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse
    ]:
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

    def __iter__(self) -> Iterator[backupplanassociation.BackupPlanAssociation]:
        for page in self.pages:
            yield from page.backup_plan_associations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchBackupPlanAssociationsForResourceTypeAsyncPager:
    """A pager for iterating through ``fetch_backup_plan_associations_for_resource_type`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_plan_associations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchBackupPlanAssociationsForResourceType`` requests and continue to iterate
    through the ``backup_plan_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse
            ],
        ],
        request: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse):
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
        self._request = (
            backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest(
                request
            )
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse
    ]:
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

    def __aiter__(self) -> AsyncIterator[backupplanassociation.BackupPlanAssociation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_plan_associations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataSourceReferencesPager:
    """A pager for iterating through ``list_data_source_references`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_source_references`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataSourceReferences`` requests and continue to iterate
    through the ``data_source_references`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datasourcereference.ListDataSourceReferencesResponse],
        request: datasourcereference.ListDataSourceReferencesRequest,
        response: datasourcereference.ListDataSourceReferencesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse):
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
        self._request = datasourcereference.ListDataSourceReferencesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[datasourcereference.ListDataSourceReferencesResponse]:
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

    def __iter__(self) -> Iterator[datasourcereference.DataSourceReference]:
        for page in self.pages:
            yield from page.data_source_references

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataSourceReferencesAsyncPager:
    """A pager for iterating through ``list_data_source_references`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_source_references`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataSourceReferences`` requests and continue to iterate
    through the ``data_source_references`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[datasourcereference.ListDataSourceReferencesResponse]
        ],
        request: datasourcereference.ListDataSourceReferencesRequest,
        response: datasourcereference.ListDataSourceReferencesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse):
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
        self._request = datasourcereference.ListDataSourceReferencesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[datasourcereference.ListDataSourceReferencesResponse]:
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

    def __aiter__(self) -> AsyncIterator[datasourcereference.DataSourceReference]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_source_references:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchDataSourceReferencesForResourceTypePager:
    """A pager for iterating through ``fetch_data_source_references_for_resource_type`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_source_references`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchDataSourceReferencesForResourceType`` requests and continue to iterate
    through the ``data_source_references`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., datasourcereference.FetchDataSourceReferencesForResourceTypeResponse
        ],
        request: datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse):
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
        self._request = (
            datasourcereference.FetchDataSourceReferencesForResourceTypeRequest(request)
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[datasourcereference.FetchDataSourceReferencesForResourceTypeResponse]:
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

    def __iter__(self) -> Iterator[datasourcereference.DataSourceReference]:
        for page in self.pages:
            yield from page.data_source_references

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchDataSourceReferencesForResourceTypeAsyncPager:
    """A pager for iterating through ``fetch_data_source_references_for_resource_type`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_source_references`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchDataSourceReferencesForResourceType`` requests and continue to iterate
    through the ``data_source_references`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                datasourcereference.FetchDataSourceReferencesForResourceTypeResponse
            ],
        ],
        request: datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse):
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
        self._request = (
            datasourcereference.FetchDataSourceReferencesForResourceTypeRequest(request)
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        datasourcereference.FetchDataSourceReferencesForResourceTypeResponse
    ]:
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

    def __aiter__(self) -> AsyncIterator[datasourcereference.DataSourceReference]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_source_references:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutoProtectionPoliciesPager:
    """A pager for iterating through ``list_auto_protection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``auto_protection_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutoProtectionPolicies`` requests and continue to iterate
    through the ``auto_protection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., autoprotectionpolicy.ListAutoProtectionPoliciesResponse],
        request: autoprotectionpolicy.ListAutoProtectionPoliciesRequest,
        response: autoprotectionpolicy.ListAutoProtectionPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesResponse):
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
        self._request = autoprotectionpolicy.ListAutoProtectionPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[autoprotectionpolicy.ListAutoProtectionPoliciesResponse]:
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

    def __iter__(self) -> Iterator[autoprotectionpolicy.AutoProtectionPolicy]:
        for page in self.pages:
            yield from page.auto_protection_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutoProtectionPoliciesAsyncPager:
    """A pager for iterating through ``list_auto_protection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``auto_protection_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutoProtectionPolicies`` requests and continue to iterate
    through the ``auto_protection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[autoprotectionpolicy.ListAutoProtectionPoliciesResponse]
        ],
        request: autoprotectionpolicy.ListAutoProtectionPoliciesRequest,
        response: autoprotectionpolicy.ListAutoProtectionPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListAutoProtectionPoliciesResponse):
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
        self._request = autoprotectionpolicy.ListAutoProtectionPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[autoprotectionpolicy.ListAutoProtectionPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[autoprotectionpolicy.AutoProtectionPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.auto_protection_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutoProtectionPolicyBindingsPager:
    """A pager for iterating through ``list_auto_protection_policy_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``auto_protection_policy_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutoProtectionPolicyBindings`` requests and continue to iterate
    through the ``auto_protection_policy_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse
        ],
        request: autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest,
        response: autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsResponse):
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
        self._request = (
            autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest(request)
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse]:
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
    ) -> Iterator[autoprotectionpolicybinding.AutoProtectionPolicyBinding]:
        for page in self.pages:
            yield from page.auto_protection_policy_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutoProtectionPolicyBindingsAsyncPager:
    """A pager for iterating through ``list_auto_protection_policy_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``auto_protection_policy_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutoProtectionPolicyBindings`` requests and continue to iterate
    through the ``auto_protection_policy_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse
            ],
        ],
        request: autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest,
        response: autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListAutoProtectionPolicyBindingsResponse):
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
        self._request = (
            autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest(request)
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse
    ]:
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
    ) -> AsyncIterator[autoprotectionpolicybinding.AutoProtectionPolicyBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.auto_protection_policy_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAppliedAutoProtectionPoliciesPager:
    """A pager for iterating through ``list_applied_auto_protection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``applied_auto_protection_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAppliedAutoProtectionPolicies`` requests and continue to iterate
    through the ``applied_auto_protection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse
        ],
        request: appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
        response: appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesResponse):
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
        self._request = (
            appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest(
                request
            )
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[
        appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse
    ]:
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
    ) -> Iterator[appliedautoprotectionpolicy.AppliedAutoProtectionPolicy]:
        for page in self.pages:
            yield from page.applied_auto_protection_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAppliedAutoProtectionPoliciesAsyncPager:
    """A pager for iterating through ``list_applied_auto_protection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``applied_auto_protection_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAppliedAutoProtectionPolicies`` requests and continue to iterate
    through the ``applied_auto_protection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse
            ],
        ],
        request: appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
        response: appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListAppliedAutoProtectionPoliciesResponse):
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
        self._request = (
            appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest(
                request
            )
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse
    ]:
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
    ) -> AsyncIterator[appliedautoprotectionpolicy.AppliedAutoProtectionPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.applied_auto_protection_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBindingMatchingResourcesPager:
    """A pager for iterating through ``list_binding_matching_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBindingMatchingResourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``matching_resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBindingMatchingResources`` requests and continue to iterate
    through the ``matching_resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBindingMatchingResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., bindingmatchingresource.ListBindingMatchingResourcesResponse
        ],
        request: bindingmatchingresource.ListBindingMatchingResourcesRequest,
        response: bindingmatchingresource.ListBindingMatchingResourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBindingMatchingResourcesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBindingMatchingResourcesResponse):
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
        self._request = bindingmatchingresource.ListBindingMatchingResourcesRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[bindingmatchingresource.ListBindingMatchingResourcesResponse]:
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

    def __iter__(self) -> Iterator[bindingmatchingresource.BindingMatchingResource]:
        for page in self.pages:
            yield from page.matching_resources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBindingMatchingResourcesAsyncPager:
    """A pager for iterating through ``list_binding_matching_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListBindingMatchingResourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``matching_resources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBindingMatchingResources`` requests and continue to iterate
    through the ``matching_resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListBindingMatchingResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[bindingmatchingresource.ListBindingMatchingResourcesResponse]
        ],
        request: bindingmatchingresource.ListBindingMatchingResourcesRequest,
        response: bindingmatchingresource.ListBindingMatchingResourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListBindingMatchingResourcesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListBindingMatchingResourcesResponse):
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
        self._request = bindingmatchingresource.ListBindingMatchingResourcesRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[bindingmatchingresource.ListBindingMatchingResourcesResponse]:
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
    ) -> AsyncIterator[bindingmatchingresource.BindingMatchingResource]:
        async def async_generator():
            async for page in self.pages:
                for response in page.matching_resources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreTemplatesPager:
    """A pager for iterating through ``list_restore_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreTemplatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restore_templates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestoreTemplates`` requests and continue to iterate
    through the ``restore_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., restore_template.ListRestoreTemplatesResponse],
        request: restore_template.ListRestoreTemplatesRequest,
        response: restore_template.ListRestoreTemplatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreTemplatesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreTemplatesResponse):
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
        self._request = restore_template.ListRestoreTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[restore_template.ListRestoreTemplatesResponse]:
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

    def __iter__(self) -> Iterator[restore_template.RestoreTemplate]:
        for page in self.pages:
            yield from page.restore_templates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreTemplatesAsyncPager:
    """A pager for iterating through ``list_restore_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreTemplatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restore_templates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestoreTemplates`` requests and continue to iterate
    through the ``restore_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[restore_template.ListRestoreTemplatesResponse]],
        request: restore_template.ListRestoreTemplatesRequest,
        response: restore_template.ListRestoreTemplatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreTemplatesRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreTemplatesResponse):
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
        self._request = restore_template.ListRestoreTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[restore_template.ListRestoreTemplatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[restore_template.RestoreTemplate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restore_templates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreTemplateExecutionsPager:
    """A pager for iterating through ``list_restore_template_executions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restore_template_executions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestoreTemplateExecutions`` requests and continue to iterate
    through the ``restore_template_executions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., restore_template_execution.ListRestoreTemplateExecutionsResponse
        ],
        request: restore_template_execution.ListRestoreTemplateExecutionsRequest,
        response: restore_template_execution.ListRestoreTemplateExecutionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsResponse):
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
        self._request = restore_template_execution.ListRestoreTemplateExecutionsRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[restore_template_execution.ListRestoreTemplateExecutionsResponse]:
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

    def __iter__(self) -> Iterator[restore_template_execution.RestoreTemplateExecution]:
        for page in self.pages:
            yield from page.restore_template_executions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreTemplateExecutionsAsyncPager:
    """A pager for iterating through ``list_restore_template_executions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restore_template_executions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestoreTemplateExecutions`` requests and continue to iterate
    through the ``restore_template_executions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[restore_template_execution.ListRestoreTemplateExecutionsResponse],
        ],
        request: restore_template_execution.ListRestoreTemplateExecutionsRequest,
        response: restore_template_execution.ListRestoreTemplateExecutionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreTemplateExecutionsResponse):
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
        self._request = restore_template_execution.ListRestoreTemplateExecutionsRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        restore_template_execution.ListRestoreTemplateExecutionsResponse
    ]:
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
    ) -> AsyncIterator[restore_template_execution.RestoreTemplateExecution]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restore_template_executions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreVerificationPlanAssociationsPager:
    """A pager for iterating through ``list_restore_verification_plan_associations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restore_verification_plan_associations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestoreVerificationPlanAssociations`` requests and continue to iterate
    through the ``restore_verification_plan_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            restore_verification_plan_association.ListRestoreVerificationPlanAssociationsResponse,
        ],
        request: restore_verification_plan_association.ListRestoreVerificationPlanAssociationsRequest,
        response: restore_verification_plan_association.ListRestoreVerificationPlanAssociationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsResponse):
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
        self._request = restore_verification_plan_association.ListRestoreVerificationPlanAssociationsRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[
        restore_verification_plan_association.ListRestoreVerificationPlanAssociationsResponse
    ]:
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
    ) -> Iterator[
        restore_verification_plan_association.RestoreVerificationPlanAssociation
    ]:
        for page in self.pages:
            yield from page.restore_verification_plan_associations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreVerificationPlanAssociationsAsyncPager:
    """A pager for iterating through ``list_restore_verification_plan_associations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restore_verification_plan_associations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestoreVerificationPlanAssociations`` requests and continue to iterate
    through the ``restore_verification_plan_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                restore_verification_plan_association.ListRestoreVerificationPlanAssociationsResponse
            ],
        ],
        request: restore_verification_plan_association.ListRestoreVerificationPlanAssociationsRequest,
        response: restore_verification_plan_association.ListRestoreVerificationPlanAssociationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreVerificationPlanAssociationsResponse):
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
        self._request = restore_verification_plan_association.ListRestoreVerificationPlanAssociationsRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[
        restore_verification_plan_association.ListRestoreVerificationPlanAssociationsResponse
    ]:
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
        restore_verification_plan_association.RestoreVerificationPlanAssociation
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restore_verification_plan_associations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreVerificationPlansPager:
    """A pager for iterating through ``list_restore_verification_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlansResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restore_verification_plans`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestoreVerificationPlans`` requests and continue to iterate
    through the ``restore_verification_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., restore_verification_plan.ListRestoreVerificationPlansResponse
        ],
        request: restore_verification_plan.ListRestoreVerificationPlansRequest,
        response: restore_verification_plan.ListRestoreVerificationPlansResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreVerificationPlansRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreVerificationPlansResponse):
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
        self._request = restore_verification_plan.ListRestoreVerificationPlansRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[restore_verification_plan.ListRestoreVerificationPlansResponse]:
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

    def __iter__(self) -> Iterator[restore_verification_plan.RestoreVerificationPlan]:
        for page in self.pages:
            yield from page.restore_verification_plans

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreVerificationPlansAsyncPager:
    """A pager for iterating through ``list_restore_verification_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlansResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restore_verification_plans`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestoreVerificationPlans`` requests and continue to iterate
    through the ``restore_verification_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.backupdr_v1.types.ListRestoreVerificationPlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[restore_verification_plan.ListRestoreVerificationPlansResponse],
        ],
        request: restore_verification_plan.ListRestoreVerificationPlansRequest,
        response: restore_verification_plan.ListRestoreVerificationPlansResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.backupdr_v1.types.ListRestoreVerificationPlansRequest):
                The initial request object.
            response (google.cloud.backupdr_v1.types.ListRestoreVerificationPlansResponse):
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
        self._request = restore_verification_plan.ListRestoreVerificationPlansRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[restore_verification_plan.ListRestoreVerificationPlansResponse]:
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
    ) -> AsyncIterator[restore_verification_plan.RestoreVerificationPlan]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restore_verification_plans:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
