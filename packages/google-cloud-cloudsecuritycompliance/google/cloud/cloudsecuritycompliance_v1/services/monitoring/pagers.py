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

from google.cloud.cloudsecuritycompliance_v1.types import monitoring


class ListFrameworkComplianceSummariesPager:
    """A pager for iterating through ``list_framework_compliance_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``framework_compliance_summaries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFrameworkComplianceSummaries`` requests and continue to iterate
    through the ``framework_compliance_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., monitoring.ListFrameworkComplianceSummariesResponse],
        request: monitoring.ListFrameworkComplianceSummariesRequest,
        response: monitoring.ListFrameworkComplianceSummariesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesRequest):
                The initial request object.
            response (google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesResponse):
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
        self._request = monitoring.ListFrameworkComplianceSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[monitoring.ListFrameworkComplianceSummariesResponse]:
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

    def __iter__(self) -> Iterator[monitoring.FrameworkComplianceSummary]:
        for page in self.pages:
            yield from page.framework_compliance_summaries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFrameworkComplianceSummariesAsyncPager:
    """A pager for iterating through ``list_framework_compliance_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``framework_compliance_summaries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFrameworkComplianceSummaries`` requests and continue to iterate
    through the ``framework_compliance_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[monitoring.ListFrameworkComplianceSummariesResponse]
        ],
        request: monitoring.ListFrameworkComplianceSummariesRequest,
        response: monitoring.ListFrameworkComplianceSummariesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesRequest):
                The initial request object.
            response (google.cloud.cloudsecuritycompliance_v1.types.ListFrameworkComplianceSummariesResponse):
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
        self._request = monitoring.ListFrameworkComplianceSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[monitoring.ListFrameworkComplianceSummariesResponse]:
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

    def __aiter__(self) -> AsyncIterator[monitoring.FrameworkComplianceSummary]:
        async def async_generator():
            async for page in self.pages:
                for response in page.framework_compliance_summaries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFindingSummariesPager:
    """A pager for iterating through ``list_finding_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``finding_summaries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFindingSummaries`` requests and continue to iterate
    through the ``finding_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., monitoring.ListFindingSummariesResponse],
        request: monitoring.ListFindingSummariesRequest,
        response: monitoring.ListFindingSummariesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesRequest):
                The initial request object.
            response (google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesResponse):
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
        self._request = monitoring.ListFindingSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[monitoring.ListFindingSummariesResponse]:
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

    def __iter__(self) -> Iterator[monitoring.FindingSummary]:
        for page in self.pages:
            yield from page.finding_summaries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFindingSummariesAsyncPager:
    """A pager for iterating through ``list_finding_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``finding_summaries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFindingSummaries`` requests and continue to iterate
    through the ``finding_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[monitoring.ListFindingSummariesResponse]],
        request: monitoring.ListFindingSummariesRequest,
        response: monitoring.ListFindingSummariesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesRequest):
                The initial request object.
            response (google.cloud.cloudsecuritycompliance_v1.types.ListFindingSummariesResponse):
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
        self._request = monitoring.ListFindingSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[monitoring.ListFindingSummariesResponse]:
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

    def __aiter__(self) -> AsyncIterator[monitoring.FindingSummary]:
        async def async_generator():
            async for page in self.pages:
                for response in page.finding_summaries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListControlComplianceSummariesPager:
    """A pager for iterating through ``list_control_compliance_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``control_compliance_summaries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListControlComplianceSummaries`` requests and continue to iterate
    through the ``control_compliance_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., monitoring.ListControlComplianceSummariesResponse],
        request: monitoring.ListControlComplianceSummariesRequest,
        response: monitoring.ListControlComplianceSummariesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesRequest):
                The initial request object.
            response (google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesResponse):
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
        self._request = monitoring.ListControlComplianceSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[monitoring.ListControlComplianceSummariesResponse]:
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

    def __iter__(self) -> Iterator[monitoring.ControlComplianceSummary]:
        for page in self.pages:
            yield from page.control_compliance_summaries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListControlComplianceSummariesAsyncPager:
    """A pager for iterating through ``list_control_compliance_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``control_compliance_summaries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListControlComplianceSummaries`` requests and continue to iterate
    through the ``control_compliance_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[monitoring.ListControlComplianceSummariesResponse]
        ],
        request: monitoring.ListControlComplianceSummariesRequest,
        response: monitoring.ListControlComplianceSummariesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesRequest):
                The initial request object.
            response (google.cloud.cloudsecuritycompliance_v1.types.ListControlComplianceSummariesResponse):
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
        self._request = monitoring.ListControlComplianceSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[monitoring.ListControlComplianceSummariesResponse]:
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

    def __aiter__(self) -> AsyncIterator[monitoring.ControlComplianceSummary]:
        async def async_generator():
            async for page in self.pages:
                for response in page.control_compliance_summaries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
