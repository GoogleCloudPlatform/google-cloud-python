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

from google.cloud.datalabeling_v1beta1.types import (
    annotation_spec_set,
    data_labeling_service,
    dataset,
    evaluation,
    evaluation_job,
    instruction,
)


class ListDatasetsPager:
    """A pager for iterating through ``list_datasets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListDatasetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``datasets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDatasets`` requests and continue to iterate
    through the ``datasets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListDatasetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.ListDatasetsResponse],
        request: data_labeling_service.ListDatasetsRequest,
        response: data_labeling_service.ListDatasetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListDatasetsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListDatasetsResponse):
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
        self._request = data_labeling_service.ListDatasetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.ListDatasetsResponse]:
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

    def __iter__(self) -> Iterator[dataset.Dataset]:
        for page in self.pages:
            yield from page.datasets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatasetsAsyncPager:
    """A pager for iterating through ``list_datasets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListDatasetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``datasets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDatasets`` requests and continue to iterate
    through the ``datasets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListDatasetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[data_labeling_service.ListDatasetsResponse]],
        request: data_labeling_service.ListDatasetsRequest,
        response: data_labeling_service.ListDatasetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListDatasetsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListDatasetsResponse):
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
        self._request = data_labeling_service.ListDatasetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[data_labeling_service.ListDatasetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataset.Dataset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.datasets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataItemsPager:
    """A pager for iterating through ``list_data_items`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListDataItemsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataItems`` requests and continue to iterate
    through the ``data_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListDataItemsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.ListDataItemsResponse],
        request: data_labeling_service.ListDataItemsRequest,
        response: data_labeling_service.ListDataItemsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListDataItemsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListDataItemsResponse):
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
        self._request = data_labeling_service.ListDataItemsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.ListDataItemsResponse]:
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

    def __iter__(self) -> Iterator[dataset.DataItem]:
        for page in self.pages:
            yield from page.data_items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataItemsAsyncPager:
    """A pager for iterating through ``list_data_items`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListDataItemsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_items`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataItems`` requests and continue to iterate
    through the ``data_items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListDataItemsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[data_labeling_service.ListDataItemsResponse]],
        request: data_labeling_service.ListDataItemsRequest,
        response: data_labeling_service.ListDataItemsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListDataItemsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListDataItemsResponse):
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
        self._request = data_labeling_service.ListDataItemsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[data_labeling_service.ListDataItemsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataset.DataItem]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_items:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnnotatedDatasetsPager:
    """A pager for iterating through ``list_annotated_datasets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``annotated_datasets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnnotatedDatasets`` requests and continue to iterate
    through the ``annotated_datasets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.ListAnnotatedDatasetsResponse],
        request: data_labeling_service.ListAnnotatedDatasetsRequest,
        response: data_labeling_service.ListAnnotatedDatasetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsResponse):
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
        self._request = data_labeling_service.ListAnnotatedDatasetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.ListAnnotatedDatasetsResponse]:
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

    def __iter__(self) -> Iterator[dataset.AnnotatedDataset]:
        for page in self.pages:
            yield from page.annotated_datasets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnnotatedDatasetsAsyncPager:
    """A pager for iterating through ``list_annotated_datasets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``annotated_datasets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnnotatedDatasets`` requests and continue to iterate
    through the ``annotated_datasets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_labeling_service.ListAnnotatedDatasetsResponse]
        ],
        request: data_labeling_service.ListAnnotatedDatasetsRequest,
        response: data_labeling_service.ListAnnotatedDatasetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsResponse):
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
        self._request = data_labeling_service.ListAnnotatedDatasetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_labeling_service.ListAnnotatedDatasetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataset.AnnotatedDataset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.annotated_datasets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExamplesPager:
    """A pager for iterating through ``list_examples`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListExamplesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``examples`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExamples`` requests and continue to iterate
    through the ``examples`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListExamplesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.ListExamplesResponse],
        request: data_labeling_service.ListExamplesRequest,
        response: data_labeling_service.ListExamplesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListExamplesRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListExamplesResponse):
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
        self._request = data_labeling_service.ListExamplesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.ListExamplesResponse]:
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

    def __iter__(self) -> Iterator[dataset.Example]:
        for page in self.pages:
            yield from page.examples

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExamplesAsyncPager:
    """A pager for iterating through ``list_examples`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListExamplesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``examples`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExamples`` requests and continue to iterate
    through the ``examples`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListExamplesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[data_labeling_service.ListExamplesResponse]],
        request: data_labeling_service.ListExamplesRequest,
        response: data_labeling_service.ListExamplesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListExamplesRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListExamplesResponse):
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
        self._request = data_labeling_service.ListExamplesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[data_labeling_service.ListExamplesResponse]:
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

    def __aiter__(self) -> AsyncIterator[dataset.Example]:
        async def async_generator():
            async for page in self.pages:
                for response in page.examples:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnnotationSpecSetsPager:
    """A pager for iterating through ``list_annotation_spec_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``annotation_spec_sets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnnotationSpecSets`` requests and continue to iterate
    through the ``annotation_spec_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.ListAnnotationSpecSetsResponse],
        request: data_labeling_service.ListAnnotationSpecSetsRequest,
        response: data_labeling_service.ListAnnotationSpecSetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsResponse):
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
        self._request = data_labeling_service.ListAnnotationSpecSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.ListAnnotationSpecSetsResponse]:
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

    def __iter__(self) -> Iterator[annotation_spec_set.AnnotationSpecSet]:
        for page in self.pages:
            yield from page.annotation_spec_sets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnnotationSpecSetsAsyncPager:
    """A pager for iterating through ``list_annotation_spec_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``annotation_spec_sets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnnotationSpecSets`` requests and continue to iterate
    through the ``annotation_spec_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_labeling_service.ListAnnotationSpecSetsResponse]
        ],
        request: data_labeling_service.ListAnnotationSpecSetsRequest,
        response: data_labeling_service.ListAnnotationSpecSetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsResponse):
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
        self._request = data_labeling_service.ListAnnotationSpecSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_labeling_service.ListAnnotationSpecSetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[annotation_spec_set.AnnotationSpecSet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.annotation_spec_sets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInstructionsPager:
    """A pager for iterating through ``list_instructions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListInstructionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``instructions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInstructions`` requests and continue to iterate
    through the ``instructions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListInstructionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.ListInstructionsResponse],
        request: data_labeling_service.ListInstructionsRequest,
        response: data_labeling_service.ListInstructionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListInstructionsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListInstructionsResponse):
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
        self._request = data_labeling_service.ListInstructionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.ListInstructionsResponse]:
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

    def __iter__(self) -> Iterator[instruction.Instruction]:
        for page in self.pages:
            yield from page.instructions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInstructionsAsyncPager:
    """A pager for iterating through ``list_instructions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListInstructionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``instructions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInstructions`` requests and continue to iterate
    through the ``instructions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListInstructionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_labeling_service.ListInstructionsResponse]
        ],
        request: data_labeling_service.ListInstructionsRequest,
        response: data_labeling_service.ListInstructionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListInstructionsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListInstructionsResponse):
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
        self._request = data_labeling_service.ListInstructionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_labeling_service.ListInstructionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[instruction.Instruction]:
        async def async_generator():
            async for page in self.pages:
                for response in page.instructions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchEvaluationsPager:
    """A pager for iterating through ``search_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.SearchEvaluationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.SearchEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.SearchEvaluationsResponse],
        request: data_labeling_service.SearchEvaluationsRequest,
        response: data_labeling_service.SearchEvaluationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.SearchEvaluationsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.SearchEvaluationsResponse):
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
        self._request = data_labeling_service.SearchEvaluationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.SearchEvaluationsResponse]:
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


class SearchEvaluationsAsyncPager:
    """A pager for iterating through ``search_evaluations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.SearchEvaluationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchEvaluations`` requests and continue to iterate
    through the ``evaluations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.SearchEvaluationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_labeling_service.SearchEvaluationsResponse]
        ],
        request: data_labeling_service.SearchEvaluationsRequest,
        response: data_labeling_service.SearchEvaluationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.SearchEvaluationsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.SearchEvaluationsResponse):
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
        self._request = data_labeling_service.SearchEvaluationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_labeling_service.SearchEvaluationsResponse]:
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


class SearchExampleComparisonsPager:
    """A pager for iterating through ``search_example_comparisons`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``example_comparisons`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchExampleComparisons`` requests and continue to iterate
    through the ``example_comparisons`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.SearchExampleComparisonsResponse],
        request: data_labeling_service.SearchExampleComparisonsRequest,
        response: data_labeling_service.SearchExampleComparisonsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsResponse):
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
        self._request = data_labeling_service.SearchExampleComparisonsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.SearchExampleComparisonsResponse]:
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
    ) -> Iterator[
        data_labeling_service.SearchExampleComparisonsResponse.ExampleComparison
    ]:
        for page in self.pages:
            yield from page.example_comparisons

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchExampleComparisonsAsyncPager:
    """A pager for iterating through ``search_example_comparisons`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``example_comparisons`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchExampleComparisons`` requests and continue to iterate
    through the ``example_comparisons`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_labeling_service.SearchExampleComparisonsResponse]
        ],
        request: data_labeling_service.SearchExampleComparisonsRequest,
        response: data_labeling_service.SearchExampleComparisonsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsResponse):
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
        self._request = data_labeling_service.SearchExampleComparisonsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_labeling_service.SearchExampleComparisonsResponse]:
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
    ) -> AsyncIterator[
        data_labeling_service.SearchExampleComparisonsResponse.ExampleComparison
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.example_comparisons:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationJobsPager:
    """A pager for iterating through ``list_evaluation_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``evaluation_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvaluationJobs`` requests and continue to iterate
    through the ``evaluation_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_labeling_service.ListEvaluationJobsResponse],
        request: data_labeling_service.ListEvaluationJobsRequest,
        response: data_labeling_service.ListEvaluationJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsResponse):
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
        self._request = data_labeling_service.ListEvaluationJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_labeling_service.ListEvaluationJobsResponse]:
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

    def __iter__(self) -> Iterator[evaluation_job.EvaluationJob]:
        for page in self.pages:
            yield from page.evaluation_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEvaluationJobsAsyncPager:
    """A pager for iterating through ``list_evaluation_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``evaluation_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvaluationJobs`` requests and continue to iterate
    through the ``evaluation_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_labeling_service.ListEvaluationJobsResponse]
        ],
        request: data_labeling_service.ListEvaluationJobsRequest,
        response: data_labeling_service.ListEvaluationJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsRequest):
                The initial request object.
            response (google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsResponse):
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
        self._request = data_labeling_service.ListEvaluationJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_labeling_service.ListEvaluationJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[evaluation_job.EvaluationJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.evaluation_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
