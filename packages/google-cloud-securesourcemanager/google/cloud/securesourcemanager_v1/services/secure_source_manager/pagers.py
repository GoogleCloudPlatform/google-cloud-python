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

from google.cloud.securesourcemanager_v1.types import secure_source_manager


class ListInstancesPager:
    """A pager for iterating through ``list_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListInstancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``instances`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInstances`` requests and continue to iterate
    through the ``instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListInstancesResponse],
        request: secure_source_manager.ListInstancesRequest,
        response: secure_source_manager.ListInstancesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListInstancesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListInstancesResponse):
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
        self._request = secure_source_manager.ListInstancesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListInstancesResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.Instance]:
        for page in self.pages:
            yield from page.instances

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInstancesAsyncPager:
    """A pager for iterating through ``list_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListInstancesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``instances`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInstances`` requests and continue to iterate
    through the ``instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[secure_source_manager.ListInstancesResponse]],
        request: secure_source_manager.ListInstancesRequest,
        response: secure_source_manager.ListInstancesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListInstancesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListInstancesResponse):
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
        self._request = secure_source_manager.ListInstancesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[secure_source_manager.ListInstancesResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.Instance]:
        async def async_generator():
            async for page in self.pages:
                for response in page.instances:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRepositoriesPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListRepositoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListRepositoriesResponse],
        request: secure_source_manager.ListRepositoriesRequest,
        response: secure_source_manager.ListRepositoriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListRepositoriesResponse):
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
        self._request = secure_source_manager.ListRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListRepositoriesResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.Repository]:
        for page in self.pages:
            yield from page.repositories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRepositoriesAsyncPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListRepositoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[secure_source_manager.ListRepositoriesResponse]
        ],
        request: secure_source_manager.ListRepositoriesRequest,
        response: secure_source_manager.ListRepositoriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListRepositoriesResponse):
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
        self._request = secure_source_manager.ListRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[secure_source_manager.ListRepositoriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.Repository]:
        async def async_generator():
            async for page in self.pages:
                for response in page.repositories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHooksPager:
    """A pager for iterating through ``list_hooks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListHooksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``hooks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListHooks`` requests and continue to iterate
    through the ``hooks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListHooksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListHooksResponse],
        request: secure_source_manager.ListHooksRequest,
        response: secure_source_manager.ListHooksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListHooksRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListHooksResponse):
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
        self._request = secure_source_manager.ListHooksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListHooksResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.Hook]:
        for page in self.pages:
            yield from page.hooks

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListHooksAsyncPager:
    """A pager for iterating through ``list_hooks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListHooksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``hooks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListHooks`` requests and continue to iterate
    through the ``hooks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListHooksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[secure_source_manager.ListHooksResponse]],
        request: secure_source_manager.ListHooksRequest,
        response: secure_source_manager.ListHooksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListHooksRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListHooksResponse):
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
        self._request = secure_source_manager.ListHooksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[secure_source_manager.ListHooksResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.Hook]:
        async def async_generator():
            async for page in self.pages:
                for response in page.hooks:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBranchRulesPager:
    """A pager for iterating through ``list_branch_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListBranchRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``branch_rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBranchRules`` requests and continue to iterate
    through the ``branch_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListBranchRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListBranchRulesResponse],
        request: secure_source_manager.ListBranchRulesRequest,
        response: secure_source_manager.ListBranchRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListBranchRulesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListBranchRulesResponse):
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
        self._request = secure_source_manager.ListBranchRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListBranchRulesResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.BranchRule]:
        for page in self.pages:
            yield from page.branch_rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBranchRulesAsyncPager:
    """A pager for iterating through ``list_branch_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListBranchRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``branch_rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBranchRules`` requests and continue to iterate
    through the ``branch_rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListBranchRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[secure_source_manager.ListBranchRulesResponse]],
        request: secure_source_manager.ListBranchRulesRequest,
        response: secure_source_manager.ListBranchRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListBranchRulesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListBranchRulesResponse):
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
        self._request = secure_source_manager.ListBranchRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[secure_source_manager.ListBranchRulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.BranchRule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.branch_rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPullRequestsPager:
    """A pager for iterating through ``list_pull_requests`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``pull_requests`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPullRequests`` requests and continue to iterate
    through the ``pull_requests`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListPullRequestsResponse],
        request: secure_source_manager.ListPullRequestsRequest,
        response: secure_source_manager.ListPullRequestsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListPullRequestsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListPullRequestsResponse):
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
        self._request = secure_source_manager.ListPullRequestsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListPullRequestsResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.PullRequest]:
        for page in self.pages:
            yield from page.pull_requests

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPullRequestsAsyncPager:
    """A pager for iterating through ``list_pull_requests`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``pull_requests`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPullRequests`` requests and continue to iterate
    through the ``pull_requests`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[secure_source_manager.ListPullRequestsResponse]
        ],
        request: secure_source_manager.ListPullRequestsRequest,
        response: secure_source_manager.ListPullRequestsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListPullRequestsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListPullRequestsResponse):
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
        self._request = secure_source_manager.ListPullRequestsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[secure_source_manager.ListPullRequestsResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.PullRequest]:
        async def async_generator():
            async for page in self.pages:
                for response in page.pull_requests:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPullRequestFileDiffsPager:
    """A pager for iterating through ``list_pull_request_file_diffs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``file_diffs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPullRequestFileDiffs`` requests and continue to iterate
    through the ``file_diffs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListPullRequestFileDiffsResponse],
        request: secure_source_manager.ListPullRequestFileDiffsRequest,
        response: secure_source_manager.ListPullRequestFileDiffsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsResponse):
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
        self._request = secure_source_manager.ListPullRequestFileDiffsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListPullRequestFileDiffsResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.FileDiff]:
        for page in self.pages:
            yield from page.file_diffs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPullRequestFileDiffsAsyncPager:
    """A pager for iterating through ``list_pull_request_file_diffs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``file_diffs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPullRequestFileDiffs`` requests and continue to iterate
    through the ``file_diffs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[secure_source_manager.ListPullRequestFileDiffsResponse]
        ],
        request: secure_source_manager.ListPullRequestFileDiffsRequest,
        response: secure_source_manager.ListPullRequestFileDiffsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListPullRequestFileDiffsResponse):
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
        self._request = secure_source_manager.ListPullRequestFileDiffsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[secure_source_manager.ListPullRequestFileDiffsResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.FileDiff]:
        async def async_generator():
            async for page in self.pages:
                for response in page.file_diffs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchTreePager:
    """A pager for iterating through ``fetch_tree`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.FetchTreeResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tree_entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchTree`` requests and continue to iterate
    through the ``tree_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.FetchTreeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.FetchTreeResponse],
        request: secure_source_manager.FetchTreeRequest,
        response: secure_source_manager.FetchTreeResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.FetchTreeRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.FetchTreeResponse):
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
        self._request = secure_source_manager.FetchTreeRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.FetchTreeResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.TreeEntry]:
        for page in self.pages:
            yield from page.tree_entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchTreeAsyncPager:
    """A pager for iterating through ``fetch_tree`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.FetchTreeResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tree_entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchTree`` requests and continue to iterate
    through the ``tree_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.FetchTreeResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[secure_source_manager.FetchTreeResponse]],
        request: secure_source_manager.FetchTreeRequest,
        response: secure_source_manager.FetchTreeResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.FetchTreeRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.FetchTreeResponse):
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
        self._request = secure_source_manager.FetchTreeRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[secure_source_manager.FetchTreeResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.TreeEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tree_entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchRefsPager:
    """A pager for iterating through ``fetch_refs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.FetchRefsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``refs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchRefs`` requests and continue to iterate
    through the ``refs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.FetchRefsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.FetchRefsResponse],
        request: secure_source_manager.FetchRefsRequest,
        response: secure_source_manager.FetchRefsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.FetchRefsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.FetchRefsResponse):
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
        self._request = secure_source_manager.FetchRefsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.FetchRefsResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.Ref]:
        for page in self.pages:
            yield from page.refs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchRefsAsyncPager:
    """A pager for iterating through ``fetch_refs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.FetchRefsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``refs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchRefs`` requests and continue to iterate
    through the ``refs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.FetchRefsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[secure_source_manager.FetchRefsResponse]],
        request: secure_source_manager.FetchRefsRequest,
        response: secure_source_manager.FetchRefsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.FetchRefsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.FetchRefsResponse):
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
        self._request = secure_source_manager.FetchRefsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[secure_source_manager.FetchRefsResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.Ref]:
        async def async_generator():
            async for page in self.pages:
                for response in page.refs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIssuesPager:
    """A pager for iterating through ``list_issues`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListIssuesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``issues`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListIssues`` requests and continue to iterate
    through the ``issues`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListIssuesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListIssuesResponse],
        request: secure_source_manager.ListIssuesRequest,
        response: secure_source_manager.ListIssuesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListIssuesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListIssuesResponse):
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
        self._request = secure_source_manager.ListIssuesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListIssuesResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.Issue]:
        for page in self.pages:
            yield from page.issues

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIssuesAsyncPager:
    """A pager for iterating through ``list_issues`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListIssuesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``issues`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListIssues`` requests and continue to iterate
    through the ``issues`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListIssuesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[secure_source_manager.ListIssuesResponse]],
        request: secure_source_manager.ListIssuesRequest,
        response: secure_source_manager.ListIssuesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListIssuesRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListIssuesResponse):
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
        self._request = secure_source_manager.ListIssuesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[secure_source_manager.ListIssuesResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.Issue]:
        async def async_generator():
            async for page in self.pages:
                for response in page.issues:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPullRequestCommentsPager:
    """A pager for iterating through ``list_pull_request_comments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``pull_request_comments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPullRequestComments`` requests and continue to iterate
    through the ``pull_request_comments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListPullRequestCommentsResponse],
        request: secure_source_manager.ListPullRequestCommentsRequest,
        response: secure_source_manager.ListPullRequestCommentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsResponse):
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
        self._request = secure_source_manager.ListPullRequestCommentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListPullRequestCommentsResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.PullRequestComment]:
        for page in self.pages:
            yield from page.pull_request_comments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPullRequestCommentsAsyncPager:
    """A pager for iterating through ``list_pull_request_comments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``pull_request_comments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPullRequestComments`` requests and continue to iterate
    through the ``pull_request_comments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[secure_source_manager.ListPullRequestCommentsResponse]
        ],
        request: secure_source_manager.ListPullRequestCommentsRequest,
        response: secure_source_manager.ListPullRequestCommentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListPullRequestCommentsResponse):
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
        self._request = secure_source_manager.ListPullRequestCommentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[secure_source_manager.ListPullRequestCommentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.PullRequestComment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.pull_request_comments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIssueCommentsPager:
    """A pager for iterating through ``list_issue_comments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListIssueCommentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``issue_comments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListIssueComments`` requests and continue to iterate
    through the ``issue_comments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListIssueCommentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., secure_source_manager.ListIssueCommentsResponse],
        request: secure_source_manager.ListIssueCommentsRequest,
        response: secure_source_manager.ListIssueCommentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListIssueCommentsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListIssueCommentsResponse):
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
        self._request = secure_source_manager.ListIssueCommentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[secure_source_manager.ListIssueCommentsResponse]:
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

    def __iter__(self) -> Iterator[secure_source_manager.IssueComment]:
        for page in self.pages:
            yield from page.issue_comments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIssueCommentsAsyncPager:
    """A pager for iterating through ``list_issue_comments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securesourcemanager_v1.types.ListIssueCommentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``issue_comments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListIssueComments`` requests and continue to iterate
    through the ``issue_comments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securesourcemanager_v1.types.ListIssueCommentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[secure_source_manager.ListIssueCommentsResponse]
        ],
        request: secure_source_manager.ListIssueCommentsRequest,
        response: secure_source_manager.ListIssueCommentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securesourcemanager_v1.types.ListIssueCommentsRequest):
                The initial request object.
            response (google.cloud.securesourcemanager_v1.types.ListIssueCommentsResponse):
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
        self._request = secure_source_manager.ListIssueCommentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[secure_source_manager.ListIssueCommentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[secure_source_manager.IssueComment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.issue_comments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
