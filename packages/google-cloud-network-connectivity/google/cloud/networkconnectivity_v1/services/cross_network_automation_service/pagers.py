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

from google.cloud.networkconnectivity_v1.types import cross_network_automation


class ListServiceConnectionMapsPager:
    """A pager for iterating through ``list_service_connection_maps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_connection_maps`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceConnectionMaps`` requests and continue to iterate
    through the ``service_connection_maps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., cross_network_automation.ListServiceConnectionMapsResponse
        ],
        request: cross_network_automation.ListServiceConnectionMapsRequest,
        response: cross_network_automation.ListServiceConnectionMapsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsResponse):
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
        self._request = cross_network_automation.ListServiceConnectionMapsRequest(
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
    ) -> Iterator[cross_network_automation.ListServiceConnectionMapsResponse]:
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

    def __iter__(self) -> Iterator[cross_network_automation.ServiceConnectionMap]:
        for page in self.pages:
            yield from page.service_connection_maps

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceConnectionMapsAsyncPager:
    """A pager for iterating through ``list_service_connection_maps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_connection_maps`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceConnectionMaps`` requests and continue to iterate
    through the ``service_connection_maps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[cross_network_automation.ListServiceConnectionMapsResponse]
        ],
        request: cross_network_automation.ListServiceConnectionMapsRequest,
        response: cross_network_automation.ListServiceConnectionMapsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceConnectionMapsResponse):
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
        self._request = cross_network_automation.ListServiceConnectionMapsRequest(
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
    ) -> AsyncIterator[cross_network_automation.ListServiceConnectionMapsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cross_network_automation.ServiceConnectionMap]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_connection_maps:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceConnectionPoliciesPager:
    """A pager for iterating through ``list_service_connection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_connection_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceConnectionPolicies`` requests and continue to iterate
    through the ``service_connection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., cross_network_automation.ListServiceConnectionPoliciesResponse
        ],
        request: cross_network_automation.ListServiceConnectionPoliciesRequest,
        response: cross_network_automation.ListServiceConnectionPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesResponse):
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
        self._request = cross_network_automation.ListServiceConnectionPoliciesRequest(
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
    ) -> Iterator[cross_network_automation.ListServiceConnectionPoliciesResponse]:
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

    def __iter__(self) -> Iterator[cross_network_automation.ServiceConnectionPolicy]:
        for page in self.pages:
            yield from page.service_connection_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceConnectionPoliciesAsyncPager:
    """A pager for iterating through ``list_service_connection_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_connection_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceConnectionPolicies`` requests and continue to iterate
    through the ``service_connection_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[cross_network_automation.ListServiceConnectionPoliciesResponse],
        ],
        request: cross_network_automation.ListServiceConnectionPoliciesRequest,
        response: cross_network_automation.ListServiceConnectionPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceConnectionPoliciesResponse):
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
        self._request = cross_network_automation.ListServiceConnectionPoliciesRequest(
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
    ) -> AsyncIterator[cross_network_automation.ListServiceConnectionPoliciesResponse]:
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
    ) -> AsyncIterator[cross_network_automation.ServiceConnectionPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_connection_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceClassesPager:
    """A pager for iterating through ``list_service_classes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceClassesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_classes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceClasses`` requests and continue to iterate
    through the ``service_classes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceClassesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cross_network_automation.ListServiceClassesResponse],
        request: cross_network_automation.ListServiceClassesRequest,
        response: cross_network_automation.ListServiceClassesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceClassesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceClassesResponse):
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
        self._request = cross_network_automation.ListServiceClassesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cross_network_automation.ListServiceClassesResponse]:
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

    def __iter__(self) -> Iterator[cross_network_automation.ServiceClass]:
        for page in self.pages:
            yield from page.service_classes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceClassesAsyncPager:
    """A pager for iterating through ``list_service_classes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceClassesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_classes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceClasses`` requests and continue to iterate
    through the ``service_classes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceClassesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[cross_network_automation.ListServiceClassesResponse]
        ],
        request: cross_network_automation.ListServiceClassesRequest,
        response: cross_network_automation.ListServiceClassesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceClassesRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceClassesResponse):
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
        self._request = cross_network_automation.ListServiceClassesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[cross_network_automation.ListServiceClassesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cross_network_automation.ServiceClass]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_classes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceConnectionTokensPager:
    """A pager for iterating through ``list_service_connection_tokens`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_connection_tokens`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceConnectionTokens`` requests and continue to iterate
    through the ``service_connection_tokens`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., cross_network_automation.ListServiceConnectionTokensResponse
        ],
        request: cross_network_automation.ListServiceConnectionTokensRequest,
        response: cross_network_automation.ListServiceConnectionTokensResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensResponse):
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
        self._request = cross_network_automation.ListServiceConnectionTokensRequest(
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
    ) -> Iterator[cross_network_automation.ListServiceConnectionTokensResponse]:
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

    def __iter__(self) -> Iterator[cross_network_automation.ServiceConnectionToken]:
        for page in self.pages:
            yield from page.service_connection_tokens

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceConnectionTokensAsyncPager:
    """A pager for iterating through ``list_service_connection_tokens`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_connection_tokens`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceConnectionTokens`` requests and continue to iterate
    through the ``service_connection_tokens`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[cross_network_automation.ListServiceConnectionTokensResponse]
        ],
        request: cross_network_automation.ListServiceConnectionTokensRequest,
        response: cross_network_automation.ListServiceConnectionTokensResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensRequest):
                The initial request object.
            response (google.cloud.networkconnectivity_v1.types.ListServiceConnectionTokensResponse):
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
        self._request = cross_network_automation.ListServiceConnectionTokensRequest(
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
    ) -> AsyncIterator[cross_network_automation.ListServiceConnectionTokensResponse]:
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
    ) -> AsyncIterator[cross_network_automation.ServiceConnectionToken]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_connection_tokens:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
