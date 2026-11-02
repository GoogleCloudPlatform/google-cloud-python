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

from google.cloud.kms_v1.types import hsm_management


class ListSingleTenantHsmInstancesPager:
    """A pager for iterating through ``list_single_tenant_hsm_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``single_tenant_hsm_instances`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSingleTenantHsmInstances`` requests and continue to iterate
    through the ``single_tenant_hsm_instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., hsm_management.ListSingleTenantHsmInstancesResponse],
        request: hsm_management.ListSingleTenantHsmInstancesRequest,
        response: hsm_management.ListSingleTenantHsmInstancesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListSingleTenantHsmInstancesRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListSingleTenantHsmInstancesResponse):
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
        self._request = hsm_management.ListSingleTenantHsmInstancesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[hsm_management.ListSingleTenantHsmInstancesResponse]:
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

    def __iter__(self) -> Iterator[hsm_management.SingleTenantHsmInstance]:
        for page in self.pages:
            yield from page.single_tenant_hsm_instances

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSingleTenantHsmInstancesAsyncPager:
    """A pager for iterating through ``list_single_tenant_hsm_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstancesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``single_tenant_hsm_instances`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSingleTenantHsmInstances`` requests and continue to iterate
    through the ``single_tenant_hsm_instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[hsm_management.ListSingleTenantHsmInstancesResponse]
        ],
        request: hsm_management.ListSingleTenantHsmInstancesRequest,
        response: hsm_management.ListSingleTenantHsmInstancesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListSingleTenantHsmInstancesRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListSingleTenantHsmInstancesResponse):
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
        self._request = hsm_management.ListSingleTenantHsmInstancesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[hsm_management.ListSingleTenantHsmInstancesResponse]:
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

    def __aiter__(self) -> AsyncIterator[hsm_management.SingleTenantHsmInstance]:
        async def async_generator():
            async for page in self.pages:
                for response in page.single_tenant_hsm_instances:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSingleTenantHsmInstanceProposalsPager:
    """A pager for iterating through ``list_single_tenant_hsm_instance_proposals`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``single_tenant_hsm_instance_proposals`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSingleTenantHsmInstanceProposals`` requests and continue to iterate
    through the ``single_tenant_hsm_instance_proposals`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., hsm_management.ListSingleTenantHsmInstanceProposalsResponse
        ],
        request: hsm_management.ListSingleTenantHsmInstanceProposalsRequest,
        response: hsm_management.ListSingleTenantHsmInstanceProposalsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse):
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
        self._request = hsm_management.ListSingleTenantHsmInstanceProposalsRequest(
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
    ) -> Iterator[hsm_management.ListSingleTenantHsmInstanceProposalsResponse]:
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

    def __iter__(self) -> Iterator[hsm_management.SingleTenantHsmInstanceProposal]:
        for page in self.pages:
            yield from page.single_tenant_hsm_instance_proposals

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSingleTenantHsmInstanceProposalsAsyncPager:
    """A pager for iterating through ``list_single_tenant_hsm_instance_proposals`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``single_tenant_hsm_instance_proposals`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSingleTenantHsmInstanceProposals`` requests and continue to iterate
    through the ``single_tenant_hsm_instance_proposals`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[hsm_management.ListSingleTenantHsmInstanceProposalsResponse]
        ],
        request: hsm_management.ListSingleTenantHsmInstanceProposalsRequest,
        response: hsm_management.ListSingleTenantHsmInstanceProposalsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse):
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
        self._request = hsm_management.ListSingleTenantHsmInstanceProposalsRequest(
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
    ) -> AsyncIterator[hsm_management.ListSingleTenantHsmInstanceProposalsResponse]:
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
    ) -> AsyncIterator[hsm_management.SingleTenantHsmInstanceProposal]:
        async def async_generator():
            async for page in self.pages:
                for response in page.single_tenant_hsm_instance_proposals:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
