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

from google.cloud.vmmigration_v1.types import vmmigration


class ListSourcesPager:
    """A pager for iterating through ``list_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListSourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``sources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSources`` requests and continue to iterate
    through the ``sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListSourcesResponse],
        request: vmmigration.ListSourcesRequest,
        response: vmmigration.ListSourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListSourcesRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListSourcesResponse):
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
        self._request = vmmigration.ListSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListSourcesResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.Source]:
        for page in self.pages:
            yield from page.sources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSourcesAsyncPager:
    """A pager for iterating through ``list_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListSourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``sources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSources`` requests and continue to iterate
    through the ``sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListSourcesResponse]],
        request: vmmigration.ListSourcesRequest,
        response: vmmigration.ListSourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListSourcesRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListSourcesResponse):
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
        self._request = vmmigration.ListSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListSourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.Source]:
        async def async_generator():
            async for page in self.pages:
                for response in page.sources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStorageInventoryPager:
    """A pager for iterating through ``fetch_storage_inventory`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.FetchStorageInventoryResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchStorageInventory`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.FetchStorageInventoryResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.FetchStorageInventoryResponse],
        request: vmmigration.FetchStorageInventoryRequest,
        response: vmmigration.FetchStorageInventoryResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.FetchStorageInventoryRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.FetchStorageInventoryResponse):
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
        self._request = vmmigration.FetchStorageInventoryRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.FetchStorageInventoryResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.SourceStorageResource]:
        for page in self.pages:
            yield from page.resources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStorageInventoryAsyncPager:
    """A pager for iterating through ``fetch_storage_inventory`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.FetchStorageInventoryResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchStorageInventory`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.FetchStorageInventoryResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.FetchStorageInventoryResponse]],
        request: vmmigration.FetchStorageInventoryRequest,
        response: vmmigration.FetchStorageInventoryResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.FetchStorageInventoryRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.FetchStorageInventoryResponse):
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
        self._request = vmmigration.FetchStorageInventoryRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.FetchStorageInventoryResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.SourceStorageResource]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUtilizationReportsPager:
    """A pager for iterating through ``list_utilization_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListUtilizationReportsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``utilization_reports`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUtilizationReports`` requests and continue to iterate
    through the ``utilization_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListUtilizationReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListUtilizationReportsResponse],
        request: vmmigration.ListUtilizationReportsRequest,
        response: vmmigration.ListUtilizationReportsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListUtilizationReportsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListUtilizationReportsResponse):
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
        self._request = vmmigration.ListUtilizationReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListUtilizationReportsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.UtilizationReport]:
        for page in self.pages:
            yield from page.utilization_reports

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUtilizationReportsAsyncPager:
    """A pager for iterating through ``list_utilization_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListUtilizationReportsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``utilization_reports`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUtilizationReports`` requests and continue to iterate
    through the ``utilization_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListUtilizationReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListUtilizationReportsResponse]],
        request: vmmigration.ListUtilizationReportsRequest,
        response: vmmigration.ListUtilizationReportsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListUtilizationReportsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListUtilizationReportsResponse):
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
        self._request = vmmigration.ListUtilizationReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListUtilizationReportsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.UtilizationReport]:
        async def async_generator():
            async for page in self.pages:
                for response in page.utilization_reports:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatacenterConnectorsPager:
    """A pager for iterating through ``list_datacenter_connectors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListDatacenterConnectorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``datacenter_connectors`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDatacenterConnectors`` requests and continue to iterate
    through the ``datacenter_connectors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListDatacenterConnectorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListDatacenterConnectorsResponse],
        request: vmmigration.ListDatacenterConnectorsRequest,
        response: vmmigration.ListDatacenterConnectorsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListDatacenterConnectorsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListDatacenterConnectorsResponse):
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
        self._request = vmmigration.ListDatacenterConnectorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListDatacenterConnectorsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.DatacenterConnector]:
        for page in self.pages:
            yield from page.datacenter_connectors

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatacenterConnectorsAsyncPager:
    """A pager for iterating through ``list_datacenter_connectors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListDatacenterConnectorsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``datacenter_connectors`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDatacenterConnectors`` requests and continue to iterate
    through the ``datacenter_connectors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListDatacenterConnectorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListDatacenterConnectorsResponse]],
        request: vmmigration.ListDatacenterConnectorsRequest,
        response: vmmigration.ListDatacenterConnectorsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListDatacenterConnectorsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListDatacenterConnectorsResponse):
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
        self._request = vmmigration.ListDatacenterConnectorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[vmmigration.ListDatacenterConnectorsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.DatacenterConnector]:
        async def async_generator():
            async for page in self.pages:
                for response in page.datacenter_connectors:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMigratingVmsPager:
    """A pager for iterating through ``list_migrating_vms`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListMigratingVmsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``migrating_vms`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMigratingVms`` requests and continue to iterate
    through the ``migrating_vms`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListMigratingVmsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListMigratingVmsResponse],
        request: vmmigration.ListMigratingVmsRequest,
        response: vmmigration.ListMigratingVmsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListMigratingVmsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListMigratingVmsResponse):
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
        self._request = vmmigration.ListMigratingVmsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListMigratingVmsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.MigratingVm]:
        for page in self.pages:
            yield from page.migrating_vms

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMigratingVmsAsyncPager:
    """A pager for iterating through ``list_migrating_vms`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListMigratingVmsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``migrating_vms`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMigratingVms`` requests and continue to iterate
    through the ``migrating_vms`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListMigratingVmsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListMigratingVmsResponse]],
        request: vmmigration.ListMigratingVmsRequest,
        response: vmmigration.ListMigratingVmsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListMigratingVmsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListMigratingVmsResponse):
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
        self._request = vmmigration.ListMigratingVmsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListMigratingVmsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.MigratingVm]:
        async def async_generator():
            async for page in self.pages:
                for response in page.migrating_vms:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCloneJobsPager:
    """A pager for iterating through ``list_clone_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListCloneJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``clone_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCloneJobs`` requests and continue to iterate
    through the ``clone_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListCloneJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListCloneJobsResponse],
        request: vmmigration.ListCloneJobsRequest,
        response: vmmigration.ListCloneJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListCloneJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListCloneJobsResponse):
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
        self._request = vmmigration.ListCloneJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListCloneJobsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.CloneJob]:
        for page in self.pages:
            yield from page.clone_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCloneJobsAsyncPager:
    """A pager for iterating through ``list_clone_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListCloneJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``clone_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCloneJobs`` requests and continue to iterate
    through the ``clone_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListCloneJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListCloneJobsResponse]],
        request: vmmigration.ListCloneJobsRequest,
        response: vmmigration.ListCloneJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListCloneJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListCloneJobsResponse):
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
        self._request = vmmigration.ListCloneJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListCloneJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.CloneJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.clone_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCutoverJobsPager:
    """A pager for iterating through ``list_cutover_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListCutoverJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``cutover_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCutoverJobs`` requests and continue to iterate
    through the ``cutover_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListCutoverJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListCutoverJobsResponse],
        request: vmmigration.ListCutoverJobsRequest,
        response: vmmigration.ListCutoverJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListCutoverJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListCutoverJobsResponse):
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
        self._request = vmmigration.ListCutoverJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListCutoverJobsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.CutoverJob]:
        for page in self.pages:
            yield from page.cutover_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCutoverJobsAsyncPager:
    """A pager for iterating through ``list_cutover_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListCutoverJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``cutover_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCutoverJobs`` requests and continue to iterate
    through the ``cutover_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListCutoverJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListCutoverJobsResponse]],
        request: vmmigration.ListCutoverJobsRequest,
        response: vmmigration.ListCutoverJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListCutoverJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListCutoverJobsResponse):
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
        self._request = vmmigration.ListCutoverJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListCutoverJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.CutoverJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.cutover_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGroupsPager:
    """A pager for iterating through ``list_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGroups`` requests and continue to iterate
    through the ``groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListGroupsResponse],
        request: vmmigration.ListGroupsRequest,
        response: vmmigration.ListGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListGroupsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListGroupsResponse):
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
        self._request = vmmigration.ListGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListGroupsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.Group]:
        for page in self.pages:
            yield from page.groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGroupsAsyncPager:
    """A pager for iterating through ``list_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGroups`` requests and continue to iterate
    through the ``groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListGroupsResponse]],
        request: vmmigration.ListGroupsRequest,
        response: vmmigration.ListGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListGroupsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListGroupsResponse):
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
        self._request = vmmigration.ListGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.Group]:
        async def async_generator():
            async for page in self.pages:
                for response in page.groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTargetProjectsPager:
    """A pager for iterating through ``list_target_projects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListTargetProjectsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``target_projects`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTargetProjects`` requests and continue to iterate
    through the ``target_projects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListTargetProjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListTargetProjectsResponse],
        request: vmmigration.ListTargetProjectsRequest,
        response: vmmigration.ListTargetProjectsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListTargetProjectsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListTargetProjectsResponse):
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
        self._request = vmmigration.ListTargetProjectsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListTargetProjectsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.TargetProject]:
        for page in self.pages:
            yield from page.target_projects

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTargetProjectsAsyncPager:
    """A pager for iterating through ``list_target_projects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListTargetProjectsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``target_projects`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTargetProjects`` requests and continue to iterate
    through the ``target_projects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListTargetProjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListTargetProjectsResponse]],
        request: vmmigration.ListTargetProjectsRequest,
        response: vmmigration.ListTargetProjectsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListTargetProjectsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListTargetProjectsResponse):
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
        self._request = vmmigration.ListTargetProjectsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListTargetProjectsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.TargetProject]:
        async def async_generator():
            async for page in self.pages:
                for response in page.target_projects:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReplicationCyclesPager:
    """A pager for iterating through ``list_replication_cycles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListReplicationCyclesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``replication_cycles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReplicationCycles`` requests and continue to iterate
    through the ``replication_cycles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListReplicationCyclesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListReplicationCyclesResponse],
        request: vmmigration.ListReplicationCyclesRequest,
        response: vmmigration.ListReplicationCyclesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListReplicationCyclesRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListReplicationCyclesResponse):
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
        self._request = vmmigration.ListReplicationCyclesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListReplicationCyclesResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.ReplicationCycle]:
        for page in self.pages:
            yield from page.replication_cycles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReplicationCyclesAsyncPager:
    """A pager for iterating through ``list_replication_cycles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListReplicationCyclesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``replication_cycles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReplicationCycles`` requests and continue to iterate
    through the ``replication_cycles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListReplicationCyclesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListReplicationCyclesResponse]],
        request: vmmigration.ListReplicationCyclesRequest,
        response: vmmigration.ListReplicationCyclesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListReplicationCyclesRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListReplicationCyclesResponse):
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
        self._request = vmmigration.ListReplicationCyclesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListReplicationCyclesResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.ReplicationCycle]:
        async def async_generator():
            async for page in self.pages:
                for response in page.replication_cycles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImageImportsPager:
    """A pager for iterating through ``list_image_imports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListImageImportsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``image_imports`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListImageImports`` requests and continue to iterate
    through the ``image_imports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListImageImportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListImageImportsResponse],
        request: vmmigration.ListImageImportsRequest,
        response: vmmigration.ListImageImportsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListImageImportsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListImageImportsResponse):
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
        self._request = vmmigration.ListImageImportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListImageImportsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.ImageImport]:
        for page in self.pages:
            yield from page.image_imports

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImageImportsAsyncPager:
    """A pager for iterating through ``list_image_imports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListImageImportsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``image_imports`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListImageImports`` requests and continue to iterate
    through the ``image_imports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListImageImportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListImageImportsResponse]],
        request: vmmigration.ListImageImportsRequest,
        response: vmmigration.ListImageImportsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListImageImportsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListImageImportsResponse):
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
        self._request = vmmigration.ListImageImportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListImageImportsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.ImageImport]:
        async def async_generator():
            async for page in self.pages:
                for response in page.image_imports:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImageImportJobsPager:
    """A pager for iterating through ``list_image_import_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListImageImportJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``image_import_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListImageImportJobs`` requests and continue to iterate
    through the ``image_import_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListImageImportJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListImageImportJobsResponse],
        request: vmmigration.ListImageImportJobsRequest,
        response: vmmigration.ListImageImportJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListImageImportJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListImageImportJobsResponse):
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
        self._request = vmmigration.ListImageImportJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListImageImportJobsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.ImageImportJob]:
        for page in self.pages:
            yield from page.image_import_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImageImportJobsAsyncPager:
    """A pager for iterating through ``list_image_import_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListImageImportJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``image_import_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListImageImportJobs`` requests and continue to iterate
    through the ``image_import_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListImageImportJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListImageImportJobsResponse]],
        request: vmmigration.ListImageImportJobsRequest,
        response: vmmigration.ListImageImportJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListImageImportJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListImageImportJobsResponse):
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
        self._request = vmmigration.ListImageImportJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListImageImportJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.ImageImportJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.image_import_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDiskMigrationJobsPager:
    """A pager for iterating through ``list_disk_migration_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListDiskMigrationJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``disk_migration_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDiskMigrationJobs`` requests and continue to iterate
    through the ``disk_migration_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListDiskMigrationJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vmmigration.ListDiskMigrationJobsResponse],
        request: vmmigration.ListDiskMigrationJobsRequest,
        response: vmmigration.ListDiskMigrationJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListDiskMigrationJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListDiskMigrationJobsResponse):
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
        self._request = vmmigration.ListDiskMigrationJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vmmigration.ListDiskMigrationJobsResponse]:
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

    def __iter__(self) -> Iterator[vmmigration.DiskMigrationJob]:
        for page in self.pages:
            yield from page.disk_migration_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDiskMigrationJobsAsyncPager:
    """A pager for iterating through ``list_disk_migration_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.vmmigration_v1.types.ListDiskMigrationJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``disk_migration_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDiskMigrationJobs`` requests and continue to iterate
    through the ``disk_migration_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.vmmigration_v1.types.ListDiskMigrationJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[vmmigration.ListDiskMigrationJobsResponse]],
        request: vmmigration.ListDiskMigrationJobsRequest,
        response: vmmigration.ListDiskMigrationJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.vmmigration_v1.types.ListDiskMigrationJobsRequest):
                The initial request object.
            response (google.cloud.vmmigration_v1.types.ListDiskMigrationJobsResponse):
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
        self._request = vmmigration.ListDiskMigrationJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[vmmigration.ListDiskMigrationJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vmmigration.DiskMigrationJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.disk_migration_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
