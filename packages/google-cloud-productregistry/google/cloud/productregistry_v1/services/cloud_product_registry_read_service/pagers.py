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

from google.cloud.productregistry_v1.types import (
    cloud_product_registry_read_service,
    logical_product,
    logical_product_variant,
    product_suite,
)


class ListProductSuitesPager:
    """A pager for iterating through ``list_product_suites`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.productregistry_v1.types.ListProductSuitesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``product_suites`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProductSuites`` requests and continue to iterate
    through the ``product_suites`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.productregistry_v1.types.ListProductSuitesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., cloud_product_registry_read_service.ListProductSuitesResponse
        ],
        request: cloud_product_registry_read_service.ListProductSuitesRequest,
        response: cloud_product_registry_read_service.ListProductSuitesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.productregistry_v1.types.ListProductSuitesRequest):
                The initial request object.
            response (google.cloud.productregistry_v1.types.ListProductSuitesResponse):
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
        self._request = cloud_product_registry_read_service.ListProductSuitesRequest(
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
    ) -> Iterator[cloud_product_registry_read_service.ListProductSuitesResponse]:
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

    def __iter__(self) -> Iterator[product_suite.ProductSuite]:
        for page in self.pages:
            yield from page.product_suites

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProductSuitesAsyncPager:
    """A pager for iterating through ``list_product_suites`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.productregistry_v1.types.ListProductSuitesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``product_suites`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProductSuites`` requests and continue to iterate
    through the ``product_suites`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.productregistry_v1.types.ListProductSuitesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[cloud_product_registry_read_service.ListProductSuitesResponse],
        ],
        request: cloud_product_registry_read_service.ListProductSuitesRequest,
        response: cloud_product_registry_read_service.ListProductSuitesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.productregistry_v1.types.ListProductSuitesRequest):
                The initial request object.
            response (google.cloud.productregistry_v1.types.ListProductSuitesResponse):
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
        self._request = cloud_product_registry_read_service.ListProductSuitesRequest(
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
    ) -> AsyncIterator[cloud_product_registry_read_service.ListProductSuitesResponse]:
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

    def __aiter__(self) -> AsyncIterator[product_suite.ProductSuite]:
        async def async_generator():
            async for page in self.pages:
                for response in page.product_suites:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLogicalProductsPager:
    """A pager for iterating through ``list_logical_products`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.productregistry_v1.types.ListLogicalProductsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``logical_products`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLogicalProducts`` requests and continue to iterate
    through the ``logical_products`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.productregistry_v1.types.ListLogicalProductsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., cloud_product_registry_read_service.ListLogicalProductsResponse
        ],
        request: cloud_product_registry_read_service.ListLogicalProductsRequest,
        response: cloud_product_registry_read_service.ListLogicalProductsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.productregistry_v1.types.ListLogicalProductsRequest):
                The initial request object.
            response (google.cloud.productregistry_v1.types.ListLogicalProductsResponse):
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
        self._request = cloud_product_registry_read_service.ListLogicalProductsRequest(
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
    ) -> Iterator[cloud_product_registry_read_service.ListLogicalProductsResponse]:
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

    def __iter__(self) -> Iterator[logical_product.LogicalProduct]:
        for page in self.pages:
            yield from page.logical_products

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLogicalProductsAsyncPager:
    """A pager for iterating through ``list_logical_products`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.productregistry_v1.types.ListLogicalProductsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``logical_products`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLogicalProducts`` requests and continue to iterate
    through the ``logical_products`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.productregistry_v1.types.ListLogicalProductsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[cloud_product_registry_read_service.ListLogicalProductsResponse],
        ],
        request: cloud_product_registry_read_service.ListLogicalProductsRequest,
        response: cloud_product_registry_read_service.ListLogicalProductsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.productregistry_v1.types.ListLogicalProductsRequest):
                The initial request object.
            response (google.cloud.productregistry_v1.types.ListLogicalProductsResponse):
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
        self._request = cloud_product_registry_read_service.ListLogicalProductsRequest(
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
    ) -> AsyncIterator[cloud_product_registry_read_service.ListLogicalProductsResponse]:
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

    def __aiter__(self) -> AsyncIterator[logical_product.LogicalProduct]:
        async def async_generator():
            async for page in self.pages:
                for response in page.logical_products:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLogicalProductVariantsPager:
    """A pager for iterating through ``list_logical_product_variants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.productregistry_v1.types.ListLogicalProductVariantsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``logical_product_variants`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLogicalProductVariants`` requests and continue to iterate
    through the ``logical_product_variants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.productregistry_v1.types.ListLogicalProductVariantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., cloud_product_registry_read_service.ListLogicalProductVariantsResponse
        ],
        request: cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
        response: cloud_product_registry_read_service.ListLogicalProductVariantsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.productregistry_v1.types.ListLogicalProductVariantsRequest):
                The initial request object.
            response (google.cloud.productregistry_v1.types.ListLogicalProductVariantsResponse):
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
        self._request = (
            cloud_product_registry_read_service.ListLogicalProductVariantsRequest(
                request
            )
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
    ) -> Iterator[
        cloud_product_registry_read_service.ListLogicalProductVariantsResponse
    ]:
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

    def __iter__(self) -> Iterator[logical_product_variant.LogicalProductVariant]:
        for page in self.pages:
            yield from page.logical_product_variants

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLogicalProductVariantsAsyncPager:
    """A pager for iterating through ``list_logical_product_variants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.productregistry_v1.types.ListLogicalProductVariantsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``logical_product_variants`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLogicalProductVariants`` requests and continue to iterate
    through the ``logical_product_variants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.productregistry_v1.types.ListLogicalProductVariantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                cloud_product_registry_read_service.ListLogicalProductVariantsResponse
            ],
        ],
        request: cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
        response: cloud_product_registry_read_service.ListLogicalProductVariantsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.productregistry_v1.types.ListLogicalProductVariantsRequest):
                The initial request object.
            response (google.cloud.productregistry_v1.types.ListLogicalProductVariantsResponse):
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
        self._request = (
            cloud_product_registry_read_service.ListLogicalProductVariantsRequest(
                request
            )
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
    ) -> AsyncIterator[
        cloud_product_registry_read_service.ListLogicalProductVariantsResponse
    ]:
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

    def __aiter__(self) -> AsyncIterator[logical_product_variant.LogicalProductVariant]:
        async def async_generator():
            async for page in self.pages:
                for response in page.logical_product_variants:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
