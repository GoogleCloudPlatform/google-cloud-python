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

from google.cloud.agentregistry_v1.types import (
    agent,
    agentregistry_service,
    binding,
    endpoint,
    mcp_server,
    service,
)


class ListAgentsPager:
    """A pager for iterating through ``list_agents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListAgentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``agents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAgents`` requests and continue to iterate
    through the ``agents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListAgentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.ListAgentsResponse],
        request: agentregistry_service.ListAgentsRequest,
        response: agentregistry_service.ListAgentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListAgentsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListAgentsResponse):
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
        self._request = agentregistry_service.ListAgentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.ListAgentsResponse]:
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

    def __iter__(self) -> Iterator[agent.Agent]:
        for page in self.pages:
            yield from page.agents

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAgentsAsyncPager:
    """A pager for iterating through ``list_agents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListAgentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``agents`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAgents`` requests and continue to iterate
    through the ``agents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListAgentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agentregistry_service.ListAgentsResponse]],
        request: agentregistry_service.ListAgentsRequest,
        response: agentregistry_service.ListAgentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListAgentsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListAgentsResponse):
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
        self._request = agentregistry_service.ListAgentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agentregistry_service.ListAgentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[agent.Agent]:
        async def async_generator():
            async for page in self.pages:
                for response in page.agents:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAgentsPager:
    """A pager for iterating through ``search_agents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.SearchAgentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``agents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAgents`` requests and continue to iterate
    through the ``agents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.SearchAgentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.SearchAgentsResponse],
        request: agentregistry_service.SearchAgentsRequest,
        response: agentregistry_service.SearchAgentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.SearchAgentsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.SearchAgentsResponse):
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
        self._request = agentregistry_service.SearchAgentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.SearchAgentsResponse]:
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

    def __iter__(self) -> Iterator[agent.Agent]:
        for page in self.pages:
            yield from page.agents

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAgentsAsyncPager:
    """A pager for iterating through ``search_agents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.SearchAgentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``agents`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAgents`` requests and continue to iterate
    through the ``agents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.SearchAgentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agentregistry_service.SearchAgentsResponse]],
        request: agentregistry_service.SearchAgentsRequest,
        response: agentregistry_service.SearchAgentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.SearchAgentsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.SearchAgentsResponse):
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
        self._request = agentregistry_service.SearchAgentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agentregistry_service.SearchAgentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[agent.Agent]:
        async def async_generator():
            async for page in self.pages:
                for response in page.agents:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEndpointsPager:
    """A pager for iterating through ``list_endpoints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListEndpointsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``endpoints`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEndpoints`` requests and continue to iterate
    through the ``endpoints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListEndpointsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.ListEndpointsResponse],
        request: agentregistry_service.ListEndpointsRequest,
        response: agentregistry_service.ListEndpointsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListEndpointsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListEndpointsResponse):
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
        self._request = agentregistry_service.ListEndpointsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.ListEndpointsResponse]:
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

    def __iter__(self) -> Iterator[endpoint.Endpoint]:
        for page in self.pages:
            yield from page.endpoints

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEndpointsAsyncPager:
    """A pager for iterating through ``list_endpoints`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListEndpointsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``endpoints`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEndpoints`` requests and continue to iterate
    through the ``endpoints`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListEndpointsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agentregistry_service.ListEndpointsResponse]],
        request: agentregistry_service.ListEndpointsRequest,
        response: agentregistry_service.ListEndpointsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListEndpointsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListEndpointsResponse):
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
        self._request = agentregistry_service.ListEndpointsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agentregistry_service.ListEndpointsResponse]:
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

    def __aiter__(self) -> AsyncIterator[endpoint.Endpoint]:
        async def async_generator():
            async for page in self.pages:
                for response in page.endpoints:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMcpServersPager:
    """A pager for iterating through ``list_mcp_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListMcpServersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``mcp_servers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMcpServers`` requests and continue to iterate
    through the ``mcp_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListMcpServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.ListMcpServersResponse],
        request: agentregistry_service.ListMcpServersRequest,
        response: agentregistry_service.ListMcpServersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListMcpServersRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListMcpServersResponse):
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
        self._request = agentregistry_service.ListMcpServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.ListMcpServersResponse]:
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

    def __iter__(self) -> Iterator[mcp_server.McpServer]:
        for page in self.pages:
            yield from page.mcp_servers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMcpServersAsyncPager:
    """A pager for iterating through ``list_mcp_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListMcpServersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``mcp_servers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMcpServers`` requests and continue to iterate
    through the ``mcp_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListMcpServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agentregistry_service.ListMcpServersResponse]],
        request: agentregistry_service.ListMcpServersRequest,
        response: agentregistry_service.ListMcpServersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListMcpServersRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListMcpServersResponse):
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
        self._request = agentregistry_service.ListMcpServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[agentregistry_service.ListMcpServersResponse]:
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

    def __aiter__(self) -> AsyncIterator[mcp_server.McpServer]:
        async def async_generator():
            async for page in self.pages:
                for response in page.mcp_servers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchMcpServersPager:
    """A pager for iterating through ``search_mcp_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.SearchMcpServersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``mcp_servers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchMcpServers`` requests and continue to iterate
    through the ``mcp_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.SearchMcpServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.SearchMcpServersResponse],
        request: agentregistry_service.SearchMcpServersRequest,
        response: agentregistry_service.SearchMcpServersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.SearchMcpServersRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.SearchMcpServersResponse):
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
        self._request = agentregistry_service.SearchMcpServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.SearchMcpServersResponse]:
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

    def __iter__(self) -> Iterator[mcp_server.McpServer]:
        for page in self.pages:
            yield from page.mcp_servers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchMcpServersAsyncPager:
    """A pager for iterating through ``search_mcp_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.SearchMcpServersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``mcp_servers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchMcpServers`` requests and continue to iterate
    through the ``mcp_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.SearchMcpServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[agentregistry_service.SearchMcpServersResponse]
        ],
        request: agentregistry_service.SearchMcpServersRequest,
        response: agentregistry_service.SearchMcpServersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.SearchMcpServersRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.SearchMcpServersResponse):
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
        self._request = agentregistry_service.SearchMcpServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[agentregistry_service.SearchMcpServersResponse]:
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

    def __aiter__(self) -> AsyncIterator[mcp_server.McpServer]:
        async def async_generator():
            async for page in self.pages:
                for response in page.mcp_servers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServicesPager:
    """A pager for iterating through ``list_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListServicesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.ListServicesResponse],
        request: agentregistry_service.ListServicesRequest,
        response: agentregistry_service.ListServicesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListServicesResponse):
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
        self._request = agentregistry_service.ListServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.ListServicesResponse]:
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

    def __iter__(self) -> Iterator[service.Service]:
        for page in self.pages:
            yield from page.services

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListServicesAsyncPager:
    """A pager for iterating through ``list_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListServicesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``services`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListServices`` requests and continue to iterate
    through the ``services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agentregistry_service.ListServicesResponse]],
        request: agentregistry_service.ListServicesRequest,
        response: agentregistry_service.ListServicesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListServicesRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListServicesResponse):
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
        self._request = agentregistry_service.ListServicesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agentregistry_service.ListServicesResponse]:
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

    def __aiter__(self) -> AsyncIterator[service.Service]:
        async def async_generator():
            async for page in self.pages:
                for response in page.services:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBindingsPager:
    """A pager for iterating through ``list_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBindings`` requests and continue to iterate
    through the ``bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.ListBindingsResponse],
        request: agentregistry_service.ListBindingsRequest,
        response: agentregistry_service.ListBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListBindingsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListBindingsResponse):
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
        self._request = agentregistry_service.ListBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.ListBindingsResponse]:
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

    def __iter__(self) -> Iterator[binding.Binding]:
        for page in self.pages:
            yield from page.bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBindingsAsyncPager:
    """A pager for iterating through ``list_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.ListBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBindings`` requests and continue to iterate
    through the ``bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.ListBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agentregistry_service.ListBindingsResponse]],
        request: agentregistry_service.ListBindingsRequest,
        response: agentregistry_service.ListBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.ListBindingsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.ListBindingsResponse):
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
        self._request = agentregistry_service.ListBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agentregistry_service.ListBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[binding.Binding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchAvailableBindingsPager:
    """A pager for iterating through ``fetch_available_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.FetchAvailableBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchAvailableBindings`` requests and continue to iterate
    through the ``bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.FetchAvailableBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agentregistry_service.FetchAvailableBindingsResponse],
        request: agentregistry_service.FetchAvailableBindingsRequest,
        response: agentregistry_service.FetchAvailableBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.FetchAvailableBindingsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.FetchAvailableBindingsResponse):
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
        self._request = agentregistry_service.FetchAvailableBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agentregistry_service.FetchAvailableBindingsResponse]:
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

    def __iter__(self) -> Iterator[binding.Binding]:
        for page in self.pages:
            yield from page.bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchAvailableBindingsAsyncPager:
    """A pager for iterating through ``fetch_available_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.agentregistry_v1.types.FetchAvailableBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchAvailableBindings`` requests and continue to iterate
    through the ``bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.agentregistry_v1.types.FetchAvailableBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[agentregistry_service.FetchAvailableBindingsResponse]
        ],
        request: agentregistry_service.FetchAvailableBindingsRequest,
        response: agentregistry_service.FetchAvailableBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.agentregistry_v1.types.FetchAvailableBindingsRequest):
                The initial request object.
            response (google.cloud.agentregistry_v1.types.FetchAvailableBindingsResponse):
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
        self._request = agentregistry_service.FetchAvailableBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[agentregistry_service.FetchAvailableBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[binding.Binding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
