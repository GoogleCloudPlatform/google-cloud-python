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

from google.cloud.chronicle_v1.types import rule


class ListRulesPager:
    """A pager for iterating through ``list_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRules`` requests and continue to iterate
    through the ``rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., rule.ListRulesResponse],
        request: rule.ListRulesRequest,
        response: rule.ListRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRulesRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRulesResponse):
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
        self._request = rule.ListRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[rule.ListRulesResponse]:
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

    def __iter__(self) -> Iterator[rule.Rule]:
        for page in self.pages:
            yield from page.rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRulesAsyncPager:
    """A pager for iterating through ``list_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRules`` requests and continue to iterate
    through the ``rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[rule.ListRulesResponse]],
        request: rule.ListRulesRequest,
        response: rule.ListRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRulesRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRulesResponse):
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
        self._request = rule.ListRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[rule.ListRulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[rule.Rule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRuleRevisionsPager:
    """A pager for iterating through ``list_rule_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRuleRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRuleRevisions`` requests and continue to iterate
    through the ``rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRuleRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., rule.ListRuleRevisionsResponse],
        request: rule.ListRuleRevisionsRequest,
        response: rule.ListRuleRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRuleRevisionsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRuleRevisionsResponse):
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
        self._request = rule.ListRuleRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[rule.ListRuleRevisionsResponse]:
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

    def __iter__(self) -> Iterator[rule.Rule]:
        for page in self.pages:
            yield from page.rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRuleRevisionsAsyncPager:
    """A pager for iterating through ``list_rule_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRuleRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRuleRevisions`` requests and continue to iterate
    through the ``rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRuleRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[rule.ListRuleRevisionsResponse]],
        request: rule.ListRuleRevisionsRequest,
        response: rule.ListRuleRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRuleRevisionsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRuleRevisionsResponse):
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
        self._request = rule.ListRuleRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[rule.ListRuleRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[rule.Rule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRetrohuntsPager:
    """A pager for iterating through ``list_retrohunts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRetrohuntsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``retrohunts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRetrohunts`` requests and continue to iterate
    through the ``retrohunts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRetrohuntsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., rule.ListRetrohuntsResponse],
        request: rule.ListRetrohuntsRequest,
        response: rule.ListRetrohuntsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRetrohuntsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRetrohuntsResponse):
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
        self._request = rule.ListRetrohuntsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[rule.ListRetrohuntsResponse]:
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

    def __iter__(self) -> Iterator[rule.Retrohunt]:
        for page in self.pages:
            yield from page.retrohunts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRetrohuntsAsyncPager:
    """A pager for iterating through ``list_retrohunts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRetrohuntsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``retrohunts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRetrohunts`` requests and continue to iterate
    through the ``retrohunts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRetrohuntsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[rule.ListRetrohuntsResponse]],
        request: rule.ListRetrohuntsRequest,
        response: rule.ListRetrohuntsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRetrohuntsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRetrohuntsResponse):
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
        self._request = rule.ListRetrohuntsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[rule.ListRetrohuntsResponse]:
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

    def __aiter__(self) -> AsyncIterator[rule.Retrohunt]:
        async def async_generator():
            async for page in self.pages:
                for response in page.retrohunts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRuleDeploymentsPager:
    """A pager for iterating through ``list_rule_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRuleDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rule_deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRuleDeployments`` requests and continue to iterate
    through the ``rule_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRuleDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., rule.ListRuleDeploymentsResponse],
        request: rule.ListRuleDeploymentsRequest,
        response: rule.ListRuleDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRuleDeploymentsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRuleDeploymentsResponse):
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
        self._request = rule.ListRuleDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[rule.ListRuleDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[rule.RuleDeployment]:
        for page in self.pages:
            yield from page.rule_deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRuleDeploymentsAsyncPager:
    """A pager for iterating through ``list_rule_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.chronicle_v1.types.ListRuleDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rule_deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRuleDeployments`` requests and continue to iterate
    through the ``rule_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.chronicle_v1.types.ListRuleDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[rule.ListRuleDeploymentsResponse]],
        request: rule.ListRuleDeploymentsRequest,
        response: rule.ListRuleDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.chronicle_v1.types.ListRuleDeploymentsRequest):
                The initial request object.
            response (google.cloud.chronicle_v1.types.ListRuleDeploymentsResponse):
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
        self._request = rule.ListRuleDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[rule.ListRuleDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[rule.RuleDeployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rule_deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
