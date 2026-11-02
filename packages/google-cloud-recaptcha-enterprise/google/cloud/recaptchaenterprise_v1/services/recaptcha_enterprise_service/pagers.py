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

from google.cloud.recaptchaenterprise_v1.types import recaptchaenterprise


class ListKeysPager:
    """A pager for iterating through ``list_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListKeysResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``keys`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListKeys`` requests and continue to iterate
    through the ``keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., recaptchaenterprise.ListKeysResponse],
        request: recaptchaenterprise.ListKeysRequest,
        response: recaptchaenterprise.ListKeysResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListKeysRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListKeysResponse):
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
        self._request = recaptchaenterprise.ListKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[recaptchaenterprise.ListKeysResponse]:
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

    def __iter__(self) -> Iterator[recaptchaenterprise.Key]:
        for page in self.pages:
            yield from page.keys

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKeysAsyncPager:
    """A pager for iterating through ``list_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListKeysResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``keys`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListKeys`` requests and continue to iterate
    through the ``keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[recaptchaenterprise.ListKeysResponse]],
        request: recaptchaenterprise.ListKeysRequest,
        response: recaptchaenterprise.ListKeysResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListKeysRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListKeysResponse):
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
        self._request = recaptchaenterprise.ListKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[recaptchaenterprise.ListKeysResponse]:
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

    def __aiter__(self) -> AsyncIterator[recaptchaenterprise.Key]:
        async def async_generator():
            async for page in self.pages:
                for response in page.keys:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIpOverridesPager:
    """A pager for iterating through ``list_ip_overrides`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListIpOverridesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``ip_overrides`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListIpOverrides`` requests and continue to iterate
    through the ``ip_overrides`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListIpOverridesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., recaptchaenterprise.ListIpOverridesResponse],
        request: recaptchaenterprise.ListIpOverridesRequest,
        response: recaptchaenterprise.ListIpOverridesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListIpOverridesRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListIpOverridesResponse):
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
        self._request = recaptchaenterprise.ListIpOverridesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[recaptchaenterprise.ListIpOverridesResponse]:
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

    def __iter__(self) -> Iterator[recaptchaenterprise.IpOverrideData]:
        for page in self.pages:
            yield from page.ip_overrides

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListIpOverridesAsyncPager:
    """A pager for iterating through ``list_ip_overrides`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListIpOverridesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``ip_overrides`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListIpOverrides`` requests and continue to iterate
    through the ``ip_overrides`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListIpOverridesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[recaptchaenterprise.ListIpOverridesResponse]],
        request: recaptchaenterprise.ListIpOverridesRequest,
        response: recaptchaenterprise.ListIpOverridesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListIpOverridesRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListIpOverridesResponse):
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
        self._request = recaptchaenterprise.ListIpOverridesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[recaptchaenterprise.ListIpOverridesResponse]:
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

    def __aiter__(self) -> AsyncIterator[recaptchaenterprise.IpOverrideData]:
        async def async_generator():
            async for page in self.pages:
                for response in page.ip_overrides:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFirewallPoliciesPager:
    """A pager for iterating through ``list_firewall_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``firewall_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFirewallPolicies`` requests and continue to iterate
    through the ``firewall_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., recaptchaenterprise.ListFirewallPoliciesResponse],
        request: recaptchaenterprise.ListFirewallPoliciesRequest,
        response: recaptchaenterprise.ListFirewallPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesResponse):
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
        self._request = recaptchaenterprise.ListFirewallPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[recaptchaenterprise.ListFirewallPoliciesResponse]:
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

    def __iter__(self) -> Iterator[recaptchaenterprise.FirewallPolicy]:
        for page in self.pages:
            yield from page.firewall_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFirewallPoliciesAsyncPager:
    """A pager for iterating through ``list_firewall_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``firewall_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFirewallPolicies`` requests and continue to iterate
    through the ``firewall_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[recaptchaenterprise.ListFirewallPoliciesResponse]
        ],
        request: recaptchaenterprise.ListFirewallPoliciesRequest,
        response: recaptchaenterprise.ListFirewallPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesResponse):
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
        self._request = recaptchaenterprise.ListFirewallPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[recaptchaenterprise.ListFirewallPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[recaptchaenterprise.FirewallPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.firewall_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRelatedAccountGroupsPager:
    """A pager for iterating through ``list_related_account_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``related_account_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRelatedAccountGroups`` requests and continue to iterate
    through the ``related_account_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., recaptchaenterprise.ListRelatedAccountGroupsResponse],
        request: recaptchaenterprise.ListRelatedAccountGroupsRequest,
        response: recaptchaenterprise.ListRelatedAccountGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsResponse):
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
        self._request = recaptchaenterprise.ListRelatedAccountGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[recaptchaenterprise.ListRelatedAccountGroupsResponse]:
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

    def __iter__(self) -> Iterator[recaptchaenterprise.RelatedAccountGroup]:
        for page in self.pages:
            yield from page.related_account_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRelatedAccountGroupsAsyncPager:
    """A pager for iterating through ``list_related_account_groups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``related_account_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRelatedAccountGroups`` requests and continue to iterate
    through the ``related_account_groups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[recaptchaenterprise.ListRelatedAccountGroupsResponse]
        ],
        request: recaptchaenterprise.ListRelatedAccountGroupsRequest,
        response: recaptchaenterprise.ListRelatedAccountGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsResponse):
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
        self._request = recaptchaenterprise.ListRelatedAccountGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[recaptchaenterprise.ListRelatedAccountGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[recaptchaenterprise.RelatedAccountGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.related_account_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRelatedAccountGroupMembershipsPager:
    """A pager for iterating through ``list_related_account_group_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``related_account_group_memberships`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRelatedAccountGroupMemberships`` requests and continue to iterate
    through the ``related_account_group_memberships`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse
        ],
        request: recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest,
        response: recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsResponse):
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
        self._request = recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest(
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
    ) -> Iterator[recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse]:
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

    def __iter__(self) -> Iterator[recaptchaenterprise.RelatedAccountGroupMembership]:
        for page in self.pages:
            yield from page.related_account_group_memberships

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRelatedAccountGroupMembershipsAsyncPager:
    """A pager for iterating through ``list_related_account_group_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``related_account_group_memberships`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRelatedAccountGroupMemberships`` requests and continue to iterate
    through the ``related_account_group_memberships`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse],
        ],
        request: recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest,
        response: recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsResponse):
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
        self._request = recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest(
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
    ) -> AsyncIterator[recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse]:
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

    def __aiter__(
        self,
    ) -> AsyncIterator[recaptchaenterprise.RelatedAccountGroupMembership]:
        async def async_generator():
            async for page in self.pages:
                for response in page.related_account_group_memberships:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchRelatedAccountGroupMembershipsPager:
    """A pager for iterating through ``search_related_account_group_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``related_account_group_memberships`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchRelatedAccountGroupMemberships`` requests and continue to iterate
    through the ``related_account_group_memberships`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse
        ],
        request: recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest,
        response: recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsResponse):
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
        self._request = recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest(
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
    ) -> Iterator[recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse]:
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

    def __iter__(self) -> Iterator[recaptchaenterprise.RelatedAccountGroupMembership]:
        for page in self.pages:
            yield from page.related_account_group_memberships

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchRelatedAccountGroupMembershipsAsyncPager:
    """A pager for iterating through ``search_related_account_group_memberships`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``related_account_group_memberships`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchRelatedAccountGroupMemberships`` requests and continue to iterate
    through the ``related_account_group_memberships`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse],
        ],
        request: recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest,
        response: recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsRequest):
                The initial request object.
            response (google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsResponse):
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
        self._request = recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest(
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
    ) -> AsyncIterator[
        recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse
    ]:
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

    def __aiter__(
        self,
    ) -> AsyncIterator[recaptchaenterprise.RelatedAccountGroupMembership]:
        async def async_generator():
            async for page in self.pages:
                for response in page.related_account_group_memberships:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
