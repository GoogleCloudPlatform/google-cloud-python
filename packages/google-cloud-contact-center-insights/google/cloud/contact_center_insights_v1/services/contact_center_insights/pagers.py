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

from google.cloud.contact_center_insights_v1.types import (
    contact_center_insights,
    resources,
)


class ListConversationsPager:
    """A pager for iterating through ``list_conversations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListConversationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversations`` requests and continue to iterate
    through the ``conversations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListConversationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListConversationsResponse],
        request: contact_center_insights.ListConversationsRequest,
        response: contact_center_insights.ListConversationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListConversationsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListConversationsResponse):
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
        self._request = contact_center_insights.ListConversationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListConversationsResponse]:
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

    def __iter__(self) -> Iterator[resources.Conversation]:
        for page in self.pages:
            yield from page.conversations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversationsAsyncPager:
    """A pager for iterating through ``list_conversations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListConversationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversations`` requests and continue to iterate
    through the ``conversations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListConversationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListConversationsResponse]
        ],
        request: contact_center_insights.ListConversationsRequest,
        response: contact_center_insights.ListConversationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListConversationsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListConversationsResponse):
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
        self._request = contact_center_insights.ListConversationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListConversationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Conversation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.conversations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalysesPager:
    """A pager for iterating through ``list_analyses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListAnalysesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``analyses`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnalyses`` requests and continue to iterate
    through the ``analyses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListAnalysesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListAnalysesResponse],
        request: contact_center_insights.ListAnalysesRequest,
        response: contact_center_insights.ListAnalysesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListAnalysesRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListAnalysesResponse):
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
        self._request = contact_center_insights.ListAnalysesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListAnalysesResponse]:
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

    def __iter__(self) -> Iterator[resources.Analysis]:
        for page in self.pages:
            yield from page.analyses

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalysesAsyncPager:
    """A pager for iterating through ``list_analyses`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListAnalysesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``analyses`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnalyses`` requests and continue to iterate
    through the ``analyses`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListAnalysesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[contact_center_insights.ListAnalysesResponse]],
        request: contact_center_insights.ListAnalysesRequest,
        response: contact_center_insights.ListAnalysesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListAnalysesRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListAnalysesResponse):
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
        self._request = contact_center_insights.ListAnalysesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListAnalysesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Analysis]:
        async def async_generator():
            async for page in self.pages:
                for response in page.analyses:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPhraseMatchersPager:
    """A pager for iterating through ``list_phrase_matchers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListPhraseMatchersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``phrase_matchers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPhraseMatchers`` requests and continue to iterate
    through the ``phrase_matchers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListPhraseMatchersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListPhraseMatchersResponse],
        request: contact_center_insights.ListPhraseMatchersRequest,
        response: contact_center_insights.ListPhraseMatchersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListPhraseMatchersRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListPhraseMatchersResponse):
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
        self._request = contact_center_insights.ListPhraseMatchersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListPhraseMatchersResponse]:
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

    def __iter__(self) -> Iterator[resources.PhraseMatcher]:
        for page in self.pages:
            yield from page.phrase_matchers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPhraseMatchersAsyncPager:
    """A pager for iterating through ``list_phrase_matchers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListPhraseMatchersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``phrase_matchers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPhraseMatchers`` requests and continue to iterate
    through the ``phrase_matchers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListPhraseMatchersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListPhraseMatchersResponse]
        ],
        request: contact_center_insights.ListPhraseMatchersRequest,
        response: contact_center_insights.ListPhraseMatchersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListPhraseMatchersRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListPhraseMatchersResponse):
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
        self._request = contact_center_insights.ListPhraseMatchersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListPhraseMatchersResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.PhraseMatcher]:
        async def async_generator():
            async for page in self.pages:
                for response in page.phrase_matchers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalysisRulesPager:
    """A pager for iterating through ``list_analysis_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListAnalysisRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``analysis_rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnalysisRules`` requests and continue to iterate
    through the ``analysis_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListAnalysisRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListAnalysisRulesResponse],
        request: contact_center_insights.ListAnalysisRulesRequest,
        response: contact_center_insights.ListAnalysisRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListAnalysisRulesRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListAnalysisRulesResponse):
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
        self._request = contact_center_insights.ListAnalysisRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListAnalysisRulesResponse]:
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

    def __iter__(self) -> Iterator[resources.AnalysisRule]:
        for page in self.pages:
            yield from page.analysis_rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalysisRulesAsyncPager:
    """A pager for iterating through ``list_analysis_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListAnalysisRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``analysis_rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnalysisRules`` requests and continue to iterate
    through the ``analysis_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListAnalysisRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListAnalysisRulesResponse]
        ],
        request: contact_center_insights.ListAnalysisRulesRequest,
        response: contact_center_insights.ListAnalysisRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListAnalysisRulesRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListAnalysisRulesResponse):
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
        self._request = contact_center_insights.ListAnalysisRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListAnalysisRulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.AnalysisRule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.analysis_rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListViewsPager:
    """A pager for iterating through ``list_views`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListViewsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``views`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListViews`` requests and continue to iterate
    through the ``views`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListViewsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListViewsResponse],
        request: contact_center_insights.ListViewsRequest,
        response: contact_center_insights.ListViewsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListViewsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListViewsResponse):
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
        self._request = contact_center_insights.ListViewsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListViewsResponse]:
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

    def __iter__(self) -> Iterator[resources.View]:
        for page in self.pages:
            yield from page.views

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListViewsAsyncPager:
    """A pager for iterating through ``list_views`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListViewsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``views`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListViews`` requests and continue to iterate
    through the ``views`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListViewsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[contact_center_insights.ListViewsResponse]],
        request: contact_center_insights.ListViewsRequest,
        response: contact_center_insights.ListViewsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListViewsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListViewsResponse):
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
        self._request = contact_center_insights.ListViewsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[contact_center_insights.ListViewsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.View]:
        async def async_generator():
            async for page in self.pages:
                for response in page.views:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQaQuestionsPager:
    """A pager for iterating through ``list_qa_questions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListQaQuestionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``qa_questions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListQaQuestions`` requests and continue to iterate
    through the ``qa_questions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListQaQuestionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListQaQuestionsResponse],
        request: contact_center_insights.ListQaQuestionsRequest,
        response: contact_center_insights.ListQaQuestionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListQaQuestionsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListQaQuestionsResponse):
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
        self._request = contact_center_insights.ListQaQuestionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListQaQuestionsResponse]:
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

    def __iter__(self) -> Iterator[resources.QaQuestion]:
        for page in self.pages:
            yield from page.qa_questions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQaQuestionsAsyncPager:
    """A pager for iterating through ``list_qa_questions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListQaQuestionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``qa_questions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListQaQuestions`` requests and continue to iterate
    through the ``qa_questions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListQaQuestionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListQaQuestionsResponse]
        ],
        request: contact_center_insights.ListQaQuestionsRequest,
        response: contact_center_insights.ListQaQuestionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListQaQuestionsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListQaQuestionsResponse):
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
        self._request = contact_center_insights.ListQaQuestionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListQaQuestionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.QaQuestion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.qa_questions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQaScorecardsPager:
    """A pager for iterating through ``list_qa_scorecards`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``qa_scorecards`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListQaScorecards`` requests and continue to iterate
    through the ``qa_scorecards`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListQaScorecardsResponse],
        request: contact_center_insights.ListQaScorecardsRequest,
        response: contact_center_insights.ListQaScorecardsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListQaScorecardsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListQaScorecardsResponse):
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
        self._request = contact_center_insights.ListQaScorecardsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListQaScorecardsResponse]:
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

    def __iter__(self) -> Iterator[resources.QaScorecard]:
        for page in self.pages:
            yield from page.qa_scorecards

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQaScorecardsAsyncPager:
    """A pager for iterating through ``list_qa_scorecards`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``qa_scorecards`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListQaScorecards`` requests and continue to iterate
    through the ``qa_scorecards`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListQaScorecardsResponse]
        ],
        request: contact_center_insights.ListQaScorecardsRequest,
        response: contact_center_insights.ListQaScorecardsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListQaScorecardsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListQaScorecardsResponse):
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
        self._request = contact_center_insights.ListQaScorecardsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListQaScorecardsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.QaScorecard]:
        async def async_generator():
            async for page in self.pages:
                for response in page.qa_scorecards:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQaScorecardRevisionsPager:
    """A pager for iterating through ``list_qa_scorecard_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``qa_scorecard_revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListQaScorecardRevisions`` requests and continue to iterate
    through the ``qa_scorecard_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListQaScorecardRevisionsResponse],
        request: contact_center_insights.ListQaScorecardRevisionsRequest,
        response: contact_center_insights.ListQaScorecardRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsResponse):
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
        self._request = contact_center_insights.ListQaScorecardRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[contact_center_insights.ListQaScorecardRevisionsResponse]:
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

    def __iter__(self) -> Iterator[resources.QaScorecardRevision]:
        for page in self.pages:
            yield from page.qa_scorecard_revisions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListQaScorecardRevisionsAsyncPager:
    """A pager for iterating through ``list_qa_scorecard_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``qa_scorecard_revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListQaScorecardRevisions`` requests and continue to iterate
    through the ``qa_scorecard_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListQaScorecardRevisionsResponse]
        ],
        request: contact_center_insights.ListQaScorecardRevisionsRequest,
        response: contact_center_insights.ListQaScorecardRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsResponse):
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
        self._request = contact_center_insights.ListQaScorecardRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListQaScorecardRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.QaScorecardRevision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.qa_scorecard_revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeedbackLabelsPager:
    """A pager for iterating through ``list_feedback_labels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``feedback_labels`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFeedbackLabels`` requests and continue to iterate
    through the ``feedback_labels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListFeedbackLabelsResponse],
        request: contact_center_insights.ListFeedbackLabelsRequest,
        response: contact_center_insights.ListFeedbackLabelsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsResponse):
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
        self._request = contact_center_insights.ListFeedbackLabelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListFeedbackLabelsResponse]:
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

    def __iter__(self) -> Iterator[resources.FeedbackLabel]:
        for page in self.pages:
            yield from page.feedback_labels

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFeedbackLabelsAsyncPager:
    """A pager for iterating through ``list_feedback_labels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``feedback_labels`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFeedbackLabels`` requests and continue to iterate
    through the ``feedback_labels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListFeedbackLabelsResponse]
        ],
        request: contact_center_insights.ListFeedbackLabelsRequest,
        response: contact_center_insights.ListFeedbackLabelsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsResponse):
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
        self._request = contact_center_insights.ListFeedbackLabelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListFeedbackLabelsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.FeedbackLabel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.feedback_labels:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAllFeedbackLabelsPager:
    """A pager for iterating through ``list_all_feedback_labels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``feedback_labels`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAllFeedbackLabels`` requests and continue to iterate
    through the ``feedback_labels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., contact_center_insights.ListAllFeedbackLabelsResponse],
        request: contact_center_insights.ListAllFeedbackLabelsRequest,
        response: contact_center_insights.ListAllFeedbackLabelsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsResponse):
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
        self._request = contact_center_insights.ListAllFeedbackLabelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[contact_center_insights.ListAllFeedbackLabelsResponse]:
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

    def __iter__(self) -> Iterator[resources.FeedbackLabel]:
        for page in self.pages:
            yield from page.feedback_labels

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAllFeedbackLabelsAsyncPager:
    """A pager for iterating through ``list_all_feedback_labels`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``feedback_labels`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAllFeedbackLabels`` requests and continue to iterate
    through the ``feedback_labels`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[contact_center_insights.ListAllFeedbackLabelsResponse]
        ],
        request: contact_center_insights.ListAllFeedbackLabelsRequest,
        response: contact_center_insights.ListAllFeedbackLabelsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsRequest):
                The initial request object.
            response (google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsResponse):
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
        self._request = contact_center_insights.ListAllFeedbackLabelsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[contact_center_insights.ListAllFeedbackLabelsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.FeedbackLabel]:
        async def async_generator():
            async for page in self.pages:
                for response in page.feedback_labels:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
