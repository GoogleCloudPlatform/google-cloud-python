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

from google.cloud.osconfig_v1.types import patch_deployments, patch_jobs


class ListPatchJobsPager:
    """A pager for iterating through ``list_patch_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListPatchJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``patch_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPatchJobs`` requests and continue to iterate
    through the ``patch_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListPatchJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., patch_jobs.ListPatchJobsResponse],
        request: patch_jobs.ListPatchJobsRequest,
        response: patch_jobs.ListPatchJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListPatchJobsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListPatchJobsResponse):
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
        self._request = patch_jobs.ListPatchJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[patch_jobs.ListPatchJobsResponse]:
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

    def __iter__(self) -> Iterator[patch_jobs.PatchJob]:
        for page in self.pages:
            yield from page.patch_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPatchJobsAsyncPager:
    """A pager for iterating through ``list_patch_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListPatchJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``patch_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPatchJobs`` requests and continue to iterate
    through the ``patch_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListPatchJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[patch_jobs.ListPatchJobsResponse]],
        request: patch_jobs.ListPatchJobsRequest,
        response: patch_jobs.ListPatchJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListPatchJobsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListPatchJobsResponse):
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
        self._request = patch_jobs.ListPatchJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[patch_jobs.ListPatchJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[patch_jobs.PatchJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.patch_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPatchJobInstanceDetailsPager:
    """A pager for iterating through ``list_patch_job_instance_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``patch_job_instance_details`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPatchJobInstanceDetails`` requests and continue to iterate
    through the ``patch_job_instance_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., patch_jobs.ListPatchJobInstanceDetailsResponse],
        request: patch_jobs.ListPatchJobInstanceDetailsRequest,
        response: patch_jobs.ListPatchJobInstanceDetailsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsResponse):
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
        self._request = patch_jobs.ListPatchJobInstanceDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[patch_jobs.ListPatchJobInstanceDetailsResponse]:
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

    def __iter__(self) -> Iterator[patch_jobs.PatchJobInstanceDetails]:
        for page in self.pages:
            yield from page.patch_job_instance_details

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPatchJobInstanceDetailsAsyncPager:
    """A pager for iterating through ``list_patch_job_instance_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``patch_job_instance_details`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPatchJobInstanceDetails`` requests and continue to iterate
    through the ``patch_job_instance_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[patch_jobs.ListPatchJobInstanceDetailsResponse]
        ],
        request: patch_jobs.ListPatchJobInstanceDetailsRequest,
        response: patch_jobs.ListPatchJobInstanceDetailsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListPatchJobInstanceDetailsResponse):
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
        self._request = patch_jobs.ListPatchJobInstanceDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[patch_jobs.ListPatchJobInstanceDetailsResponse]:
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

    def __aiter__(self) -> AsyncIterator[patch_jobs.PatchJobInstanceDetails]:
        async def async_generator():
            async for page in self.pages:
                for response in page.patch_job_instance_details:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPatchDeploymentsPager:
    """A pager for iterating through ``list_patch_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListPatchDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``patch_deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPatchDeployments`` requests and continue to iterate
    through the ``patch_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListPatchDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., patch_deployments.ListPatchDeploymentsResponse],
        request: patch_deployments.ListPatchDeploymentsRequest,
        response: patch_deployments.ListPatchDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListPatchDeploymentsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListPatchDeploymentsResponse):
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
        self._request = patch_deployments.ListPatchDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[patch_deployments.ListPatchDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[patch_deployments.PatchDeployment]:
        for page in self.pages:
            yield from page.patch_deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPatchDeploymentsAsyncPager:
    """A pager for iterating through ``list_patch_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.osconfig_v1.types.ListPatchDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``patch_deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPatchDeployments`` requests and continue to iterate
    through the ``patch_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.osconfig_v1.types.ListPatchDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[patch_deployments.ListPatchDeploymentsResponse]
        ],
        request: patch_deployments.ListPatchDeploymentsRequest,
        response: patch_deployments.ListPatchDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.osconfig_v1.types.ListPatchDeploymentsRequest):
                The initial request object.
            response (google.cloud.osconfig_v1.types.ListPatchDeploymentsResponse):
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
        self._request = patch_deployments.ListPatchDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[patch_deployments.ListPatchDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[patch_deployments.PatchDeployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.patch_deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
