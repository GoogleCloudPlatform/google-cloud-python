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

from google.cloud.edgenetwork_v1.types import resources, service


class ListZonesPager:
    """A pager for iterating through ``list_zones`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListZonesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``zones`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListZones`` requests and continue to iterate
    through the ``zones`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListZonesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListZonesResponse],
        request: service.ListZonesRequest,
        response: service.ListZonesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListZonesRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListZonesResponse):
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
        self._request = service.ListZonesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListZonesResponse]:
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

    def __iter__(self) -> Iterator[resources.Zone]:
        for page in self.pages:
            yield from page.zones

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListZonesAsyncPager:
    """A pager for iterating through ``list_zones`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListZonesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``zones`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListZones`` requests and continue to iterate
    through the ``zones`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListZonesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListZonesResponse]],
        request: service.ListZonesRequest,
        response: service.ListZonesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListZonesRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListZonesResponse):
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
        self._request = service.ListZonesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListZonesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Zone]:
        async def async_generator():
            async for page in self.pages:
                for response in page.zones:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNetworksPager:
    """A pager for iterating through ``list_networks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListNetworksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``networks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNetworks`` requests and continue to iterate
    through the ``networks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListNetworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListNetworksResponse],
        request: service.ListNetworksRequest,
        response: service.ListNetworksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListNetworksRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListNetworksResponse):
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
        self._request = service.ListNetworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListNetworksResponse]:
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

    def __iter__(self) -> Iterator[resources.Network]:
        for page in self.pages:
            yield from page.networks

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNetworksAsyncPager:
    """A pager for iterating through ``list_networks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListNetworksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``networks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNetworks`` requests and continue to iterate
    through the ``networks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListNetworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListNetworksResponse]],
        request: service.ListNetworksRequest,
        response: service.ListNetworksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListNetworksRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListNetworksResponse):
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
        self._request = service.ListNetworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListNetworksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Network]:
        async def async_generator():
            async for page in self.pages:
                for response in page.networks:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSubnetsPager:
    """A pager for iterating through ``list_subnets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListSubnetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``subnets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSubnets`` requests and continue to iterate
    through the ``subnets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListSubnetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListSubnetsResponse],
        request: service.ListSubnetsRequest,
        response: service.ListSubnetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListSubnetsRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListSubnetsResponse):
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
        self._request = service.ListSubnetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListSubnetsResponse]:
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

    def __iter__(self) -> Iterator[resources.Subnet]:
        for page in self.pages:
            yield from page.subnets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSubnetsAsyncPager:
    """A pager for iterating through ``list_subnets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListSubnetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``subnets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSubnets`` requests and continue to iterate
    through the ``subnets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListSubnetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListSubnetsResponse]],
        request: service.ListSubnetsRequest,
        response: service.ListSubnetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListSubnetsRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListSubnetsResponse):
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
        self._request = service.ListSubnetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListSubnetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Subnet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.subnets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterconnectsPager:
    """A pager for iterating through ``list_interconnects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListInterconnectsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``interconnects`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInterconnects`` requests and continue to iterate
    through the ``interconnects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListInterconnectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListInterconnectsResponse],
        request: service.ListInterconnectsRequest,
        response: service.ListInterconnectsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListInterconnectsRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListInterconnectsResponse):
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
        self._request = service.ListInterconnectsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListInterconnectsResponse]:
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

    def __iter__(self) -> Iterator[resources.Interconnect]:
        for page in self.pages:
            yield from page.interconnects

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterconnectsAsyncPager:
    """A pager for iterating through ``list_interconnects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListInterconnectsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``interconnects`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInterconnects`` requests and continue to iterate
    through the ``interconnects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListInterconnectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListInterconnectsResponse]],
        request: service.ListInterconnectsRequest,
        response: service.ListInterconnectsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListInterconnectsRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListInterconnectsResponse):
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
        self._request = service.ListInterconnectsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListInterconnectsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Interconnect]:
        async def async_generator():
            async for page in self.pages:
                for response in page.interconnects:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterconnectAttachmentsPager:
    """A pager for iterating through ``list_interconnect_attachments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``interconnect_attachments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInterconnectAttachments`` requests and continue to iterate
    through the ``interconnect_attachments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListInterconnectAttachmentsResponse],
        request: service.ListInterconnectAttachmentsRequest,
        response: service.ListInterconnectAttachmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse):
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
        self._request = service.ListInterconnectAttachmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListInterconnectAttachmentsResponse]:
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

    def __iter__(self) -> Iterator[resources.InterconnectAttachment]:
        for page in self.pages:
            yield from page.interconnect_attachments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterconnectAttachmentsAsyncPager:
    """A pager for iterating through ``list_interconnect_attachments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``interconnect_attachments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInterconnectAttachments`` requests and continue to iterate
    through the ``interconnect_attachments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListInterconnectAttachmentsResponse]],
        request: service.ListInterconnectAttachmentsRequest,
        response: service.ListInterconnectAttachmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse):
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
        self._request = service.ListInterconnectAttachmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListInterconnectAttachmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.InterconnectAttachment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.interconnect_attachments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutersPager:
    """A pager for iterating through ``list_routers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListRoutersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``routers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRouters`` requests and continue to iterate
    through the ``routers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListRoutersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListRoutersResponse],
        request: service.ListRoutersRequest,
        response: service.ListRoutersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListRoutersRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListRoutersResponse):
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
        self._request = service.ListRoutersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListRoutersResponse]:
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

    def __iter__(self) -> Iterator[resources.Router]:
        for page in self.pages:
            yield from page.routers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutersAsyncPager:
    """A pager for iterating through ``list_routers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgenetwork_v1.types.ListRoutersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``routers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRouters`` requests and continue to iterate
    through the ``routers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgenetwork_v1.types.ListRoutersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListRoutersResponse]],
        request: service.ListRoutersRequest,
        response: service.ListRoutersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgenetwork_v1.types.ListRoutersRequest):
                The initial request object.
            response (google.cloud.edgenetwork_v1.types.ListRoutersResponse):
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
        self._request = service.ListRoutersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListRoutersResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Router]:
        async def async_generator():
            async for page in self.pages:
                for response in page.routers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
