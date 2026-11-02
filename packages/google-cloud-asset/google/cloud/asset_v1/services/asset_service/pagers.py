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

from google.cloud.asset_v1.types import asset_service, assets


class ListAssetsPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.ListAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., asset_service.ListAssetsResponse],
        request: asset_service.ListAssetsRequest,
        response: asset_service.ListAssetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.ListAssetsResponse):
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
        self._request = asset_service.ListAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.ListAssetsResponse]:
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

    def __iter__(self) -> Iterator[assets.Asset]:
        for page in self.pages:
            yield from page.assets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAssetsAsyncPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.ListAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[asset_service.ListAssetsResponse]],
        request: asset_service.ListAssetsRequest,
        response: asset_service.ListAssetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.ListAssetsResponse):
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
        self._request = asset_service.ListAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.ListAssetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[assets.Asset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAllResourcesPager:
    """A pager for iterating through ``search_all_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAllResources`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., asset_service.SearchAllResourcesResponse],
        request: asset_service.SearchAllResourcesRequest,
        response: asset_service.SearchAllResourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllResourcesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllResourcesResponse):
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
        self._request = asset_service.SearchAllResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.SearchAllResourcesResponse]:
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

    def __iter__(self) -> Iterator[assets.ResourceSearchResult]:
        for page in self.pages:
            yield from page.results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAllResourcesAsyncPager:
    """A pager for iterating through ``search_all_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAllResources`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[asset_service.SearchAllResourcesResponse]],
        request: asset_service.SearchAllResourcesRequest,
        response: asset_service.SearchAllResourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllResourcesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllResourcesResponse):
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
        self._request = asset_service.SearchAllResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.SearchAllResourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[assets.ResourceSearchResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAllIamPoliciesPager:
    """A pager for iterating through ``search_all_iam_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAllIamPolicies`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., asset_service.SearchAllIamPoliciesResponse],
        request: asset_service.SearchAllIamPoliciesRequest,
        response: asset_service.SearchAllIamPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllIamPoliciesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllIamPoliciesResponse):
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
        self._request = asset_service.SearchAllIamPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.SearchAllIamPoliciesResponse]:
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

    def __iter__(self) -> Iterator[assets.IamPolicySearchResult]:
        for page in self.pages:
            yield from page.results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchAllIamPoliciesAsyncPager:
    """A pager for iterating through ``search_all_iam_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAllIamPolicies`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[asset_service.SearchAllIamPoliciesResponse]],
        request: asset_service.SearchAllIamPoliciesRequest,
        response: asset_service.SearchAllIamPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllIamPoliciesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllIamPoliciesResponse):
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
        self._request = asset_service.SearchAllIamPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.SearchAllIamPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[assets.IamPolicySearchResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSavedQueriesPager:
    """A pager for iterating through ``list_saved_queries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.ListSavedQueriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``saved_queries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSavedQueries`` requests and continue to iterate
    through the ``saved_queries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.ListSavedQueriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., asset_service.ListSavedQueriesResponse],
        request: asset_service.ListSavedQueriesRequest,
        response: asset_service.ListSavedQueriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.ListSavedQueriesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.ListSavedQueriesResponse):
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
        self._request = asset_service.ListSavedQueriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.ListSavedQueriesResponse]:
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

    def __iter__(self) -> Iterator[asset_service.SavedQuery]:
        for page in self.pages:
            yield from page.saved_queries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSavedQueriesAsyncPager:
    """A pager for iterating through ``list_saved_queries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.ListSavedQueriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``saved_queries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSavedQueries`` requests and continue to iterate
    through the ``saved_queries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.ListSavedQueriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[asset_service.ListSavedQueriesResponse]],
        request: asset_service.ListSavedQueriesRequest,
        response: asset_service.ListSavedQueriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.ListSavedQueriesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.ListSavedQueriesResponse):
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
        self._request = asset_service.ListSavedQueriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.ListSavedQueriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[asset_service.SavedQuery]:
        async def async_generator():
            async for page in self.pages:
                for response in page.saved_queries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AnalyzeOrgPoliciesPager:
    """A pager for iterating through ``analyze_org_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``org_policy_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``AnalyzeOrgPolicies`` requests and continue to iterate
    through the ``org_policy_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., asset_service.AnalyzeOrgPoliciesResponse],
        request: asset_service.AnalyzeOrgPoliciesRequest,
        response: asset_service.AnalyzeOrgPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.AnalyzeOrgPoliciesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse):
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
        self._request = asset_service.AnalyzeOrgPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.AnalyzeOrgPoliciesResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[asset_service.AnalyzeOrgPoliciesResponse.OrgPolicyResult]:
        for page in self.pages:
            yield from page.org_policy_results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AnalyzeOrgPoliciesAsyncPager:
    """A pager for iterating through ``analyze_org_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``org_policy_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``AnalyzeOrgPolicies`` requests and continue to iterate
    through the ``org_policy_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[asset_service.AnalyzeOrgPoliciesResponse]],
        request: asset_service.AnalyzeOrgPoliciesRequest,
        response: asset_service.AnalyzeOrgPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.AnalyzeOrgPoliciesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse):
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
        self._request = asset_service.AnalyzeOrgPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.AnalyzeOrgPoliciesResponse]:
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
    ) -> AsyncIterator[asset_service.AnalyzeOrgPoliciesResponse.OrgPolicyResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.org_policy_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AnalyzeOrgPolicyGovernedContainersPager:
    """A pager for iterating through ``analyze_org_policy_governed_containers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``governed_containers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``AnalyzeOrgPolicyGovernedContainers`` requests and continue to iterate
    through the ``governed_containers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., asset_service.AnalyzeOrgPolicyGovernedContainersResponse],
        request: asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        response: asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse):
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
        self._request = asset_service.AnalyzeOrgPolicyGovernedContainersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[asset_service.AnalyzeOrgPolicyGovernedContainersResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[
        asset_service.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer
    ]:
        for page in self.pages:
            yield from page.governed_containers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AnalyzeOrgPolicyGovernedContainersAsyncPager:
    """A pager for iterating through ``analyze_org_policy_governed_containers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``governed_containers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``AnalyzeOrgPolicyGovernedContainers`` requests and continue to iterate
    through the ``governed_containers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[asset_service.AnalyzeOrgPolicyGovernedContainersResponse]
        ],
        request: asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        response: asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse):
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
        self._request = asset_service.AnalyzeOrgPolicyGovernedContainersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[asset_service.AnalyzeOrgPolicyGovernedContainersResponse]:
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
    ) -> AsyncIterator[
        asset_service.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.governed_containers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AnalyzeOrgPolicyGovernedAssetsPager:
    """A pager for iterating through ``analyze_org_policy_governed_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``governed_assets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``AnalyzeOrgPolicyGovernedAssets`` requests and continue to iterate
    through the ``governed_assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., asset_service.AnalyzeOrgPolicyGovernedAssetsResponse],
        request: asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        response: asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse):
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
        self._request = asset_service.AnalyzeOrgPolicyGovernedAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.AnalyzeOrgPolicyGovernedAssetsResponse]:
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

    def __iter__(
        self,
    ) -> Iterator[asset_service.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset]:
        for page in self.pages:
            yield from page.governed_assets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class AnalyzeOrgPolicyGovernedAssetsAsyncPager:
    """A pager for iterating through ``analyze_org_policy_governed_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``governed_assets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``AnalyzeOrgPolicyGovernedAssets`` requests and continue to iterate
    through the ``governed_assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[asset_service.AnalyzeOrgPolicyGovernedAssetsResponse]
        ],
        request: asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        response: asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse):
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
        self._request = asset_service.AnalyzeOrgPolicyGovernedAssetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[asset_service.AnalyzeOrgPolicyGovernedAssetsResponse]:
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
    ) -> AsyncIterator[
        asset_service.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.governed_assets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
