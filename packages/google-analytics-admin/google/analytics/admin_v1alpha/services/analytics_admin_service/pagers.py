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

from google.analytics.admin_v1alpha.types import (
    analytics_admin,
    audience,
    channel_group,
    event_create_and_edit,
    expanded_data_set,
    resources,
    subproperty_event_filter,
)


class ListAccountsPager:
    """A pager for iterating through ``list_accounts`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAccountsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``accounts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccounts`` requests and continue to iterate
    through the ``accounts`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAccountsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListAccountsResponse],
        request: analytics_admin.ListAccountsRequest,
        response: analytics_admin.ListAccountsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAccountsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAccountsResponse):
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
        self._request = analytics_admin.ListAccountsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListAccountsResponse]:
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

    def __iter__(self) -> Iterator[resources.Account]:
        for page in self.pages:
            yield from page.accounts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccountsAsyncPager:
    """A pager for iterating through ``list_accounts`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAccountsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``accounts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccounts`` requests and continue to iterate
    through the ``accounts`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAccountsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListAccountsResponse]],
        request: analytics_admin.ListAccountsRequest,
        response: analytics_admin.ListAccountsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAccountsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAccountsResponse):
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
        self._request = analytics_admin.ListAccountsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListAccountsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Account]:
        async def async_generator():
            async for page in self.pages:
                for response in page.accounts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccountSummariesPager:
    """A pager for iterating through ``list_account_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAccountSummariesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``account_summaries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccountSummaries`` requests and continue to iterate
    through the ``account_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAccountSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListAccountSummariesResponse],
        request: analytics_admin.ListAccountSummariesRequest,
        response: analytics_admin.ListAccountSummariesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAccountSummariesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAccountSummariesResponse):
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
        self._request = analytics_admin.ListAccountSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListAccountSummariesResponse]:
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

    def __iter__(self) -> Iterator[resources.AccountSummary]:
        for page in self.pages:
            yield from page.account_summaries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccountSummariesAsyncPager:
    """A pager for iterating through ``list_account_summaries`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAccountSummariesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``account_summaries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccountSummaries`` requests and continue to iterate
    through the ``account_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAccountSummariesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListAccountSummariesResponse]],
        request: analytics_admin.ListAccountSummariesRequest,
        response: analytics_admin.ListAccountSummariesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAccountSummariesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAccountSummariesResponse):
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
        self._request = analytics_admin.ListAccountSummariesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListAccountSummariesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.AccountSummary]:
        async def async_generator():
            async for page in self.pages:
                for response in page.account_summaries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPropertiesPager:
    """A pager for iterating through ``list_properties`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListPropertiesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``properties`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProperties`` requests and continue to iterate
    through the ``properties`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListPropertiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListPropertiesResponse],
        request: analytics_admin.ListPropertiesRequest,
        response: analytics_admin.ListPropertiesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListPropertiesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListPropertiesResponse):
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
        self._request = analytics_admin.ListPropertiesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListPropertiesResponse]:
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

    def __iter__(self) -> Iterator[resources.Property]:
        for page in self.pages:
            yield from page.properties

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPropertiesAsyncPager:
    """A pager for iterating through ``list_properties`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListPropertiesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``properties`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProperties`` requests and continue to iterate
    through the ``properties`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListPropertiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListPropertiesResponse]],
        request: analytics_admin.ListPropertiesRequest,
        response: analytics_admin.ListPropertiesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListPropertiesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListPropertiesResponse):
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
        self._request = analytics_admin.ListPropertiesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListPropertiesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Property]:
        async def async_generator():
            async for page in self.pages:
                for response in page.properties:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFirebaseLinksPager:
    """A pager for iterating through ``list_firebase_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListFirebaseLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``firebase_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFirebaseLinks`` requests and continue to iterate
    through the ``firebase_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListFirebaseLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListFirebaseLinksResponse],
        request: analytics_admin.ListFirebaseLinksRequest,
        response: analytics_admin.ListFirebaseLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListFirebaseLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListFirebaseLinksResponse):
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
        self._request = analytics_admin.ListFirebaseLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListFirebaseLinksResponse]:
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

    def __iter__(self) -> Iterator[resources.FirebaseLink]:
        for page in self.pages:
            yield from page.firebase_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFirebaseLinksAsyncPager:
    """A pager for iterating through ``list_firebase_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListFirebaseLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``firebase_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFirebaseLinks`` requests and continue to iterate
    through the ``firebase_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListFirebaseLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListFirebaseLinksResponse]],
        request: analytics_admin.ListFirebaseLinksRequest,
        response: analytics_admin.ListFirebaseLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListFirebaseLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListFirebaseLinksResponse):
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
        self._request = analytics_admin.ListFirebaseLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListFirebaseLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.FirebaseLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.firebase_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoogleAdsLinksPager:
    """A pager for iterating through ``list_google_ads_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListGoogleAdsLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``google_ads_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoogleAdsLinks`` requests and continue to iterate
    through the ``google_ads_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListGoogleAdsLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListGoogleAdsLinksResponse],
        request: analytics_admin.ListGoogleAdsLinksRequest,
        response: analytics_admin.ListGoogleAdsLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListGoogleAdsLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListGoogleAdsLinksResponse):
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
        self._request = analytics_admin.ListGoogleAdsLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListGoogleAdsLinksResponse]:
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

    def __iter__(self) -> Iterator[resources.GoogleAdsLink]:
        for page in self.pages:
            yield from page.google_ads_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoogleAdsLinksAsyncPager:
    """A pager for iterating through ``list_google_ads_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListGoogleAdsLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``google_ads_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoogleAdsLinks`` requests and continue to iterate
    through the ``google_ads_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListGoogleAdsLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListGoogleAdsLinksResponse]],
        request: analytics_admin.ListGoogleAdsLinksRequest,
        response: analytics_admin.ListGoogleAdsLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListGoogleAdsLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListGoogleAdsLinksResponse):
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
        self._request = analytics_admin.ListGoogleAdsLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListGoogleAdsLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.GoogleAdsLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.google_ads_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMeasurementProtocolSecretsPager:
    """A pager for iterating through ``list_measurement_protocol_secrets`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``measurement_protocol_secrets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMeasurementProtocolSecrets`` requests and continue to iterate
    through the ``measurement_protocol_secrets`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListMeasurementProtocolSecretsResponse],
        request: analytics_admin.ListMeasurementProtocolSecretsRequest,
        response: analytics_admin.ListMeasurementProtocolSecretsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsResponse):
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
        self._request = analytics_admin.ListMeasurementProtocolSecretsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListMeasurementProtocolSecretsResponse]:
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

    def __iter__(self) -> Iterator[resources.MeasurementProtocolSecret]:
        for page in self.pages:
            yield from page.measurement_protocol_secrets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMeasurementProtocolSecretsAsyncPager:
    """A pager for iterating through ``list_measurement_protocol_secrets`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``measurement_protocol_secrets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMeasurementProtocolSecrets`` requests and continue to iterate
    through the ``measurement_protocol_secrets`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.ListMeasurementProtocolSecretsResponse]
        ],
        request: analytics_admin.ListMeasurementProtocolSecretsRequest,
        response: analytics_admin.ListMeasurementProtocolSecretsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListMeasurementProtocolSecretsResponse):
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
        self._request = analytics_admin.ListMeasurementProtocolSecretsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListMeasurementProtocolSecretsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.MeasurementProtocolSecret]:
        async def async_generator():
            async for page in self.pages:
                for response in page.measurement_protocol_secrets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSKAdNetworkConversionValueSchemasPager:
    """A pager for iterating through ``list_sk_ad_network_conversion_value_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``skadnetwork_conversion_value_schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSKAdNetworkConversionValueSchemas`` requests and continue to iterate
    through the ``skadnetwork_conversion_value_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., analytics_admin.ListSKAdNetworkConversionValueSchemasResponse
        ],
        request: analytics_admin.ListSKAdNetworkConversionValueSchemasRequest,
        response: analytics_admin.ListSKAdNetworkConversionValueSchemasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasResponse):
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
        self._request = analytics_admin.ListSKAdNetworkConversionValueSchemasRequest(
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
    ) -> Iterator[analytics_admin.ListSKAdNetworkConversionValueSchemasResponse]:
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

    def __iter__(self) -> Iterator[resources.SKAdNetworkConversionValueSchema]:
        for page in self.pages:
            yield from page.skadnetwork_conversion_value_schemas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSKAdNetworkConversionValueSchemasAsyncPager:
    """A pager for iterating through ``list_sk_ad_network_conversion_value_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``skadnetwork_conversion_value_schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSKAdNetworkConversionValueSchemas`` requests and continue to iterate
    through the ``skadnetwork_conversion_value_schemas`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[analytics_admin.ListSKAdNetworkConversionValueSchemasResponse],
        ],
        request: analytics_admin.ListSKAdNetworkConversionValueSchemasRequest,
        response: analytics_admin.ListSKAdNetworkConversionValueSchemasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSKAdNetworkConversionValueSchemasResponse):
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
        self._request = analytics_admin.ListSKAdNetworkConversionValueSchemasRequest(
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
    ) -> AsyncIterator[analytics_admin.ListSKAdNetworkConversionValueSchemasResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.SKAdNetworkConversionValueSchema]:
        async def async_generator():
            async for page in self.pages:
                for response in page.skadnetwork_conversion_value_schemas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchChangeHistoryEventsPager:
    """A pager for iterating through ``search_change_history_events`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``change_history_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchChangeHistoryEvents`` requests and continue to iterate
    through the ``change_history_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.SearchChangeHistoryEventsResponse],
        request: analytics_admin.SearchChangeHistoryEventsRequest,
        response: analytics_admin.SearchChangeHistoryEventsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsResponse):
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
        self._request = analytics_admin.SearchChangeHistoryEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.SearchChangeHistoryEventsResponse]:
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

    def __iter__(self) -> Iterator[resources.ChangeHistoryEvent]:
        for page in self.pages:
            yield from page.change_history_events

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchChangeHistoryEventsAsyncPager:
    """A pager for iterating through ``search_change_history_events`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``change_history_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchChangeHistoryEvents`` requests and continue to iterate
    through the ``change_history_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.SearchChangeHistoryEventsResponse]
        ],
        request: analytics_admin.SearchChangeHistoryEventsRequest,
        response: analytics_admin.SearchChangeHistoryEventsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.SearchChangeHistoryEventsResponse):
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
        self._request = analytics_admin.SearchChangeHistoryEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.SearchChangeHistoryEventsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.ChangeHistoryEvent]:
        async def async_generator():
            async for page in self.pages:
                for response in page.change_history_events:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversionEventsPager:
    """A pager for iterating through ``list_conversion_events`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListConversionEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversion_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversionEvents`` requests and continue to iterate
    through the ``conversion_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListConversionEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListConversionEventsResponse],
        request: analytics_admin.ListConversionEventsRequest,
        response: analytics_admin.ListConversionEventsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListConversionEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListConversionEventsResponse):
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
        self._request = analytics_admin.ListConversionEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListConversionEventsResponse]:
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

    def __iter__(self) -> Iterator[resources.ConversionEvent]:
        for page in self.pages:
            yield from page.conversion_events

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversionEventsAsyncPager:
    """A pager for iterating through ``list_conversion_events`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListConversionEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversion_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversionEvents`` requests and continue to iterate
    through the ``conversion_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListConversionEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListConversionEventsResponse]],
        request: analytics_admin.ListConversionEventsRequest,
        response: analytics_admin.ListConversionEventsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListConversionEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListConversionEventsResponse):
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
        self._request = analytics_admin.ListConversionEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListConversionEventsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.ConversionEvent]:
        async def async_generator():
            async for page in self.pages:
                for response in page.conversion_events:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKeyEventsPager:
    """A pager for iterating through ``list_key_events`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListKeyEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``key_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListKeyEvents`` requests and continue to iterate
    through the ``key_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListKeyEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListKeyEventsResponse],
        request: analytics_admin.ListKeyEventsRequest,
        response: analytics_admin.ListKeyEventsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListKeyEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListKeyEventsResponse):
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
        self._request = analytics_admin.ListKeyEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListKeyEventsResponse]:
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

    def __iter__(self) -> Iterator[resources.KeyEvent]:
        for page in self.pages:
            yield from page.key_events

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKeyEventsAsyncPager:
    """A pager for iterating through ``list_key_events`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListKeyEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``key_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListKeyEvents`` requests and continue to iterate
    through the ``key_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListKeyEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListKeyEventsResponse]],
        request: analytics_admin.ListKeyEventsRequest,
        response: analytics_admin.ListKeyEventsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListKeyEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListKeyEventsResponse):
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
        self._request = analytics_admin.ListKeyEventsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListKeyEventsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.KeyEvent]:
        async def async_generator():
            async for page in self.pages:
                for response in page.key_events:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDisplayVideo360AdvertiserLinksPager:
    """A pager for iterating through ``list_display_video360_advertiser_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``display_video_360_advertiser_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDisplayVideo360AdvertiserLinks`` requests and continue to iterate
    through the ``display_video_360_advertiser_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., analytics_admin.ListDisplayVideo360AdvertiserLinksResponse
        ],
        request: analytics_admin.ListDisplayVideo360AdvertiserLinksRequest,
        response: analytics_admin.ListDisplayVideo360AdvertiserLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksResponse):
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
        self._request = analytics_admin.ListDisplayVideo360AdvertiserLinksRequest(
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
    ) -> Iterator[analytics_admin.ListDisplayVideo360AdvertiserLinksResponse]:
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

    def __iter__(self) -> Iterator[resources.DisplayVideo360AdvertiserLink]:
        for page in self.pages:
            yield from page.display_video_360_advertiser_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDisplayVideo360AdvertiserLinksAsyncPager:
    """A pager for iterating through ``list_display_video360_advertiser_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``display_video_360_advertiser_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDisplayVideo360AdvertiserLinks`` requests and continue to iterate
    through the ``display_video_360_advertiser_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.ListDisplayVideo360AdvertiserLinksResponse]
        ],
        request: analytics_admin.ListDisplayVideo360AdvertiserLinksRequest,
        response: analytics_admin.ListDisplayVideo360AdvertiserLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinksResponse):
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
        self._request = analytics_admin.ListDisplayVideo360AdvertiserLinksRequest(
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
    ) -> AsyncIterator[analytics_admin.ListDisplayVideo360AdvertiserLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.DisplayVideo360AdvertiserLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.display_video_360_advertiser_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDisplayVideo360AdvertiserLinkProposalsPager:
    """A pager for iterating through ``list_display_video360_advertiser_link_proposals`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``display_video_360_advertiser_link_proposals`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDisplayVideo360AdvertiserLinkProposals`` requests and continue to iterate
    through the ``display_video_360_advertiser_link_proposals`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse
        ],
        request: analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsRequest,
        response: analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsResponse):
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
        self._request = (
            analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsRequest(request)
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
    ) -> Iterator[analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse]:
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

    def __iter__(self) -> Iterator[resources.DisplayVideo360AdvertiserLinkProposal]:
        for page in self.pages:
            yield from page.display_video_360_advertiser_link_proposals

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDisplayVideo360AdvertiserLinkProposalsAsyncPager:
    """A pager for iterating through ``list_display_video360_advertiser_link_proposals`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``display_video_360_advertiser_link_proposals`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDisplayVideo360AdvertiserLinkProposals`` requests and continue to iterate
    through the ``display_video_360_advertiser_link_proposals`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse
            ],
        ],
        request: analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsRequest,
        response: analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListDisplayVideo360AdvertiserLinkProposalsResponse):
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
        self._request = (
            analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsRequest(request)
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
        analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse
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
    ) -> AsyncIterator[resources.DisplayVideo360AdvertiserLinkProposal]:
        async def async_generator():
            async for page in self.pages:
                for response in page.display_video_360_advertiser_link_proposals:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomDimensionsPager:
    """A pager for iterating through ``list_custom_dimensions`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListCustomDimensionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_dimensions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomDimensions`` requests and continue to iterate
    through the ``custom_dimensions`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListCustomDimensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListCustomDimensionsResponse],
        request: analytics_admin.ListCustomDimensionsRequest,
        response: analytics_admin.ListCustomDimensionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListCustomDimensionsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListCustomDimensionsResponse):
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
        self._request = analytics_admin.ListCustomDimensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListCustomDimensionsResponse]:
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

    def __iter__(self) -> Iterator[resources.CustomDimension]:
        for page in self.pages:
            yield from page.custom_dimensions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomDimensionsAsyncPager:
    """A pager for iterating through ``list_custom_dimensions`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListCustomDimensionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_dimensions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomDimensions`` requests and continue to iterate
    through the ``custom_dimensions`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListCustomDimensionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListCustomDimensionsResponse]],
        request: analytics_admin.ListCustomDimensionsRequest,
        response: analytics_admin.ListCustomDimensionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListCustomDimensionsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListCustomDimensionsResponse):
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
        self._request = analytics_admin.ListCustomDimensionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListCustomDimensionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.CustomDimension]:
        async def async_generator():
            async for page in self.pages:
                for response in page.custom_dimensions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomMetricsPager:
    """A pager for iterating through ``list_custom_metrics`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListCustomMetricsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_metrics`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomMetrics`` requests and continue to iterate
    through the ``custom_metrics`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListCustomMetricsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListCustomMetricsResponse],
        request: analytics_admin.ListCustomMetricsRequest,
        response: analytics_admin.ListCustomMetricsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListCustomMetricsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListCustomMetricsResponse):
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
        self._request = analytics_admin.ListCustomMetricsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListCustomMetricsResponse]:
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

    def __iter__(self) -> Iterator[resources.CustomMetric]:
        for page in self.pages:
            yield from page.custom_metrics

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomMetricsAsyncPager:
    """A pager for iterating through ``list_custom_metrics`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListCustomMetricsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_metrics`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomMetrics`` requests and continue to iterate
    through the ``custom_metrics`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListCustomMetricsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListCustomMetricsResponse]],
        request: analytics_admin.ListCustomMetricsRequest,
        response: analytics_admin.ListCustomMetricsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListCustomMetricsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListCustomMetricsResponse):
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
        self._request = analytics_admin.ListCustomMetricsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListCustomMetricsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.CustomMetric]:
        async def async_generator():
            async for page in self.pages:
                for response in page.custom_metrics:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataStreamsPager:
    """A pager for iterating through ``list_data_streams`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListDataStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataStreams`` requests and continue to iterate
    through the ``data_streams`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListDataStreamsResponse],
        request: analytics_admin.ListDataStreamsRequest,
        response: analytics_admin.ListDataStreamsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListDataStreamsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListDataStreamsResponse):
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
        self._request = analytics_admin.ListDataStreamsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListDataStreamsResponse]:
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

    def __iter__(self) -> Iterator[resources.DataStream]:
        for page in self.pages:
            yield from page.data_streams

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataStreamsAsyncPager:
    """A pager for iterating through ``list_data_streams`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListDataStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataStreams`` requests and continue to iterate
    through the ``data_streams`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListDataStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListDataStreamsResponse]],
        request: analytics_admin.ListDataStreamsRequest,
        response: analytics_admin.ListDataStreamsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListDataStreamsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListDataStreamsResponse):
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
        self._request = analytics_admin.ListDataStreamsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListDataStreamsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.DataStream]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_streams:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAudiencesPager:
    """A pager for iterating through ``list_audiences`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAudiencesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``audiences`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAudiences`` requests and continue to iterate
    through the ``audiences`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAudiencesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListAudiencesResponse],
        request: analytics_admin.ListAudiencesRequest,
        response: analytics_admin.ListAudiencesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAudiencesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAudiencesResponse):
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
        self._request = analytics_admin.ListAudiencesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListAudiencesResponse]:
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

    def __iter__(self) -> Iterator[audience.Audience]:
        for page in self.pages:
            yield from page.audiences

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAudiencesAsyncPager:
    """A pager for iterating through ``list_audiences`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAudiencesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``audiences`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAudiences`` requests and continue to iterate
    through the ``audiences`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAudiencesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListAudiencesResponse]],
        request: analytics_admin.ListAudiencesRequest,
        response: analytics_admin.ListAudiencesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAudiencesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAudiencesResponse):
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
        self._request = analytics_admin.ListAudiencesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListAudiencesResponse]:
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

    def __aiter__(self) -> AsyncIterator[audience.Audience]:
        async def async_generator():
            async for page in self.pages:
                for response in page.audiences:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSearchAds360LinksPager:
    """A pager for iterating through ``list_search_ads360_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSearchAds360LinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``search_ads_360_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSearchAds360Links`` requests and continue to iterate
    through the ``search_ads_360_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSearchAds360LinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListSearchAds360LinksResponse],
        request: analytics_admin.ListSearchAds360LinksRequest,
        response: analytics_admin.ListSearchAds360LinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSearchAds360LinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSearchAds360LinksResponse):
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
        self._request = analytics_admin.ListSearchAds360LinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListSearchAds360LinksResponse]:
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

    def __iter__(self) -> Iterator[resources.SearchAds360Link]:
        for page in self.pages:
            yield from page.search_ads_360_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSearchAds360LinksAsyncPager:
    """A pager for iterating through ``list_search_ads360_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSearchAds360LinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``search_ads_360_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSearchAds360Links`` requests and continue to iterate
    through the ``search_ads_360_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSearchAds360LinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListSearchAds360LinksResponse]],
        request: analytics_admin.ListSearchAds360LinksRequest,
        response: analytics_admin.ListSearchAds360LinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSearchAds360LinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSearchAds360LinksResponse):
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
        self._request = analytics_admin.ListSearchAds360LinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListSearchAds360LinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.SearchAds360Link]:
        async def async_generator():
            async for page in self.pages:
                for response in page.search_ads_360_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccessBindingsPager:
    """A pager for iterating through ``list_access_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAccessBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``access_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccessBindings`` requests and continue to iterate
    through the ``access_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAccessBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListAccessBindingsResponse],
        request: analytics_admin.ListAccessBindingsRequest,
        response: analytics_admin.ListAccessBindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAccessBindingsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAccessBindingsResponse):
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
        self._request = analytics_admin.ListAccessBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListAccessBindingsResponse]:
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

    def __iter__(self) -> Iterator[resources.AccessBinding]:
        for page in self.pages:
            yield from page.access_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAccessBindingsAsyncPager:
    """A pager for iterating through ``list_access_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAccessBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``access_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccessBindings`` requests and continue to iterate
    through the ``access_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAccessBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListAccessBindingsResponse]],
        request: analytics_admin.ListAccessBindingsRequest,
        response: analytics_admin.ListAccessBindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAccessBindingsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAccessBindingsResponse):
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
        self._request = analytics_admin.ListAccessBindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListAccessBindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.AccessBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.access_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExpandedDataSetsPager:
    """A pager for iterating through ``list_expanded_data_sets`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListExpandedDataSetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``expanded_data_sets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExpandedDataSets`` requests and continue to iterate
    through the ``expanded_data_sets`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListExpandedDataSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListExpandedDataSetsResponse],
        request: analytics_admin.ListExpandedDataSetsRequest,
        response: analytics_admin.ListExpandedDataSetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListExpandedDataSetsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListExpandedDataSetsResponse):
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
        self._request = analytics_admin.ListExpandedDataSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListExpandedDataSetsResponse]:
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

    def __iter__(self) -> Iterator[expanded_data_set.ExpandedDataSet]:
        for page in self.pages:
            yield from page.expanded_data_sets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExpandedDataSetsAsyncPager:
    """A pager for iterating through ``list_expanded_data_sets`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListExpandedDataSetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``expanded_data_sets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExpandedDataSets`` requests and continue to iterate
    through the ``expanded_data_sets`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListExpandedDataSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListExpandedDataSetsResponse]],
        request: analytics_admin.ListExpandedDataSetsRequest,
        response: analytics_admin.ListExpandedDataSetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListExpandedDataSetsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListExpandedDataSetsResponse):
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
        self._request = analytics_admin.ListExpandedDataSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListExpandedDataSetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[expanded_data_set.ExpandedDataSet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.expanded_data_sets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListChannelGroupsPager:
    """A pager for iterating through ``list_channel_groups`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListChannelGroupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``channel_groups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListChannelGroups`` requests and continue to iterate
    through the ``channel_groups`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListChannelGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListChannelGroupsResponse],
        request: analytics_admin.ListChannelGroupsRequest,
        response: analytics_admin.ListChannelGroupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListChannelGroupsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListChannelGroupsResponse):
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
        self._request = analytics_admin.ListChannelGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListChannelGroupsResponse]:
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

    def __iter__(self) -> Iterator[channel_group.ChannelGroup]:
        for page in self.pages:
            yield from page.channel_groups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListChannelGroupsAsyncPager:
    """A pager for iterating through ``list_channel_groups`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListChannelGroupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``channel_groups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListChannelGroups`` requests and continue to iterate
    through the ``channel_groups`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListChannelGroupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListChannelGroupsResponse]],
        request: analytics_admin.ListChannelGroupsRequest,
        response: analytics_admin.ListChannelGroupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListChannelGroupsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListChannelGroupsResponse):
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
        self._request = analytics_admin.ListChannelGroupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListChannelGroupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[channel_group.ChannelGroup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.channel_groups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBigQueryLinksPager:
    """A pager for iterating through ``list_big_query_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListBigQueryLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``bigquery_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBigQueryLinks`` requests and continue to iterate
    through the ``bigquery_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListBigQueryLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListBigQueryLinksResponse],
        request: analytics_admin.ListBigQueryLinksRequest,
        response: analytics_admin.ListBigQueryLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListBigQueryLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListBigQueryLinksResponse):
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
        self._request = analytics_admin.ListBigQueryLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListBigQueryLinksResponse]:
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

    def __iter__(self) -> Iterator[resources.BigQueryLink]:
        for page in self.pages:
            yield from page.bigquery_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBigQueryLinksAsyncPager:
    """A pager for iterating through ``list_big_query_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListBigQueryLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``bigquery_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBigQueryLinks`` requests and continue to iterate
    through the ``bigquery_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListBigQueryLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListBigQueryLinksResponse]],
        request: analytics_admin.ListBigQueryLinksRequest,
        response: analytics_admin.ListBigQueryLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListBigQueryLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListBigQueryLinksResponse):
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
        self._request = analytics_admin.ListBigQueryLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListBigQueryLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.BigQueryLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.bigquery_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAdSenseLinksPager:
    """A pager for iterating through ``list_ad_sense_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAdSenseLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``adsense_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAdSenseLinks`` requests and continue to iterate
    through the ``adsense_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAdSenseLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListAdSenseLinksResponse],
        request: analytics_admin.ListAdSenseLinksRequest,
        response: analytics_admin.ListAdSenseLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAdSenseLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAdSenseLinksResponse):
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
        self._request = analytics_admin.ListAdSenseLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListAdSenseLinksResponse]:
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

    def __iter__(self) -> Iterator[resources.AdSenseLink]:
        for page in self.pages:
            yield from page.adsense_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAdSenseLinksAsyncPager:
    """A pager for iterating through ``list_ad_sense_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListAdSenseLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``adsense_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAdSenseLinks`` requests and continue to iterate
    through the ``adsense_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListAdSenseLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListAdSenseLinksResponse]],
        request: analytics_admin.ListAdSenseLinksRequest,
        response: analytics_admin.ListAdSenseLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListAdSenseLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListAdSenseLinksResponse):
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
        self._request = analytics_admin.ListAdSenseLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListAdSenseLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.AdSenseLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.adsense_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEventCreateRulesPager:
    """A pager for iterating through ``list_event_create_rules`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListEventCreateRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``event_create_rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEventCreateRules`` requests and continue to iterate
    through the ``event_create_rules`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListEventCreateRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListEventCreateRulesResponse],
        request: analytics_admin.ListEventCreateRulesRequest,
        response: analytics_admin.ListEventCreateRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListEventCreateRulesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListEventCreateRulesResponse):
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
        self._request = analytics_admin.ListEventCreateRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListEventCreateRulesResponse]:
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

    def __iter__(self) -> Iterator[event_create_and_edit.EventCreateRule]:
        for page in self.pages:
            yield from page.event_create_rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEventCreateRulesAsyncPager:
    """A pager for iterating through ``list_event_create_rules`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListEventCreateRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``event_create_rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEventCreateRules`` requests and continue to iterate
    through the ``event_create_rules`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListEventCreateRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListEventCreateRulesResponse]],
        request: analytics_admin.ListEventCreateRulesRequest,
        response: analytics_admin.ListEventCreateRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListEventCreateRulesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListEventCreateRulesResponse):
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
        self._request = analytics_admin.ListEventCreateRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListEventCreateRulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[event_create_and_edit.EventCreateRule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.event_create_rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEventEditRulesPager:
    """A pager for iterating through ``list_event_edit_rules`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListEventEditRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``event_edit_rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEventEditRules`` requests and continue to iterate
    through the ``event_edit_rules`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListEventEditRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListEventEditRulesResponse],
        request: analytics_admin.ListEventEditRulesRequest,
        response: analytics_admin.ListEventEditRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListEventEditRulesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListEventEditRulesResponse):
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
        self._request = analytics_admin.ListEventEditRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListEventEditRulesResponse]:
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

    def __iter__(self) -> Iterator[event_create_and_edit.EventEditRule]:
        for page in self.pages:
            yield from page.event_edit_rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEventEditRulesAsyncPager:
    """A pager for iterating through ``list_event_edit_rules`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListEventEditRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``event_edit_rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEventEditRules`` requests and continue to iterate
    through the ``event_edit_rules`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListEventEditRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListEventEditRulesResponse]],
        request: analytics_admin.ListEventEditRulesRequest,
        response: analytics_admin.ListEventEditRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListEventEditRulesRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListEventEditRulesResponse):
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
        self._request = analytics_admin.ListEventEditRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[analytics_admin.ListEventEditRulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[event_create_and_edit.EventEditRule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.event_edit_rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCalculatedMetricsPager:
    """A pager for iterating through ``list_calculated_metrics`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListCalculatedMetricsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``calculated_metrics`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCalculatedMetrics`` requests and continue to iterate
    through the ``calculated_metrics`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListCalculatedMetricsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListCalculatedMetricsResponse],
        request: analytics_admin.ListCalculatedMetricsRequest,
        response: analytics_admin.ListCalculatedMetricsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListCalculatedMetricsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListCalculatedMetricsResponse):
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
        self._request = analytics_admin.ListCalculatedMetricsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListCalculatedMetricsResponse]:
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

    def __iter__(self) -> Iterator[resources.CalculatedMetric]:
        for page in self.pages:
            yield from page.calculated_metrics

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCalculatedMetricsAsyncPager:
    """A pager for iterating through ``list_calculated_metrics`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListCalculatedMetricsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``calculated_metrics`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCalculatedMetrics`` requests and continue to iterate
    through the ``calculated_metrics`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListCalculatedMetricsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[analytics_admin.ListCalculatedMetricsResponse]],
        request: analytics_admin.ListCalculatedMetricsRequest,
        response: analytics_admin.ListCalculatedMetricsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListCalculatedMetricsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListCalculatedMetricsResponse):
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
        self._request = analytics_admin.ListCalculatedMetricsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListCalculatedMetricsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.CalculatedMetric]:
        async def async_generator():
            async for page in self.pages:
                for response in page.calculated_metrics:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRollupPropertySourceLinksPager:
    """A pager for iterating through ``list_rollup_property_source_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rollup_property_source_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRollupPropertySourceLinks`` requests and continue to iterate
    through the ``rollup_property_source_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListRollupPropertySourceLinksResponse],
        request: analytics_admin.ListRollupPropertySourceLinksRequest,
        response: analytics_admin.ListRollupPropertySourceLinksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksResponse):
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
        self._request = analytics_admin.ListRollupPropertySourceLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListRollupPropertySourceLinksResponse]:
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

    def __iter__(self) -> Iterator[resources.RollupPropertySourceLink]:
        for page in self.pages:
            yield from page.rollup_property_source_links

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRollupPropertySourceLinksAsyncPager:
    """A pager for iterating through ``list_rollup_property_source_links`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rollup_property_source_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRollupPropertySourceLinks`` requests and continue to iterate
    through the ``rollup_property_source_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.ListRollupPropertySourceLinksResponse]
        ],
        request: analytics_admin.ListRollupPropertySourceLinksRequest,
        response: analytics_admin.ListRollupPropertySourceLinksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListRollupPropertySourceLinksResponse):
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
        self._request = analytics_admin.ListRollupPropertySourceLinksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListRollupPropertySourceLinksResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.RollupPropertySourceLink]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rollup_property_source_links:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSubpropertyEventFiltersPager:
    """A pager for iterating through ``list_subproperty_event_filters`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``subproperty_event_filters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSubpropertyEventFilters`` requests and continue to iterate
    through the ``subproperty_event_filters`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListSubpropertyEventFiltersResponse],
        request: analytics_admin.ListSubpropertyEventFiltersRequest,
        response: analytics_admin.ListSubpropertyEventFiltersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersResponse):
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
        self._request = analytics_admin.ListSubpropertyEventFiltersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListSubpropertyEventFiltersResponse]:
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

    def __iter__(self) -> Iterator[subproperty_event_filter.SubpropertyEventFilter]:
        for page in self.pages:
            yield from page.subproperty_event_filters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSubpropertyEventFiltersAsyncPager:
    """A pager for iterating through ``list_subproperty_event_filters`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``subproperty_event_filters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSubpropertyEventFilters`` requests and continue to iterate
    through the ``subproperty_event_filters`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.ListSubpropertyEventFiltersResponse]
        ],
        request: analytics_admin.ListSubpropertyEventFiltersRequest,
        response: analytics_admin.ListSubpropertyEventFiltersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSubpropertyEventFiltersResponse):
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
        self._request = analytics_admin.ListSubpropertyEventFiltersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListSubpropertyEventFiltersResponse]:
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
    ) -> AsyncIterator[subproperty_event_filter.SubpropertyEventFilter]:
        async def async_generator():
            async for page in self.pages:
                for response in page.subproperty_event_filters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReportingDataAnnotationsPager:
    """A pager for iterating through ``list_reporting_data_annotations`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``reporting_data_annotations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReportingDataAnnotations`` requests and continue to iterate
    through the ``reporting_data_annotations`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListReportingDataAnnotationsResponse],
        request: analytics_admin.ListReportingDataAnnotationsRequest,
        response: analytics_admin.ListReportingDataAnnotationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsResponse):
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
        self._request = analytics_admin.ListReportingDataAnnotationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListReportingDataAnnotationsResponse]:
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

    def __iter__(self) -> Iterator[resources.ReportingDataAnnotation]:
        for page in self.pages:
            yield from page.reporting_data_annotations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReportingDataAnnotationsAsyncPager:
    """A pager for iterating through ``list_reporting_data_annotations`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``reporting_data_annotations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReportingDataAnnotations`` requests and continue to iterate
    through the ``reporting_data_annotations`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.ListReportingDataAnnotationsResponse]
        ],
        request: analytics_admin.ListReportingDataAnnotationsRequest,
        response: analytics_admin.ListReportingDataAnnotationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListReportingDataAnnotationsResponse):
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
        self._request = analytics_admin.ListReportingDataAnnotationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListReportingDataAnnotationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.ReportingDataAnnotation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.reporting_data_annotations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSubpropertySyncConfigsPager:
    """A pager for iterating through ``list_subproperty_sync_configs`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``subproperty_sync_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSubpropertySyncConfigs`` requests and continue to iterate
    through the ``subproperty_sync_configs`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., analytics_admin.ListSubpropertySyncConfigsResponse],
        request: analytics_admin.ListSubpropertySyncConfigsRequest,
        response: analytics_admin.ListSubpropertySyncConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsResponse):
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
        self._request = analytics_admin.ListSubpropertySyncConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[analytics_admin.ListSubpropertySyncConfigsResponse]:
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

    def __iter__(self) -> Iterator[resources.SubpropertySyncConfig]:
        for page in self.pages:
            yield from page.subproperty_sync_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSubpropertySyncConfigsAsyncPager:
    """A pager for iterating through ``list_subproperty_sync_configs`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``subproperty_sync_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSubpropertySyncConfigs`` requests and continue to iterate
    through the ``subproperty_sync_configs`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[analytics_admin.ListSubpropertySyncConfigsResponse]
        ],
        request: analytics_admin.ListSubpropertySyncConfigsRequest,
        response: analytics_admin.ListSubpropertySyncConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsRequest):
                The initial request object.
            response (google.analytics.admin_v1alpha.types.ListSubpropertySyncConfigsResponse):
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
        self._request = analytics_admin.ListSubpropertySyncConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[analytics_admin.ListSubpropertySyncConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.SubpropertySyncConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.subproperty_sync_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
