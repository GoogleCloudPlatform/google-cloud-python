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

from google.cloud.deploy_v1.types import cloud_deploy


class ListDeliveryPipelinesPager:
    """A pager for iterating through ``list_delivery_pipelines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``delivery_pipelines`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeliveryPipelines`` requests and continue to iterate
    through the ``delivery_pipelines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListDeliveryPipelinesResponse],
        request: cloud_deploy.ListDeliveryPipelinesRequest,
        response: cloud_deploy.ListDeliveryPipelinesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse):
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
        self._request = cloud_deploy.ListDeliveryPipelinesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListDeliveryPipelinesResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.DeliveryPipeline]:
        for page in self.pages:
            yield from page.delivery_pipelines

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeliveryPipelinesAsyncPager:
    """A pager for iterating through ``list_delivery_pipelines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``delivery_pipelines`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeliveryPipelines`` requests and continue to iterate
    through the ``delivery_pipelines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListDeliveryPipelinesResponse]],
        request: cloud_deploy.ListDeliveryPipelinesRequest,
        response: cloud_deploy.ListDeliveryPipelinesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse):
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
        self._request = cloud_deploy.ListDeliveryPipelinesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListDeliveryPipelinesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.DeliveryPipeline]:
        async def async_generator():
            async for page in self.pages:
                for response in page.delivery_pipelines:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTargetsPager:
    """A pager for iterating through ``list_targets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListTargetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``targets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTargets`` requests and continue to iterate
    through the ``targets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListTargetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListTargetsResponse],
        request: cloud_deploy.ListTargetsRequest,
        response: cloud_deploy.ListTargetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListTargetsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListTargetsResponse):
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
        self._request = cloud_deploy.ListTargetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListTargetsResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.Target]:
        for page in self.pages:
            yield from page.targets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTargetsAsyncPager:
    """A pager for iterating through ``list_targets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListTargetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``targets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTargets`` requests and continue to iterate
    through the ``targets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListTargetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListTargetsResponse]],
        request: cloud_deploy.ListTargetsRequest,
        response: cloud_deploy.ListTargetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListTargetsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListTargetsResponse):
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
        self._request = cloud_deploy.ListTargetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListTargetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Target]:
        async def async_generator():
            async for page in self.pages:
                for response in page.targets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomTargetTypesPager:
    """A pager for iterating through ``list_custom_target_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_target_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomTargetTypes`` requests and continue to iterate
    through the ``custom_target_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListCustomTargetTypesResponse],
        request: cloud_deploy.ListCustomTargetTypesRequest,
        response: cloud_deploy.ListCustomTargetTypesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListCustomTargetTypesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListCustomTargetTypesResponse):
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
        self._request = cloud_deploy.ListCustomTargetTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListCustomTargetTypesResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.CustomTargetType]:
        for page in self.pages:
            yield from page.custom_target_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomTargetTypesAsyncPager:
    """A pager for iterating through ``list_custom_target_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_target_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomTargetTypes`` requests and continue to iterate
    through the ``custom_target_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListCustomTargetTypesResponse]],
        request: cloud_deploy.ListCustomTargetTypesRequest,
        response: cloud_deploy.ListCustomTargetTypesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListCustomTargetTypesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListCustomTargetTypesResponse):
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
        self._request = cloud_deploy.ListCustomTargetTypesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListCustomTargetTypesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.CustomTargetType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.custom_target_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListReleasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListReleasesResponse],
        request: cloud_deploy.ListReleasesRequest,
        response: cloud_deploy.ListReleasesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListReleasesResponse):
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
        self._request = cloud_deploy.ListReleasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListReleasesResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.Release]:
        for page in self.pages:
            yield from page.releases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesAsyncPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListReleasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListReleasesResponse]],
        request: cloud_deploy.ListReleasesRequest,
        response: cloud_deploy.ListReleasesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListReleasesResponse):
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
        self._request = cloud_deploy.ListReleasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListReleasesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Release]:
        async def async_generator():
            async for page in self.pages:
                for response in page.releases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeployPoliciesPager:
    """A pager for iterating through ``list_deploy_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListDeployPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deploy_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeployPolicies`` requests and continue to iterate
    through the ``deploy_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListDeployPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListDeployPoliciesResponse],
        request: cloud_deploy.ListDeployPoliciesRequest,
        response: cloud_deploy.ListDeployPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListDeployPoliciesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListDeployPoliciesResponse):
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
        self._request = cloud_deploy.ListDeployPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListDeployPoliciesResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.DeployPolicy]:
        for page in self.pages:
            yield from page.deploy_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeployPoliciesAsyncPager:
    """A pager for iterating through ``list_deploy_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListDeployPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deploy_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeployPolicies`` requests and continue to iterate
    through the ``deploy_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListDeployPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListDeployPoliciesResponse]],
        request: cloud_deploy.ListDeployPoliciesRequest,
        response: cloud_deploy.ListDeployPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListDeployPoliciesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListDeployPoliciesResponse):
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
        self._request = cloud_deploy.ListDeployPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListDeployPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.DeployPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deploy_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRolloutsPager:
    """A pager for iterating through ``list_rollouts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListRolloutsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rollouts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRollouts`` requests and continue to iterate
    through the ``rollouts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListRolloutsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListRolloutsResponse],
        request: cloud_deploy.ListRolloutsRequest,
        response: cloud_deploy.ListRolloutsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListRolloutsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListRolloutsResponse):
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
        self._request = cloud_deploy.ListRolloutsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListRolloutsResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.Rollout]:
        for page in self.pages:
            yield from page.rollouts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRolloutsAsyncPager:
    """A pager for iterating through ``list_rollouts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListRolloutsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rollouts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRollouts`` requests and continue to iterate
    through the ``rollouts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListRolloutsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListRolloutsResponse]],
        request: cloud_deploy.ListRolloutsRequest,
        response: cloud_deploy.ListRolloutsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListRolloutsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListRolloutsResponse):
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
        self._request = cloud_deploy.ListRolloutsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListRolloutsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Rollout]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rollouts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobRunsPager:
    """A pager for iterating through ``list_job_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListJobRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``job_runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListJobRuns`` requests and continue to iterate
    through the ``job_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListJobRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListJobRunsResponse],
        request: cloud_deploy.ListJobRunsRequest,
        response: cloud_deploy.ListJobRunsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListJobRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListJobRunsResponse):
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
        self._request = cloud_deploy.ListJobRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListJobRunsResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.JobRun]:
        for page in self.pages:
            yield from page.job_runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobRunsAsyncPager:
    """A pager for iterating through ``list_job_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListJobRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``job_runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListJobRuns`` requests and continue to iterate
    through the ``job_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListJobRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListJobRunsResponse]],
        request: cloud_deploy.ListJobRunsRequest,
        response: cloud_deploy.ListJobRunsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListJobRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListJobRunsResponse):
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
        self._request = cloud_deploy.ListJobRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListJobRunsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.JobRun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.job_runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationsPager:
    """A pager for iterating through ``list_automations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``automations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutomations`` requests and continue to iterate
    through the ``automations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListAutomationsResponse],
        request: cloud_deploy.ListAutomationsRequest,
        response: cloud_deploy.ListAutomationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationsResponse):
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
        self._request = cloud_deploy.ListAutomationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListAutomationsResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.Automation]:
        for page in self.pages:
            yield from page.automations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationsAsyncPager:
    """A pager for iterating through ``list_automations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``automations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutomations`` requests and continue to iterate
    through the ``automations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListAutomationsResponse]],
        request: cloud_deploy.ListAutomationsRequest,
        response: cloud_deploy.ListAutomationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationsResponse):
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
        self._request = cloud_deploy.ListAutomationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListAutomationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Automation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.automations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationRunsPager:
    """A pager for iterating through ``list_automation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``automation_runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutomationRuns`` requests and continue to iterate
    through the ``automation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListAutomationRunsResponse],
        request: cloud_deploy.ListAutomationRunsRequest,
        response: cloud_deploy.ListAutomationRunsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationRunsResponse):
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
        self._request = cloud_deploy.ListAutomationRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListAutomationRunsResponse]:
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

    def __iter__(self) -> Iterator[cloud_deploy.AutomationRun]:
        for page in self.pages:
            yield from page.automation_runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationRunsAsyncPager:
    """A pager for iterating through ``list_automation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``automation_runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutomationRuns`` requests and continue to iterate
    through the ``automation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListAutomationRunsResponse]],
        request: cloud_deploy.ListAutomationRunsRequest,
        response: cloud_deploy.ListAutomationRunsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationRunsResponse):
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
        self._request = cloud_deploy.ListAutomationRunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListAutomationRunsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_deploy.AutomationRun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.automation_runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
