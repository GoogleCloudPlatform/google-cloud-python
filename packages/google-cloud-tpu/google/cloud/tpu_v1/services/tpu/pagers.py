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

from google.cloud.tpu_v1.types import cloud_tpu


class ListNodesPager:
    """A pager for iterating through ``list_nodes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.tpu_v1.types.ListNodesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``nodes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNodes`` requests and continue to iterate
    through the ``nodes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.tpu_v1.types.ListNodesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_tpu.ListNodesResponse],
        request: cloud_tpu.ListNodesRequest,
        response: cloud_tpu.ListNodesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.tpu_v1.types.ListNodesRequest):
                The initial request object.
            response (google.cloud.tpu_v1.types.ListNodesResponse):
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
        self._request = cloud_tpu.ListNodesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_tpu.ListNodesResponse]:
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

    def __iter__(self) -> Iterator[cloud_tpu.Node]:
        for page in self.pages:
            yield from page.nodes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNodesAsyncPager:
    """A pager for iterating through ``list_nodes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.tpu_v1.types.ListNodesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``nodes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNodes`` requests and continue to iterate
    through the ``nodes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.tpu_v1.types.ListNodesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_tpu.ListNodesResponse]],
        request: cloud_tpu.ListNodesRequest,
        response: cloud_tpu.ListNodesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.tpu_v1.types.ListNodesRequest):
                The initial request object.
            response (google.cloud.tpu_v1.types.ListNodesResponse):
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
        self._request = cloud_tpu.ListNodesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_tpu.ListNodesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_tpu.Node]:
        async def async_generator():
            async for page in self.pages:
                for response in page.nodes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTensorFlowVersionsPager:
    """A pager for iterating through ``list_tensor_flow_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.tpu_v1.types.ListTensorFlowVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tensorflow_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTensorFlowVersions`` requests and continue to iterate
    through the ``tensorflow_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.tpu_v1.types.ListTensorFlowVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_tpu.ListTensorFlowVersionsResponse],
        request: cloud_tpu.ListTensorFlowVersionsRequest,
        response: cloud_tpu.ListTensorFlowVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.tpu_v1.types.ListTensorFlowVersionsRequest):
                The initial request object.
            response (google.cloud.tpu_v1.types.ListTensorFlowVersionsResponse):
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
        self._request = cloud_tpu.ListTensorFlowVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_tpu.ListTensorFlowVersionsResponse]:
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

    def __iter__(self) -> Iterator[cloud_tpu.TensorFlowVersion]:
        for page in self.pages:
            yield from page.tensorflow_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTensorFlowVersionsAsyncPager:
    """A pager for iterating through ``list_tensor_flow_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.tpu_v1.types.ListTensorFlowVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tensorflow_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTensorFlowVersions`` requests and continue to iterate
    through the ``tensorflow_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.tpu_v1.types.ListTensorFlowVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_tpu.ListTensorFlowVersionsResponse]],
        request: cloud_tpu.ListTensorFlowVersionsRequest,
        response: cloud_tpu.ListTensorFlowVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.tpu_v1.types.ListTensorFlowVersionsRequest):
                The initial request object.
            response (google.cloud.tpu_v1.types.ListTensorFlowVersionsResponse):
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
        self._request = cloud_tpu.ListTensorFlowVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_tpu.ListTensorFlowVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_tpu.TensorFlowVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tensorflow_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAcceleratorTypesPager:
    """A pager for iterating through ``list_accelerator_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.tpu_v1.types.ListAcceleratorTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``accelerator_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAcceleratorTypes`` requests and continue to iterate
    through the ``accelerator_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.tpu_v1.types.ListAcceleratorTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_tpu.ListAcceleratorTypesResponse],
        request: cloud_tpu.ListAcceleratorTypesRequest,
        response: cloud_tpu.ListAcceleratorTypesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.tpu_v1.types.ListAcceleratorTypesRequest):
                The initial request object.
            response (google.cloud.tpu_v1.types.ListAcceleratorTypesResponse):
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
        self._request = cloud_tpu.ListAcceleratorTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_tpu.ListAcceleratorTypesResponse]:
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

    def __iter__(self) -> Iterator[cloud_tpu.AcceleratorType]:
        for page in self.pages:
            yield from page.accelerator_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAcceleratorTypesAsyncPager:
    """A pager for iterating through ``list_accelerator_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.tpu_v1.types.ListAcceleratorTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``accelerator_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAcceleratorTypes`` requests and continue to iterate
    through the ``accelerator_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.tpu_v1.types.ListAcceleratorTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_tpu.ListAcceleratorTypesResponse]],
        request: cloud_tpu.ListAcceleratorTypesRequest,
        response: cloud_tpu.ListAcceleratorTypesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.tpu_v1.types.ListAcceleratorTypesRequest):
                The initial request object.
            response (google.cloud.tpu_v1.types.ListAcceleratorTypesResponse):
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
        self._request = cloud_tpu.ListAcceleratorTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_tpu.ListAcceleratorTypesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_tpu.AcceleratorType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.accelerator_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
