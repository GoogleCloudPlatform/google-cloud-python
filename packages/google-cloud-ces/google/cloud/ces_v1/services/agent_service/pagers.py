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

from google.cloud.ces_v1.types import (
    agent,
    agent_service,
    app,
    app_version,
    changelog,
    conversation,
    deployment,
    example,
    guardrail,
    tool,
    toolset,
)


class ListAppsPager:
    """A pager for iterating through ``list_apps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListAppsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``apps`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApps`` requests and continue to iterate
    through the ``apps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListAppsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListAppsResponse],
        request: agent_service.ListAppsRequest,
        response: agent_service.ListAppsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListAppsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListAppsResponse):
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
        self._request = agent_service.ListAppsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListAppsResponse]:
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

    def __iter__(self) -> Iterator[app.App]:
        for page in self.pages:
            yield from page.apps

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAppsAsyncPager:
    """A pager for iterating through ``list_apps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListAppsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``apps`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApps`` requests and continue to iterate
    through the ``apps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListAppsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListAppsResponse]],
        request: agent_service.ListAppsRequest,
        response: agent_service.ListAppsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListAppsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListAppsResponse):
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
        self._request = agent_service.ListAppsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListAppsResponse]:
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

    def __aiter__(self) -> AsyncIterator[app.App]:
        async def async_generator():
            async for page in self.pages:
                for response in page.apps:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAgentsPager:
    """A pager for iterating through ``list_agents`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListAgentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``agents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAgents`` requests and continue to iterate
    through the ``agents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListAgentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListAgentsResponse],
        request: agent_service.ListAgentsRequest,
        response: agent_service.ListAgentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListAgentsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListAgentsResponse):
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
        self._request = agent_service.ListAgentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListAgentsResponse]:
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
    :class:`google.cloud.ces_v1.types.ListAgentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``agents`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAgents`` requests and continue to iterate
    through the ``agents`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListAgentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListAgentsResponse]],
        request: agent_service.ListAgentsRequest,
        response: agent_service.ListAgentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListAgentsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListAgentsResponse):
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
        self._request = agent_service.ListAgentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListAgentsResponse]:
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


class ListExamplesPager:
    """A pager for iterating through ``list_examples`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListExamplesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``examples`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExamples`` requests and continue to iterate
    through the ``examples`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListExamplesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListExamplesResponse],
        request: agent_service.ListExamplesRequest,
        response: agent_service.ListExamplesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListExamplesRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListExamplesResponse):
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
        self._request = agent_service.ListExamplesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListExamplesResponse]:
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

    def __iter__(self) -> Iterator[example.Example]:
        for page in self.pages:
            yield from page.examples

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExamplesAsyncPager:
    """A pager for iterating through ``list_examples`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListExamplesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``examples`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExamples`` requests and continue to iterate
    through the ``examples`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListExamplesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListExamplesResponse]],
        request: agent_service.ListExamplesRequest,
        response: agent_service.ListExamplesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListExamplesRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListExamplesResponse):
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
        self._request = agent_service.ListExamplesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListExamplesResponse]:
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

    def __aiter__(self) -> AsyncIterator[example.Example]:
        async def async_generator():
            async for page in self.pages:
                for response in page.examples:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListToolsPager:
    """A pager for iterating through ``list_tools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListToolsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tools`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTools`` requests and continue to iterate
    through the ``tools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListToolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListToolsResponse],
        request: agent_service.ListToolsRequest,
        response: agent_service.ListToolsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListToolsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListToolsResponse):
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
        self._request = agent_service.ListToolsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListToolsResponse]:
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

    def __iter__(self) -> Iterator[tool.Tool]:
        for page in self.pages:
            yield from page.tools

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListToolsAsyncPager:
    """A pager for iterating through ``list_tools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListToolsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tools`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTools`` requests and continue to iterate
    through the ``tools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListToolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListToolsResponse]],
        request: agent_service.ListToolsRequest,
        response: agent_service.ListToolsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListToolsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListToolsResponse):
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
        self._request = agent_service.ListToolsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListToolsResponse]:
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

    def __aiter__(self) -> AsyncIterator[tool.Tool]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tools:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversationsPager:
    """A pager for iterating through ``list_conversations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListConversationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversations`` requests and continue to iterate
    through the ``conversations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListConversationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListConversationsResponse],
        request: agent_service.ListConversationsRequest,
        response: agent_service.ListConversationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListConversationsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListConversationsResponse):
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
        self._request = agent_service.ListConversationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListConversationsResponse]:
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

    def __iter__(self) -> Iterator[conversation.Conversation]:
        for page in self.pages:
            yield from page.conversations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversationsAsyncPager:
    """A pager for iterating through ``list_conversations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListConversationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversations`` requests and continue to iterate
    through the ``conversations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListConversationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListConversationsResponse]],
        request: agent_service.ListConversationsRequest,
        response: agent_service.ListConversationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListConversationsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListConversationsResponse):
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
        self._request = agent_service.ListConversationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListConversationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[conversation.Conversation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.conversations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGuardrailsPager:
    """A pager for iterating through ``list_guardrails`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListGuardrailsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``guardrails`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGuardrails`` requests and continue to iterate
    through the ``guardrails`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListGuardrailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListGuardrailsResponse],
        request: agent_service.ListGuardrailsRequest,
        response: agent_service.ListGuardrailsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListGuardrailsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListGuardrailsResponse):
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
        self._request = agent_service.ListGuardrailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListGuardrailsResponse]:
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

    def __iter__(self) -> Iterator[guardrail.Guardrail]:
        for page in self.pages:
            yield from page.guardrails

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGuardrailsAsyncPager:
    """A pager for iterating through ``list_guardrails`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListGuardrailsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``guardrails`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGuardrails`` requests and continue to iterate
    through the ``guardrails`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListGuardrailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListGuardrailsResponse]],
        request: agent_service.ListGuardrailsRequest,
        response: agent_service.ListGuardrailsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListGuardrailsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListGuardrailsResponse):
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
        self._request = agent_service.ListGuardrailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListGuardrailsResponse]:
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

    def __aiter__(self) -> AsyncIterator[guardrail.Guardrail]:
        async def async_generator():
            async for page in self.pages:
                for response in page.guardrails:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentsPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListDeploymentsResponse],
        request: agent_service.ListDeploymentsRequest,
        response: agent_service.ListDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListDeploymentsResponse):
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
        self._request = agent_service.ListDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[deployment.Deployment]:
        for page in self.pages:
            yield from page.deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeploymentsAsyncPager:
    """A pager for iterating through ``list_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeployments`` requests and continue to iterate
    through the ``deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListDeploymentsResponse]],
        request: agent_service.ListDeploymentsRequest,
        response: agent_service.ListDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListDeploymentsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListDeploymentsResponse):
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
        self._request = agent_service.ListDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployment.Deployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListToolsetsPager:
    """A pager for iterating through ``list_toolsets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListToolsetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``toolsets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListToolsets`` requests and continue to iterate
    through the ``toolsets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListToolsetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListToolsetsResponse],
        request: agent_service.ListToolsetsRequest,
        response: agent_service.ListToolsetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListToolsetsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListToolsetsResponse):
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
        self._request = agent_service.ListToolsetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListToolsetsResponse]:
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

    def __iter__(self) -> Iterator[toolset.Toolset]:
        for page in self.pages:
            yield from page.toolsets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListToolsetsAsyncPager:
    """A pager for iterating through ``list_toolsets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListToolsetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``toolsets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListToolsets`` requests and continue to iterate
    through the ``toolsets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListToolsetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListToolsetsResponse]],
        request: agent_service.ListToolsetsRequest,
        response: agent_service.ListToolsetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListToolsetsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListToolsetsResponse):
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
        self._request = agent_service.ListToolsetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListToolsetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[toolset.Toolset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.toolsets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAppVersionsPager:
    """A pager for iterating through ``list_app_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListAppVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``app_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAppVersions`` requests and continue to iterate
    through the ``app_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListAppVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListAppVersionsResponse],
        request: agent_service.ListAppVersionsRequest,
        response: agent_service.ListAppVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListAppVersionsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListAppVersionsResponse):
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
        self._request = agent_service.ListAppVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListAppVersionsResponse]:
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

    def __iter__(self) -> Iterator[app_version.AppVersion]:
        for page in self.pages:
            yield from page.app_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAppVersionsAsyncPager:
    """A pager for iterating through ``list_app_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListAppVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``app_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAppVersions`` requests and continue to iterate
    through the ``app_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListAppVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListAppVersionsResponse]],
        request: agent_service.ListAppVersionsRequest,
        response: agent_service.ListAppVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListAppVersionsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListAppVersionsResponse):
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
        self._request = agent_service.ListAppVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListAppVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[app_version.AppVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.app_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListChangelogsPager:
    """A pager for iterating through ``list_changelogs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListChangelogsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``changelogs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListChangelogs`` requests and continue to iterate
    through the ``changelogs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListChangelogsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., agent_service.ListChangelogsResponse],
        request: agent_service.ListChangelogsRequest,
        response: agent_service.ListChangelogsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListChangelogsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListChangelogsResponse):
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
        self._request = agent_service.ListChangelogsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[agent_service.ListChangelogsResponse]:
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

    def __iter__(self) -> Iterator[changelog.Changelog]:
        for page in self.pages:
            yield from page.changelogs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListChangelogsAsyncPager:
    """A pager for iterating through ``list_changelogs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.ces_v1.types.ListChangelogsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``changelogs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListChangelogs`` requests and continue to iterate
    through the ``changelogs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.ces_v1.types.ListChangelogsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[agent_service.ListChangelogsResponse]],
        request: agent_service.ListChangelogsRequest,
        response: agent_service.ListChangelogsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.ces_v1.types.ListChangelogsRequest):
                The initial request object.
            response (google.cloud.ces_v1.types.ListChangelogsResponse):
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
        self._request = agent_service.ListChangelogsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[agent_service.ListChangelogsResponse]:
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

    def __aiter__(self) -> AsyncIterator[changelog.Changelog]:
        async def async_generator():
            async for page in self.pages:
                for response in page.changelogs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
