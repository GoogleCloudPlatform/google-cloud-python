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

from google.cloud.gke_backup_v1.types import (
    backup,
    backup_channel,
    backup_plan,
    backup_plan_binding,
    gkebackup,
    restore,
    restore_channel,
    restore_plan,
    restore_plan_binding,
    volume,
)


class ListBackupPlansPager:
    """A pager for iterating through ``list_backup_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListBackupPlansResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_plans`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupPlans`` requests and continue to iterate
    through the ``backup_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupPlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListBackupPlansResponse],
        request: gkebackup.ListBackupPlansRequest,
        response: gkebackup.ListBackupPlansResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupPlansRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupPlansResponse):
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
        self._request = gkebackup.ListBackupPlansRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListBackupPlansResponse]:
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

    def __iter__(self) -> Iterator[backup_plan.BackupPlan]:
        for page in self.pages:
            yield from page.backup_plans

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlansAsyncPager:
    """A pager for iterating through ``list_backup_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListBackupPlansResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_plans`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupPlans`` requests and continue to iterate
    through the ``backup_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupPlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListBackupPlansResponse]],
        request: gkebackup.ListBackupPlansRequest,
        response: gkebackup.ListBackupPlansResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupPlansRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupPlansResponse):
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
        self._request = gkebackup.ListBackupPlansRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListBackupPlansResponse]:
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

    def __aiter__(self) -> AsyncIterator[backup_plan.BackupPlan]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_plans:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupChannelsPager:
    """A pager for iterating through ``list_backup_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListBackupChannelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_channels`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupChannels`` requests and continue to iterate
    through the ``backup_channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListBackupChannelsResponse],
        request: gkebackup.ListBackupChannelsRequest,
        response: gkebackup.ListBackupChannelsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupChannelsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupChannelsResponse):
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
        self._request = gkebackup.ListBackupChannelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListBackupChannelsResponse]:
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

    def __iter__(self) -> Iterator[backup_channel.BackupChannel]:
        for page in self.pages:
            yield from page.backup_channels

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupChannelsAsyncPager:
    """A pager for iterating through ``list_backup_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListBackupChannelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_channels`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupChannels`` requests and continue to iterate
    through the ``backup_channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListBackupChannelsResponse]],
        request: gkebackup.ListBackupChannelsRequest,
        response: gkebackup.ListBackupChannelsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupChannelsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupChannelsResponse):
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
        self._request = gkebackup.ListBackupChannelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListBackupChannelsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backup_channel.BackupChannel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_channels:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlanBindingsPager:
    """A pager for iterating through ``list_backup_plan_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListBackupPlanBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_plan_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupPlanBindings`` requests and continue to iterate
    through the ``backup_plan_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupPlanBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListBackupPlanBindingsResponse],
        request: gkebackup.ListBackupPlanBindingsRequest,
        response: gkebackup.ListBackupPlanBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupPlanBindingsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupPlanBindingsResponse):
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
        self._request = gkebackup.ListBackupPlanBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListBackupPlanBindingsResponse]:
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

    def __iter__(self) -> Iterator[backup_plan_binding.BackupPlanBinding]:
        for page in self.pages:
            yield from page.backup_plan_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupPlanBindingsAsyncPager:
    """A pager for iterating through ``list_backup_plan_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListBackupPlanBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_plan_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupPlanBindings`` requests and continue to iterate
    through the ``backup_plan_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupPlanBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListBackupPlanBindingsResponse]],
        request: gkebackup.ListBackupPlanBindingsRequest,
        response: gkebackup.ListBackupPlanBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupPlanBindingsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupPlanBindingsResponse):
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
        self._request = gkebackup.ListBackupPlanBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListBackupPlanBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[backup_plan_binding.BackupPlanBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_plan_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupsPager:
    """A pager for iterating through ``list_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListBackupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListBackupsResponse],
        request: gkebackup.ListBackupsRequest,
        response: gkebackup.ListBackupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupsResponse):
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
        self._request = gkebackup.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListBackupsResponse]:
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
    :class:`google.cloud.gke_backup_v1.types.ListBackupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListBackupsResponse]],
        request: gkebackup.ListBackupsRequest,
        response: gkebackup.ListBackupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListBackupsResponse):
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
        self._request = gkebackup.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListBackupsResponse]:
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


class ListVolumeBackupsPager:
    """A pager for iterating through ``list_volume_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListVolumeBackupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``volume_backups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVolumeBackups`` requests and continue to iterate
    through the ``volume_backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListVolumeBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListVolumeBackupsResponse],
        request: gkebackup.ListVolumeBackupsRequest,
        response: gkebackup.ListVolumeBackupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListVolumeBackupsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListVolumeBackupsResponse):
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
        self._request = gkebackup.ListVolumeBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListVolumeBackupsResponse]:
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

    def __iter__(self) -> Iterator[volume.VolumeBackup]:
        for page in self.pages:
            yield from page.volume_backups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumeBackupsAsyncPager:
    """A pager for iterating through ``list_volume_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListVolumeBackupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``volume_backups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVolumeBackups`` requests and continue to iterate
    through the ``volume_backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListVolumeBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListVolumeBackupsResponse]],
        request: gkebackup.ListVolumeBackupsRequest,
        response: gkebackup.ListVolumeBackupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListVolumeBackupsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListVolumeBackupsResponse):
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
        self._request = gkebackup.ListVolumeBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListVolumeBackupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[volume.VolumeBackup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.volume_backups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestorePlansPager:
    """A pager for iterating through ``list_restore_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestorePlansResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restore_plans`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestorePlans`` requests and continue to iterate
    through the ``restore_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestorePlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListRestorePlansResponse],
        request: gkebackup.ListRestorePlansRequest,
        response: gkebackup.ListRestorePlansResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestorePlansRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestorePlansResponse):
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
        self._request = gkebackup.ListRestorePlansRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListRestorePlansResponse]:
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

    def __iter__(self) -> Iterator[restore_plan.RestorePlan]:
        for page in self.pages:
            yield from page.restore_plans

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestorePlansAsyncPager:
    """A pager for iterating through ``list_restore_plans`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestorePlansResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restore_plans`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestorePlans`` requests and continue to iterate
    through the ``restore_plans`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestorePlansResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListRestorePlansResponse]],
        request: gkebackup.ListRestorePlansRequest,
        response: gkebackup.ListRestorePlansResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestorePlansRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestorePlansResponse):
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
        self._request = gkebackup.ListRestorePlansRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListRestorePlansResponse]:
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

    def __aiter__(self) -> AsyncIterator[restore_plan.RestorePlan]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restore_plans:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreChannelsPager:
    """A pager for iterating through ``list_restore_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestoreChannelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restore_channels`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestoreChannels`` requests and continue to iterate
    through the ``restore_channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestoreChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListRestoreChannelsResponse],
        request: gkebackup.ListRestoreChannelsRequest,
        response: gkebackup.ListRestoreChannelsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestoreChannelsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestoreChannelsResponse):
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
        self._request = gkebackup.ListRestoreChannelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListRestoreChannelsResponse]:
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

    def __iter__(self) -> Iterator[restore_channel.RestoreChannel]:
        for page in self.pages:
            yield from page.restore_channels

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoreChannelsAsyncPager:
    """A pager for iterating through ``list_restore_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestoreChannelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restore_channels`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestoreChannels`` requests and continue to iterate
    through the ``restore_channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestoreChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListRestoreChannelsResponse]],
        request: gkebackup.ListRestoreChannelsRequest,
        response: gkebackup.ListRestoreChannelsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestoreChannelsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestoreChannelsResponse):
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
        self._request = gkebackup.ListRestoreChannelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListRestoreChannelsResponse]:
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

    def __aiter__(self) -> AsyncIterator[restore_channel.RestoreChannel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restore_channels:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestorePlanBindingsPager:
    """A pager for iterating through ``list_restore_plan_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestorePlanBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restore_plan_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestorePlanBindings`` requests and continue to iterate
    through the ``restore_plan_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestorePlanBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListRestorePlanBindingsResponse],
        request: gkebackup.ListRestorePlanBindingsRequest,
        response: gkebackup.ListRestorePlanBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestorePlanBindingsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestorePlanBindingsResponse):
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
        self._request = gkebackup.ListRestorePlanBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListRestorePlanBindingsResponse]:
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

    def __iter__(self) -> Iterator[restore_plan_binding.RestorePlanBinding]:
        for page in self.pages:
            yield from page.restore_plan_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestorePlanBindingsAsyncPager:
    """A pager for iterating through ``list_restore_plan_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestorePlanBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restore_plan_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestorePlanBindings`` requests and continue to iterate
    through the ``restore_plan_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestorePlanBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListRestorePlanBindingsResponse]],
        request: gkebackup.ListRestorePlanBindingsRequest,
        response: gkebackup.ListRestorePlanBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestorePlanBindingsRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestorePlanBindingsResponse):
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
        self._request = gkebackup.ListRestorePlanBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListRestorePlanBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[restore_plan_binding.RestorePlanBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restore_plan_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoresPager:
    """A pager for iterating through ``list_restores`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestoresResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``restores`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRestores`` requests and continue to iterate
    through the ``restores`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestoresResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListRestoresResponse],
        request: gkebackup.ListRestoresRequest,
        response: gkebackup.ListRestoresResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestoresRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestoresResponse):
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
        self._request = gkebackup.ListRestoresRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListRestoresResponse]:
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

    def __iter__(self) -> Iterator[restore.Restore]:
        for page in self.pages:
            yield from page.restores

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRestoresAsyncPager:
    """A pager for iterating through ``list_restores`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListRestoresResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``restores`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRestores`` requests and continue to iterate
    through the ``restores`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListRestoresResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListRestoresResponse]],
        request: gkebackup.ListRestoresRequest,
        response: gkebackup.ListRestoresResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListRestoresRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListRestoresResponse):
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
        self._request = gkebackup.ListRestoresRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListRestoresResponse]:
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

    def __aiter__(self) -> AsyncIterator[restore.Restore]:
        async def async_generator():
            async for page in self.pages:
                for response in page.restores:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumeRestoresPager:
    """A pager for iterating through ``list_volume_restores`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListVolumeRestoresResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``volume_restores`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVolumeRestores`` requests and continue to iterate
    through the ``volume_restores`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListVolumeRestoresResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkebackup.ListVolumeRestoresResponse],
        request: gkebackup.ListVolumeRestoresRequest,
        response: gkebackup.ListVolumeRestoresResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListVolumeRestoresRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListVolumeRestoresResponse):
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
        self._request = gkebackup.ListVolumeRestoresRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkebackup.ListVolumeRestoresResponse]:
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

    def __iter__(self) -> Iterator[volume.VolumeRestore]:
        for page in self.pages:
            yield from page.volume_restores

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumeRestoresAsyncPager:
    """A pager for iterating through ``list_volume_restores`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_backup_v1.types.ListVolumeRestoresResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``volume_restores`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVolumeRestores`` requests and continue to iterate
    through the ``volume_restores`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_backup_v1.types.ListVolumeRestoresResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkebackup.ListVolumeRestoresResponse]],
        request: gkebackup.ListVolumeRestoresRequest,
        response: gkebackup.ListVolumeRestoresResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_backup_v1.types.ListVolumeRestoresRequest):
                The initial request object.
            response (google.cloud.gke_backup_v1.types.ListVolumeRestoresResponse):
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
        self._request = gkebackup.ListVolumeRestoresRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkebackup.ListVolumeRestoresResponse]:
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

    def __aiter__(self) -> AsyncIterator[volume.VolumeRestore]:
        async def async_generator():
            async for page in self.pages:
                for response in page.volume_restores:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
