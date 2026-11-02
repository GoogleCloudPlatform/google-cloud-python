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

from google.cloud.gke_multicloud_v1.types import azure_resources, azure_service


class ListAzureClientsPager:
    """A pager for iterating through ``list_azure_clients`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAzureClientsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``azure_clients`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAzureClients`` requests and continue to iterate
    through the ``azure_clients`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAzureClientsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., azure_service.ListAzureClientsResponse],
        request: azure_service.ListAzureClientsRequest,
        response: azure_service.ListAzureClientsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAzureClientsRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAzureClientsResponse):
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
        self._request = azure_service.ListAzureClientsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[azure_service.ListAzureClientsResponse]:
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

    def __iter__(self) -> Iterator[azure_resources.AzureClient]:
        for page in self.pages:
            yield from page.azure_clients

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAzureClientsAsyncPager:
    """A pager for iterating through ``list_azure_clients`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAzureClientsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``azure_clients`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAzureClients`` requests and continue to iterate
    through the ``azure_clients`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAzureClientsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[azure_service.ListAzureClientsResponse]],
        request: azure_service.ListAzureClientsRequest,
        response: azure_service.ListAzureClientsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAzureClientsRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAzureClientsResponse):
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
        self._request = azure_service.ListAzureClientsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[azure_service.ListAzureClientsResponse]:
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

    def __aiter__(self) -> AsyncIterator[azure_resources.AzureClient]:
        async def async_generator():
            async for page in self.pages:
                for response in page.azure_clients:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAzureClustersPager:
    """A pager for iterating through ``list_azure_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAzureClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``azure_clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAzureClusters`` requests and continue to iterate
    through the ``azure_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAzureClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., azure_service.ListAzureClustersResponse],
        request: azure_service.ListAzureClustersRequest,
        response: azure_service.ListAzureClustersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAzureClustersRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAzureClustersResponse):
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
        self._request = azure_service.ListAzureClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[azure_service.ListAzureClustersResponse]:
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

    def __iter__(self) -> Iterator[azure_resources.AzureCluster]:
        for page in self.pages:
            yield from page.azure_clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAzureClustersAsyncPager:
    """A pager for iterating through ``list_azure_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAzureClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``azure_clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAzureClusters`` requests and continue to iterate
    through the ``azure_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAzureClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[azure_service.ListAzureClustersResponse]],
        request: azure_service.ListAzureClustersRequest,
        response: azure_service.ListAzureClustersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAzureClustersRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAzureClustersResponse):
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
        self._request = azure_service.ListAzureClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[azure_service.ListAzureClustersResponse]:
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

    def __aiter__(self) -> AsyncIterator[azure_resources.AzureCluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.azure_clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAzureNodePoolsPager:
    """A pager for iterating through ``list_azure_node_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``azure_node_pools`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAzureNodePools`` requests and continue to iterate
    through the ``azure_node_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., azure_service.ListAzureNodePoolsResponse],
        request: azure_service.ListAzureNodePoolsRequest,
        response: azure_service.ListAzureNodePoolsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsResponse):
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
        self._request = azure_service.ListAzureNodePoolsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[azure_service.ListAzureNodePoolsResponse]:
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

    def __iter__(self) -> Iterator[azure_resources.AzureNodePool]:
        for page in self.pages:
            yield from page.azure_node_pools

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAzureNodePoolsAsyncPager:
    """A pager for iterating through ``list_azure_node_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``azure_node_pools`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAzureNodePools`` requests and continue to iterate
    through the ``azure_node_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[azure_service.ListAzureNodePoolsResponse]],
        request: azure_service.ListAzureNodePoolsRequest,
        response: azure_service.ListAzureNodePoolsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsResponse):
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
        self._request = azure_service.ListAzureNodePoolsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[azure_service.ListAzureNodePoolsResponse]:
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

    def __aiter__(self) -> AsyncIterator[azure_resources.AzureNodePool]:
        async def async_generator():
            async for page in self.pages:
                for response in page.azure_node_pools:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
