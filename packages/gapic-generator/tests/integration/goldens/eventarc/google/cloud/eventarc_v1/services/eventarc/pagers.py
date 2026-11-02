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
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import retry_async as retries_async
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator, Union
try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, object, None]  # type: ignore

from google.cloud.eventarc_v1.types import channel
from google.cloud.eventarc_v1.types import channel_connection
from google.cloud.eventarc_v1.types import discovery
from google.cloud.eventarc_v1.types import enrollment
from google.cloud.eventarc_v1.types import eventarc
from google.cloud.eventarc_v1.types import google_api_source
from google.cloud.eventarc_v1.types import message_bus
from google.cloud.eventarc_v1.types import pipeline
from google.cloud.eventarc_v1.types import trigger


class ListTriggersPager:
    """A pager for iterating through ``list_triggers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListTriggersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``triggers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTriggers`` requests and continue to iterate
    through the ``triggers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListTriggersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListTriggersResponse],
            request: eventarc.ListTriggersRequest,
            response: eventarc.ListTriggersResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListTriggersRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListTriggersResponse):
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
        self._request = eventarc.ListTriggersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListTriggersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[trigger.Trigger]:
        for page in self.pages:
            yield from page.triggers

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListTriggersAsyncPager:
    """A pager for iterating through ``list_triggers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListTriggersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``triggers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTriggers`` requests and continue to iterate
    through the ``triggers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListTriggersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListTriggersResponse]],
            request: eventarc.ListTriggersRequest,
            response: eventarc.ListTriggersResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListTriggersRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListTriggersResponse):
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
        self._request = eventarc.ListTriggersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListTriggersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[trigger.Trigger]:
        async def async_generator():
            async for page in self.pages:
                for response in page.triggers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListChannelsPager:
    """A pager for iterating through ``list_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListChannelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``channels`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListChannels`` requests and continue to iterate
    through the ``channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListChannelsResponse],
            request: eventarc.ListChannelsRequest,
            response: eventarc.ListChannelsResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListChannelsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListChannelsResponse):
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
        self._request = eventarc.ListChannelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListChannelsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[channel.Channel]:
        for page in self.pages:
            yield from page.channels

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListChannelsAsyncPager:
    """A pager for iterating through ``list_channels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListChannelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``channels`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListChannels`` requests and continue to iterate
    through the ``channels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListChannelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListChannelsResponse]],
            request: eventarc.ListChannelsRequest,
            response: eventarc.ListChannelsResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListChannelsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListChannelsResponse):
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
        self._request = eventarc.ListChannelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListChannelsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[channel.Channel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.channels:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListProvidersPager:
    """A pager for iterating through ``list_providers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListProvidersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``providers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProviders`` requests and continue to iterate
    through the ``providers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListProvidersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListProvidersResponse],
            request: eventarc.ListProvidersRequest,
            response: eventarc.ListProvidersResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListProvidersRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListProvidersResponse):
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
        self._request = eventarc.ListProvidersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListProvidersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[discovery.Provider]:
        for page in self.pages:
            yield from page.providers

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListProvidersAsyncPager:
    """A pager for iterating through ``list_providers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListProvidersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``providers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProviders`` requests and continue to iterate
    through the ``providers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListProvidersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListProvidersResponse]],
            request: eventarc.ListProvidersRequest,
            response: eventarc.ListProvidersResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListProvidersRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListProvidersResponse):
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
        self._request = eventarc.ListProvidersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListProvidersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[discovery.Provider]:
        async def async_generator():
            async for page in self.pages:
                for response in page.providers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListChannelConnectionsPager:
    """A pager for iterating through ``list_channel_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListChannelConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``channel_connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListChannelConnections`` requests and continue to iterate
    through the ``channel_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListChannelConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListChannelConnectionsResponse],
            request: eventarc.ListChannelConnectionsRequest,
            response: eventarc.ListChannelConnectionsResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListChannelConnectionsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListChannelConnectionsResponse):
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
        self._request = eventarc.ListChannelConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListChannelConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[channel_connection.ChannelConnection]:
        for page in self.pages:
            yield from page.channel_connections

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListChannelConnectionsAsyncPager:
    """A pager for iterating through ``list_channel_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListChannelConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``channel_connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListChannelConnections`` requests and continue to iterate
    through the ``channel_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListChannelConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListChannelConnectionsResponse]],
            request: eventarc.ListChannelConnectionsRequest,
            response: eventarc.ListChannelConnectionsResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListChannelConnectionsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListChannelConnectionsResponse):
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
        self._request = eventarc.ListChannelConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListChannelConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[channel_connection.ChannelConnection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.channel_connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListMessageBusesPager:
    """A pager for iterating through ``list_message_buses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListMessageBusesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``message_buses`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMessageBuses`` requests and continue to iterate
    through the ``message_buses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListMessageBusesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListMessageBusesResponse],
            request: eventarc.ListMessageBusesRequest,
            response: eventarc.ListMessageBusesResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListMessageBusesRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListMessageBusesResponse):
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
        self._request = eventarc.ListMessageBusesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListMessageBusesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[message_bus.MessageBus]:
        for page in self.pages:
            yield from page.message_buses

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListMessageBusesAsyncPager:
    """A pager for iterating through ``list_message_buses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListMessageBusesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``message_buses`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMessageBuses`` requests and continue to iterate
    through the ``message_buses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListMessageBusesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListMessageBusesResponse]],
            request: eventarc.ListMessageBusesRequest,
            response: eventarc.ListMessageBusesResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListMessageBusesRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListMessageBusesResponse):
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
        self._request = eventarc.ListMessageBusesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListMessageBusesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[message_bus.MessageBus]:
        async def async_generator():
            async for page in self.pages:
                for response in page.message_buses:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListMessageBusEnrollmentsPager:
    """A pager for iterating through ``list_message_bus_enrollments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``enrollments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMessageBusEnrollments`` requests and continue to iterate
    through the ``enrollments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListMessageBusEnrollmentsResponse],
            request: eventarc.ListMessageBusEnrollmentsRequest,
            response: eventarc.ListMessageBusEnrollmentsResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsResponse):
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
        self._request = eventarc.ListMessageBusEnrollmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListMessageBusEnrollmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[str]:
        for page in self.pages:
            yield from page.enrollments

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListMessageBusEnrollmentsAsyncPager:
    """A pager for iterating through ``list_message_bus_enrollments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``enrollments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMessageBusEnrollments`` requests and continue to iterate
    through the ``enrollments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListMessageBusEnrollmentsResponse]],
            request: eventarc.ListMessageBusEnrollmentsRequest,
            response: eventarc.ListMessageBusEnrollmentsResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListMessageBusEnrollmentsResponse):
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
        self._request = eventarc.ListMessageBusEnrollmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListMessageBusEnrollmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[str]:
        async def async_generator():
            async for page in self.pages:
                for response in page.enrollments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEnrollmentsPager:
    """A pager for iterating through ``list_enrollments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListEnrollmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``enrollments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEnrollments`` requests and continue to iterate
    through the ``enrollments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListEnrollmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListEnrollmentsResponse],
            request: eventarc.ListEnrollmentsRequest,
            response: eventarc.ListEnrollmentsResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListEnrollmentsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListEnrollmentsResponse):
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
        self._request = eventarc.ListEnrollmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListEnrollmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[enrollment.Enrollment]:
        for page in self.pages:
            yield from page.enrollments

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEnrollmentsAsyncPager:
    """A pager for iterating through ``list_enrollments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListEnrollmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``enrollments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEnrollments`` requests and continue to iterate
    through the ``enrollments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListEnrollmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListEnrollmentsResponse]],
            request: eventarc.ListEnrollmentsRequest,
            response: eventarc.ListEnrollmentsResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListEnrollmentsRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListEnrollmentsResponse):
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
        self._request = eventarc.ListEnrollmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListEnrollmentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[enrollment.Enrollment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.enrollments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListPipelinesPager:
    """A pager for iterating through ``list_pipelines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListPipelinesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``pipelines`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPipelines`` requests and continue to iterate
    through the ``pipelines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListPipelinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListPipelinesResponse],
            request: eventarc.ListPipelinesRequest,
            response: eventarc.ListPipelinesResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListPipelinesRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListPipelinesResponse):
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
        self._request = eventarc.ListPipelinesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListPipelinesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[pipeline.Pipeline]:
        for page in self.pages:
            yield from page.pipelines

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListPipelinesAsyncPager:
    """A pager for iterating through ``list_pipelines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListPipelinesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``pipelines`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPipelines`` requests and continue to iterate
    through the ``pipelines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListPipelinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListPipelinesResponse]],
            request: eventarc.ListPipelinesRequest,
            response: eventarc.ListPipelinesResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListPipelinesRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListPipelinesResponse):
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
        self._request = eventarc.ListPipelinesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListPipelinesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[pipeline.Pipeline]:
        async def async_generator():
            async for page in self.pages:
                for response in page.pipelines:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListGoogleApiSourcesPager:
    """A pager for iterating through ``list_google_api_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListGoogleApiSourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``google_api_sources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoogleApiSources`` requests and continue to iterate
    through the ``google_api_sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListGoogleApiSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., eventarc.ListGoogleApiSourcesResponse],
            request: eventarc.ListGoogleApiSourcesRequest,
            response: eventarc.ListGoogleApiSourcesResponse,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListGoogleApiSourcesRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListGoogleApiSourcesResponse):
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
        self._request = eventarc.ListGoogleApiSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[eventarc.ListGoogleApiSourcesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[google_api_source.GoogleApiSource]:
        for page in self.pages:
            yield from page.google_api_sources

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListGoogleApiSourcesAsyncPager:
    """A pager for iterating through ``list_google_api_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.eventarc_v1.types.ListGoogleApiSourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``google_api_sources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoogleApiSources`` requests and continue to iterate
    through the ``google_api_sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.eventarc_v1.types.ListGoogleApiSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[eventarc.ListGoogleApiSourcesResponse]],
            request: eventarc.ListGoogleApiSourcesRequest,
            response: eventarc.ListGoogleApiSourcesResponse,
            *,
            retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
            timeout: Union[float, object] = gapic_v1.method.DEFAULT,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.eventarc_v1.types.ListGoogleApiSourcesRequest):
                The initial request object.
            response (google.cloud.eventarc_v1.types.ListGoogleApiSourcesResponse):
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
        self._request = eventarc.ListGoogleApiSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[eventarc.ListGoogleApiSourcesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, retry=self._retry, timeout=self._timeout, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[google_api_source.GoogleApiSource]:
        async def async_generator():
            async for page in self.pages:
                for response in page.google_api_sources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
