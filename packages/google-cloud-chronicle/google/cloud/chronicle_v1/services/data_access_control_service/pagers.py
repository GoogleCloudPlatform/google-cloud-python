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

from google.cloud.chronicle_v1.types import data_access_control


class ListDataAccessLabelsPager:
    """A pager for iterating through ``list_data_access_labels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListDataAccessLabelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_access_labels`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataAccessLabels`` requests and continue to iterate
    through the ``data_access_labels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListDataAccessLabelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_access_control.ListDataAccessLabelsResponse],
        request: data_access_control.ListDataAccessLabelsRequest,
        response: data_access_control.ListDataAccessLabelsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListDataAccessLabelsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListDataAccessLabelsResponse):
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
        self._request = data_access_control.ListDataAccessLabelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_access_control.ListDataAccessLabelsResponse]:
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

    def __iter__(self) -> Iterator[data_access_control.DataAccessLabel]:
        for page in self.pages:
            yield from page.data_access_labels

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataAccessLabelsAsyncPager:
    """A pager for iterating through ``list_data_access_labels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListDataAccessLabelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_access_labels`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataAccessLabels`` requests and continue to iterate
    through the ``data_access_labels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListDataAccessLabelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_access_control.ListDataAccessLabelsResponse]
        ],
        request: data_access_control.ListDataAccessLabelsRequest,
        response: data_access_control.ListDataAccessLabelsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListDataAccessLabelsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListDataAccessLabelsResponse):
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
        self._request = data_access_control.ListDataAccessLabelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_access_control.ListDataAccessLabelsResponse]:
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

    def __aiter__(self) -> AsyncIterator[data_access_control.DataAccessLabel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_access_labels:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataAccessScopesPager:
    """A pager for iterating through ``list_data_access_scopes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListDataAccessScopesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_access_scopes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataAccessScopes`` requests and continue to iterate
    through the ``data_access_scopes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListDataAccessScopesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_access_control.ListDataAccessScopesResponse],
        request: data_access_control.ListDataAccessScopesRequest,
        response: data_access_control.ListDataAccessScopesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListDataAccessScopesRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListDataAccessScopesResponse):
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
        self._request = data_access_control.ListDataAccessScopesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_access_control.ListDataAccessScopesResponse]:
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

    def __iter__(self) -> Iterator[data_access_control.DataAccessScope]:
        for page in self.pages:
            yield from page.data_access_scopes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataAccessScopesAsyncPager:
    """A pager for iterating through ``list_data_access_scopes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListDataAccessScopesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_access_scopes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataAccessScopes`` requests and continue to iterate
    through the ``data_access_scopes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListDataAccessScopesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_access_control.ListDataAccessScopesResponse]
        ],
        request: data_access_control.ListDataAccessScopesRequest,
        response: data_access_control.ListDataAccessScopesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListDataAccessScopesRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListDataAccessScopesResponse):
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
        self._request = data_access_control.ListDataAccessScopesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_access_control.ListDataAccessScopesResponse]:
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

    def __aiter__(self) -> AsyncIterator[data_access_control.DataAccessScope]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_access_scopes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
