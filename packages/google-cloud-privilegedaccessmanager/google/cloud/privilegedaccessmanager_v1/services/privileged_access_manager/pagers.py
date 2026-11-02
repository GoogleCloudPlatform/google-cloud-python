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

from google.cloud.privilegedaccessmanager_v1.types import privilegedaccessmanager


class ListEntitlementsPager:
    """A pager for iterating through ``list_entitlements`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entitlements`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEntitlements`` requests and continue to iterate
    through the ``entitlements`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., privilegedaccessmanager.ListEntitlementsResponse],
        request: privilegedaccessmanager.ListEntitlementsRequest,
        response: privilegedaccessmanager.ListEntitlementsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsResponse):
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
        self._request = privilegedaccessmanager.ListEntitlementsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[privilegedaccessmanager.ListEntitlementsResponse]:
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

    def __iter__(self) -> Iterator[privilegedaccessmanager.Entitlement]:
        for page in self.pages:
            yield from page.entitlements

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntitlementsAsyncPager:
    """A pager for iterating through ``list_entitlements`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entitlements`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEntitlements`` requests and continue to iterate
    through the ``entitlements`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[privilegedaccessmanager.ListEntitlementsResponse]
        ],
        request: privilegedaccessmanager.ListEntitlementsRequest,
        response: privilegedaccessmanager.ListEntitlementsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.ListEntitlementsResponse):
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
        self._request = privilegedaccessmanager.ListEntitlementsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[privilegedaccessmanager.ListEntitlementsResponse]:
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

    def __aiter__(self) -> AsyncIterator[privilegedaccessmanager.Entitlement]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entitlements:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchEntitlementsPager:
    """A pager for iterating through ``search_entitlements`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entitlements`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchEntitlements`` requests and continue to iterate
    through the ``entitlements`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., privilegedaccessmanager.SearchEntitlementsResponse],
        request: privilegedaccessmanager.SearchEntitlementsRequest,
        response: privilegedaccessmanager.SearchEntitlementsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsResponse):
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
        self._request = privilegedaccessmanager.SearchEntitlementsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[privilegedaccessmanager.SearchEntitlementsResponse]:
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

    def __iter__(self) -> Iterator[privilegedaccessmanager.Entitlement]:
        for page in self.pages:
            yield from page.entitlements

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchEntitlementsAsyncPager:
    """A pager for iterating through ``search_entitlements`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entitlements`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchEntitlements`` requests and continue to iterate
    through the ``entitlements`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[privilegedaccessmanager.SearchEntitlementsResponse]
        ],
        request: privilegedaccessmanager.SearchEntitlementsRequest,
        response: privilegedaccessmanager.SearchEntitlementsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.SearchEntitlementsResponse):
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
        self._request = privilegedaccessmanager.SearchEntitlementsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[privilegedaccessmanager.SearchEntitlementsResponse]:
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

    def __aiter__(self) -> AsyncIterator[privilegedaccessmanager.Entitlement]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entitlements:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGrantsPager:
    """A pager for iterating through ``list_grants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.ListGrantsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``grants`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGrants`` requests and continue to iterate
    through the ``grants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.ListGrantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., privilegedaccessmanager.ListGrantsResponse],
        request: privilegedaccessmanager.ListGrantsRequest,
        response: privilegedaccessmanager.ListGrantsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.ListGrantsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.ListGrantsResponse):
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
        self._request = privilegedaccessmanager.ListGrantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[privilegedaccessmanager.ListGrantsResponse]:
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

    def __iter__(self) -> Iterator[privilegedaccessmanager.Grant]:
        for page in self.pages:
            yield from page.grants

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGrantsAsyncPager:
    """A pager for iterating through ``list_grants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.ListGrantsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``grants`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGrants`` requests and continue to iterate
    through the ``grants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.ListGrantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[privilegedaccessmanager.ListGrantsResponse]],
        request: privilegedaccessmanager.ListGrantsRequest,
        response: privilegedaccessmanager.ListGrantsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.ListGrantsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.ListGrantsResponse):
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
        self._request = privilegedaccessmanager.ListGrantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[privilegedaccessmanager.ListGrantsResponse]:
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

    def __aiter__(self) -> AsyncIterator[privilegedaccessmanager.Grant]:
        async def async_generator():
            async for page in self.pages:
                for response in page.grants:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchGrantsPager:
    """A pager for iterating through ``search_grants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.SearchGrantsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``grants`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchGrants`` requests and continue to iterate
    through the ``grants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.SearchGrantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., privilegedaccessmanager.SearchGrantsResponse],
        request: privilegedaccessmanager.SearchGrantsRequest,
        response: privilegedaccessmanager.SearchGrantsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.SearchGrantsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.SearchGrantsResponse):
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
        self._request = privilegedaccessmanager.SearchGrantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[privilegedaccessmanager.SearchGrantsResponse]:
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

    def __iter__(self) -> Iterator[privilegedaccessmanager.Grant]:
        for page in self.pages:
            yield from page.grants

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchGrantsAsyncPager:
    """A pager for iterating through ``search_grants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.privilegedaccessmanager_v1.types.SearchGrantsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``grants`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchGrants`` requests and continue to iterate
    through the ``grants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.privilegedaccessmanager_v1.types.SearchGrantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[privilegedaccessmanager.SearchGrantsResponse]],
        request: privilegedaccessmanager.SearchGrantsRequest,
        response: privilegedaccessmanager.SearchGrantsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.privilegedaccessmanager_v1.types.SearchGrantsRequest):
                The initial request object.
            response (google.cloud.privilegedaccessmanager_v1.types.SearchGrantsResponse):
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
        self._request = privilegedaccessmanager.SearchGrantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[privilegedaccessmanager.SearchGrantsResponse]:
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

    def __aiter__(self) -> AsyncIterator[privilegedaccessmanager.Grant]:
        async def async_generator():
            async for page in self.pages:
                for response in page.grants:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
