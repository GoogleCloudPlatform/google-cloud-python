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

from google.analytics.admin_v1beta.types import analytics_admin, resources


class ListAccountsPager:
    """A pager for iterating through ``list_accounts`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1beta.types.ListAccountsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``accounts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccounts`` requests and continue to iterate
    through the ``accounts`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListAccountsResponse`
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
            request (google.analytics.admin_v1beta.types.ListAccountsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListAccountsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListAccountsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``accounts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccounts`` requests and continue to iterate
    through the ``accounts`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListAccountsResponse`
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
            request (google.analytics.admin_v1beta.types.ListAccountsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListAccountsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListAccountSummariesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``account_summaries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAccountSummaries`` requests and continue to iterate
    through the ``account_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListAccountSummariesResponse`
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
            request (google.analytics.admin_v1beta.types.ListAccountSummariesRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListAccountSummariesResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListAccountSummariesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``account_summaries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAccountSummaries`` requests and continue to iterate
    through the ``account_summaries`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListAccountSummariesResponse`
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
            request (google.analytics.admin_v1beta.types.ListAccountSummariesRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListAccountSummariesResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListPropertiesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``properties`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProperties`` requests and continue to iterate
    through the ``properties`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListPropertiesResponse`
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
            request (google.analytics.admin_v1beta.types.ListPropertiesRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListPropertiesResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListPropertiesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``properties`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProperties`` requests and continue to iterate
    through the ``properties`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListPropertiesResponse`
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
            request (google.analytics.admin_v1beta.types.ListPropertiesRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListPropertiesResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListFirebaseLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``firebase_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFirebaseLinks`` requests and continue to iterate
    through the ``firebase_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListFirebaseLinksResponse`
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
            request (google.analytics.admin_v1beta.types.ListFirebaseLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListFirebaseLinksResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListFirebaseLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``firebase_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFirebaseLinks`` requests and continue to iterate
    through the ``firebase_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListFirebaseLinksResponse`
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
            request (google.analytics.admin_v1beta.types.ListFirebaseLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListFirebaseLinksResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListGoogleAdsLinksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``google_ads_links`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoogleAdsLinks`` requests and continue to iterate
    through the ``google_ads_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListGoogleAdsLinksResponse`
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
            request (google.analytics.admin_v1beta.types.ListGoogleAdsLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListGoogleAdsLinksResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListGoogleAdsLinksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``google_ads_links`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoogleAdsLinks`` requests and continue to iterate
    through the ``google_ads_links`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListGoogleAdsLinksResponse`
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
            request (google.analytics.admin_v1beta.types.ListGoogleAdsLinksRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListGoogleAdsLinksResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``measurement_protocol_secrets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMeasurementProtocolSecrets`` requests and continue to iterate
    through the ``measurement_protocol_secrets`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsResponse`
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
            request (google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``measurement_protocol_secrets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMeasurementProtocolSecrets`` requests and continue to iterate
    through the ``measurement_protocol_secrets`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsResponse`
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
            request (google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListMeasurementProtocolSecretsResponse):
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


class SearchChangeHistoryEventsPager:
    """A pager for iterating through ``search_change_history_events`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1beta.types.SearchChangeHistoryEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``change_history_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchChangeHistoryEvents`` requests and continue to iterate
    through the ``change_history_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.SearchChangeHistoryEventsResponse`
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
            request (google.analytics.admin_v1beta.types.SearchChangeHistoryEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.SearchChangeHistoryEventsResponse):
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
    :class:`google.analytics.admin_v1beta.types.SearchChangeHistoryEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``change_history_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchChangeHistoryEvents`` requests and continue to iterate
    through the ``change_history_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.SearchChangeHistoryEventsResponse`
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
            request (google.analytics.admin_v1beta.types.SearchChangeHistoryEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.SearchChangeHistoryEventsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListConversionEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversion_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversionEvents`` requests and continue to iterate
    through the ``conversion_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListConversionEventsResponse`
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
            request (google.analytics.admin_v1beta.types.ListConversionEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListConversionEventsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListConversionEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversion_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversionEvents`` requests and continue to iterate
    through the ``conversion_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListConversionEventsResponse`
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
            request (google.analytics.admin_v1beta.types.ListConversionEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListConversionEventsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListKeyEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``key_events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListKeyEvents`` requests and continue to iterate
    through the ``key_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListKeyEventsResponse`
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
            request (google.analytics.admin_v1beta.types.ListKeyEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListKeyEventsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListKeyEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``key_events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListKeyEvents`` requests and continue to iterate
    through the ``key_events`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListKeyEventsResponse`
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
            request (google.analytics.admin_v1beta.types.ListKeyEventsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListKeyEventsResponse):
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


class ListCustomDimensionsPager:
    """A pager for iterating through ``list_custom_dimensions`` requests.

    This class thinly wraps an initial
    :class:`google.analytics.admin_v1beta.types.ListCustomDimensionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_dimensions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomDimensions`` requests and continue to iterate
    through the ``custom_dimensions`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListCustomDimensionsResponse`
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
            request (google.analytics.admin_v1beta.types.ListCustomDimensionsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListCustomDimensionsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListCustomDimensionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_dimensions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomDimensions`` requests and continue to iterate
    through the ``custom_dimensions`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListCustomDimensionsResponse`
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
            request (google.analytics.admin_v1beta.types.ListCustomDimensionsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListCustomDimensionsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListCustomMetricsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_metrics`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomMetrics`` requests and continue to iterate
    through the ``custom_metrics`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListCustomMetricsResponse`
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
            request (google.analytics.admin_v1beta.types.ListCustomMetricsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListCustomMetricsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListCustomMetricsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_metrics`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomMetrics`` requests and continue to iterate
    through the ``custom_metrics`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListCustomMetricsResponse`
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
            request (google.analytics.admin_v1beta.types.ListCustomMetricsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListCustomMetricsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListDataStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataStreams`` requests and continue to iterate
    through the ``data_streams`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListDataStreamsResponse`
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
            request (google.analytics.admin_v1beta.types.ListDataStreamsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListDataStreamsResponse):
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
    :class:`google.analytics.admin_v1beta.types.ListDataStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataStreams`` requests and continue to iterate
    through the ``data_streams`` field on the
    corresponding responses.

    All the usual :class:`google.analytics.admin_v1beta.types.ListDataStreamsResponse`
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
            request (google.analytics.admin_v1beta.types.ListDataStreamsRequest):
                The initial request object.
            response (google.analytics.admin_v1beta.types.ListDataStreamsResponse):
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
