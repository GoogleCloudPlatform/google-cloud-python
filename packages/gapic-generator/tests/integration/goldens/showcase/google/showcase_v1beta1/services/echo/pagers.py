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
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import retry_async as retries_async
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator, Union
try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, object, None]  # type: ignore

from google.showcase_v1beta1.types import echo as gs_echo


class PagedExpandPager:
    """A pager for iterating through ``paged_expand`` requests.

    This class thinly wraps an initial
    :class:`google.showcase_v1beta1.types.PagedExpandResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``responses`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``PagedExpand`` requests and continue to iterate
    through the ``responses`` field on the
    corresponding responses.

    All the usual :class:`google.showcase_v1beta1.types.PagedExpandResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., gs_echo.PagedExpandResponse],
            request: gs_echo.PagedExpandRequest,
            response: gs_echo.PagedExpandResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.showcase_v1beta1.types.PagedExpandRequest):
                The initial request object.
            response (google.showcase_v1beta1.types.PagedExpandResponse):
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
        self._request = gs_echo.PagedExpandRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gs_echo.PagedExpandResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[gs_echo.EchoResponse]:
        for page in self.pages:
            yield from page.responses

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class PagedExpandAsyncPager:
    """A pager for iterating through ``paged_expand`` requests.

    This class thinly wraps an initial
    :class:`google.showcase_v1beta1.types.PagedExpandResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``responses`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``PagedExpand`` requests and continue to iterate
    through the ``responses`` field on the
    corresponding responses.

    All the usual :class:`google.showcase_v1beta1.types.PagedExpandResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[gs_echo.PagedExpandResponse]],
            request: gs_echo.PagedExpandRequest,
            response: gs_echo.PagedExpandResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.showcase_v1beta1.types.PagedExpandRequest):
                The initial request object.
            response (google.showcase_v1beta1.types.PagedExpandResponse):
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
        self._request = gs_echo.PagedExpandRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gs_echo.PagedExpandResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[gs_echo.EchoResponse]:
        async def async_generator():
            async for page in self.pages:
                for response in page.responses:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class PagedExpandLegacyPager:
    """A pager for iterating through ``paged_expand_legacy`` requests.

    This class thinly wraps an initial
    :class:`google.showcase_v1beta1.types.PagedExpandResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``responses`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``PagedExpandLegacy`` requests and continue to iterate
    through the ``responses`` field on the
    corresponding responses.

    All the usual :class:`google.showcase_v1beta1.types.PagedExpandResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., gs_echo.PagedExpandResponse],
            request: gs_echo.PagedExpandLegacyRequest,
            response: gs_echo.PagedExpandResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.showcase_v1beta1.types.PagedExpandLegacyRequest):
                The initial request object.
            response (google.showcase_v1beta1.types.PagedExpandResponse):
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
        self._request = gs_echo.PagedExpandLegacyRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gs_echo.PagedExpandResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[gs_echo.EchoResponse]:
        for page in self.pages:
            yield from page.responses

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class PagedExpandLegacyAsyncPager:
    """A pager for iterating through ``paged_expand_legacy`` requests.

    This class thinly wraps an initial
    :class:`google.showcase_v1beta1.types.PagedExpandResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``responses`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``PagedExpandLegacy`` requests and continue to iterate
    through the ``responses`` field on the
    corresponding responses.

    All the usual :class:`google.showcase_v1beta1.types.PagedExpandResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[gs_echo.PagedExpandResponse]],
            request: gs_echo.PagedExpandLegacyRequest,
            response: gs_echo.PagedExpandResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.showcase_v1beta1.types.PagedExpandLegacyRequest):
                The initial request object.
            response (google.showcase_v1beta1.types.PagedExpandResponse):
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
        self._request = gs_echo.PagedExpandLegacyRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gs_echo.PagedExpandResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[gs_echo.EchoResponse]:
        async def async_generator():
            async for page in self.pages:
                for response in page.responses:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class PagedExpandLegacyMappedPager:
    """A pager for iterating through ``paged_expand_legacy_mapped`` requests.

    This class thinly wraps an initial
    :class:`google.showcase_v1beta1.types.PagedExpandLegacyMappedResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``alphabetized`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``PagedExpandLegacyMapped`` requests and continue to iterate
    through the ``alphabetized`` field on the
    corresponding responses.

    All the usual :class:`google.showcase_v1beta1.types.PagedExpandLegacyMappedResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., gs_echo.PagedExpandLegacyMappedResponse],
            request: gs_echo.PagedExpandRequest,
            response: gs_echo.PagedExpandLegacyMappedResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.showcase_v1beta1.types.PagedExpandRequest):
                The initial request object.
            response (google.showcase_v1beta1.types.PagedExpandLegacyMappedResponse):
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
        self._request = gs_echo.PagedExpandRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gs_echo.PagedExpandLegacyMappedResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[Tuple[str, gs_echo.PagedExpandResponseList]]:
        for page in self.pages:
            yield from page.alphabetized.items()

    def get(self, key: str) -> Optional[gs_echo.PagedExpandResponseList]:
        return self._response.alphabetized.get(key)

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class PagedExpandLegacyMappedAsyncPager:
    """A pager for iterating through ``paged_expand_legacy_mapped`` requests.

    This class thinly wraps an initial
    :class:`google.showcase_v1beta1.types.PagedExpandLegacyMappedResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``alphabetized`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``PagedExpandLegacyMapped`` requests and continue to iterate
    through the ``alphabetized`` field on the
    corresponding responses.

    All the usual :class:`google.showcase_v1beta1.types.PagedExpandLegacyMappedResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[gs_echo.PagedExpandLegacyMappedResponse]],
            request: gs_echo.PagedExpandRequest,
            response: gs_echo.PagedExpandLegacyMappedResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.showcase_v1beta1.types.PagedExpandRequest):
                The initial request object.
            response (google.showcase_v1beta1.types.PagedExpandLegacyMappedResponse):
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
        self._request = gs_echo.PagedExpandRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gs_echo.PagedExpandLegacyMappedResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> Iterator[Tuple[str, gs_echo.PagedExpandResponseList]]:
        async def async_generator():
            async for page in self.pages:
                for response in page.alphabetized.items():
                    yield response

        return async_generator()

    def get(self, key: str) -> Optional[gs_echo.PagedExpandResponseList]:
        return self._response.alphabetized.get(key)

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
