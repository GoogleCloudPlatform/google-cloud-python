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

from google.cloud.configdelivery_v1alpha.types import config_delivery


class ListResourceBundlesPager:
    """A pager for iterating through ``list_resource_bundles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListResourceBundlesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resource_bundles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListResourceBundles`` requests and continue to iterate
    through the ``resource_bundles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListResourceBundlesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., config_delivery.ListResourceBundlesResponse],
        request: config_delivery.ListResourceBundlesRequest,
        response: config_delivery.ListResourceBundlesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListResourceBundlesRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListResourceBundlesResponse):
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
        self._request = config_delivery.ListResourceBundlesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config_delivery.ListResourceBundlesResponse]:
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

    def __iter__(self) -> Iterator[config_delivery.ResourceBundle]:
        for page in self.pages:
            yield from page.resource_bundles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListResourceBundlesAsyncPager:
    """A pager for iterating through ``list_resource_bundles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListResourceBundlesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resource_bundles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListResourceBundles`` requests and continue to iterate
    through the ``resource_bundles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListResourceBundlesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[config_delivery.ListResourceBundlesResponse]],
        request: config_delivery.ListResourceBundlesRequest,
        response: config_delivery.ListResourceBundlesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListResourceBundlesRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListResourceBundlesResponse):
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
        self._request = config_delivery.ListResourceBundlesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config_delivery.ListResourceBundlesResponse]:
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

    def __aiter__(self) -> AsyncIterator[config_delivery.ResourceBundle]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resource_bundles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFleetPackagesPager:
    """A pager for iterating through ``list_fleet_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListFleetPackagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``fleet_packages`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFleetPackages`` requests and continue to iterate
    through the ``fleet_packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListFleetPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., config_delivery.ListFleetPackagesResponse],
        request: config_delivery.ListFleetPackagesRequest,
        response: config_delivery.ListFleetPackagesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListFleetPackagesRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListFleetPackagesResponse):
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
        self._request = config_delivery.ListFleetPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config_delivery.ListFleetPackagesResponse]:
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

    def __iter__(self) -> Iterator[config_delivery.FleetPackage]:
        for page in self.pages:
            yield from page.fleet_packages

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFleetPackagesAsyncPager:
    """A pager for iterating through ``list_fleet_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListFleetPackagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``fleet_packages`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFleetPackages`` requests and continue to iterate
    through the ``fleet_packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListFleetPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[config_delivery.ListFleetPackagesResponse]],
        request: config_delivery.ListFleetPackagesRequest,
        response: config_delivery.ListFleetPackagesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListFleetPackagesRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListFleetPackagesResponse):
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
        self._request = config_delivery.ListFleetPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config_delivery.ListFleetPackagesResponse]:
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

    def __aiter__(self) -> AsyncIterator[config_delivery.FleetPackage]:
        async def async_generator():
            async for page in self.pages:
                for response in page.fleet_packages:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListReleasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., config_delivery.ListReleasesResponse],
        request: config_delivery.ListReleasesRequest,
        response: config_delivery.ListReleasesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListReleasesResponse):
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
        self._request = config_delivery.ListReleasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config_delivery.ListReleasesResponse]:
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

    def __iter__(self) -> Iterator[config_delivery.Release]:
        for page in self.pages:
            yield from page.releases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesAsyncPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListReleasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[config_delivery.ListReleasesResponse]],
        request: config_delivery.ListReleasesRequest,
        response: config_delivery.ListReleasesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListReleasesResponse):
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
        self._request = config_delivery.ListReleasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config_delivery.ListReleasesResponse]:
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

    def __aiter__(self) -> AsyncIterator[config_delivery.Release]:
        async def async_generator():
            async for page in self.pages:
                for response in page.releases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVariantsPager:
    """A pager for iterating through ``list_variants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListVariantsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``variants`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVariants`` requests and continue to iterate
    through the ``variants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListVariantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., config_delivery.ListVariantsResponse],
        request: config_delivery.ListVariantsRequest,
        response: config_delivery.ListVariantsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListVariantsRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListVariantsResponse):
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
        self._request = config_delivery.ListVariantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config_delivery.ListVariantsResponse]:
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

    def __iter__(self) -> Iterator[config_delivery.Variant]:
        for page in self.pages:
            yield from page.variants

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVariantsAsyncPager:
    """A pager for iterating through ``list_variants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListVariantsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``variants`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVariants`` requests and continue to iterate
    through the ``variants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListVariantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[config_delivery.ListVariantsResponse]],
        request: config_delivery.ListVariantsRequest,
        response: config_delivery.ListVariantsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListVariantsRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListVariantsResponse):
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
        self._request = config_delivery.ListVariantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config_delivery.ListVariantsResponse]:
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

    def __aiter__(self) -> AsyncIterator[config_delivery.Variant]:
        async def async_generator():
            async for page in self.pages:
                for response in page.variants:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRolloutsPager:
    """A pager for iterating through ``list_rollouts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListRolloutsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rollouts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRollouts`` requests and continue to iterate
    through the ``rollouts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListRolloutsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., config_delivery.ListRolloutsResponse],
        request: config_delivery.ListRolloutsRequest,
        response: config_delivery.ListRolloutsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListRolloutsRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListRolloutsResponse):
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
        self._request = config_delivery.ListRolloutsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[config_delivery.ListRolloutsResponse]:
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

    def __iter__(self) -> Iterator[config_delivery.Rollout]:
        for page in self.pages:
            yield from page.rollouts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRolloutsAsyncPager:
    """A pager for iterating through ``list_rollouts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.configdelivery_v1alpha.types.ListRolloutsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rollouts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRollouts`` requests and continue to iterate
    through the ``rollouts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.configdelivery_v1alpha.types.ListRolloutsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[config_delivery.ListRolloutsResponse]],
        request: config_delivery.ListRolloutsRequest,
        response: config_delivery.ListRolloutsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.configdelivery_v1alpha.types.ListRolloutsRequest):
                The initial request object.
            response (google.cloud.configdelivery_v1alpha.types.ListRolloutsResponse):
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
        self._request = config_delivery.ListRolloutsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[config_delivery.ListRolloutsResponse]:
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

    def __aiter__(self) -> AsyncIterator[config_delivery.Rollout]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rollouts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
