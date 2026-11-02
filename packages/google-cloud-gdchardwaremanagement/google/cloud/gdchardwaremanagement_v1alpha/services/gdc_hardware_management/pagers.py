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

from google.cloud.gdchardwaremanagement_v1alpha.types import resources, service


class ListOrdersPager:
    """A pager for iterating through ``list_orders`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``orders`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOrders`` requests and continue to iterate
    through the ``orders`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListOrdersResponse],
        request: service.ListOrdersRequest,
        response: service.ListOrdersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersResponse):
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
        self._request = service.ListOrdersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListOrdersResponse]:
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

    def __iter__(self) -> Iterator[resources.Order]:
        for page in self.pages:
            yield from page.orders

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOrdersAsyncPager:
    """A pager for iterating through ``list_orders`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``orders`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOrders`` requests and continue to iterate
    through the ``orders`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListOrdersResponse]],
        request: service.ListOrdersRequest,
        response: service.ListOrdersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersResponse):
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
        self._request = service.ListOrdersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListOrdersResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Order]:
        async def async_generator():
            async for page in self.pages:
                for response in page.orders:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSitesPager:
    """A pager for iterating through ``list_sites`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``sites`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSites`` requests and continue to iterate
    through the ``sites`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListSitesResponse],
        request: service.ListSitesRequest,
        response: service.ListSitesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesResponse):
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
        self._request = service.ListSitesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListSitesResponse]:
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

    def __iter__(self) -> Iterator[resources.Site]:
        for page in self.pages:
            yield from page.sites

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSitesAsyncPager:
    """A pager for iterating through ``list_sites`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``sites`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSites`` requests and continue to iterate
    through the ``sites`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListSitesResponse]],
        request: service.ListSitesRequest,
        response: service.ListSitesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesResponse):
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
        self._request = service.ListSitesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListSitesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Site]:
        async def async_generator():
            async for page in self.pages:
                for response in page.sites:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHardwareGroupsPager:
    """A pager for iterating through ``list_hardware_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``hardware_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHardwareGroups`` requests and continue to iterate
    through the ``hardware_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListHardwareGroupsResponse],
        request: service.ListHardwareGroupsRequest,
        response: service.ListHardwareGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsResponse):
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
        self._request = service.ListHardwareGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListHardwareGroupsResponse]:
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

    def __iter__(self) -> Iterator[resources.HardwareGroup]:
        for page in self.pages:
            yield from page.hardware_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHardwareGroupsAsyncPager:
    """A pager for iterating through ``list_hardware_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``hardware_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHardwareGroups`` requests and continue to iterate
    through the ``hardware_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListHardwareGroupsResponse]],
        request: service.ListHardwareGroupsRequest,
        response: service.ListHardwareGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsResponse):
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
        self._request = service.ListHardwareGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListHardwareGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.HardwareGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.hardware_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHardwarePager:
    """A pager for iterating through ``list_hardware`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``hardware`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHardware`` requests and continue to iterate
    through the ``hardware`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListHardwareResponse],
        request: service.ListHardwareRequest,
        response: service.ListHardwareResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareResponse):
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
        self._request = service.ListHardwareRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListHardwareResponse]:
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

    def __iter__(self) -> Iterator[resources.Hardware]:
        for page in self.pages:
            yield from page.hardware

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHardwareAsyncPager:
    """A pager for iterating through ``list_hardware`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``hardware`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHardware`` requests and continue to iterate
    through the ``hardware`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListHardwareResponse]],
        request: service.ListHardwareRequest,
        response: service.ListHardwareResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareResponse):
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
        self._request = service.ListHardwareRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListHardwareResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Hardware]:
        async def async_generator():
            async for page in self.pages:
                for response in page.hardware:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCommentsPager:
    """A pager for iterating through ``list_comments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``comments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListComments`` requests and continue to iterate
    through the ``comments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListCommentsResponse],
        request: service.ListCommentsRequest,
        response: service.ListCommentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsResponse):
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
        self._request = service.ListCommentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListCommentsResponse]:
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

    def __iter__(self) -> Iterator[resources.Comment]:
        for page in self.pages:
            yield from page.comments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCommentsAsyncPager:
    """A pager for iterating through ``list_comments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``comments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListComments`` requests and continue to iterate
    through the ``comments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListCommentsResponse]],
        request: service.ListCommentsRequest,
        response: service.ListCommentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsResponse):
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
        self._request = service.ListCommentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListCommentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Comment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.comments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListChangeLogEntriesPager:
    """A pager for iterating through ``list_change_log_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``change_log_entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListChangeLogEntries`` requests and continue to iterate
    through the ``change_log_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListChangeLogEntriesResponse],
        request: service.ListChangeLogEntriesRequest,
        response: service.ListChangeLogEntriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesResponse):
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
        self._request = service.ListChangeLogEntriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListChangeLogEntriesResponse]:
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

    def __iter__(self) -> Iterator[resources.ChangeLogEntry]:
        for page in self.pages:
            yield from page.change_log_entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListChangeLogEntriesAsyncPager:
    """A pager for iterating through ``list_change_log_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``change_log_entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListChangeLogEntries`` requests and continue to iterate
    through the ``change_log_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListChangeLogEntriesResponse]],
        request: service.ListChangeLogEntriesRequest,
        response: service.ListChangeLogEntriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesResponse):
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
        self._request = service.ListChangeLogEntriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListChangeLogEntriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.ChangeLogEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.change_log_entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSkusPager:
    """A pager for iterating through ``list_skus`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``skus`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSkus`` requests and continue to iterate
    through the ``skus`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListSkusResponse],
        request: service.ListSkusRequest,
        response: service.ListSkusResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusResponse):
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
        self._request = service.ListSkusRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListSkusResponse]:
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

    def __iter__(self) -> Iterator[resources.Sku]:
        for page in self.pages:
            yield from page.skus

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSkusAsyncPager:
    """A pager for iterating through ``list_skus`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``skus`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSkus`` requests and continue to iterate
    through the ``skus`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListSkusResponse]],
        request: service.ListSkusRequest,
        response: service.ListSkusResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusResponse):
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
        self._request = service.ListSkusRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListSkusResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Sku]:
        async def async_generator():
            async for page in self.pages:
                for response in page.skus:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListZonesPager:
    """A pager for iterating through ``list_zones`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``zones`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListZones`` requests and continue to iterate
    through the ``zones`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesResponse`
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
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesResponse):
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
    :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``zones`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListZones`` requests and continue to iterate
    through the ``zones`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesResponse`
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
            request (google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesRequest):
                The initial request object.
            response (google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesResponse):
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
