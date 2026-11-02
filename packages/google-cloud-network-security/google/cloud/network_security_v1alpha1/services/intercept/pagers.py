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

from google.cloud.network_security_v1alpha1.types import intercept


class ListInterceptEndpointGroupsPager:
    """A pager for iterating through ``list_intercept_endpoint_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``intercept_endpoint_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInterceptEndpointGroups`` requests and continue to iterate
    through the ``intercept_endpoint_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., intercept.ListInterceptEndpointGroupsResponse],
        request: intercept.ListInterceptEndpointGroupsRequest,
        response: intercept.ListInterceptEndpointGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsResponse):
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
        self._request = intercept.ListInterceptEndpointGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[intercept.ListInterceptEndpointGroupsResponse]:
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

    def __iter__(self) -> Iterator[intercept.InterceptEndpointGroup]:
        for page in self.pages:
            yield from page.intercept_endpoint_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterceptEndpointGroupsAsyncPager:
    """A pager for iterating through ``list_intercept_endpoint_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``intercept_endpoint_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInterceptEndpointGroups`` requests and continue to iterate
    through the ``intercept_endpoint_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[intercept.ListInterceptEndpointGroupsResponse]],
        request: intercept.ListInterceptEndpointGroupsRequest,
        response: intercept.ListInterceptEndpointGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupsResponse):
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
        self._request = intercept.ListInterceptEndpointGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[intercept.ListInterceptEndpointGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[intercept.InterceptEndpointGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.intercept_endpoint_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterceptEndpointGroupAssociationsPager:
    """A pager for iterating through ``list_intercept_endpoint_group_associations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``intercept_endpoint_group_associations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInterceptEndpointGroupAssociations`` requests and continue to iterate
    through the ``intercept_endpoint_group_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., intercept.ListInterceptEndpointGroupAssociationsResponse],
        request: intercept.ListInterceptEndpointGroupAssociationsRequest,
        response: intercept.ListInterceptEndpointGroupAssociationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsResponse):
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
        self._request = intercept.ListInterceptEndpointGroupAssociationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[intercept.ListInterceptEndpointGroupAssociationsResponse]:
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

    def __iter__(self) -> Iterator[intercept.InterceptEndpointGroupAssociation]:
        for page in self.pages:
            yield from page.intercept_endpoint_group_associations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterceptEndpointGroupAssociationsAsyncPager:
    """A pager for iterating through ``list_intercept_endpoint_group_associations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``intercept_endpoint_group_associations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInterceptEndpointGroupAssociations`` requests and continue to iterate
    through the ``intercept_endpoint_group_associations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[intercept.ListInterceptEndpointGroupAssociationsResponse]
        ],
        request: intercept.ListInterceptEndpointGroupAssociationsRequest,
        response: intercept.ListInterceptEndpointGroupAssociationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptEndpointGroupAssociationsResponse):
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
        self._request = intercept.ListInterceptEndpointGroupAssociationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[intercept.ListInterceptEndpointGroupAssociationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[intercept.InterceptEndpointGroupAssociation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.intercept_endpoint_group_associations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterceptDeploymentGroupsPager:
    """A pager for iterating through ``list_intercept_deployment_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``intercept_deployment_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInterceptDeploymentGroups`` requests and continue to iterate
    through the ``intercept_deployment_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., intercept.ListInterceptDeploymentGroupsResponse],
        request: intercept.ListInterceptDeploymentGroupsRequest,
        response: intercept.ListInterceptDeploymentGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsResponse):
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
        self._request = intercept.ListInterceptDeploymentGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[intercept.ListInterceptDeploymentGroupsResponse]:
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

    def __iter__(self) -> Iterator[intercept.InterceptDeploymentGroup]:
        for page in self.pages:
            yield from page.intercept_deployment_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterceptDeploymentGroupsAsyncPager:
    """A pager for iterating through ``list_intercept_deployment_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``intercept_deployment_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInterceptDeploymentGroups`` requests and continue to iterate
    through the ``intercept_deployment_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[intercept.ListInterceptDeploymentGroupsResponse]
        ],
        request: intercept.ListInterceptDeploymentGroupsRequest,
        response: intercept.ListInterceptDeploymentGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentGroupsResponse):
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
        self._request = intercept.ListInterceptDeploymentGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[intercept.ListInterceptDeploymentGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[intercept.InterceptDeploymentGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.intercept_deployment_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterceptDeploymentsPager:
    """A pager for iterating through ``list_intercept_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``intercept_deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInterceptDeployments`` requests and continue to iterate
    through the ``intercept_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., intercept.ListInterceptDeploymentsResponse],
        request: intercept.ListInterceptDeploymentsRequest,
        response: intercept.ListInterceptDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsResponse):
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
        self._request = intercept.ListInterceptDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[intercept.ListInterceptDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[intercept.InterceptDeployment]:
        for page in self.pages:
            yield from page.intercept_deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInterceptDeploymentsAsyncPager:
    """A pager for iterating through ``list_intercept_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``intercept_deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInterceptDeployments`` requests and continue to iterate
    through the ``intercept_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[intercept.ListInterceptDeploymentsResponse]],
        request: intercept.ListInterceptDeploymentsRequest,
        response: intercept.ListInterceptDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsRequest):
                The initial request object.
            response (google.cloud.network_security_v1alpha1.types.ListInterceptDeploymentsResponse):
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
        self._request = intercept.ListInterceptDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[intercept.ListInterceptDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[intercept.InterceptDeployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.intercept_deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
