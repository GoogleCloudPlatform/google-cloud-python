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

from google.cloud.dlp_v2.types import dlp


class ListInspectTemplatesPager:
    """A pager for iterating through ``list_inspect_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListInspectTemplatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``inspect_templates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInspectTemplates`` requests and continue to iterate
    through the ``inspect_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListInspectTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListInspectTemplatesResponse],
        request: dlp.ListInspectTemplatesRequest,
        response: dlp.ListInspectTemplatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListInspectTemplatesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListInspectTemplatesResponse):
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
        self._request = dlp.ListInspectTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListInspectTemplatesResponse]:
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

    def __iter__(self) -> Iterator[dlp.InspectTemplate]:
        for page in self.pages:
            yield from page.inspect_templates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInspectTemplatesAsyncPager:
    """A pager for iterating through ``list_inspect_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListInspectTemplatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``inspect_templates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInspectTemplates`` requests and continue to iterate
    through the ``inspect_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListInspectTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListInspectTemplatesResponse]],
        request: dlp.ListInspectTemplatesRequest,
        response: dlp.ListInspectTemplatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListInspectTemplatesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListInspectTemplatesResponse):
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
        self._request = dlp.ListInspectTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListInspectTemplatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.InspectTemplate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.inspect_templates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeidentifyTemplatesPager:
    """A pager for iterating through ``list_deidentify_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListDeidentifyTemplatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deidentify_templates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeidentifyTemplates`` requests and continue to iterate
    through the ``deidentify_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListDeidentifyTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListDeidentifyTemplatesResponse],
        request: dlp.ListDeidentifyTemplatesRequest,
        response: dlp.ListDeidentifyTemplatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListDeidentifyTemplatesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListDeidentifyTemplatesResponse):
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
        self._request = dlp.ListDeidentifyTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListDeidentifyTemplatesResponse]:
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

    def __iter__(self) -> Iterator[dlp.DeidentifyTemplate]:
        for page in self.pages:
            yield from page.deidentify_templates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeidentifyTemplatesAsyncPager:
    """A pager for iterating through ``list_deidentify_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListDeidentifyTemplatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deidentify_templates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeidentifyTemplates`` requests and continue to iterate
    through the ``deidentify_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListDeidentifyTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListDeidentifyTemplatesResponse]],
        request: dlp.ListDeidentifyTemplatesRequest,
        response: dlp.ListDeidentifyTemplatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListDeidentifyTemplatesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListDeidentifyTemplatesResponse):
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
        self._request = dlp.ListDeidentifyTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListDeidentifyTemplatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.DeidentifyTemplate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deidentify_templates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobTriggersPager:
    """A pager for iterating through ``list_job_triggers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListJobTriggersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``job_triggers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListJobTriggers`` requests and continue to iterate
    through the ``job_triggers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListJobTriggersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListJobTriggersResponse],
        request: dlp.ListJobTriggersRequest,
        response: dlp.ListJobTriggersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListJobTriggersRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListJobTriggersResponse):
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
        self._request = dlp.ListJobTriggersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListJobTriggersResponse]:
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

    def __iter__(self) -> Iterator[dlp.JobTrigger]:
        for page in self.pages:
            yield from page.job_triggers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobTriggersAsyncPager:
    """A pager for iterating through ``list_job_triggers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListJobTriggersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``job_triggers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListJobTriggers`` requests and continue to iterate
    through the ``job_triggers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListJobTriggersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListJobTriggersResponse]],
        request: dlp.ListJobTriggersRequest,
        response: dlp.ListJobTriggersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListJobTriggersRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListJobTriggersResponse):
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
        self._request = dlp.ListJobTriggersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListJobTriggersResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.JobTrigger]:
        async def async_generator():
            async for page in self.pages:
                for response in page.job_triggers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDiscoveryConfigsPager:
    """A pager for iterating through ``list_discovery_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListDiscoveryConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``discovery_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDiscoveryConfigs`` requests and continue to iterate
    through the ``discovery_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListDiscoveryConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListDiscoveryConfigsResponse],
        request: dlp.ListDiscoveryConfigsRequest,
        response: dlp.ListDiscoveryConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListDiscoveryConfigsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListDiscoveryConfigsResponse):
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
        self._request = dlp.ListDiscoveryConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListDiscoveryConfigsResponse]:
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

    def __iter__(self) -> Iterator[dlp.DiscoveryConfig]:
        for page in self.pages:
            yield from page.discovery_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDiscoveryConfigsAsyncPager:
    """A pager for iterating through ``list_discovery_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListDiscoveryConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``discovery_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDiscoveryConfigs`` requests and continue to iterate
    through the ``discovery_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListDiscoveryConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListDiscoveryConfigsResponse]],
        request: dlp.ListDiscoveryConfigsRequest,
        response: dlp.ListDiscoveryConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListDiscoveryConfigsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListDiscoveryConfigsResponse):
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
        self._request = dlp.ListDiscoveryConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListDiscoveryConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.DiscoveryConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.discovery_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDlpJobsPager:
    """A pager for iterating through ``list_dlp_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListDlpJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDlpJobs`` requests and continue to iterate
    through the ``jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListDlpJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListDlpJobsResponse],
        request: dlp.ListDlpJobsRequest,
        response: dlp.ListDlpJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListDlpJobsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListDlpJobsResponse):
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
        self._request = dlp.ListDlpJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListDlpJobsResponse]:
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

    def __iter__(self) -> Iterator[dlp.DlpJob]:
        for page in self.pages:
            yield from page.jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDlpJobsAsyncPager:
    """A pager for iterating through ``list_dlp_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListDlpJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDlpJobs`` requests and continue to iterate
    through the ``jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListDlpJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListDlpJobsResponse]],
        request: dlp.ListDlpJobsRequest,
        response: dlp.ListDlpJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListDlpJobsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListDlpJobsResponse):
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
        self._request = dlp.ListDlpJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListDlpJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.DlpJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStoredInfoTypesPager:
    """A pager for iterating through ``list_stored_info_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListStoredInfoTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``stored_info_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStoredInfoTypes`` requests and continue to iterate
    through the ``stored_info_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListStoredInfoTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListStoredInfoTypesResponse],
        request: dlp.ListStoredInfoTypesRequest,
        response: dlp.ListStoredInfoTypesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListStoredInfoTypesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListStoredInfoTypesResponse):
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
        self._request = dlp.ListStoredInfoTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListStoredInfoTypesResponse]:
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

    def __iter__(self) -> Iterator[dlp.StoredInfoType]:
        for page in self.pages:
            yield from page.stored_info_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStoredInfoTypesAsyncPager:
    """A pager for iterating through ``list_stored_info_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListStoredInfoTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``stored_info_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStoredInfoTypes`` requests and continue to iterate
    through the ``stored_info_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListStoredInfoTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListStoredInfoTypesResponse]],
        request: dlp.ListStoredInfoTypesRequest,
        response: dlp.ListStoredInfoTypesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListStoredInfoTypesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListStoredInfoTypesResponse):
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
        self._request = dlp.ListStoredInfoTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListStoredInfoTypesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.StoredInfoType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.stored_info_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProjectDataProfilesPager:
    """A pager for iterating through ``list_project_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListProjectDataProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``project_data_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProjectDataProfiles`` requests and continue to iterate
    through the ``project_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListProjectDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListProjectDataProfilesResponse],
        request: dlp.ListProjectDataProfilesRequest,
        response: dlp.ListProjectDataProfilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListProjectDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListProjectDataProfilesResponse):
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
        self._request = dlp.ListProjectDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListProjectDataProfilesResponse]:
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

    def __iter__(self) -> Iterator[dlp.ProjectDataProfile]:
        for page in self.pages:
            yield from page.project_data_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProjectDataProfilesAsyncPager:
    """A pager for iterating through ``list_project_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListProjectDataProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``project_data_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProjectDataProfiles`` requests and continue to iterate
    through the ``project_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListProjectDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListProjectDataProfilesResponse]],
        request: dlp.ListProjectDataProfilesRequest,
        response: dlp.ListProjectDataProfilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListProjectDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListProjectDataProfilesResponse):
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
        self._request = dlp.ListProjectDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListProjectDataProfilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.ProjectDataProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.project_data_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTableDataProfilesPager:
    """A pager for iterating through ``list_table_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListTableDataProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``table_data_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTableDataProfiles`` requests and continue to iterate
    through the ``table_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListTableDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListTableDataProfilesResponse],
        request: dlp.ListTableDataProfilesRequest,
        response: dlp.ListTableDataProfilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListTableDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListTableDataProfilesResponse):
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
        self._request = dlp.ListTableDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListTableDataProfilesResponse]:
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

    def __iter__(self) -> Iterator[dlp.TableDataProfile]:
        for page in self.pages:
            yield from page.table_data_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTableDataProfilesAsyncPager:
    """A pager for iterating through ``list_table_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListTableDataProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``table_data_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTableDataProfiles`` requests and continue to iterate
    through the ``table_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListTableDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListTableDataProfilesResponse]],
        request: dlp.ListTableDataProfilesRequest,
        response: dlp.ListTableDataProfilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListTableDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListTableDataProfilesResponse):
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
        self._request = dlp.ListTableDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListTableDataProfilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.TableDataProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.table_data_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListColumnDataProfilesPager:
    """A pager for iterating through ``list_column_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListColumnDataProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``column_data_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListColumnDataProfiles`` requests and continue to iterate
    through the ``column_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListColumnDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListColumnDataProfilesResponse],
        request: dlp.ListColumnDataProfilesRequest,
        response: dlp.ListColumnDataProfilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListColumnDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListColumnDataProfilesResponse):
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
        self._request = dlp.ListColumnDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListColumnDataProfilesResponse]:
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

    def __iter__(self) -> Iterator[dlp.ColumnDataProfile]:
        for page in self.pages:
            yield from page.column_data_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListColumnDataProfilesAsyncPager:
    """A pager for iterating through ``list_column_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListColumnDataProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``column_data_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListColumnDataProfiles`` requests and continue to iterate
    through the ``column_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListColumnDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListColumnDataProfilesResponse]],
        request: dlp.ListColumnDataProfilesRequest,
        response: dlp.ListColumnDataProfilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListColumnDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListColumnDataProfilesResponse):
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
        self._request = dlp.ListColumnDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListColumnDataProfilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.ColumnDataProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.column_data_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFileStoreDataProfilesPager:
    """A pager for iterating through ``list_file_store_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListFileStoreDataProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``file_store_data_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFileStoreDataProfiles`` requests and continue to iterate
    through the ``file_store_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListFileStoreDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListFileStoreDataProfilesResponse],
        request: dlp.ListFileStoreDataProfilesRequest,
        response: dlp.ListFileStoreDataProfilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListFileStoreDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListFileStoreDataProfilesResponse):
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
        self._request = dlp.ListFileStoreDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListFileStoreDataProfilesResponse]:
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

    def __iter__(self) -> Iterator[dlp.FileStoreDataProfile]:
        for page in self.pages:
            yield from page.file_store_data_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFileStoreDataProfilesAsyncPager:
    """A pager for iterating through ``list_file_store_data_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListFileStoreDataProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``file_store_data_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFileStoreDataProfiles`` requests and continue to iterate
    through the ``file_store_data_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListFileStoreDataProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListFileStoreDataProfilesResponse]],
        request: dlp.ListFileStoreDataProfilesRequest,
        response: dlp.ListFileStoreDataProfilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListFileStoreDataProfilesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListFileStoreDataProfilesResponse):
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
        self._request = dlp.ListFileStoreDataProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListFileStoreDataProfilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.FileStoreDataProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.file_store_data_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionsPager:
    """A pager for iterating through ``list_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListConnectionsResponse],
        request: dlp.ListConnectionsRequest,
        response: dlp.ListConnectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListConnectionsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListConnectionsResponse):
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
        self._request = dlp.ListConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListConnectionsResponse]:
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

    def __iter__(self) -> Iterator[dlp.Connection]:
        for page in self.pages:
            yield from page.connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionsAsyncPager:
    """A pager for iterating through ``list_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListConnectionsResponse]],
        request: dlp.ListConnectionsRequest,
        response: dlp.ListConnectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListConnectionsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListConnectionsResponse):
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
        self._request = dlp.ListConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListConnectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.Connection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchConnectionsPager:
    """A pager for iterating through ``search_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.SearchConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.SearchConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.SearchConnectionsResponse],
        request: dlp.SearchConnectionsRequest,
        response: dlp.SearchConnectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.SearchConnectionsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.SearchConnectionsResponse):
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
        self._request = dlp.SearchConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.SearchConnectionsResponse]:
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

    def __iter__(self) -> Iterator[dlp.Connection]:
        for page in self.pages:
            yield from page.connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchConnectionsAsyncPager:
    """A pager for iterating through ``search_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.SearchConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.SearchConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.SearchConnectionsResponse]],
        request: dlp.SearchConnectionsRequest,
        response: dlp.SearchConnectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.SearchConnectionsRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.SearchConnectionsResponse):
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
        self._request = dlp.SearchConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.SearchConnectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.Connection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListContentPoliciesPager:
    """A pager for iterating through ``list_content_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListContentPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``content_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListContentPolicies`` requests and continue to iterate
    through the ``content_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListContentPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., dlp.ListContentPoliciesResponse],
        request: dlp.ListContentPoliciesRequest,
        response: dlp.ListContentPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListContentPoliciesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListContentPoliciesResponse):
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
        self._request = dlp.ListContentPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[dlp.ListContentPoliciesResponse]:
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

    def __iter__(self) -> Iterator[dlp.ContentPolicy]:
        for page in self.pages:
            yield from page.content_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListContentPoliciesAsyncPager:
    """A pager for iterating through ``list_content_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dlp_v2.types.ListContentPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``content_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListContentPolicies`` requests and continue to iterate
    through the ``content_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dlp_v2.types.ListContentPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[dlp.ListContentPoliciesResponse]],
        request: dlp.ListContentPoliciesRequest,
        response: dlp.ListContentPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dlp_v2.types.ListContentPoliciesRequest):
                The initial request object.
            response (google.cloud.dlp_v2.types.ListContentPoliciesResponse):
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
        self._request = dlp.ListContentPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[dlp.ListContentPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dlp.ContentPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.content_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
