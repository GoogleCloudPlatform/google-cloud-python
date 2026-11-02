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

from google.cloud.managedkafka_v1.types import managed_kafka_connect, resources


class ListConnectClustersPager:
    """A pager for iterating through ``list_connect_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.managedkafka_v1.types.ListConnectClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connect_clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnectClusters`` requests and continue to iterate
    through the ``connect_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.managedkafka_v1.types.ListConnectClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., managed_kafka_connect.ListConnectClustersResponse],
        request: managed_kafka_connect.ListConnectClustersRequest,
        response: managed_kafka_connect.ListConnectClustersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.managedkafka_v1.types.ListConnectClustersRequest):
                The initial request object.
            response (google.cloud.managedkafka_v1.types.ListConnectClustersResponse):
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
        self._request = managed_kafka_connect.ListConnectClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[managed_kafka_connect.ListConnectClustersResponse]:
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

    def __iter__(self) -> Iterator[resources.ConnectCluster]:
        for page in self.pages:
            yield from page.connect_clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectClustersAsyncPager:
    """A pager for iterating through ``list_connect_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.managedkafka_v1.types.ListConnectClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connect_clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnectClusters`` requests and continue to iterate
    through the ``connect_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.managedkafka_v1.types.ListConnectClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[managed_kafka_connect.ListConnectClustersResponse]
        ],
        request: managed_kafka_connect.ListConnectClustersRequest,
        response: managed_kafka_connect.ListConnectClustersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.managedkafka_v1.types.ListConnectClustersRequest):
                The initial request object.
            response (google.cloud.managedkafka_v1.types.ListConnectClustersResponse):
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
        self._request = managed_kafka_connect.ListConnectClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[managed_kafka_connect.ListConnectClustersResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.ConnectCluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connect_clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectorsPager:
    """A pager for iterating through ``list_connectors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.managedkafka_v1.types.ListConnectorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connectors`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnectors`` requests and continue to iterate
    through the ``connectors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.managedkafka_v1.types.ListConnectorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., managed_kafka_connect.ListConnectorsResponse],
        request: managed_kafka_connect.ListConnectorsRequest,
        response: managed_kafka_connect.ListConnectorsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.managedkafka_v1.types.ListConnectorsRequest):
                The initial request object.
            response (google.cloud.managedkafka_v1.types.ListConnectorsResponse):
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
        self._request = managed_kafka_connect.ListConnectorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[managed_kafka_connect.ListConnectorsResponse]:
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

    def __iter__(self) -> Iterator[resources.Connector]:
        for page in self.pages:
            yield from page.connectors

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectorsAsyncPager:
    """A pager for iterating through ``list_connectors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.managedkafka_v1.types.ListConnectorsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connectors`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnectors`` requests and continue to iterate
    through the ``connectors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.managedkafka_v1.types.ListConnectorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[managed_kafka_connect.ListConnectorsResponse]],
        request: managed_kafka_connect.ListConnectorsRequest,
        response: managed_kafka_connect.ListConnectorsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.managedkafka_v1.types.ListConnectorsRequest):
                The initial request object.
            response (google.cloud.managedkafka_v1.types.ListConnectorsResponse):
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
        self._request = managed_kafka_connect.ListConnectorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[managed_kafka_connect.ListConnectorsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Connector]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connectors:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
