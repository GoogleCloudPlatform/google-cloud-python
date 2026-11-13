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

from google.ads.marketingplatform_admin_v1alpha.types import (
    marketingplatform_admin,
    resources,
)


class ListOrganizationsPager:
    """A pager for iterating through ``list_organizations`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``organizations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOrganizations`` requests and continue to iterate
    through the ``organizations`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., marketingplatform_admin.ListOrganizationsResponse],
        request: marketingplatform_admin.ListOrganizationsRequest,
        response: marketingplatform_admin.ListOrganizationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsResponse):
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
        self._request = marketingplatform_admin.ListOrganizationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[marketingplatform_admin.ListOrganizationsResponse]:
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

    def __iter__(self) -> Iterator[resources.Organization]:
        for page in self.pages:
            yield from page.organizations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOrganizationsAsyncPager:
    """A pager for iterating through ``list_organizations`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``organizations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOrganizations`` requests and continue to iterate
    through the ``organizations`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[marketingplatform_admin.ListOrganizationsResponse]
        ],
        request: marketingplatform_admin.ListOrganizationsRequest,
        response: marketingplatform_admin.ListOrganizationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsResponse):
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
        self._request = marketingplatform_admin.ListOrganizationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[marketingplatform_admin.ListOrganizationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Organization]:
        async def async_generator():
            async for page in self.pages:
                for response in page.organizations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalyticsAccountLinksPager:
    """A pager for iterating through ``list_analytics_account_links`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``analytics_account_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAnalyticsAccountLinks`` requests and continue to iterate
    through the ``analytics_account_links`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., marketingplatform_admin.ListAnalyticsAccountLinksResponse
        ],
        request: marketingplatform_admin.ListAnalyticsAccountLinksRequest,
        response: marketingplatform_admin.ListAnalyticsAccountLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksResponse):
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
        self._request = marketingplatform_admin.ListAnalyticsAccountLinksRequest(
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
    ) -> Iterator[marketingplatform_admin.ListAnalyticsAccountLinksResponse]:
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

    def __iter__(self) -> Iterator[resources.AnalyticsAccountLink]:
        for page in self.pages:
            yield from page.analytics_account_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAnalyticsAccountLinksAsyncPager:
    """A pager for iterating through ``list_analytics_account_links`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``analytics_account_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAnalyticsAccountLinks`` requests and continue to iterate
    through the ``analytics_account_links`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[marketingplatform_admin.ListAnalyticsAccountLinksResponse]
        ],
        request: marketingplatform_admin.ListAnalyticsAccountLinksRequest,
        response: marketingplatform_admin.ListAnalyticsAccountLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksResponse):
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
        self._request = marketingplatform_admin.ListAnalyticsAccountLinksRequest(
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
    ) -> AsyncIterator[marketingplatform_admin.ListAnalyticsAccountLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.AnalyticsAccountLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.analytics_account_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserGroupsPager:
    """A pager for iterating through ``list_user_groups`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``user_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUserGroups`` requests and continue to iterate
    through the ``user_groups`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., marketingplatform_admin.ListUserGroupsResponse],
        request: marketingplatform_admin.ListUserGroupsRequest,
        response: marketingplatform_admin.ListUserGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsResponse):
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
        self._request = marketingplatform_admin.ListUserGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[marketingplatform_admin.ListUserGroupsResponse]:
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

    def __iter__(self) -> Iterator[resources.UserGroup]:
        for page in self.pages:
            yield from page.user_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserGroupsAsyncPager:
    """A pager for iterating through ``list_user_groups`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``user_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUserGroups`` requests and continue to iterate
    through the ``user_groups`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[marketingplatform_admin.ListUserGroupsResponse]
        ],
        request: marketingplatform_admin.ListUserGroupsRequest,
        response: marketingplatform_admin.ListUserGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsResponse):
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
        self._request = marketingplatform_admin.ListUserGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[marketingplatform_admin.ListUserGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.UserGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.user_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserGroupMembersPager:
    """A pager for iterating through ``list_user_group_members`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``user_group_members`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUserGroupMembers`` requests and continue to iterate
    through the ``user_group_members`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., marketingplatform_admin.ListUserGroupMembersResponse],
        request: marketingplatform_admin.ListUserGroupMembersRequest,
        response: marketingplatform_admin.ListUserGroupMembersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersResponse):
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
        self._request = marketingplatform_admin.ListUserGroupMembersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[marketingplatform_admin.ListUserGroupMembersResponse]:
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

    def __iter__(self) -> Iterator[resources.UserGroupMember]:
        for page in self.pages:
            yield from page.user_group_members

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserGroupMembersAsyncPager:
    """A pager for iterating through ``list_user_group_members`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``user_group_members`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUserGroupMembers`` requests and continue to iterate
    through the ``user_group_members`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[marketingplatform_admin.ListUserGroupMembersResponse]
        ],
        request: marketingplatform_admin.ListUserGroupMembersRequest,
        response: marketingplatform_admin.ListUserGroupMembersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersResponse):
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
        self._request = marketingplatform_admin.ListUserGroupMembersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[marketingplatform_admin.ListUserGroupMembersResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.UserGroupMember]:
        async def async_generator():
            async for page in self.pages:
                for response in page.user_group_members:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAdminAccessBindingsPager:
    """A pager for iterating through ``list_admin_access_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``admin_access_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAdminAccessBindings`` requests and continue to iterate
    through the ``admin_access_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., marketingplatform_admin.ListAdminAccessBindingsResponse],
        request: marketingplatform_admin.ListAdminAccessBindingsRequest,
        response: marketingplatform_admin.ListAdminAccessBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsResponse):
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
        self._request = marketingplatform_admin.ListAdminAccessBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[marketingplatform_admin.ListAdminAccessBindingsResponse]:
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

    def __iter__(self) -> Iterator[resources.AdminAccessBinding]:
        for page in self.pages:
            yield from page.admin_access_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAdminAccessBindingsAsyncPager:
    """A pager for iterating through ``list_admin_access_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``admin_access_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAdminAccessBindings`` requests and continue to iterate
    through the ``admin_access_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[marketingplatform_admin.ListAdminAccessBindingsResponse]
        ],
        request: marketingplatform_admin.ListAdminAccessBindingsRequest,
        response: marketingplatform_admin.ListAdminAccessBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsRequest):
                The initial request object.
            response (google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsResponse):
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
        self._request = marketingplatform_admin.ListAdminAccessBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[marketingplatform_admin.ListAdminAccessBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.AdminAccessBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.admin_access_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
