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

from google.cloud.iam_v3beta.types import (
    access_policies_service,
    access_policy_resources,
    policy_binding_resources,
)


class ListAccessPoliciesPager:
    """A pager for iterating through ``list_access_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.iam_v3beta.types.ListAccessPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``access_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccessPolicies`` requests and continue to iterate
    through the ``access_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.iam_v3beta.types.ListAccessPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., access_policies_service.ListAccessPoliciesResponse],
        request: access_policies_service.ListAccessPoliciesRequest,
        response: access_policies_service.ListAccessPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.iam_v3beta.types.ListAccessPoliciesRequest):
                The initial request object.
            response (google.cloud.iam_v3beta.types.ListAccessPoliciesResponse):
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
        self._request = access_policies_service.ListAccessPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[access_policies_service.ListAccessPoliciesResponse]:
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

    def __iter__(self) -> Iterator[access_policy_resources.AccessPolicy]:
        for page in self.pages:
            yield from page.access_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccessPoliciesAsyncPager:
    """A pager for iterating through ``list_access_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.iam_v3beta.types.ListAccessPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``access_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccessPolicies`` requests and continue to iterate
    through the ``access_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.iam_v3beta.types.ListAccessPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[access_policies_service.ListAccessPoliciesResponse]
        ],
        request: access_policies_service.ListAccessPoliciesRequest,
        response: access_policies_service.ListAccessPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.iam_v3beta.types.ListAccessPoliciesRequest):
                The initial request object.
            response (google.cloud.iam_v3beta.types.ListAccessPoliciesResponse):
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
        self._request = access_policies_service.ListAccessPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[access_policies_service.ListAccessPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[access_policy_resources.AccessPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.access_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAccessPolicyBindingsPager:
    """A pager for iterating through ``search_access_policy_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``policy_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAccessPolicyBindings`` requests and continue to iterate
    through the ``policy_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., access_policies_service.SearchAccessPolicyBindingsResponse
        ],
        request: access_policies_service.SearchAccessPolicyBindingsRequest,
        response: access_policies_service.SearchAccessPolicyBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsRequest):
                The initial request object.
            response (google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse):
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
        self._request = access_policies_service.SearchAccessPolicyBindingsRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[access_policies_service.SearchAccessPolicyBindingsResponse]:
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

    def __iter__(self) -> Iterator[policy_binding_resources.PolicyBinding]:
        for page in self.pages:
            yield from page.policy_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAccessPolicyBindingsAsyncPager:
    """A pager for iterating through ``search_access_policy_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``policy_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAccessPolicyBindings`` requests and continue to iterate
    through the ``policy_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[access_policies_service.SearchAccessPolicyBindingsResponse]
        ],
        request: access_policies_service.SearchAccessPolicyBindingsRequest,
        response: access_policies_service.SearchAccessPolicyBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsRequest):
                The initial request object.
            response (google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse):
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
        self._request = access_policies_service.SearchAccessPolicyBindingsRequest(
            request
        )
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[access_policies_service.SearchAccessPolicyBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[policy_binding_resources.PolicyBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.policy_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
