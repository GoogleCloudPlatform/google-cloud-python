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

from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import (
    deployments_resources,
    deployments_service,
)


class ListSaasPager:
    """A pager for iterating through ``list_saas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``saas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSaas`` requests and continue to iterate
    through the ``saas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., deployments_service.ListSaasResponse],
        request: deployments_service.ListSaasRequest,
        response: deployments_service.ListSaasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasResponse):
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
        self._request = deployments_service.ListSaasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[deployments_service.ListSaasResponse]:
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

    def __iter__(self) -> Iterator[deployments_resources.Saas]:
        for page in self.pages:
            yield from page.saas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSaasAsyncPager:
    """A pager for iterating through ``list_saas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``saas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSaas`` requests and continue to iterate
    through the ``saas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[deployments_service.ListSaasResponse]],
        request: deployments_service.ListSaasRequest,
        response: deployments_service.ListSaasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListSaasResponse):
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
        self._request = deployments_service.ListSaasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[deployments_service.ListSaasResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployments_resources.Saas]:
        async def async_generator():
            async for page in self.pages:
                for response in page.saas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTenantsPager:
    """A pager for iterating through ``list_tenants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tenants`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTenants`` requests and continue to iterate
    through the ``tenants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., deployments_service.ListTenantsResponse],
        request: deployments_service.ListTenantsRequest,
        response: deployments_service.ListTenantsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsResponse):
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
        self._request = deployments_service.ListTenantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[deployments_service.ListTenantsResponse]:
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

    def __iter__(self) -> Iterator[deployments_resources.Tenant]:
        for page in self.pages:
            yield from page.tenants

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTenantsAsyncPager:
    """A pager for iterating through ``list_tenants`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tenants`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTenants`` requests and continue to iterate
    through the ``tenants`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[deployments_service.ListTenantsResponse]],
        request: deployments_service.ListTenantsRequest,
        response: deployments_service.ListTenantsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListTenantsResponse):
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
        self._request = deployments_service.ListTenantsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[deployments_service.ListTenantsResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployments_resources.Tenant]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tenants:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUnitKindsPager:
    """A pager for iterating through ``list_unit_kinds`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``unit_kinds`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUnitKinds`` requests and continue to iterate
    through the ``unit_kinds`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., deployments_service.ListUnitKindsResponse],
        request: deployments_service.ListUnitKindsRequest,
        response: deployments_service.ListUnitKindsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsResponse):
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
        self._request = deployments_service.ListUnitKindsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[deployments_service.ListUnitKindsResponse]:
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

    def __iter__(self) -> Iterator[deployments_resources.UnitKind]:
        for page in self.pages:
            yield from page.unit_kinds

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUnitKindsAsyncPager:
    """A pager for iterating through ``list_unit_kinds`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``unit_kinds`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUnitKinds`` requests and continue to iterate
    through the ``unit_kinds`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[deployments_service.ListUnitKindsResponse]],
        request: deployments_service.ListUnitKindsRequest,
        response: deployments_service.ListUnitKindsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitKindsResponse):
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
        self._request = deployments_service.ListUnitKindsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[deployments_service.ListUnitKindsResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployments_resources.UnitKind]:
        async def async_generator():
            async for page in self.pages:
                for response in page.unit_kinds:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUnitsPager:
    """A pager for iterating through ``list_units`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``units`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUnits`` requests and continue to iterate
    through the ``units`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., deployments_service.ListUnitsResponse],
        request: deployments_service.ListUnitsRequest,
        response: deployments_service.ListUnitsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsResponse):
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
        self._request = deployments_service.ListUnitsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[deployments_service.ListUnitsResponse]:
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

    def __iter__(self) -> Iterator[deployments_resources.Unit]:
        for page in self.pages:
            yield from page.units

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUnitsAsyncPager:
    """A pager for iterating through ``list_units`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``units`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUnits`` requests and continue to iterate
    through the ``units`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[deployments_service.ListUnitsResponse]],
        request: deployments_service.ListUnitsRequest,
        response: deployments_service.ListUnitsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitsResponse):
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
        self._request = deployments_service.ListUnitsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[deployments_service.ListUnitsResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployments_resources.Unit]:
        async def async_generator():
            async for page in self.pages:
                for response in page.units:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUnitOperationsPager:
    """A pager for iterating through ``list_unit_operations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``unit_operations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUnitOperations`` requests and continue to iterate
    through the ``unit_operations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., deployments_service.ListUnitOperationsResponse],
        request: deployments_service.ListUnitOperationsRequest,
        response: deployments_service.ListUnitOperationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsResponse):
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
        self._request = deployments_service.ListUnitOperationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[deployments_service.ListUnitOperationsResponse]:
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

    def __iter__(self) -> Iterator[deployments_resources.UnitOperation]:
        for page in self.pages:
            yield from page.unit_operations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUnitOperationsAsyncPager:
    """A pager for iterating through ``list_unit_operations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``unit_operations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUnitOperations`` requests and continue to iterate
    through the ``unit_operations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[deployments_service.ListUnitOperationsResponse]
        ],
        request: deployments_service.ListUnitOperationsRequest,
        response: deployments_service.ListUnitOperationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListUnitOperationsResponse):
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
        self._request = deployments_service.ListUnitOperationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[deployments_service.ListUnitOperationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployments_resources.UnitOperation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.unit_operations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., deployments_service.ListReleasesResponse],
        request: deployments_service.ListReleasesRequest,
        response: deployments_service.ListReleasesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesResponse):
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
        self._request = deployments_service.ListReleasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[deployments_service.ListReleasesResponse]:
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

    def __iter__(self) -> Iterator[deployments_resources.Release]:
        for page in self.pages:
            yield from page.releases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesAsyncPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[deployments_service.ListReleasesResponse]],
        request: deployments_service.ListReleasesRequest,
        response: deployments_service.ListReleasesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListReleasesResponse):
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
        self._request = deployments_service.ListReleasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[deployments_service.ListReleasesResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployments_resources.Release]:
        async def async_generator():
            async for page in self.pages:
                for response in page.releases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
