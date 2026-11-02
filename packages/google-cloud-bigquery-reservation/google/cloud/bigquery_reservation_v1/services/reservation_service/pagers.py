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

from google.cloud.bigquery_reservation_v1.types import reservation


class ListReservationsPager:
    """A pager for iterating through ``list_reservations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListReservationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``reservations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReservations`` requests and continue to iterate
    through the ``reservations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListReservationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.ListReservationsResponse],
        request: reservation.ListReservationsRequest,
        response: reservation.ListReservationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListReservationsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListReservationsResponse):
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
        self._request = reservation.ListReservationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[reservation.ListReservationsResponse]:
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

    def __iter__(self) -> Iterator[reservation.Reservation]:
        for page in self.pages:
            yield from page.reservations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReservationsAsyncPager:
    """A pager for iterating through ``list_reservations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListReservationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``reservations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReservations`` requests and continue to iterate
    through the ``reservations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListReservationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.ListReservationsResponse]],
        request: reservation.ListReservationsRequest,
        response: reservation.ListReservationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListReservationsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListReservationsResponse):
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
        self._request = reservation.ListReservationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[reservation.ListReservationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[reservation.Reservation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.reservations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCapacityCommitmentsPager:
    """A pager for iterating through ``list_capacity_commitments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``capacity_commitments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCapacityCommitments`` requests and continue to iterate
    through the ``capacity_commitments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.ListCapacityCommitmentsResponse],
        request: reservation.ListCapacityCommitmentsRequest,
        response: reservation.ListCapacityCommitmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsResponse):
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
        self._request = reservation.ListCapacityCommitmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[reservation.ListCapacityCommitmentsResponse]:
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

    def __iter__(self) -> Iterator[reservation.CapacityCommitment]:
        for page in self.pages:
            yield from page.capacity_commitments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCapacityCommitmentsAsyncPager:
    """A pager for iterating through ``list_capacity_commitments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``capacity_commitments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCapacityCommitments`` requests and continue to iterate
    through the ``capacity_commitments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.ListCapacityCommitmentsResponse]],
        request: reservation.ListCapacityCommitmentsRequest,
        response: reservation.ListCapacityCommitmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListCapacityCommitmentsResponse):
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
        self._request = reservation.ListCapacityCommitmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[reservation.ListCapacityCommitmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[reservation.CapacityCommitment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.capacity_commitments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAssignmentsPager:
    """A pager for iterating through ``list_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListAssignmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.ListAssignmentsResponse],
        request: reservation.ListAssignmentsRequest,
        response: reservation.ListAssignmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListAssignmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListAssignmentsResponse):
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
        self._request = reservation.ListAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[reservation.ListAssignmentsResponse]:
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

    def __iter__(self) -> Iterator[reservation.Assignment]:
        for page in self.pages:
            yield from page.assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAssignmentsAsyncPager:
    """A pager for iterating through ``list_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListAssignmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.ListAssignmentsResponse]],
        request: reservation.ListAssignmentsRequest,
        response: reservation.ListAssignmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListAssignmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListAssignmentsResponse):
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
        self._request = reservation.ListAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[reservation.ListAssignmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[reservation.Assignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAssignmentsPager:
    """A pager for iterating through ``search_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.SearchAssignmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.SearchAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.SearchAssignmentsResponse],
        request: reservation.SearchAssignmentsRequest,
        response: reservation.SearchAssignmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.SearchAssignmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.SearchAssignmentsResponse):
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
        self._request = reservation.SearchAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[reservation.SearchAssignmentsResponse]:
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

    def __iter__(self) -> Iterator[reservation.Assignment]:
        for page in self.pages:
            yield from page.assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAssignmentsAsyncPager:
    """A pager for iterating through ``search_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.SearchAssignmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.SearchAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.SearchAssignmentsResponse]],
        request: reservation.SearchAssignmentsRequest,
        response: reservation.SearchAssignmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.SearchAssignmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.SearchAssignmentsResponse):
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
        self._request = reservation.SearchAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[reservation.SearchAssignmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[reservation.Assignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAllAssignmentsPager:
    """A pager for iterating through ``search_all_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAllAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.SearchAllAssignmentsResponse],
        request: reservation.SearchAllAssignmentsRequest,
        response: reservation.SearchAllAssignmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsResponse):
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
        self._request = reservation.SearchAllAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[reservation.SearchAllAssignmentsResponse]:
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

    def __iter__(self) -> Iterator[reservation.Assignment]:
        for page in self.pages:
            yield from page.assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAllAssignmentsAsyncPager:
    """A pager for iterating through ``search_all_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAllAssignments`` requests and continue to iterate
    through the ``assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.SearchAllAssignmentsResponse]],
        request: reservation.SearchAllAssignmentsRequest,
        response: reservation.SearchAllAssignmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.SearchAllAssignmentsResponse):
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
        self._request = reservation.SearchAllAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[reservation.SearchAllAssignmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[reservation.Assignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReservationGroupsPager:
    """A pager for iterating through ``list_reservation_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListReservationGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``reservation_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReservationGroups`` requests and continue to iterate
    through the ``reservation_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListReservationGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., reservation.ListReservationGroupsResponse],
        request: reservation.ListReservationGroupsRequest,
        response: reservation.ListReservationGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListReservationGroupsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListReservationGroupsResponse):
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
        self._request = reservation.ListReservationGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[reservation.ListReservationGroupsResponse]:
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

    def __iter__(self) -> Iterator[reservation.ReservationGroup]:
        for page in self.pages:
            yield from page.reservation_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReservationGroupsAsyncPager:
    """A pager for iterating through ``list_reservation_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bigquery_reservation_v1.types.ListReservationGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``reservation_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReservationGroups`` requests and continue to iterate
    through the ``reservation_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bigquery_reservation_v1.types.ListReservationGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[reservation.ListReservationGroupsResponse]],
        request: reservation.ListReservationGroupsRequest,
        response: reservation.ListReservationGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bigquery_reservation_v1.types.ListReservationGroupsRequest):
                The initial request object.
            response (google.cloud.bigquery_reservation_v1.types.ListReservationGroupsResponse):
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
        self._request = reservation.ListReservationGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[reservation.ListReservationGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[reservation.ReservationGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.reservation_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
