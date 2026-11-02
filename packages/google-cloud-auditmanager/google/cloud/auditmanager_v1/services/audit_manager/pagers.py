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

from google.cloud.auditmanager_v1.types import auditmanager


class ListAuditSchedulesPager:
    """A pager for iterating through ``list_audit_schedules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListAuditSchedulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``audit_schedules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuditSchedules`` requests and continue to iterate
    through the ``audit_schedules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListAuditSchedulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auditmanager.ListAuditSchedulesResponse],
        request: auditmanager.ListAuditSchedulesRequest,
        response: auditmanager.ListAuditSchedulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListAuditSchedulesRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListAuditSchedulesResponse):
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
        self._request = auditmanager.ListAuditSchedulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auditmanager.ListAuditSchedulesResponse]:
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

    def __iter__(self) -> Iterator[auditmanager.AuditSchedule]:
        for page in self.pages:
            yield from page.audit_schedules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuditSchedulesAsyncPager:
    """A pager for iterating through ``list_audit_schedules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListAuditSchedulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``audit_schedules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuditSchedules`` requests and continue to iterate
    through the ``audit_schedules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListAuditSchedulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[auditmanager.ListAuditSchedulesResponse]],
        request: auditmanager.ListAuditSchedulesRequest,
        response: auditmanager.ListAuditSchedulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListAuditSchedulesRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListAuditSchedulesResponse):
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
        self._request = auditmanager.ListAuditSchedulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[auditmanager.ListAuditSchedulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[auditmanager.AuditSchedule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.audit_schedules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuditReportsPager:
    """A pager for iterating through ``list_audit_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListAuditReportsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``audit_reports`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuditReports`` requests and continue to iterate
    through the ``audit_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListAuditReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auditmanager.ListAuditReportsResponse],
        request: auditmanager.ListAuditReportsRequest,
        response: auditmanager.ListAuditReportsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListAuditReportsRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListAuditReportsResponse):
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
        self._request = auditmanager.ListAuditReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auditmanager.ListAuditReportsResponse]:
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

    def __iter__(self) -> Iterator[auditmanager.AuditReport]:
        for page in self.pages:
            yield from page.audit_reports

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuditReportsAsyncPager:
    """A pager for iterating through ``list_audit_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListAuditReportsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``audit_reports`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuditReports`` requests and continue to iterate
    through the ``audit_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListAuditReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[auditmanager.ListAuditReportsResponse]],
        request: auditmanager.ListAuditReportsRequest,
        response: auditmanager.ListAuditReportsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListAuditReportsRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListAuditReportsResponse):
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
        self._request = auditmanager.ListAuditReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[auditmanager.ListAuditReportsResponse]:
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

    def __aiter__(self) -> AsyncIterator[auditmanager.AuditReport]:
        async def async_generator():
            async for page in self.pages:
                for response in page.audit_reports:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListResourceEnrollmentStatusesPager:
    """A pager for iterating through ``list_resource_enrollment_statuses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resource_enrollment_statuses`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListResourceEnrollmentStatuses`` requests and continue to iterate
    through the ``resource_enrollment_statuses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auditmanager.ListResourceEnrollmentStatusesResponse],
        request: auditmanager.ListResourceEnrollmentStatusesRequest,
        response: auditmanager.ListResourceEnrollmentStatusesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesResponse):
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
        self._request = auditmanager.ListResourceEnrollmentStatusesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auditmanager.ListResourceEnrollmentStatusesResponse]:
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

    def __iter__(self) -> Iterator[auditmanager.ResourceEnrollmentStatus]:
        for page in self.pages:
            yield from page.resource_enrollment_statuses

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListResourceEnrollmentStatusesAsyncPager:
    """A pager for iterating through ``list_resource_enrollment_statuses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resource_enrollment_statuses`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListResourceEnrollmentStatuses`` requests and continue to iterate
    through the ``resource_enrollment_statuses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[auditmanager.ListResourceEnrollmentStatusesResponse]
        ],
        request: auditmanager.ListResourceEnrollmentStatusesRequest,
        response: auditmanager.ListResourceEnrollmentStatusesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesResponse):
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
        self._request = auditmanager.ListResourceEnrollmentStatusesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[auditmanager.ListResourceEnrollmentStatusesResponse]:
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

    def __aiter__(self) -> AsyncIterator[auditmanager.ResourceEnrollmentStatus]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resource_enrollment_statuses:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListControlsPager:
    """A pager for iterating through ``list_controls`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListControlsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``controls`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListControls`` requests and continue to iterate
    through the ``controls`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListControlsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., auditmanager.ListControlsResponse],
        request: auditmanager.ListControlsRequest,
        response: auditmanager.ListControlsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListControlsRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListControlsResponse):
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
        self._request = auditmanager.ListControlsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[auditmanager.ListControlsResponse]:
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

    def __iter__(self) -> Iterator[auditmanager.Control]:
        for page in self.pages:
            yield from page.controls

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListControlsAsyncPager:
    """A pager for iterating through ``list_controls`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.auditmanager_v1.types.ListControlsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``controls`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListControls`` requests and continue to iterate
    through the ``controls`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.auditmanager_v1.types.ListControlsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[auditmanager.ListControlsResponse]],
        request: auditmanager.ListControlsRequest,
        response: auditmanager.ListControlsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.auditmanager_v1.types.ListControlsRequest):
                The initial request object.
            response (google.cloud.auditmanager_v1.types.ListControlsResponse):
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
        self._request = auditmanager.ListControlsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[auditmanager.ListControlsResponse]:
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

    def __aiter__(self) -> AsyncIterator[auditmanager.Control]:
        async def async_generator():
            async for page in self.pages:
                for response in page.controls:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
