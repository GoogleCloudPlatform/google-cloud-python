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

from google.cloud.gkehub_v1.types import feature, fleet, membership, service


class ListMembershipsPager:
    """A pager for iterating through ``list_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListMembershipsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMemberships`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListMembershipsResponse],
        request: service.ListMembershipsRequest,
        response: service.ListMembershipsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListMembershipsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListMembershipsResponse):
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
        self._request = service.ListMembershipsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListMembershipsResponse]:
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

    def __iter__(self) -> Iterator[membership.Membership]:
        for page in self.pages:
            yield from page.resources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMembershipsAsyncPager:
    """A pager for iterating through ``list_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListMembershipsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMemberships`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListMembershipsResponse]],
        request: service.ListMembershipsRequest,
        response: service.ListMembershipsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListMembershipsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListMembershipsResponse):
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
        self._request = service.ListMembershipsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListMembershipsResponse]:
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

    def __aiter__(self) -> AsyncIterator[membership.Membership]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBoundMembershipsPager:
    """A pager for iterating through ``list_bound_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListBoundMembershipsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``memberships`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBoundMemberships`` requests and continue to iterate
    through the ``memberships`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListBoundMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListBoundMembershipsResponse],
        request: service.ListBoundMembershipsRequest,
        response: service.ListBoundMembershipsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListBoundMembershipsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListBoundMembershipsResponse):
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
        self._request = service.ListBoundMembershipsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListBoundMembershipsResponse]:
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

    def __iter__(self) -> Iterator[membership.Membership]:
        for page in self.pages:
            yield from page.memberships

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBoundMembershipsAsyncPager:
    """A pager for iterating through ``list_bound_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListBoundMembershipsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``memberships`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBoundMemberships`` requests and continue to iterate
    through the ``memberships`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListBoundMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListBoundMembershipsResponse]],
        request: service.ListBoundMembershipsRequest,
        response: service.ListBoundMembershipsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListBoundMembershipsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListBoundMembershipsResponse):
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
        self._request = service.ListBoundMembershipsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListBoundMembershipsResponse]:
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

    def __aiter__(self) -> AsyncIterator[membership.Membership]:
        async def async_generator():
            async for page in self.pages:
                for response in page.memberships:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeaturesPager:
    """A pager for iterating through ``list_features`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListFeaturesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFeatures`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListFeaturesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListFeaturesResponse],
        request: service.ListFeaturesRequest,
        response: service.ListFeaturesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListFeaturesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListFeaturesResponse):
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
        self._request = service.ListFeaturesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListFeaturesResponse]:
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

    def __iter__(self) -> Iterator[feature.Feature]:
        for page in self.pages:
            yield from page.resources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeaturesAsyncPager:
    """A pager for iterating through ``list_features`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListFeaturesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFeatures`` requests and continue to iterate
    through the ``resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListFeaturesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListFeaturesResponse]],
        request: service.ListFeaturesRequest,
        response: service.ListFeaturesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListFeaturesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListFeaturesResponse):
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
        self._request = service.ListFeaturesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListFeaturesResponse]:
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

    def __aiter__(self) -> AsyncIterator[feature.Feature]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFleetsPager:
    """A pager for iterating through ``list_fleets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListFleetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``fleets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFleets`` requests and continue to iterate
    through the ``fleets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListFleetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListFleetsResponse],
        request: service.ListFleetsRequest,
        response: service.ListFleetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListFleetsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListFleetsResponse):
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
        self._request = service.ListFleetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListFleetsResponse]:
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

    def __iter__(self) -> Iterator[fleet.Fleet]:
        for page in self.pages:
            yield from page.fleets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFleetsAsyncPager:
    """A pager for iterating through ``list_fleets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListFleetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``fleets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFleets`` requests and continue to iterate
    through the ``fleets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListFleetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListFleetsResponse]],
        request: service.ListFleetsRequest,
        response: service.ListFleetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListFleetsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListFleetsResponse):
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
        self._request = service.ListFleetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListFleetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[fleet.Fleet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.fleets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScopeNamespacesPager:
    """A pager for iterating through ``list_scope_namespaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListScopeNamespacesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``scope_namespaces`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListScopeNamespaces`` requests and continue to iterate
    through the ``scope_namespaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListScopeNamespacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListScopeNamespacesResponse],
        request: service.ListScopeNamespacesRequest,
        response: service.ListScopeNamespacesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListScopeNamespacesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListScopeNamespacesResponse):
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
        self._request = service.ListScopeNamespacesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListScopeNamespacesResponse]:
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

    def __iter__(self) -> Iterator[fleet.Namespace]:
        for page in self.pages:
            yield from page.scope_namespaces

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScopeNamespacesAsyncPager:
    """A pager for iterating through ``list_scope_namespaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListScopeNamespacesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``scope_namespaces`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListScopeNamespaces`` requests and continue to iterate
    through the ``scope_namespaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListScopeNamespacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListScopeNamespacesResponse]],
        request: service.ListScopeNamespacesRequest,
        response: service.ListScopeNamespacesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListScopeNamespacesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListScopeNamespacesResponse):
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
        self._request = service.ListScopeNamespacesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListScopeNamespacesResponse]:
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

    def __aiter__(self) -> AsyncIterator[fleet.Namespace]:
        async def async_generator():
            async for page in self.pages:
                for response in page.scope_namespaces:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScopeRBACRoleBindingsPager:
    """A pager for iterating through ``list_scope_rbac_role_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rbacrolebindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListScopeRBACRoleBindings`` requests and continue to iterate
    through the ``rbacrolebindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListScopeRBACRoleBindingsResponse],
        request: service.ListScopeRBACRoleBindingsRequest,
        response: service.ListScopeRBACRoleBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsResponse):
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
        self._request = service.ListScopeRBACRoleBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListScopeRBACRoleBindingsResponse]:
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

    def __iter__(self) -> Iterator[fleet.RBACRoleBinding]:
        for page in self.pages:
            yield from page.rbacrolebindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScopeRBACRoleBindingsAsyncPager:
    """A pager for iterating through ``list_scope_rbac_role_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rbacrolebindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListScopeRBACRoleBindings`` requests and continue to iterate
    through the ``rbacrolebindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListScopeRBACRoleBindingsResponse]],
        request: service.ListScopeRBACRoleBindingsRequest,
        response: service.ListScopeRBACRoleBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListScopeRBACRoleBindingsResponse):
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
        self._request = service.ListScopeRBACRoleBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListScopeRBACRoleBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[fleet.RBACRoleBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rbacrolebindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScopesPager:
    """A pager for iterating through ``list_scopes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListScopesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``scopes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListScopes`` requests and continue to iterate
    through the ``scopes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListScopesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListScopesResponse],
        request: service.ListScopesRequest,
        response: service.ListScopesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListScopesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListScopesResponse):
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
        self._request = service.ListScopesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListScopesResponse]:
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

    def __iter__(self) -> Iterator[fleet.Scope]:
        for page in self.pages:
            yield from page.scopes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListScopesAsyncPager:
    """A pager for iterating through ``list_scopes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListScopesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``scopes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListScopes`` requests and continue to iterate
    through the ``scopes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListScopesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListScopesResponse]],
        request: service.ListScopesRequest,
        response: service.ListScopesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListScopesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListScopesResponse):
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
        self._request = service.ListScopesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListScopesResponse]:
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

    def __aiter__(self) -> AsyncIterator[fleet.Scope]:
        async def async_generator():
            async for page in self.pages:
                for response in page.scopes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPermittedScopesPager:
    """A pager for iterating through ``list_permitted_scopes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListPermittedScopesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``scopes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPermittedScopes`` requests and continue to iterate
    through the ``scopes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListPermittedScopesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListPermittedScopesResponse],
        request: service.ListPermittedScopesRequest,
        response: service.ListPermittedScopesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListPermittedScopesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListPermittedScopesResponse):
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
        self._request = service.ListPermittedScopesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListPermittedScopesResponse]:
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

    def __iter__(self) -> Iterator[fleet.Scope]:
        for page in self.pages:
            yield from page.scopes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPermittedScopesAsyncPager:
    """A pager for iterating through ``list_permitted_scopes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListPermittedScopesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``scopes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPermittedScopes`` requests and continue to iterate
    through the ``scopes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListPermittedScopesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListPermittedScopesResponse]],
        request: service.ListPermittedScopesRequest,
        response: service.ListPermittedScopesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListPermittedScopesRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListPermittedScopesResponse):
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
        self._request = service.ListPermittedScopesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListPermittedScopesResponse]:
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

    def __aiter__(self) -> AsyncIterator[fleet.Scope]:
        async def async_generator():
            async for page in self.pages:
                for response in page.scopes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMembershipBindingsPager:
    """A pager for iterating through ``list_membership_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListMembershipBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``membership_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMembershipBindings`` requests and continue to iterate
    through the ``membership_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListMembershipBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListMembershipBindingsResponse],
        request: service.ListMembershipBindingsRequest,
        response: service.ListMembershipBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListMembershipBindingsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListMembershipBindingsResponse):
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
        self._request = service.ListMembershipBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListMembershipBindingsResponse]:
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

    def __iter__(self) -> Iterator[fleet.MembershipBinding]:
        for page in self.pages:
            yield from page.membership_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMembershipBindingsAsyncPager:
    """A pager for iterating through ``list_membership_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListMembershipBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``membership_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMembershipBindings`` requests and continue to iterate
    through the ``membership_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListMembershipBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListMembershipBindingsResponse]],
        request: service.ListMembershipBindingsRequest,
        response: service.ListMembershipBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListMembershipBindingsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListMembershipBindingsResponse):
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
        self._request = service.ListMembershipBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListMembershipBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[fleet.MembershipBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.membership_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMembershipRBACRoleBindingsPager:
    """A pager for iterating through ``list_membership_rbac_role_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rbacrolebindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMembershipRBACRoleBindings`` requests and continue to iterate
    through the ``rbacrolebindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListMembershipRBACRoleBindingsResponse],
        request: service.ListMembershipRBACRoleBindingsRequest,
        response: service.ListMembershipRBACRoleBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsResponse):
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
        self._request = service.ListMembershipRBACRoleBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListMembershipRBACRoleBindingsResponse]:
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

    def __iter__(self) -> Iterator[fleet.RBACRoleBinding]:
        for page in self.pages:
            yield from page.rbacrolebindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMembershipRBACRoleBindingsAsyncPager:
    """A pager for iterating through ``list_membership_rbac_role_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rbacrolebindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMembershipRBACRoleBindings`` requests and continue to iterate
    through the ``rbacrolebindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[service.ListMembershipRBACRoleBindingsResponse]
        ],
        request: service.ListMembershipRBACRoleBindingsRequest,
        response: service.ListMembershipRBACRoleBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsRequest):
                The initial request object.
            response (google.cloud.gkehub_v1.types.ListMembershipRBACRoleBindingsResponse):
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
        self._request = service.ListMembershipRBACRoleBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[service.ListMembershipRBACRoleBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[fleet.RBACRoleBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rbacrolebindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
