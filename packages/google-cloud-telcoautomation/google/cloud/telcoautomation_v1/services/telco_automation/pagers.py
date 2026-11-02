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

from google.cloud.telcoautomation_v1.types import telcoautomation


class ListOrchestrationClustersPager:
    """A pager for iterating through ``list_orchestration_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListOrchestrationClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``orchestration_clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOrchestrationClusters`` requests and continue to iterate
    through the ``orchestration_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListOrchestrationClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListOrchestrationClustersResponse],
        request: telcoautomation.ListOrchestrationClustersRequest,
        response: telcoautomation.ListOrchestrationClustersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListOrchestrationClustersRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListOrchestrationClustersResponse):
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
        self._request = telcoautomation.ListOrchestrationClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListOrchestrationClustersResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.OrchestrationCluster]:
        for page in self.pages:
            yield from page.orchestration_clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOrchestrationClustersAsyncPager:
    """A pager for iterating through ``list_orchestration_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListOrchestrationClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``orchestration_clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOrchestrationClusters`` requests and continue to iterate
    through the ``orchestration_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListOrchestrationClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[telcoautomation.ListOrchestrationClustersResponse]
        ],
        request: telcoautomation.ListOrchestrationClustersRequest,
        response: telcoautomation.ListOrchestrationClustersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListOrchestrationClustersRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListOrchestrationClustersResponse):
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
        self._request = telcoautomation.ListOrchestrationClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[telcoautomation.ListOrchestrationClustersResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.OrchestrationCluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.orchestration_clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEdgeSlmsPager:
    """A pager for iterating through ``list_edge_slms`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListEdgeSlmsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``edge_slms`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEdgeSlms`` requests and continue to iterate
    through the ``edge_slms`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListEdgeSlmsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListEdgeSlmsResponse],
        request: telcoautomation.ListEdgeSlmsRequest,
        response: telcoautomation.ListEdgeSlmsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListEdgeSlmsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListEdgeSlmsResponse):
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
        self._request = telcoautomation.ListEdgeSlmsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListEdgeSlmsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.EdgeSlm]:
        for page in self.pages:
            yield from page.edge_slms

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEdgeSlmsAsyncPager:
    """A pager for iterating through ``list_edge_slms`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListEdgeSlmsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``edge_slms`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEdgeSlms`` requests and continue to iterate
    through the ``edge_slms`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListEdgeSlmsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[telcoautomation.ListEdgeSlmsResponse]],
        request: telcoautomation.ListEdgeSlmsRequest,
        response: telcoautomation.ListEdgeSlmsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListEdgeSlmsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListEdgeSlmsResponse):
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
        self._request = telcoautomation.ListEdgeSlmsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[telcoautomation.ListEdgeSlmsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.EdgeSlm]:
        async def async_generator():
            async for page in self.pages:
                for response in page.edge_slms:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBlueprintsPager:
    """A pager for iterating through ``list_blueprints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListBlueprintsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``blueprints`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBlueprints`` requests and continue to iterate
    through the ``blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListBlueprintsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListBlueprintsResponse],
        request: telcoautomation.ListBlueprintsRequest,
        response: telcoautomation.ListBlueprintsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListBlueprintsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListBlueprintsResponse):
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
        self._request = telcoautomation.ListBlueprintsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListBlueprintsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.Blueprint]:
        for page in self.pages:
            yield from page.blueprints

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBlueprintsAsyncPager:
    """A pager for iterating through ``list_blueprints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListBlueprintsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``blueprints`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBlueprints`` requests and continue to iterate
    through the ``blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListBlueprintsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[telcoautomation.ListBlueprintsResponse]],
        request: telcoautomation.ListBlueprintsRequest,
        response: telcoautomation.ListBlueprintsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListBlueprintsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListBlueprintsResponse):
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
        self._request = telcoautomation.ListBlueprintsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[telcoautomation.ListBlueprintsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.Blueprint]:
        async def async_generator():
            async for page in self.pages:
                for response in page.blueprints:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBlueprintRevisionsPager:
    """A pager for iterating through ``list_blueprint_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``blueprints`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBlueprintRevisions`` requests and continue to iterate
    through the ``blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListBlueprintRevisionsResponse],
        request: telcoautomation.ListBlueprintRevisionsRequest,
        response: telcoautomation.ListBlueprintRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsResponse):
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
        self._request = telcoautomation.ListBlueprintRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListBlueprintRevisionsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.Blueprint]:
        for page in self.pages:
            yield from page.blueprints

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBlueprintRevisionsAsyncPager:
    """A pager for iterating through ``list_blueprint_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``blueprints`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBlueprintRevisions`` requests and continue to iterate
    through the ``blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[telcoautomation.ListBlueprintRevisionsResponse]
        ],
        request: telcoautomation.ListBlueprintRevisionsRequest,
        response: telcoautomation.ListBlueprintRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListBlueprintRevisionsResponse):
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
        self._request = telcoautomation.ListBlueprintRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[telcoautomation.ListBlueprintRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.Blueprint]:
        async def async_generator():
            async for page in self.pages:
                for response in page.blueprints:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchBlueprintRevisionsPager:
    """A pager for iterating through ``search_blueprint_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``blueprints`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchBlueprintRevisions`` requests and continue to iterate
    through the ``blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.SearchBlueprintRevisionsResponse],
        request: telcoautomation.SearchBlueprintRevisionsRequest,
        response: telcoautomation.SearchBlueprintRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsResponse):
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
        self._request = telcoautomation.SearchBlueprintRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.SearchBlueprintRevisionsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.Blueprint]:
        for page in self.pages:
            yield from page.blueprints

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchBlueprintRevisionsAsyncPager:
    """A pager for iterating through ``search_blueprint_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``blueprints`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchBlueprintRevisions`` requests and continue to iterate
    through the ``blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[telcoautomation.SearchBlueprintRevisionsResponse]
        ],
        request: telcoautomation.SearchBlueprintRevisionsRequest,
        response: telcoautomation.SearchBlueprintRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.SearchBlueprintRevisionsResponse):
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
        self._request = telcoautomation.SearchBlueprintRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[telcoautomation.SearchBlueprintRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.Blueprint]:
        async def async_generator():
            async for page in self.pages:
                for response in page.blueprints:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchDeploymentRevisionsPager:
    """A pager for iterating through ``search_deployment_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchDeploymentRevisions`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.SearchDeploymentRevisionsResponse],
        request: telcoautomation.SearchDeploymentRevisionsRequest,
        response: telcoautomation.SearchDeploymentRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsResponse):
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
        self._request = telcoautomation.SearchDeploymentRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.SearchDeploymentRevisionsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.Deployment]:
        for page in self.pages:
            yield from page.deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchDeploymentRevisionsAsyncPager:
    """A pager for iterating through ``search_deployment_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchDeploymentRevisions`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[telcoautomation.SearchDeploymentRevisionsResponse]
        ],
        request: telcoautomation.SearchDeploymentRevisionsRequest,
        response: telcoautomation.SearchDeploymentRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsResponse):
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
        self._request = telcoautomation.SearchDeploymentRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[telcoautomation.SearchDeploymentRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.Deployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPublicBlueprintsPager:
    """A pager for iterating through ``list_public_blueprints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListPublicBlueprintsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``public_blueprints`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPublicBlueprints`` requests and continue to iterate
    through the ``public_blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListPublicBlueprintsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListPublicBlueprintsResponse],
        request: telcoautomation.ListPublicBlueprintsRequest,
        response: telcoautomation.ListPublicBlueprintsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListPublicBlueprintsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListPublicBlueprintsResponse):
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
        self._request = telcoautomation.ListPublicBlueprintsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListPublicBlueprintsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.PublicBlueprint]:
        for page in self.pages:
            yield from page.public_blueprints

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPublicBlueprintsAsyncPager:
    """A pager for iterating through ``list_public_blueprints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListPublicBlueprintsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``public_blueprints`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPublicBlueprints`` requests and continue to iterate
    through the ``public_blueprints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListPublicBlueprintsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[telcoautomation.ListPublicBlueprintsResponse]],
        request: telcoautomation.ListPublicBlueprintsRequest,
        response: telcoautomation.ListPublicBlueprintsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListPublicBlueprintsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListPublicBlueprintsResponse):
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
        self._request = telcoautomation.ListPublicBlueprintsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[telcoautomation.ListPublicBlueprintsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.PublicBlueprint]:
        async def async_generator():
            async for page in self.pages:
                for response in page.public_blueprints:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentsPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListDeploymentsResponse],
        request: telcoautomation.ListDeploymentsRequest,
        response: telcoautomation.ListDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListDeploymentsResponse):
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
        self._request = telcoautomation.ListDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.Deployment]:
        for page in self.pages:
            yield from page.deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentsAsyncPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[telcoautomation.ListDeploymentsResponse]],
        request: telcoautomation.ListDeploymentsRequest,
        response: telcoautomation.ListDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListDeploymentsResponse):
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
        self._request = telcoautomation.ListDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[telcoautomation.ListDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.Deployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentRevisionsPager:
    """A pager for iterating through ``list_deployment_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeploymentRevisions`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListDeploymentRevisionsResponse],
        request: telcoautomation.ListDeploymentRevisionsRequest,
        response: telcoautomation.ListDeploymentRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsResponse):
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
        self._request = telcoautomation.ListDeploymentRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListDeploymentRevisionsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.Deployment]:
        for page in self.pages:
            yield from page.deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentRevisionsAsyncPager:
    """A pager for iterating through ``list_deployment_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeploymentRevisions`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[telcoautomation.ListDeploymentRevisionsResponse]
        ],
        request: telcoautomation.ListDeploymentRevisionsRequest,
        response: telcoautomation.ListDeploymentRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListDeploymentRevisionsResponse):
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
        self._request = telcoautomation.ListDeploymentRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[telcoautomation.ListDeploymentRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.Deployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHydratedDeploymentsPager:
    """A pager for iterating through ``list_hydrated_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``hydrated_deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHydratedDeployments`` requests and continue to iterate
    through the ``hydrated_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., telcoautomation.ListHydratedDeploymentsResponse],
        request: telcoautomation.ListHydratedDeploymentsRequest,
        response: telcoautomation.ListHydratedDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsResponse):
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
        self._request = telcoautomation.ListHydratedDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[telcoautomation.ListHydratedDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[telcoautomation.HydratedDeployment]:
        for page in self.pages:
            yield from page.hydrated_deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHydratedDeploymentsAsyncPager:
    """A pager for iterating through ``list_hydrated_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``hydrated_deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHydratedDeployments`` requests and continue to iterate
    through the ``hydrated_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[telcoautomation.ListHydratedDeploymentsResponse]
        ],
        request: telcoautomation.ListHydratedDeploymentsRequest,
        response: telcoautomation.ListHydratedDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsRequest):
                The initial request object.
            response (google.cloud.telcoautomation_v1.types.ListHydratedDeploymentsResponse):
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
        self._request = telcoautomation.ListHydratedDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[telcoautomation.ListHydratedDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[telcoautomation.HydratedDeployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.hydrated_deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
