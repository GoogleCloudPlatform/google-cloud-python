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

from google.cloud.commerceproducer_v1beta.types import (
    commerce_transaction,
    private_offer,
    service,
    sku,
    sku_group,
    standard_offer,
)


class ListServicesPager:
    """A pager for iterating through ``list_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListServicesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., commerce_transaction.ListServicesResponse],
        request: commerce_transaction.ListServicesRequest,
        response: commerce_transaction.ListServicesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListServicesResponse):
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
        self._request = commerce_transaction.ListServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[commerce_transaction.ListServicesResponse]:
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

    def __iter__(self) -> Iterator[service.Service]:
        for page in self.pages:
            yield from page.services

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServicesAsyncPager:
    """A pager for iterating through ``list_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListServicesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[commerce_transaction.ListServicesResponse]],
        request: commerce_transaction.ListServicesRequest,
        response: commerce_transaction.ListServicesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListServicesResponse):
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
        self._request = commerce_transaction.ListServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[commerce_transaction.ListServicesResponse]:
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

    def __aiter__(self) -> AsyncIterator[service.Service]:
        async def async_generator():
            async for page in self.pages:
                for response in page.services:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateOffersPager:
    """A pager for iterating through ``list_private_offers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOffersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``private_offers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPrivateOffers`` requests and continue to iterate
    through the ``private_offers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOffersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., commerce_transaction.ListPrivateOffersResponse],
        request: commerce_transaction.ListPrivateOffersRequest,
        response: commerce_transaction.ListPrivateOffersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListPrivateOffersRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListPrivateOffersResponse):
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
        self._request = commerce_transaction.ListPrivateOffersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[commerce_transaction.ListPrivateOffersResponse]:
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

    def __iter__(self) -> Iterator[private_offer.PrivateOffer]:
        for page in self.pages:
            yield from page.private_offers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateOffersAsyncPager:
    """A pager for iterating through ``list_private_offers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOffersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``private_offers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPrivateOffers`` requests and continue to iterate
    through the ``private_offers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOffersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[commerce_transaction.ListPrivateOffersResponse]
        ],
        request: commerce_transaction.ListPrivateOffersRequest,
        response: commerce_transaction.ListPrivateOffersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListPrivateOffersRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListPrivateOffersResponse):
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
        self._request = commerce_transaction.ListPrivateOffersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[commerce_transaction.ListPrivateOffersResponse]:
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

    def __aiter__(self) -> AsyncIterator[private_offer.PrivateOffer]:
        async def async_generator():
            async for page in self.pages:
                for response in page.private_offers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateOfferDocumentsPager:
    """A pager for iterating through ``list_private_offer_documents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``private_offer_documents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPrivateOfferDocuments`` requests and continue to iterate
    through the ``private_offer_documents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., commerce_transaction.ListPrivateOfferDocumentsResponse],
        request: commerce_transaction.ListPrivateOfferDocumentsRequest,
        response: commerce_transaction.ListPrivateOfferDocumentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsResponse):
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
        self._request = commerce_transaction.ListPrivateOfferDocumentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[commerce_transaction.ListPrivateOfferDocumentsResponse]:
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

    def __iter__(self) -> Iterator[private_offer.PrivateOfferDocument]:
        for page in self.pages:
            yield from page.private_offer_documents

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateOfferDocumentsAsyncPager:
    """A pager for iterating through ``list_private_offer_documents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``private_offer_documents`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPrivateOfferDocuments`` requests and continue to iterate
    through the ``private_offer_documents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[commerce_transaction.ListPrivateOfferDocumentsResponse]
        ],
        request: commerce_transaction.ListPrivateOfferDocumentsRequest,
        response: commerce_transaction.ListPrivateOfferDocumentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListPrivateOfferDocumentsResponse):
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
        self._request = commerce_transaction.ListPrivateOfferDocumentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[commerce_transaction.ListPrivateOfferDocumentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[private_offer.PrivateOfferDocument]:
        async def async_generator():
            async for page in self.pages:
                for response in page.private_offer_documents:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStandardOffersPager:
    """A pager for iterating through ``list_standard_offers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListStandardOffersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``standard_offers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStandardOffers`` requests and continue to iterate
    through the ``standard_offers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListStandardOffersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., commerce_transaction.ListStandardOffersResponse],
        request: commerce_transaction.ListStandardOffersRequest,
        response: commerce_transaction.ListStandardOffersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListStandardOffersRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListStandardOffersResponse):
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
        self._request = commerce_transaction.ListStandardOffersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[commerce_transaction.ListStandardOffersResponse]:
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

    def __iter__(self) -> Iterator[standard_offer.StandardOffer]:
        for page in self.pages:
            yield from page.standard_offers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStandardOffersAsyncPager:
    """A pager for iterating through ``list_standard_offers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListStandardOffersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``standard_offers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStandardOffers`` requests and continue to iterate
    through the ``standard_offers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListStandardOffersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[commerce_transaction.ListStandardOffersResponse]
        ],
        request: commerce_transaction.ListStandardOffersRequest,
        response: commerce_transaction.ListStandardOffersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListStandardOffersRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListStandardOffersResponse):
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
        self._request = commerce_transaction.ListStandardOffersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[commerce_transaction.ListStandardOffersResponse]:
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

    def __aiter__(self) -> AsyncIterator[standard_offer.StandardOffer]:
        async def async_generator():
            async for page in self.pages:
                for response in page.standard_offers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSkusPager:
    """A pager for iterating through ``list_skus`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListSkusResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``skus`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSkus`` requests and continue to iterate
    through the ``skus`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListSkusResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., commerce_transaction.ListSkusResponse],
        request: commerce_transaction.ListSkusRequest,
        response: commerce_transaction.ListSkusResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListSkusRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListSkusResponse):
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
        self._request = commerce_transaction.ListSkusRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[commerce_transaction.ListSkusResponse]:
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

    def __iter__(self) -> Iterator[sku.Sku]:
        for page in self.pages:
            yield from page.skus

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSkusAsyncPager:
    """A pager for iterating through ``list_skus`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListSkusResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``skus`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSkus`` requests and continue to iterate
    through the ``skus`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListSkusResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[commerce_transaction.ListSkusResponse]],
        request: commerce_transaction.ListSkusRequest,
        response: commerce_transaction.ListSkusResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListSkusRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListSkusResponse):
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
        self._request = commerce_transaction.ListSkusRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[commerce_transaction.ListSkusResponse]:
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

    def __aiter__(self) -> AsyncIterator[sku.Sku]:
        async def async_generator():
            async for page in self.pages:
                for response in page.skus:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSkuGroupsPager:
    """A pager for iterating through ``list_sku_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListSkuGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``sku_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSkuGroups`` requests and continue to iterate
    through the ``sku_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListSkuGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., commerce_transaction.ListSkuGroupsResponse],
        request: commerce_transaction.ListSkuGroupsRequest,
        response: commerce_transaction.ListSkuGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListSkuGroupsRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListSkuGroupsResponse):
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
        self._request = commerce_transaction.ListSkuGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[commerce_transaction.ListSkuGroupsResponse]:
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

    def __iter__(self) -> Iterator[sku_group.SkuGroup]:
        for page in self.pages:
            yield from page.sku_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSkuGroupsAsyncPager:
    """A pager for iterating through ``list_sku_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.commerceproducer_v1beta.types.ListSkuGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``sku_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSkuGroups`` requests and continue to iterate
    through the ``sku_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.commerceproducer_v1beta.types.ListSkuGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[commerce_transaction.ListSkuGroupsResponse]],
        request: commerce_transaction.ListSkuGroupsRequest,
        response: commerce_transaction.ListSkuGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.commerceproducer_v1beta.types.ListSkuGroupsRequest):
                The initial request object.
            response (google.cloud.commerceproducer_v1beta.types.ListSkuGroupsResponse):
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
        self._request = commerce_transaction.ListSkuGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[commerce_transaction.ListSkuGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[sku_group.SkuGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.sku_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
