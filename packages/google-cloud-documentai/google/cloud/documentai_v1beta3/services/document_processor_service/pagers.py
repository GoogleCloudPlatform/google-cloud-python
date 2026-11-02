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

from google.cloud.documentai_v1beta3.types import (
    document_processor_service,
    evaluation,
    processor,
    processor_type,
)


class ListProcessorTypesPager:
    """A pager for iterating through ``list_processor_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``processor_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProcessorTypes`` requests and continue to iterate
    through the ``processor_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., document_processor_service.ListProcessorTypesResponse],
        request: document_processor_service.ListProcessorTypesRequest,
        response: document_processor_service.ListProcessorTypesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse):
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
        self._request = document_processor_service.ListProcessorTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[document_processor_service.ListProcessorTypesResponse]:
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

    def __iter__(self) -> Iterator[processor_type.ProcessorType]:
        for page in self.pages:
            yield from page.processor_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessorTypesAsyncPager:
    """A pager for iterating through ``list_processor_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``processor_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProcessorTypes`` requests and continue to iterate
    through the ``processor_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[document_processor_service.ListProcessorTypesResponse]
        ],
        request: document_processor_service.ListProcessorTypesRequest,
        response: document_processor_service.ListProcessorTypesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse):
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
        self._request = document_processor_service.ListProcessorTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[document_processor_service.ListProcessorTypesResponse]:
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

    def __aiter__(self) -> AsyncIterator[processor_type.ProcessorType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.processor_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessorsPager:
    """A pager for iterating through ``list_processors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListProcessorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``processors`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProcessors`` requests and continue to iterate
    through the ``processors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListProcessorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., document_processor_service.ListProcessorsResponse],
        request: document_processor_service.ListProcessorsRequest,
        response: document_processor_service.ListProcessorsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListProcessorsRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListProcessorsResponse):
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
        self._request = document_processor_service.ListProcessorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[document_processor_service.ListProcessorsResponse]:
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

    def __iter__(self) -> Iterator[processor.Processor]:
        for page in self.pages:
            yield from page.processors

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessorsAsyncPager:
    """A pager for iterating through ``list_processors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListProcessorsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``processors`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProcessors`` requests and continue to iterate
    through the ``processors`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListProcessorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[document_processor_service.ListProcessorsResponse]
        ],
        request: document_processor_service.ListProcessorsRequest,
        response: document_processor_service.ListProcessorsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListProcessorsRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListProcessorsResponse):
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
        self._request = document_processor_service.ListProcessorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[document_processor_service.ListProcessorsResponse]:
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

    def __aiter__(self) -> AsyncIterator[processor.Processor]:
        async def async_generator():
            async for page in self.pages:
                for response in page.processors:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessorVersionsPager:
    """A pager for iterating through ``list_processor_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListProcessorVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``processor_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProcessorVersions`` requests and continue to iterate
    through the ``processor_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListProcessorVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., document_processor_service.ListProcessorVersionsResponse],
        request: document_processor_service.ListProcessorVersionsRequest,
        response: document_processor_service.ListProcessorVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListProcessorVersionsRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListProcessorVersionsResponse):
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
        self._request = document_processor_service.ListProcessorVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[document_processor_service.ListProcessorVersionsResponse]:
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

    def __iter__(self) -> Iterator[processor.ProcessorVersion]:
        for page in self.pages:
            yield from page.processor_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessorVersionsAsyncPager:
    """A pager for iterating through ``list_processor_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListProcessorVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``processor_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProcessorVersions`` requests and continue to iterate
    through the ``processor_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListProcessorVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[document_processor_service.ListProcessorVersionsResponse]
        ],
        request: document_processor_service.ListProcessorVersionsRequest,
        response: document_processor_service.ListProcessorVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListProcessorVersionsRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListProcessorVersionsResponse):
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
        self._request = document_processor_service.ListProcessorVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[document_processor_service.ListProcessorVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[processor.ProcessorVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.processor_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationsPager:
    """A pager for iterating through ``list_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListEvaluationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., document_processor_service.ListEvaluationsResponse],
        request: document_processor_service.ListEvaluationsRequest,
        response: document_processor_service.ListEvaluationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListEvaluationsRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListEvaluationsResponse):
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
        self._request = document_processor_service.ListEvaluationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[document_processor_service.ListEvaluationsResponse]:
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

    def __iter__(self) -> Iterator[evaluation.Evaluation]:
        for page in self.pages:
            yield from page.evaluations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationsAsyncPager:
    """A pager for iterating through ``list_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.documentai_v1beta3.types.ListEvaluationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.documentai_v1beta3.types.ListEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[document_processor_service.ListEvaluationsResponse]
        ],
        request: document_processor_service.ListEvaluationsRequest,
        response: document_processor_service.ListEvaluationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.documentai_v1beta3.types.ListEvaluationsRequest):
                The initial request object.
            response (google.cloud.documentai_v1beta3.types.ListEvaluationsResponse):
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
        self._request = document_processor_service.ListEvaluationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[document_processor_service.ListEvaluationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[evaluation.Evaluation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
