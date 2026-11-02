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

from google.cloud.datastream_v1.types import datastream, datastream_resources


class ListConnectionProfilesPager:
    """A pager for iterating through ``list_connection_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListConnectionProfilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connection_profiles`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnectionProfiles`` requests and continue to iterate
    through the ``connection_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListConnectionProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListConnectionProfilesResponse],
        request: datastream.ListConnectionProfilesRequest,
        response: datastream.ListConnectionProfilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListConnectionProfilesRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListConnectionProfilesResponse):
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
        self._request = datastream.ListConnectionProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[datastream.ListConnectionProfilesResponse]:
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

    def __iter__(self) -> Iterator[datastream_resources.ConnectionProfile]:
        for page in self.pages:
            yield from page.connection_profiles

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionProfilesAsyncPager:
    """A pager for iterating through ``list_connection_profiles`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListConnectionProfilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connection_profiles`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnectionProfiles`` requests and continue to iterate
    through the ``connection_profiles`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListConnectionProfilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListConnectionProfilesResponse]],
        request: datastream.ListConnectionProfilesRequest,
        response: datastream.ListConnectionProfilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListConnectionProfilesRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListConnectionProfilesResponse):
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
        self._request = datastream.ListConnectionProfilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[datastream.ListConnectionProfilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[datastream_resources.ConnectionProfile]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connection_profiles:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStreamsPager:
    """A pager for iterating through ``list_streams`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStreams`` requests and continue to iterate
    through the ``streams`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListStreamsResponse],
        request: datastream.ListStreamsRequest,
        response: datastream.ListStreamsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListStreamsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListStreamsResponse):
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
        self._request = datastream.ListStreamsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[datastream.ListStreamsResponse]:
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

    def __iter__(self) -> Iterator[datastream_resources.Stream]:
        for page in self.pages:
            yield from page.streams

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStreamsAsyncPager:
    """A pager for iterating through ``list_streams`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStreams`` requests and continue to iterate
    through the ``streams`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListStreamsResponse]],
        request: datastream.ListStreamsRequest,
        response: datastream.ListStreamsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListStreamsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListStreamsResponse):
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
        self._request = datastream.ListStreamsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[datastream.ListStreamsResponse]:
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

    def __aiter__(self) -> AsyncIterator[datastream_resources.Stream]:
        async def async_generator():
            async for page in self.pages:
                for response in page.streams:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStreamObjectsPager:
    """A pager for iterating through ``list_stream_objects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListStreamObjectsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``stream_objects`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStreamObjects`` requests and continue to iterate
    through the ``stream_objects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListStreamObjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListStreamObjectsResponse],
        request: datastream.ListStreamObjectsRequest,
        response: datastream.ListStreamObjectsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListStreamObjectsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListStreamObjectsResponse):
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
        self._request = datastream.ListStreamObjectsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[datastream.ListStreamObjectsResponse]:
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

    def __iter__(self) -> Iterator[datastream_resources.StreamObject]:
        for page in self.pages:
            yield from page.stream_objects

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListStreamObjectsAsyncPager:
    """A pager for iterating through ``list_stream_objects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListStreamObjectsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``stream_objects`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStreamObjects`` requests and continue to iterate
    through the ``stream_objects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListStreamObjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListStreamObjectsResponse]],
        request: datastream.ListStreamObjectsRequest,
        response: datastream.ListStreamObjectsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListStreamObjectsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListStreamObjectsResponse):
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
        self._request = datastream.ListStreamObjectsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[datastream.ListStreamObjectsResponse]:
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

    def __aiter__(self) -> AsyncIterator[datastream_resources.StreamObject]:
        async def async_generator():
            async for page in self.pages:
                for response in page.stream_objects:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStaticIpsPager:
    """A pager for iterating through ``fetch_static_ips`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.FetchStaticIpsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``static_ips`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchStaticIps`` requests and continue to iterate
    through the ``static_ips`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.FetchStaticIpsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.FetchStaticIpsResponse],
        request: datastream.FetchStaticIpsRequest,
        response: datastream.FetchStaticIpsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.FetchStaticIpsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.FetchStaticIpsResponse):
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
        self._request = datastream.FetchStaticIpsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[datastream.FetchStaticIpsResponse]:
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
            yield from page.static_ips

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchStaticIpsAsyncPager:
    """A pager for iterating through ``fetch_static_ips`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.FetchStaticIpsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``static_ips`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchStaticIps`` requests and continue to iterate
    through the ``static_ips`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.FetchStaticIpsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.FetchStaticIpsResponse]],
        request: datastream.FetchStaticIpsRequest,
        response: datastream.FetchStaticIpsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.FetchStaticIpsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.FetchStaticIpsResponse):
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
        self._request = datastream.FetchStaticIpsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[datastream.FetchStaticIpsResponse]:
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
                for response in page.static_ips:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateConnectionsPager:
    """A pager for iterating through ``list_private_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListPrivateConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``private_connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPrivateConnections`` requests and continue to iterate
    through the ``private_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListPrivateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListPrivateConnectionsResponse],
        request: datastream.ListPrivateConnectionsRequest,
        response: datastream.ListPrivateConnectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListPrivateConnectionsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListPrivateConnectionsResponse):
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
        self._request = datastream.ListPrivateConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[datastream.ListPrivateConnectionsResponse]:
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

    def __iter__(self) -> Iterator[datastream_resources.PrivateConnection]:
        for page in self.pages:
            yield from page.private_connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPrivateConnectionsAsyncPager:
    """A pager for iterating through ``list_private_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListPrivateConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``private_connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPrivateConnections`` requests and continue to iterate
    through the ``private_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListPrivateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListPrivateConnectionsResponse]],
        request: datastream.ListPrivateConnectionsRequest,
        response: datastream.ListPrivateConnectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListPrivateConnectionsRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListPrivateConnectionsResponse):
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
        self._request = datastream.ListPrivateConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[datastream.ListPrivateConnectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[datastream_resources.PrivateConnection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.private_connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutesPager:
    """A pager for iterating through ``list_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListRoutesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``routes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRoutes`` requests and continue to iterate
    through the ``routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., datastream.ListRoutesResponse],
        request: datastream.ListRoutesRequest,
        response: datastream.ListRoutesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListRoutesRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListRoutesResponse):
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
        self._request = datastream.ListRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[datastream.ListRoutesResponse]:
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

    def __iter__(self) -> Iterator[datastream_resources.Route]:
        for page in self.pages:
            yield from page.routes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRoutesAsyncPager:
    """A pager for iterating through ``list_routes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.datastream_v1.types.ListRoutesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``routes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRoutes`` requests and continue to iterate
    through the ``routes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.datastream_v1.types.ListRoutesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[datastream.ListRoutesResponse]],
        request: datastream.ListRoutesRequest,
        response: datastream.ListRoutesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.datastream_v1.types.ListRoutesRequest):
                The initial request object.
            response (google.cloud.datastream_v1.types.ListRoutesResponse):
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
        self._request = datastream.ListRoutesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[datastream.ListRoutesResponse]:
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

    def __aiter__(self) -> AsyncIterator[datastream_resources.Route]:
        async def async_generator():
            async for page in self.pages:
                for response in page.routes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
