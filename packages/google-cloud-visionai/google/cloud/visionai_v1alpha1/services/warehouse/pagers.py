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

from google.cloud.visionai_v1alpha1.types import warehouse


class ListAssetsPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1alpha1.types.ListAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListAssetsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListAssetsResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListAssetsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListAssetsResponse):
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


class ListCorporaPager:
    """A pager for iterating through ``list_corpora`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1alpha1.types.ListCorporaResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListCorporaResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListCorporaRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListCorporaResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListCorporaResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListCorporaResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListCorporaRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListCorporaResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListDataSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataSchemas`` requests and continue to iterate
    through the ``data_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListDataSchemasResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListDataSchemasRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListDataSchemasResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListDataSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataSchemas`` requests and continue to iterate
    through the ``data_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListDataSchemasResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListDataSchemasRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListDataSchemasResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListAnnotationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``annotations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnnotations`` requests and continue to iterate
    through the ``annotations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListAnnotationsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListAnnotationsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListAnnotationsResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListAnnotationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``annotations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnnotations`` requests and continue to iterate
    through the ``annotations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListAnnotationsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListAnnotationsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListAnnotationsResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListSearchConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSearchConfigs`` requests and continue to iterate
    through the ``search_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListSearchConfigsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListSearchConfigsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListSearchConfigsResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.ListSearchConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSearchConfigs`` requests and continue to iterate
    through the ``search_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.ListSearchConfigsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.ListSearchConfigsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.ListSearchConfigsResponse):
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


class SearchAssetsPager:
    """A pager for iterating through ``search_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1alpha1.types.SearchAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_result_items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAssets`` requests and continue to iterate
    through the ``search_result_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.SearchAssetsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.SearchAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.SearchAssetsResponse):
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
    :class:`google.cloud.visionai_v1alpha1.types.SearchAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_result_items`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAssets`` requests and continue to iterate
    through the ``search_result_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1alpha1.types.SearchAssetsResponse`
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
            request (google.cloud.visionai_v1alpha1.types.SearchAssetsRequest):
                The initial request object.
            response (google.cloud.visionai_v1alpha1.types.SearchAssetsResponse):
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
