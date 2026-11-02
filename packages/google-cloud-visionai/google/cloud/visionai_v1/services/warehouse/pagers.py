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

from google.cloud.visionai_v1.types import warehouse


class ListAssetsPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListAssetsResponse],
        request: warehouse.ListAssetsRequest,
        response: warehouse.ListAssetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListAssetsResponse):
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
        self._request = warehouse.ListAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListAssetsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.Asset]:
        for page in self.pages:
            yield from page.assets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAssetsAsyncPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListAssetsResponse]],
        request: warehouse.ListAssetsRequest,
        response: warehouse.ListAssetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListAssetsResponse):
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
        self._request = warehouse.ListAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListAssetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.Asset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ViewIndexedAssetsPager:
    """A pager for iterating through ``view_indexed_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ViewIndexedAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``indexed_assets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ViewIndexedAssets`` requests and continue to iterate
    through the ``indexed_assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ViewIndexedAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ViewIndexedAssetsResponse],
        request: warehouse.ViewIndexedAssetsRequest,
        response: warehouse.ViewIndexedAssetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ViewIndexedAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ViewIndexedAssetsResponse):
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
        self._request = warehouse.ViewIndexedAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ViewIndexedAssetsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.IndexedAsset]:
        for page in self.pages:
            yield from page.indexed_assets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ViewIndexedAssetsAsyncPager:
    """A pager for iterating through ``view_indexed_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ViewIndexedAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``indexed_assets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ViewIndexedAssets`` requests and continue to iterate
    through the ``indexed_assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ViewIndexedAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ViewIndexedAssetsResponse]],
        request: warehouse.ViewIndexedAssetsRequest,
        response: warehouse.ViewIndexedAssetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ViewIndexedAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ViewIndexedAssetsResponse):
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
        self._request = warehouse.ViewIndexedAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ViewIndexedAssetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.IndexedAsset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.indexed_assets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIndexesPager:
    """A pager for iterating through ``list_indexes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListIndexesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``indexes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListIndexes`` requests and continue to iterate
    through the ``indexes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListIndexesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListIndexesResponse],
        request: warehouse.ListIndexesRequest,
        response: warehouse.ListIndexesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListIndexesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListIndexesResponse):
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
        self._request = warehouse.ListIndexesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListIndexesResponse]:
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

    def __iter__(self) -> Iterator[warehouse.Index]:
        for page in self.pages:
            yield from page.indexes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIndexesAsyncPager:
    """A pager for iterating through ``list_indexes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListIndexesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``indexes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListIndexes`` requests and continue to iterate
    through the ``indexes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListIndexesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListIndexesResponse]],
        request: warehouse.ListIndexesRequest,
        response: warehouse.ListIndexesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListIndexesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListIndexesResponse):
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
        self._request = warehouse.ListIndexesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListIndexesResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.Index]:
        async def async_generator():
            async for page in self.pages:
                for response in page.indexes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCorporaPager:
    """A pager for iterating through ``list_corpora`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListCorporaResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListCorporaResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListCorporaResponse],
        request: warehouse.ListCorporaRequest,
        response: warehouse.ListCorporaResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListCorporaRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListCorporaResponse):
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
        self._request = warehouse.ListCorporaRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListCorporaResponse]:
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

    def __iter__(self) -> Iterator[warehouse.Corpus]:
        for page in self.pages:
            yield from page.corpora

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCorporaAsyncPager:
    """A pager for iterating through ``list_corpora`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListCorporaResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListCorporaResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListCorporaResponse]],
        request: warehouse.ListCorporaRequest,
        response: warehouse.ListCorporaResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListCorporaRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListCorporaResponse):
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
        self._request = warehouse.ListCorporaRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListCorporaResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.Corpus]:
        async def async_generator():
            async for page in self.pages:
                for response in page.corpora:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataSchemasPager:
    """A pager for iterating through ``list_data_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListDataSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataSchemas`` requests and continue to iterate
    through the ``data_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListDataSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListDataSchemasResponse],
        request: warehouse.ListDataSchemasRequest,
        response: warehouse.ListDataSchemasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListDataSchemasRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListDataSchemasResponse):
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
        self._request = warehouse.ListDataSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListDataSchemasResponse]:
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

    def __iter__(self) -> Iterator[warehouse.DataSchema]:
        for page in self.pages:
            yield from page.data_schemas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataSchemasAsyncPager:
    """A pager for iterating through ``list_data_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListDataSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataSchemas`` requests and continue to iterate
    through the ``data_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListDataSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListDataSchemasResponse]],
        request: warehouse.ListDataSchemasRequest,
        response: warehouse.ListDataSchemasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListDataSchemasRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListDataSchemasResponse):
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
        self._request = warehouse.ListDataSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListDataSchemasResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.DataSchema]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_schemas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnnotationsPager:
    """A pager for iterating through ``list_annotations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListAnnotationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``annotations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnnotations`` requests and continue to iterate
    through the ``annotations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListAnnotationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListAnnotationsResponse],
        request: warehouse.ListAnnotationsRequest,
        response: warehouse.ListAnnotationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListAnnotationsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListAnnotationsResponse):
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
        self._request = warehouse.ListAnnotationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListAnnotationsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.Annotation]:
        for page in self.pages:
            yield from page.annotations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnnotationsAsyncPager:
    """A pager for iterating through ``list_annotations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListAnnotationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``annotations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnnotations`` requests and continue to iterate
    through the ``annotations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListAnnotationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListAnnotationsResponse]],
        request: warehouse.ListAnnotationsRequest,
        response: warehouse.ListAnnotationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListAnnotationsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListAnnotationsResponse):
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
        self._request = warehouse.ListAnnotationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListAnnotationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.Annotation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.annotations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSearchConfigsPager:
    """A pager for iterating through ``list_search_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListSearchConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSearchConfigs`` requests and continue to iterate
    through the ``search_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListSearchConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListSearchConfigsResponse],
        request: warehouse.ListSearchConfigsRequest,
        response: warehouse.ListSearchConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListSearchConfigsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListSearchConfigsResponse):
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
        self._request = warehouse.ListSearchConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListSearchConfigsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.SearchConfig]:
        for page in self.pages:
            yield from page.search_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSearchConfigsAsyncPager:
    """A pager for iterating through ``list_search_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListSearchConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSearchConfigs`` requests and continue to iterate
    through the ``search_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListSearchConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListSearchConfigsResponse]],
        request: warehouse.ListSearchConfigsRequest,
        response: warehouse.ListSearchConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListSearchConfigsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListSearchConfigsResponse):
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
        self._request = warehouse.ListSearchConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListSearchConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.SearchConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.search_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSearchHypernymsPager:
    """A pager for iterating through ``list_search_hypernyms`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListSearchHypernymsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_hypernyms`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSearchHypernyms`` requests and continue to iterate
    through the ``search_hypernyms`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListSearchHypernymsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListSearchHypernymsResponse],
        request: warehouse.ListSearchHypernymsRequest,
        response: warehouse.ListSearchHypernymsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListSearchHypernymsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListSearchHypernymsResponse):
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
        self._request = warehouse.ListSearchHypernymsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListSearchHypernymsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.SearchHypernym]:
        for page in self.pages:
            yield from page.search_hypernyms

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSearchHypernymsAsyncPager:
    """A pager for iterating through ``list_search_hypernyms`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListSearchHypernymsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_hypernyms`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSearchHypernyms`` requests and continue to iterate
    through the ``search_hypernyms`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListSearchHypernymsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListSearchHypernymsResponse]],
        request: warehouse.ListSearchHypernymsRequest,
        response: warehouse.ListSearchHypernymsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListSearchHypernymsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListSearchHypernymsResponse):
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
        self._request = warehouse.ListSearchHypernymsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListSearchHypernymsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.SearchHypernym]:
        async def async_generator():
            async for page in self.pages:
                for response in page.search_hypernyms:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAssetsPager:
    """A pager for iterating through ``search_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.SearchAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_result_items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAssets`` requests and continue to iterate
    through the ``search_result_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.SearchAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.SearchAssetsResponse],
        request: warehouse.SearchAssetsRequest,
        response: warehouse.SearchAssetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.SearchAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.SearchAssetsResponse):
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
        self._request = warehouse.SearchAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.SearchAssetsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.SearchResultItem]:
        for page in self.pages:
            yield from page.search_result_items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAssetsAsyncPager:
    """A pager for iterating through ``search_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.SearchAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_result_items`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAssets`` requests and continue to iterate
    through the ``search_result_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.SearchAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.SearchAssetsResponse]],
        request: warehouse.SearchAssetsRequest,
        response: warehouse.SearchAssetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.SearchAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.SearchAssetsResponse):
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
        self._request = warehouse.SearchAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.SearchAssetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.SearchResultItem]:
        async def async_generator():
            async for page in self.pages:
                for response in page.search_result_items:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchIndexEndpointPager:
    """A pager for iterating through ``search_index_endpoint`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.SearchIndexEndpointResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_result_items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchIndexEndpoint`` requests and continue to iterate
    through the ``search_result_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.SearchIndexEndpointResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.SearchIndexEndpointResponse],
        request: warehouse.SearchIndexEndpointRequest,
        response: warehouse.SearchIndexEndpointResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.SearchIndexEndpointRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.SearchIndexEndpointResponse):
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
        self._request = warehouse.SearchIndexEndpointRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.SearchIndexEndpointResponse]:
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

    def __iter__(self) -> Iterator[warehouse.SearchResultItem]:
        for page in self.pages:
            yield from page.search_result_items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchIndexEndpointAsyncPager:
    """A pager for iterating through ``search_index_endpoint`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.SearchIndexEndpointResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_result_items`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchIndexEndpoint`` requests and continue to iterate
    through the ``search_result_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.SearchIndexEndpointResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.SearchIndexEndpointResponse]],
        request: warehouse.SearchIndexEndpointRequest,
        response: warehouse.SearchIndexEndpointResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.SearchIndexEndpointRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.SearchIndexEndpointResponse):
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
        self._request = warehouse.SearchIndexEndpointRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.SearchIndexEndpointResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.SearchResultItem]:
        async def async_generator():
            async for page in self.pages:
                for response in page.search_result_items:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIndexEndpointsPager:
    """A pager for iterating through ``list_index_endpoints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListIndexEndpointsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``index_endpoints`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListIndexEndpoints`` requests and continue to iterate
    through the ``index_endpoints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListIndexEndpointsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListIndexEndpointsResponse],
        request: warehouse.ListIndexEndpointsRequest,
        response: warehouse.ListIndexEndpointsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListIndexEndpointsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListIndexEndpointsResponse):
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
        self._request = warehouse.ListIndexEndpointsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListIndexEndpointsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.IndexEndpoint]:
        for page in self.pages:
            yield from page.index_endpoints

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIndexEndpointsAsyncPager:
    """A pager for iterating through ``list_index_endpoints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListIndexEndpointsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``index_endpoints`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListIndexEndpoints`` requests and continue to iterate
    through the ``index_endpoints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListIndexEndpointsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListIndexEndpointsResponse]],
        request: warehouse.ListIndexEndpointsRequest,
        response: warehouse.ListIndexEndpointsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListIndexEndpointsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListIndexEndpointsResponse):
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
        self._request = warehouse.ListIndexEndpointsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListIndexEndpointsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.IndexEndpoint]:
        async def async_generator():
            async for page in self.pages:
                for response in page.index_endpoints:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCollectionsPager:
    """A pager for iterating through ``list_collections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListCollectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``collections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCollections`` requests and continue to iterate
    through the ``collections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListCollectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ListCollectionsResponse],
        request: warehouse.ListCollectionsRequest,
        response: warehouse.ListCollectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListCollectionsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListCollectionsResponse):
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
        self._request = warehouse.ListCollectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ListCollectionsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.Collection]:
        for page in self.pages:
            yield from page.collections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCollectionsAsyncPager:
    """A pager for iterating through ``list_collections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListCollectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``collections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCollections`` requests and continue to iterate
    through the ``collections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListCollectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ListCollectionsResponse]],
        request: warehouse.ListCollectionsRequest,
        response: warehouse.ListCollectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListCollectionsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListCollectionsResponse):
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
        self._request = warehouse.ListCollectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ListCollectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.Collection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.collections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ViewCollectionItemsPager:
    """A pager for iterating through ``view_collection_items`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ViewCollectionItemsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ViewCollectionItems`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ViewCollectionItemsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., warehouse.ViewCollectionItemsResponse],
        request: warehouse.ViewCollectionItemsRequest,
        response: warehouse.ViewCollectionItemsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ViewCollectionItemsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ViewCollectionItemsResponse):
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
        self._request = warehouse.ViewCollectionItemsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[warehouse.ViewCollectionItemsResponse]:
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

    def __iter__(self) -> Iterator[warehouse.CollectionItem]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ViewCollectionItemsAsyncPager:
    """A pager for iterating through ``view_collection_items`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ViewCollectionItemsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ViewCollectionItems`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ViewCollectionItemsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[warehouse.ViewCollectionItemsResponse]],
        request: warehouse.ViewCollectionItemsRequest,
        response: warehouse.ViewCollectionItemsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ViewCollectionItemsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ViewCollectionItemsResponse):
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
        self._request = warehouse.ViewCollectionItemsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[warehouse.ViewCollectionItemsResponse]:
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

    def __aiter__(self) -> AsyncIterator[warehouse.CollectionItem]:
        async def async_generator():
            async for page in self.pages:
                for response in page.items:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
