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

from google.cloud.ces_v1beta.types import evaluation, evaluation_service


class ListEvaluationsPager:
    """A pager for iterating through ``list_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., evaluation_service.ListEvaluationsResponse],
        request: evaluation_service.ListEvaluationsRequest,
        response: evaluation_service.ListEvaluationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationsResponse):
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
        self._request = evaluation_service.ListEvaluationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListEvaluationsResponse]:
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
    :class:`google.cloud.ces_v1beta.types.ListEvaluationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[evaluation_service.ListEvaluationsResponse]],
        request: evaluation_service.ListEvaluationsRequest,
        response: evaluation_service.ListEvaluationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationsResponse):
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
        self._request = evaluation_service.ListEvaluationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[evaluation_service.ListEvaluationsResponse]:
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


class ListEvaluationResultsPager:
    """A pager for iterating through ``list_evaluation_results`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationResultsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluation_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluationResults`` requests and continue to iterate
    through the ``evaluation_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationResultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., evaluation_service.ListEvaluationResultsResponse],
        request: evaluation_service.ListEvaluationResultsRequest,
        response: evaluation_service.ListEvaluationResultsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationResultsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationResultsResponse):
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
        self._request = evaluation_service.ListEvaluationResultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListEvaluationResultsResponse]:
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

    def __iter__(self) -> Iterator[evaluation.EvaluationResult]:
        for page in self.pages:
            yield from page.evaluation_results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationResultsAsyncPager:
    """A pager for iterating through ``list_evaluation_results`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationResultsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluation_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluationResults`` requests and continue to iterate
    through the ``evaluation_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationResultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[evaluation_service.ListEvaluationResultsResponse]
        ],
        request: evaluation_service.ListEvaluationResultsRequest,
        response: evaluation_service.ListEvaluationResultsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationResultsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationResultsResponse):
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
        self._request = evaluation_service.ListEvaluationResultsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[evaluation_service.ListEvaluationResultsResponse]:
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

    def __aiter__(self) -> AsyncIterator[evaluation.EvaluationResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluation_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationDatasetsPager:
    """A pager for iterating through ``list_evaluation_datasets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationDatasetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluation_datasets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluationDatasets`` requests and continue to iterate
    through the ``evaluation_datasets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationDatasetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., evaluation_service.ListEvaluationDatasetsResponse],
        request: evaluation_service.ListEvaluationDatasetsRequest,
        response: evaluation_service.ListEvaluationDatasetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationDatasetsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationDatasetsResponse):
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
        self._request = evaluation_service.ListEvaluationDatasetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListEvaluationDatasetsResponse]:
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

    def __iter__(self) -> Iterator[evaluation.EvaluationDataset]:
        for page in self.pages:
            yield from page.evaluation_datasets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationDatasetsAsyncPager:
    """A pager for iterating through ``list_evaluation_datasets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationDatasetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluation_datasets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluationDatasets`` requests and continue to iterate
    through the ``evaluation_datasets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationDatasetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[evaluation_service.ListEvaluationDatasetsResponse]
        ],
        request: evaluation_service.ListEvaluationDatasetsRequest,
        response: evaluation_service.ListEvaluationDatasetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationDatasetsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationDatasetsResponse):
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
        self._request = evaluation_service.ListEvaluationDatasetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[evaluation_service.ListEvaluationDatasetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[evaluation.EvaluationDataset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluation_datasets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationRunsPager:
    """A pager for iterating through ``list_evaluation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluation_runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluationRuns`` requests and continue to iterate
    through the ``evaluation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., evaluation_service.ListEvaluationRunsResponse],
        request: evaluation_service.ListEvaluationRunsRequest,
        response: evaluation_service.ListEvaluationRunsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationRunsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationRunsResponse):
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
        self._request = evaluation_service.ListEvaluationRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListEvaluationRunsResponse]:
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

    def __iter__(self) -> Iterator[evaluation.EvaluationRun]:
        for page in self.pages:
            yield from page.evaluation_runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationRunsAsyncPager:
    """A pager for iterating through ``list_evaluation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluation_runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluationRuns`` requests and continue to iterate
    through the ``evaluation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[evaluation_service.ListEvaluationRunsResponse]],
        request: evaluation_service.ListEvaluationRunsRequest,
        response: evaluation_service.ListEvaluationRunsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationRunsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationRunsResponse):
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
        self._request = evaluation_service.ListEvaluationRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[evaluation_service.ListEvaluationRunsResponse]:
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

    def __aiter__(self) -> AsyncIterator[evaluation.EvaluationRun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluation_runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationExpectationsPager:
    """A pager for iterating through ``list_evaluation_expectations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationExpectationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluation_expectations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluationExpectations`` requests and continue to iterate
    through the ``evaluation_expectations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationExpectationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., evaluation_service.ListEvaluationExpectationsResponse],
        request: evaluation_service.ListEvaluationExpectationsRequest,
        response: evaluation_service.ListEvaluationExpectationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationExpectationsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationExpectationsResponse):
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
        self._request = evaluation_service.ListEvaluationExpectationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListEvaluationExpectationsResponse]:
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

    def __iter__(self) -> Iterator[evaluation.EvaluationExpectation]:
        for page in self.pages:
            yield from page.evaluation_expectations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationExpectationsAsyncPager:
    """A pager for iterating through ``list_evaluation_expectations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListEvaluationExpectationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluation_expectations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluationExpectations`` requests and continue to iterate
    through the ``evaluation_expectations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListEvaluationExpectationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[evaluation_service.ListEvaluationExpectationsResponse]
        ],
        request: evaluation_service.ListEvaluationExpectationsRequest,
        response: evaluation_service.ListEvaluationExpectationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListEvaluationExpectationsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListEvaluationExpectationsResponse):
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
        self._request = evaluation_service.ListEvaluationExpectationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[evaluation_service.ListEvaluationExpectationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[evaluation.EvaluationExpectation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluation_expectations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScheduledEvaluationRunsPager:
    """A pager for iterating through ``list_scheduled_evaluation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``scheduled_evaluation_runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListScheduledEvaluationRuns`` requests and continue to iterate
    through the ``scheduled_evaluation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., evaluation_service.ListScheduledEvaluationRunsResponse],
        request: evaluation_service.ListScheduledEvaluationRunsRequest,
        response: evaluation_service.ListScheduledEvaluationRunsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsResponse):
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
        self._request = evaluation_service.ListScheduledEvaluationRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[evaluation_service.ListScheduledEvaluationRunsResponse]:
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

    def __iter__(self) -> Iterator[evaluation.ScheduledEvaluationRun]:
        for page in self.pages:
            yield from page.scheduled_evaluation_runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScheduledEvaluationRunsAsyncPager:
    """A pager for iterating through ``list_scheduled_evaluation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``scheduled_evaluation_runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListScheduledEvaluationRuns`` requests and continue to iterate
    through the ``scheduled_evaluation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[evaluation_service.ListScheduledEvaluationRunsResponse]
        ],
        request: evaluation_service.ListScheduledEvaluationRunsRequest,
        response: evaluation_service.ListScheduledEvaluationRunsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsRequest):
                The initial request object.
            response (google.cloud.ces_v1beta.types.ListScheduledEvaluationRunsResponse):
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
        self._request = evaluation_service.ListScheduledEvaluationRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[evaluation_service.ListScheduledEvaluationRunsResponse]:
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

    def __aiter__(self) -> AsyncIterator[evaluation.ScheduledEvaluationRun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.scheduled_evaluation_runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
