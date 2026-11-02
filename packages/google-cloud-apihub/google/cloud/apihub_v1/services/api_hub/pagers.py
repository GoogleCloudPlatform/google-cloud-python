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

from google.cloud.apihub_v1.types import apihub_service, common_fields


class ListApisPager:
    """A pager for iterating through ``list_apis`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListApisResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``apis`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApis`` requests and continue to iterate
    through the ``apis`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListApisResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.ListApisResponse],
        request: apihub_service.ListApisRequest,
        response: apihub_service.ListApisResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListApisRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListApisResponse):
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
        self._request = apihub_service.ListApisRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.ListApisResponse]:
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

    def __iter__(self) -> Iterator[common_fields.Api]:
        for page in self.pages:
            yield from page.apis

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApisAsyncPager:
    """A pager for iterating through ``list_apis`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListApisResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``apis`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApis`` requests and continue to iterate
    through the ``apis`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListApisResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.ListApisResponse]],
        request: apihub_service.ListApisRequest,
        response: apihub_service.ListApisResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListApisRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListApisResponse):
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
        self._request = apihub_service.ListApisRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.ListApisResponse]:
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

    def __aiter__(self) -> AsyncIterator[common_fields.Api]:
        async def async_generator():
            async for page in self.pages:
                for response in page.apis:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVersionsPager:
    """A pager for iterating through ``list_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVersions`` requests and continue to iterate
    through the ``versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.ListVersionsResponse],
        request: apihub_service.ListVersionsRequest,
        response: apihub_service.ListVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListVersionsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListVersionsResponse):
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
        self._request = apihub_service.ListVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.ListVersionsResponse]:
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

    def __iter__(self) -> Iterator[common_fields.Version]:
        for page in self.pages:
            yield from page.versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVersionsAsyncPager:
    """A pager for iterating through ``list_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVersions`` requests and continue to iterate
    through the ``versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.ListVersionsResponse]],
        request: apihub_service.ListVersionsRequest,
        response: apihub_service.ListVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListVersionsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListVersionsResponse):
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
        self._request = apihub_service.ListVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.ListVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[common_fields.Version]:
        async def async_generator():
            async for page in self.pages:
                for response in page.versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSpecsPager:
    """A pager for iterating through ``list_specs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListSpecsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``specs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSpecs`` requests and continue to iterate
    through the ``specs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListSpecsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.ListSpecsResponse],
        request: apihub_service.ListSpecsRequest,
        response: apihub_service.ListSpecsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListSpecsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListSpecsResponse):
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
        self._request = apihub_service.ListSpecsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.ListSpecsResponse]:
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

    def __iter__(self) -> Iterator[common_fields.Spec]:
        for page in self.pages:
            yield from page.specs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSpecsAsyncPager:
    """A pager for iterating through ``list_specs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListSpecsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``specs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSpecs`` requests and continue to iterate
    through the ``specs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListSpecsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.ListSpecsResponse]],
        request: apihub_service.ListSpecsRequest,
        response: apihub_service.ListSpecsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListSpecsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListSpecsResponse):
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
        self._request = apihub_service.ListSpecsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.ListSpecsResponse]:
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

    def __aiter__(self) -> AsyncIterator[common_fields.Spec]:
        async def async_generator():
            async for page in self.pages:
                for response in page.specs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApiOperationsPager:
    """A pager for iterating through ``list_api_operations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListApiOperationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``api_operations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApiOperations`` requests and continue to iterate
    through the ``api_operations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListApiOperationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.ListApiOperationsResponse],
        request: apihub_service.ListApiOperationsRequest,
        response: apihub_service.ListApiOperationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListApiOperationsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListApiOperationsResponse):
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
        self._request = apihub_service.ListApiOperationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.ListApiOperationsResponse]:
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

    def __iter__(self) -> Iterator[common_fields.ApiOperation]:
        for page in self.pages:
            yield from page.api_operations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApiOperationsAsyncPager:
    """A pager for iterating through ``list_api_operations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListApiOperationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``api_operations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApiOperations`` requests and continue to iterate
    through the ``api_operations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListApiOperationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.ListApiOperationsResponse]],
        request: apihub_service.ListApiOperationsRequest,
        response: apihub_service.ListApiOperationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListApiOperationsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListApiOperationsResponse):
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
        self._request = apihub_service.ListApiOperationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.ListApiOperationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[common_fields.ApiOperation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.api_operations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentsPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.ListDeploymentsResponse],
        request: apihub_service.ListDeploymentsRequest,
        response: apihub_service.ListDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListDeploymentsResponse):
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
        self._request = apihub_service.ListDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.ListDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[common_fields.Deployment]:
        for page in self.pages:
            yield from page.deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentsAsyncPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.ListDeploymentsResponse]],
        request: apihub_service.ListDeploymentsRequest,
        response: apihub_service.ListDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListDeploymentsResponse):
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
        self._request = apihub_service.ListDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.ListDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[common_fields.Deployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAttributesPager:
    """A pager for iterating through ``list_attributes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListAttributesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``attributes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAttributes`` requests and continue to iterate
    through the ``attributes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListAttributesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.ListAttributesResponse],
        request: apihub_service.ListAttributesRequest,
        response: apihub_service.ListAttributesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListAttributesRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListAttributesResponse):
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
        self._request = apihub_service.ListAttributesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.ListAttributesResponse]:
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

    def __iter__(self) -> Iterator[common_fields.Attribute]:
        for page in self.pages:
            yield from page.attributes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAttributesAsyncPager:
    """A pager for iterating through ``list_attributes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListAttributesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``attributes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAttributes`` requests and continue to iterate
    through the ``attributes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListAttributesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.ListAttributesResponse]],
        request: apihub_service.ListAttributesRequest,
        response: apihub_service.ListAttributesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListAttributesRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListAttributesResponse):
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
        self._request = apihub_service.ListAttributesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.ListAttributesResponse]:
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

    def __aiter__(self) -> AsyncIterator[common_fields.Attribute]:
        async def async_generator():
            async for page in self.pages:
                for response in page.attributes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchResourcesPager:
    """A pager for iterating through ``search_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.SearchResourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchResources`` requests and continue to iterate
    through the ``search_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.SearchResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.SearchResourcesResponse],
        request: apihub_service.SearchResourcesRequest,
        response: apihub_service.SearchResourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.SearchResourcesRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.SearchResourcesResponse):
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
        self._request = apihub_service.SearchResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.SearchResourcesResponse]:
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

    def __iter__(self) -> Iterator[apihub_service.SearchResult]:
        for page in self.pages:
            yield from page.search_results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchResourcesAsyncPager:
    """A pager for iterating through ``search_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.SearchResourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchResources`` requests and continue to iterate
    through the ``search_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.SearchResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.SearchResourcesResponse]],
        request: apihub_service.SearchResourcesRequest,
        response: apihub_service.SearchResourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.SearchResourcesRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.SearchResourcesResponse):
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
        self._request = apihub_service.SearchResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.SearchResourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[apihub_service.SearchResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.search_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExternalApisPager:
    """A pager for iterating through ``list_external_apis`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListExternalApisResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``external_apis`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExternalApis`` requests and continue to iterate
    through the ``external_apis`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListExternalApisResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., apihub_service.ListExternalApisResponse],
        request: apihub_service.ListExternalApisRequest,
        response: apihub_service.ListExternalApisResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListExternalApisRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListExternalApisResponse):
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
        self._request = apihub_service.ListExternalApisRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[apihub_service.ListExternalApisResponse]:
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

    def __iter__(self) -> Iterator[common_fields.ExternalApi]:
        for page in self.pages:
            yield from page.external_apis

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExternalApisAsyncPager:
    """A pager for iterating through ``list_external_apis`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.apihub_v1.types.ListExternalApisResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``external_apis`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExternalApis`` requests and continue to iterate
    through the ``external_apis`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.apihub_v1.types.ListExternalApisResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[apihub_service.ListExternalApisResponse]],
        request: apihub_service.ListExternalApisRequest,
        response: apihub_service.ListExternalApisResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.apihub_v1.types.ListExternalApisRequest):
                The initial request object.
            response (google.cloud.apihub_v1.types.ListExternalApisResponse):
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
        self._request = apihub_service.ListExternalApisRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[apihub_service.ListExternalApisResponse]:
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

    def __aiter__(self) -> AsyncIterator[common_fields.ExternalApi]:
        async def async_generator():
            async for page in self.pages:
                for response in page.external_apis:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
