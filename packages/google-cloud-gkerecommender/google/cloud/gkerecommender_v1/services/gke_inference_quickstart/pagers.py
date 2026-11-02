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

from google.cloud.gkerecommender_v1.types import gkerecommender


class FetchModelsPager:
    """A pager for iterating through ``fetch_models`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchModelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``models`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchModels`` requests and continue to iterate
    through the ``models`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchModelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkerecommender.FetchModelsResponse],
        request: gkerecommender.FetchModelsRequest,
        response: gkerecommender.FetchModelsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchModelsRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchModelsResponse):
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
        self._request = gkerecommender.FetchModelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkerecommender.FetchModelsResponse]:
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

    def __iter__(self) -> Iterator[str]:
        for page in self.pages:
            yield from page.models

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchModelsAsyncPager:
    """A pager for iterating through ``fetch_models`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchModelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``models`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchModels`` requests and continue to iterate
    through the ``models`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchModelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkerecommender.FetchModelsResponse]],
        request: gkerecommender.FetchModelsRequest,
        response: gkerecommender.FetchModelsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchModelsRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchModelsResponse):
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
        self._request = gkerecommender.FetchModelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkerecommender.FetchModelsResponse]:
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

    def __aiter__(self) -> AsyncIterator[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.models:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchModelServersPager:
    """A pager for iterating through ``fetch_model_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchModelServersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``model_servers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchModelServers`` requests and continue to iterate
    through the ``model_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchModelServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkerecommender.FetchModelServersResponse],
        request: gkerecommender.FetchModelServersRequest,
        response: gkerecommender.FetchModelServersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchModelServersRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchModelServersResponse):
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
        self._request = gkerecommender.FetchModelServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkerecommender.FetchModelServersResponse]:
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

    def __iter__(self) -> Iterator[str]:
        for page in self.pages:
            yield from page.model_servers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchModelServersAsyncPager:
    """A pager for iterating through ``fetch_model_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchModelServersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``model_servers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchModelServers`` requests and continue to iterate
    through the ``model_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchModelServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkerecommender.FetchModelServersResponse]],
        request: gkerecommender.FetchModelServersRequest,
        response: gkerecommender.FetchModelServersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchModelServersRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchModelServersResponse):
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
        self._request = gkerecommender.FetchModelServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkerecommender.FetchModelServersResponse]:
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

    def __aiter__(self) -> AsyncIterator[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.model_servers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchModelServerVersionsPager:
    """A pager for iterating through ``fetch_model_server_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchModelServerVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``model_server_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchModelServerVersions`` requests and continue to iterate
    through the ``model_server_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchModelServerVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkerecommender.FetchModelServerVersionsResponse],
        request: gkerecommender.FetchModelServerVersionsRequest,
        response: gkerecommender.FetchModelServerVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchModelServerVersionsRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchModelServerVersionsResponse):
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
        self._request = gkerecommender.FetchModelServerVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkerecommender.FetchModelServerVersionsResponse]:
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

    def __iter__(self) -> Iterator[str]:
        for page in self.pages:
            yield from page.model_server_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchModelServerVersionsAsyncPager:
    """A pager for iterating through ``fetch_model_server_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchModelServerVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``model_server_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchModelServerVersions`` requests and continue to iterate
    through the ``model_server_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchModelServerVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[gkerecommender.FetchModelServerVersionsResponse]
        ],
        request: gkerecommender.FetchModelServerVersionsRequest,
        response: gkerecommender.FetchModelServerVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchModelServerVersionsRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchModelServerVersionsResponse):
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
        self._request = gkerecommender.FetchModelServerVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[gkerecommender.FetchModelServerVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.model_server_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchProfilesPager:
    """A pager for iterating through ``fetch_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``profile`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchProfiles`` requests and continue to iterate
    through the ``profile`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., gkerecommender.FetchProfilesResponse],
        request: gkerecommender.FetchProfilesRequest,
        response: gkerecommender.FetchProfilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchProfilesRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchProfilesResponse):
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
        self._request = gkerecommender.FetchProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[gkerecommender.FetchProfilesResponse]:
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

    def __iter__(self) -> Iterator[gkerecommender.Profile]:
        for page in self.pages:
            yield from page.profile

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchProfilesAsyncPager:
    """A pager for iterating through ``fetch_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gkerecommender_v1.types.FetchProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``profile`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchProfiles`` requests and continue to iterate
    through the ``profile`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gkerecommender_v1.types.FetchProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[gkerecommender.FetchProfilesResponse]],
        request: gkerecommender.FetchProfilesRequest,
        response: gkerecommender.FetchProfilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gkerecommender_v1.types.FetchProfilesRequest):
                The initial request object.
            response (google.cloud.gkerecommender_v1.types.FetchProfilesResponse):
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
        self._request = gkerecommender.FetchProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[gkerecommender.FetchProfilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[gkerecommender.Profile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.profile:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
