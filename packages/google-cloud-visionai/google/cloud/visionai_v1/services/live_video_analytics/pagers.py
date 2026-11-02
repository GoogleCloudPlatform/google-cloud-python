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

from google.cloud.visionai_v1.types import lva_resources, lva_service


class ListPublicOperatorsPager:
    """A pager for iterating through ``list_public_operators`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListPublicOperatorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``operators`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPublicOperators`` requests and continue to iterate
    through the ``operators`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListPublicOperatorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lva_service.ListPublicOperatorsResponse],
        request: lva_service.ListPublicOperatorsRequest,
        response: lva_service.ListPublicOperatorsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListPublicOperatorsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListPublicOperatorsResponse):
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
        self._request = lva_service.ListPublicOperatorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lva_service.ListPublicOperatorsResponse]:
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

    def __iter__(self) -> Iterator[lva_resources.Operator]:
        for page in self.pages:
            yield from page.operators

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPublicOperatorsAsyncPager:
    """A pager for iterating through ``list_public_operators`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListPublicOperatorsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``operators`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPublicOperators`` requests and continue to iterate
    through the ``operators`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListPublicOperatorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lva_service.ListPublicOperatorsResponse]],
        request: lva_service.ListPublicOperatorsRequest,
        response: lva_service.ListPublicOperatorsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListPublicOperatorsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListPublicOperatorsResponse):
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
        self._request = lva_service.ListPublicOperatorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lva_service.ListPublicOperatorsResponse]:
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

    def __aiter__(self) -> AsyncIterator[lva_resources.Operator]:
        async def async_generator():
            async for page in self.pages:
                for response in page.operators:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOperatorsPager:
    """A pager for iterating through ``list_operators`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListOperatorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``operators`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOperators`` requests and continue to iterate
    through the ``operators`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListOperatorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lva_service.ListOperatorsResponse],
        request: lva_service.ListOperatorsRequest,
        response: lva_service.ListOperatorsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListOperatorsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListOperatorsResponse):
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
        self._request = lva_service.ListOperatorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lva_service.ListOperatorsResponse]:
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

    def __iter__(self) -> Iterator[lva_resources.Operator]:
        for page in self.pages:
            yield from page.operators

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOperatorsAsyncPager:
    """A pager for iterating through ``list_operators`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListOperatorsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``operators`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOperators`` requests and continue to iterate
    through the ``operators`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListOperatorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lva_service.ListOperatorsResponse]],
        request: lva_service.ListOperatorsRequest,
        response: lva_service.ListOperatorsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListOperatorsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListOperatorsResponse):
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
        self._request = lva_service.ListOperatorsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lva_service.ListOperatorsResponse]:
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

    def __aiter__(self) -> AsyncIterator[lva_resources.Operator]:
        async def async_generator():
            async for page in self.pages:
                for response in page.operators:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalysesPager:
    """A pager for iterating through ``list_analyses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListAnalysesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``analyses`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnalyses`` requests and continue to iterate
    through the ``analyses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListAnalysesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lva_service.ListAnalysesResponse],
        request: lva_service.ListAnalysesRequest,
        response: lva_service.ListAnalysesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListAnalysesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListAnalysesResponse):
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
        self._request = lva_service.ListAnalysesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lva_service.ListAnalysesResponse]:
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

    def __iter__(self) -> Iterator[lva_resources.Analysis]:
        for page in self.pages:
            yield from page.analyses

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalysesAsyncPager:
    """A pager for iterating through ``list_analyses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListAnalysesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``analyses`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnalyses`` requests and continue to iterate
    through the ``analyses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListAnalysesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lva_service.ListAnalysesResponse]],
        request: lva_service.ListAnalysesRequest,
        response: lva_service.ListAnalysesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListAnalysesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListAnalysesResponse):
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
        self._request = lva_service.ListAnalysesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lva_service.ListAnalysesResponse]:
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

    def __aiter__(self) -> AsyncIterator[lva_resources.Analysis]:
        async def async_generator():
            async for page in self.pages:
                for response in page.analyses:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessesPager:
    """A pager for iterating through ``list_processes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListProcessesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``processes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProcesses`` requests and continue to iterate
    through the ``processes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListProcessesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lva_service.ListProcessesResponse],
        request: lva_service.ListProcessesRequest,
        response: lva_service.ListProcessesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListProcessesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListProcessesResponse):
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
        self._request = lva_service.ListProcessesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lva_service.ListProcessesResponse]:
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

    def __iter__(self) -> Iterator[lva_resources.Process]:
        for page in self.pages:
            yield from page.processes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProcessesAsyncPager:
    """A pager for iterating through ``list_processes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListProcessesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``processes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProcesses`` requests and continue to iterate
    through the ``processes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListProcessesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lva_service.ListProcessesResponse]],
        request: lva_service.ListProcessesRequest,
        response: lva_service.ListProcessesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListProcessesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListProcessesResponse):
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
        self._request = lva_service.ListProcessesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lva_service.ListProcessesResponse]:
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

    def __aiter__(self) -> AsyncIterator[lva_resources.Process]:
        async def async_generator():
            async for page in self.pages:
                for response in page.processes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
