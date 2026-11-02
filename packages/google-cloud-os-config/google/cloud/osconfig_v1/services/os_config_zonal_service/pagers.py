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

from google.cloud.osconfig_v1.types import (
    inventory,
    os_policy_assignment_reports,
    os_policy_assignments,
    vulnerability,
)


class ListOSPolicyAssignmentsPager:
    """A pager for iterating through ``list_os_policy_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``os_policy_assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOSPolicyAssignments`` requests and continue to iterate
    through the ``os_policy_assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., os_policy_assignments.ListOSPolicyAssignmentsResponse],
        request: os_policy_assignments.ListOSPolicyAssignmentsRequest,
        response: os_policy_assignments.ListOSPolicyAssignmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsResponse):
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
        self._request = os_policy_assignments.ListOSPolicyAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[os_policy_assignments.ListOSPolicyAssignmentsResponse]:
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

    def __iter__(self) -> Iterator[os_policy_assignments.OSPolicyAssignment]:
        for page in self.pages:
            yield from page.os_policy_assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOSPolicyAssignmentsAsyncPager:
    """A pager for iterating through ``list_os_policy_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``os_policy_assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOSPolicyAssignments`` requests and continue to iterate
    through the ``os_policy_assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[os_policy_assignments.ListOSPolicyAssignmentsResponse]
        ],
        request: os_policy_assignments.ListOSPolicyAssignmentsRequest,
        response: os_policy_assignments.ListOSPolicyAssignmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentsResponse):
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
        self._request = os_policy_assignments.ListOSPolicyAssignmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[os_policy_assignments.ListOSPolicyAssignmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[os_policy_assignments.OSPolicyAssignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.os_policy_assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOSPolicyAssignmentRevisionsPager:
    """A pager for iterating through ``list_os_policy_assignment_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``os_policy_assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOSPolicyAssignmentRevisions`` requests and continue to iterate
    through the ``os_policy_assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse
        ],
        request: os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
        response: os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsResponse):
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
        self._request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(
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
    ) -> Iterator[os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse]:
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

    def __iter__(self) -> Iterator[os_policy_assignments.OSPolicyAssignment]:
        for page in self.pages:
            yield from page.os_policy_assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOSPolicyAssignmentRevisionsAsyncPager:
    """A pager for iterating through ``list_os_policy_assignment_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``os_policy_assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOSPolicyAssignmentRevisions`` requests and continue to iterate
    through the ``os_policy_assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse],
        ],
        request: os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest,
        response: os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentRevisionsResponse):
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
        self._request = os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest(
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
    ) -> AsyncIterator[os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[os_policy_assignments.OSPolicyAssignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.os_policy_assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOSPolicyAssignmentReportsPager:
    """A pager for iterating through ``list_os_policy_assignment_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``os_policy_assignment_reports`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOSPolicyAssignmentReports`` requests and continue to iterate
    through the ``os_policy_assignment_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse
        ],
        request: os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
        response: os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsResponse):
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
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(request)
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
    ) -> Iterator[os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[os_policy_assignment_reports.OSPolicyAssignmentReport]:
        for page in self.pages:
            yield from page.os_policy_assignment_reports

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOSPolicyAssignmentReportsAsyncPager:
    """A pager for iterating through ``list_os_policy_assignment_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``os_policy_assignment_reports`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOSPolicyAssignmentReports`` requests and continue to iterate
    through the ``os_policy_assignment_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse
            ],
        ],
        request: os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest,
        response: os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListOSPolicyAssignmentReportsResponse):
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
            os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest(request)
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
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse
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

    def __aiter__(
        self,
    ) -> AsyncIterator[os_policy_assignment_reports.OSPolicyAssignmentReport]:
        async def async_generator():
            async for page in self.pages:
                for response in page.os_policy_assignment_reports:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInventoriesPager:
    """A pager for iterating through ``list_inventories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListInventoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``inventories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInventories`` requests and continue to iterate
    through the ``inventories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListInventoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., inventory.ListInventoriesResponse],
        request: inventory.ListInventoriesRequest,
        response: inventory.ListInventoriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListInventoriesRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListInventoriesResponse):
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
        self._request = inventory.ListInventoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[inventory.ListInventoriesResponse]:
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

    def __iter__(self) -> Iterator[inventory.Inventory]:
        for page in self.pages:
            yield from page.inventories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInventoriesAsyncPager:
    """A pager for iterating through ``list_inventories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListInventoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``inventories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInventories`` requests and continue to iterate
    through the ``inventories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListInventoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[inventory.ListInventoriesResponse]],
        request: inventory.ListInventoriesRequest,
        response: inventory.ListInventoriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListInventoriesRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListInventoriesResponse):
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
        self._request = inventory.ListInventoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[inventory.ListInventoriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[inventory.Inventory]:
        async def async_generator():
            async for page in self.pages:
                for response in page.inventories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVulnerabilityReportsPager:
    """A pager for iterating through ``list_vulnerability_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListVulnerabilityReportsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``vulnerability_reports`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVulnerabilityReports`` requests and continue to iterate
    through the ``vulnerability_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListVulnerabilityReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., vulnerability.ListVulnerabilityReportsResponse],
        request: vulnerability.ListVulnerabilityReportsRequest,
        response: vulnerability.ListVulnerabilityReportsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListVulnerabilityReportsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListVulnerabilityReportsResponse):
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
        self._request = vulnerability.ListVulnerabilityReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[vulnerability.ListVulnerabilityReportsResponse]:
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

    def __iter__(self) -> Iterator[vulnerability.VulnerabilityReport]:
        for page in self.pages:
            yield from page.vulnerability_reports

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVulnerabilityReportsAsyncPager:
    """A pager for iterating through ``list_vulnerability_reports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListVulnerabilityReportsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``vulnerability_reports`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVulnerabilityReports`` requests and continue to iterate
    through the ``vulnerability_reports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListVulnerabilityReportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[vulnerability.ListVulnerabilityReportsResponse]
        ],
        request: vulnerability.ListVulnerabilityReportsRequest,
        response: vulnerability.ListVulnerabilityReportsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListVulnerabilityReportsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListVulnerabilityReportsResponse):
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
        self._request = vulnerability.ListVulnerabilityReportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[vulnerability.ListVulnerabilityReportsResponse]:
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

    def __aiter__(self) -> AsyncIterator[vulnerability.VulnerabilityReport]:
        async def async_generator():
            async for page in self.pages:
                for response in page.vulnerability_reports:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
