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

from google.cloud.apphub_v1.types import (
    apphub_service,
    application,
    extended_metadata_schema,
    service,
    service_project_attachment,
    workload,
)


class ListServiceProjectAttachmentsPager:
    """A pager for iterating through ``list_service_project_attachments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListServiceProjectAttachmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``service_project_attachments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServiceProjectAttachments`` requests and continue to iterate
    through the ``service_project_attachments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListServiceProjectAttachmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apphub_service.ListServiceProjectAttachmentsResponse],
        request: apphub_service.ListServiceProjectAttachmentsRequest,
        response: apphub_service.ListServiceProjectAttachmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListServiceProjectAttachmentsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListServiceProjectAttachmentsResponse):
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
        self._request = apphub_service.ListServiceProjectAttachmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apphub_service.ListServiceProjectAttachmentsResponse]:
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

    def __iter__(self) -> Iterator[service_project_attachment.ServiceProjectAttachment]:
        for page in self.pages:
            yield from page.service_project_attachments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServiceProjectAttachmentsAsyncPager:
    """A pager for iterating through ``list_service_project_attachments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListServiceProjectAttachmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``service_project_attachments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServiceProjectAttachments`` requests and continue to iterate
    through the ``service_project_attachments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListServiceProjectAttachmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[apphub_service.ListServiceProjectAttachmentsResponse]
        ],
        request: apphub_service.ListServiceProjectAttachmentsRequest,
        response: apphub_service.ListServiceProjectAttachmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListServiceProjectAttachmentsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListServiceProjectAttachmentsResponse):
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
        self._request = apphub_service.ListServiceProjectAttachmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[apphub_service.ListServiceProjectAttachmentsResponse]:
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
    ) -> AsyncIterator[service_project_attachment.ServiceProjectAttachment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.service_project_attachments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDiscoveredServicesPager:
    """A pager for iterating through ``list_discovered_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListDiscoveredServicesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``discovered_services`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDiscoveredServices`` requests and continue to iterate
    through the ``discovered_services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListDiscoveredServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apphub_service.ListDiscoveredServicesResponse],
        request: apphub_service.ListDiscoveredServicesRequest,
        response: apphub_service.ListDiscoveredServicesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListDiscoveredServicesRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListDiscoveredServicesResponse):
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
        self._request = apphub_service.ListDiscoveredServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apphub_service.ListDiscoveredServicesResponse]:
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

    def __iter__(self) -> Iterator[service.DiscoveredService]:
        for page in self.pages:
            yield from page.discovered_services

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDiscoveredServicesAsyncPager:
    """A pager for iterating through ``list_discovered_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListDiscoveredServicesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``discovered_services`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDiscoveredServices`` requests and continue to iterate
    through the ``discovered_services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListDiscoveredServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apphub_service.ListDiscoveredServicesResponse]],
        request: apphub_service.ListDiscoveredServicesRequest,
        response: apphub_service.ListDiscoveredServicesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListDiscoveredServicesRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListDiscoveredServicesResponse):
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
        self._request = apphub_service.ListDiscoveredServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[apphub_service.ListDiscoveredServicesResponse]:
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

    def __aiter__(self) -> AsyncIterator[service.DiscoveredService]:
        async def async_generator():
            async for page in self.pages:
                for response in page.discovered_services:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServicesPager:
    """A pager for iterating through ``list_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListServicesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apphub_service.ListServicesResponse],
        request: apphub_service.ListServicesRequest,
        response: apphub_service.ListServicesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListServicesResponse):
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
        self._request = apphub_service.ListServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apphub_service.ListServicesResponse]:
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
    :class:`google.cloud.apphub_v1.types.ListServicesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apphub_service.ListServicesResponse]],
        request: apphub_service.ListServicesRequest,
        response: apphub_service.ListServicesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListServicesResponse):
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
        self._request = apphub_service.ListServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apphub_service.ListServicesResponse]:
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


class ListDiscoveredWorkloadsPager:
    """A pager for iterating through ``list_discovered_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListDiscoveredWorkloadsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``discovered_workloads`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDiscoveredWorkloads`` requests and continue to iterate
    through the ``discovered_workloads`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListDiscoveredWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apphub_service.ListDiscoveredWorkloadsResponse],
        request: apphub_service.ListDiscoveredWorkloadsRequest,
        response: apphub_service.ListDiscoveredWorkloadsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListDiscoveredWorkloadsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListDiscoveredWorkloadsResponse):
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
        self._request = apphub_service.ListDiscoveredWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apphub_service.ListDiscoveredWorkloadsResponse]:
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

    def __iter__(self) -> Iterator[workload.DiscoveredWorkload]:
        for page in self.pages:
            yield from page.discovered_workloads

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDiscoveredWorkloadsAsyncPager:
    """A pager for iterating through ``list_discovered_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListDiscoveredWorkloadsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``discovered_workloads`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDiscoveredWorkloads`` requests and continue to iterate
    through the ``discovered_workloads`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListDiscoveredWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[apphub_service.ListDiscoveredWorkloadsResponse]
        ],
        request: apphub_service.ListDiscoveredWorkloadsRequest,
        response: apphub_service.ListDiscoveredWorkloadsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListDiscoveredWorkloadsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListDiscoveredWorkloadsResponse):
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
        self._request = apphub_service.ListDiscoveredWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[apphub_service.ListDiscoveredWorkloadsResponse]:
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

    def __aiter__(self) -> AsyncIterator[workload.DiscoveredWorkload]:
        async def async_generator():
            async for page in self.pages:
                for response in page.discovered_workloads:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkloadsPager:
    """A pager for iterating through ``list_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListWorkloadsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workloads`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkloads`` requests and continue to iterate
    through the ``workloads`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apphub_service.ListWorkloadsResponse],
        request: apphub_service.ListWorkloadsRequest,
        response: apphub_service.ListWorkloadsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListWorkloadsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListWorkloadsResponse):
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
        self._request = apphub_service.ListWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apphub_service.ListWorkloadsResponse]:
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

    def __iter__(self) -> Iterator[workload.Workload]:
        for page in self.pages:
            yield from page.workloads

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkloadsAsyncPager:
    """A pager for iterating through ``list_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListWorkloadsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workloads`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkloads`` requests and continue to iterate
    through the ``workloads`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apphub_service.ListWorkloadsResponse]],
        request: apphub_service.ListWorkloadsRequest,
        response: apphub_service.ListWorkloadsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListWorkloadsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListWorkloadsResponse):
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
        self._request = apphub_service.ListWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apphub_service.ListWorkloadsResponse]:
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

    def __aiter__(self) -> AsyncIterator[workload.Workload]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workloads:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationsPager:
    """A pager for iterating through ``list_applications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListApplicationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``applications`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApplications`` requests and continue to iterate
    through the ``applications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListApplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apphub_service.ListApplicationsResponse],
        request: apphub_service.ListApplicationsRequest,
        response: apphub_service.ListApplicationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListApplicationsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListApplicationsResponse):
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
        self._request = apphub_service.ListApplicationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apphub_service.ListApplicationsResponse]:
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

    def __iter__(self) -> Iterator[application.Application]:
        for page in self.pages:
            yield from page.applications

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationsAsyncPager:
    """A pager for iterating through ``list_applications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListApplicationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``applications`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApplications`` requests and continue to iterate
    through the ``applications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListApplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apphub_service.ListApplicationsResponse]],
        request: apphub_service.ListApplicationsRequest,
        response: apphub_service.ListApplicationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListApplicationsRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListApplicationsResponse):
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
        self._request = apphub_service.ListApplicationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apphub_service.ListApplicationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[application.Application]:
        async def async_generator():
            async for page in self.pages:
                for response in page.applications:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExtendedMetadataSchemasPager:
    """A pager for iterating through ``list_extended_metadata_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListExtendedMetadataSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``extended_metadata_schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExtendedMetadataSchemas`` requests and continue to iterate
    through the ``extended_metadata_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListExtendedMetadataSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apphub_service.ListExtendedMetadataSchemasResponse],
        request: apphub_service.ListExtendedMetadataSchemasRequest,
        response: apphub_service.ListExtendedMetadataSchemasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListExtendedMetadataSchemasRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListExtendedMetadataSchemasResponse):
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
        self._request = apphub_service.ListExtendedMetadataSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apphub_service.ListExtendedMetadataSchemasResponse]:
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

    def __iter__(self) -> Iterator[extended_metadata_schema.ExtendedMetadataSchema]:
        for page in self.pages:
            yield from page.extended_metadata_schemas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExtendedMetadataSchemasAsyncPager:
    """A pager for iterating through ``list_extended_metadata_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apphub_v1.types.ListExtendedMetadataSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``extended_metadata_schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExtendedMetadataSchemas`` requests and continue to iterate
    through the ``extended_metadata_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apphub_v1.types.ListExtendedMetadataSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[apphub_service.ListExtendedMetadataSchemasResponse]
        ],
        request: apphub_service.ListExtendedMetadataSchemasRequest,
        response: apphub_service.ListExtendedMetadataSchemasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apphub_v1.types.ListExtendedMetadataSchemasRequest):
                The initial request object.
            response (google.cloud.apphub_v1.types.ListExtendedMetadataSchemasResponse):
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
        self._request = apphub_service.ListExtendedMetadataSchemasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[apphub_service.ListExtendedMetadataSchemasResponse]:
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
    ) -> AsyncIterator[extended_metadata_schema.ExtendedMetadataSchema]:
        async def async_generator():
            async for page in self.pages:
                for response in page.extended_metadata_schemas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
