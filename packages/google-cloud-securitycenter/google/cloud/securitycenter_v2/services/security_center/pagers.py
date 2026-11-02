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

from google.cloud.securitycenter_v2.types import (
    attack_path,
    bigquery_export,
    mute_config,
    notification_config,
    resource_value_config,
    securitycenter_service,
    source,
    valued_resource,
)


class GroupFindingsPager:
    """A pager for iterating through ``group_findings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.GroupFindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``group_by_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``GroupFindings`` requests and continue to iterate
    through the ``group_by_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.GroupFindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.GroupFindingsResponse],
        request: securitycenter_service.GroupFindingsRequest,
        response: securitycenter_service.GroupFindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.GroupFindingsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.GroupFindingsResponse):
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
        self._request = securitycenter_service.GroupFindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.GroupFindingsResponse]:
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

    def __iter__(self) -> Iterator[securitycenter_service.GroupResult]:
        for page in self.pages:
            yield from page.group_by_results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class GroupFindingsAsyncPager:
    """A pager for iterating through ``group_findings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.GroupFindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``group_by_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``GroupFindings`` requests and continue to iterate
    through the ``group_by_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.GroupFindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[securitycenter_service.GroupFindingsResponse]],
        request: securitycenter_service.GroupFindingsRequest,
        response: securitycenter_service.GroupFindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.GroupFindingsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.GroupFindingsResponse):
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
        self._request = securitycenter_service.GroupFindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[securitycenter_service.GroupFindingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[securitycenter_service.GroupResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.group_by_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAttackPathsPager:
    """A pager for iterating through ``list_attack_paths`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListAttackPathsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``attack_paths`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAttackPaths`` requests and continue to iterate
    through the ``attack_paths`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListAttackPathsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListAttackPathsResponse],
        request: securitycenter_service.ListAttackPathsRequest,
        response: securitycenter_service.ListAttackPathsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListAttackPathsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListAttackPathsResponse):
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
        self._request = securitycenter_service.ListAttackPathsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.ListAttackPathsResponse]:
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

    def __iter__(self) -> Iterator[attack_path.AttackPath]:
        for page in self.pages:
            yield from page.attack_paths

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAttackPathsAsyncPager:
    """A pager for iterating through ``list_attack_paths`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListAttackPathsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``attack_paths`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAttackPaths`` requests and continue to iterate
    through the ``attack_paths`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListAttackPathsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[securitycenter_service.ListAttackPathsResponse]
        ],
        request: securitycenter_service.ListAttackPathsRequest,
        response: securitycenter_service.ListAttackPathsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListAttackPathsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListAttackPathsResponse):
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
        self._request = securitycenter_service.ListAttackPathsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[securitycenter_service.ListAttackPathsResponse]:
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

    def __aiter__(self) -> AsyncIterator[attack_path.AttackPath]:
        async def async_generator():
            async for page in self.pages:
                for response in page.attack_paths:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBigQueryExportsPager:
    """A pager for iterating through ``list_big_query_exports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``big_query_exports`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBigQueryExports`` requests and continue to iterate
    through the ``big_query_exports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListBigQueryExportsResponse],
        request: securitycenter_service.ListBigQueryExportsRequest,
        response: securitycenter_service.ListBigQueryExportsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListBigQueryExportsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse):
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
        self._request = securitycenter_service.ListBigQueryExportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.ListBigQueryExportsResponse]:
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

    def __iter__(self) -> Iterator[bigquery_export.BigQueryExport]:
        for page in self.pages:
            yield from page.big_query_exports

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBigQueryExportsAsyncPager:
    """A pager for iterating through ``list_big_query_exports`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``big_query_exports`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBigQueryExports`` requests and continue to iterate
    through the ``big_query_exports`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[securitycenter_service.ListBigQueryExportsResponse]
        ],
        request: securitycenter_service.ListBigQueryExportsRequest,
        response: securitycenter_service.ListBigQueryExportsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListBigQueryExportsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse):
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
        self._request = securitycenter_service.ListBigQueryExportsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[securitycenter_service.ListBigQueryExportsResponse]:
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

    def __aiter__(self) -> AsyncIterator[bigquery_export.BigQueryExport]:
        async def async_generator():
            async for page in self.pages:
                for response in page.big_query_exports:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFindingsPager:
    """A pager for iterating through ``list_findings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListFindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``list_findings_results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFindings`` requests and continue to iterate
    through the ``list_findings_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListFindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListFindingsResponse],
        request: securitycenter_service.ListFindingsRequest,
        response: securitycenter_service.ListFindingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListFindingsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListFindingsResponse):
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
        self._request = securitycenter_service.ListFindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.ListFindingsResponse]:
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
    ) -> Iterator[securitycenter_service.ListFindingsResponse.ListFindingsResult]:
        for page in self.pages:
            yield from page.list_findings_results

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFindingsAsyncPager:
    """A pager for iterating through ``list_findings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListFindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``list_findings_results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFindings`` requests and continue to iterate
    through the ``list_findings_results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListFindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[securitycenter_service.ListFindingsResponse]],
        request: securitycenter_service.ListFindingsRequest,
        response: securitycenter_service.ListFindingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListFindingsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListFindingsResponse):
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
        self._request = securitycenter_service.ListFindingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[securitycenter_service.ListFindingsResponse]:
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
    ) -> AsyncIterator[securitycenter_service.ListFindingsResponse.ListFindingsResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.list_findings_results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMuteConfigsPager:
    """A pager for iterating through ``list_mute_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListMuteConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``mute_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMuteConfigs`` requests and continue to iterate
    through the ``mute_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListMuteConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListMuteConfigsResponse],
        request: securitycenter_service.ListMuteConfigsRequest,
        response: securitycenter_service.ListMuteConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListMuteConfigsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListMuteConfigsResponse):
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
        self._request = securitycenter_service.ListMuteConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.ListMuteConfigsResponse]:
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

    def __iter__(self) -> Iterator[mute_config.MuteConfig]:
        for page in self.pages:
            yield from page.mute_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMuteConfigsAsyncPager:
    """A pager for iterating through ``list_mute_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListMuteConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``mute_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMuteConfigs`` requests and continue to iterate
    through the ``mute_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListMuteConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[securitycenter_service.ListMuteConfigsResponse]
        ],
        request: securitycenter_service.ListMuteConfigsRequest,
        response: securitycenter_service.ListMuteConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListMuteConfigsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListMuteConfigsResponse):
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
        self._request = securitycenter_service.ListMuteConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[securitycenter_service.ListMuteConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[mute_config.MuteConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.mute_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNotificationConfigsPager:
    """A pager for iterating through ``list_notification_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``notification_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNotificationConfigs`` requests and continue to iterate
    through the ``notification_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListNotificationConfigsResponse],
        request: securitycenter_service.ListNotificationConfigsRequest,
        response: securitycenter_service.ListNotificationConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListNotificationConfigsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse):
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
        self._request = securitycenter_service.ListNotificationConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.ListNotificationConfigsResponse]:
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

    def __iter__(self) -> Iterator[notification_config.NotificationConfig]:
        for page in self.pages:
            yield from page.notification_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNotificationConfigsAsyncPager:
    """A pager for iterating through ``list_notification_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``notification_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNotificationConfigs`` requests and continue to iterate
    through the ``notification_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[securitycenter_service.ListNotificationConfigsResponse]
        ],
        request: securitycenter_service.ListNotificationConfigsRequest,
        response: securitycenter_service.ListNotificationConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListNotificationConfigsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse):
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
        self._request = securitycenter_service.ListNotificationConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[securitycenter_service.ListNotificationConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[notification_config.NotificationConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.notification_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListResourceValueConfigsPager:
    """A pager for iterating through ``list_resource_value_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``resource_value_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListResourceValueConfigs`` requests and continue to iterate
    through the ``resource_value_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListResourceValueConfigsResponse],
        request: securitycenter_service.ListResourceValueConfigsRequest,
        response: securitycenter_service.ListResourceValueConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListResourceValueConfigsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse):
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
        self._request = securitycenter_service.ListResourceValueConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[securitycenter_service.ListResourceValueConfigsResponse]:
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

    def __iter__(self) -> Iterator[resource_value_config.ResourceValueConfig]:
        for page in self.pages:
            yield from page.resource_value_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListResourceValueConfigsAsyncPager:
    """A pager for iterating through ``list_resource_value_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``resource_value_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListResourceValueConfigs`` requests and continue to iterate
    through the ``resource_value_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[securitycenter_service.ListResourceValueConfigsResponse]
        ],
        request: securitycenter_service.ListResourceValueConfigsRequest,
        response: securitycenter_service.ListResourceValueConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListResourceValueConfigsRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse):
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
        self._request = securitycenter_service.ListResourceValueConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[securitycenter_service.ListResourceValueConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resource_value_config.ResourceValueConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.resource_value_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSourcesPager:
    """A pager for iterating through ``list_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListSourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``sources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSources`` requests and continue to iterate
    through the ``sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListSourcesResponse],
        request: securitycenter_service.ListSourcesRequest,
        response: securitycenter_service.ListSourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListSourcesRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListSourcesResponse):
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
        self._request = securitycenter_service.ListSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.ListSourcesResponse]:
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

    def __iter__(self) -> Iterator[source.Source]:
        for page in self.pages:
            yield from page.sources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSourcesAsyncPager:
    """A pager for iterating through ``list_sources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListSourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``sources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSources`` requests and continue to iterate
    through the ``sources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListSourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[securitycenter_service.ListSourcesResponse]],
        request: securitycenter_service.ListSourcesRequest,
        response: securitycenter_service.ListSourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListSourcesRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListSourcesResponse):
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
        self._request = securitycenter_service.ListSourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[securitycenter_service.ListSourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[source.Source]:
        async def async_generator():
            async for page in self.pages:
                for response in page.sources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListValuedResourcesPager:
    """A pager for iterating through ``list_valued_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListValuedResourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``valued_resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListValuedResources`` requests and continue to iterate
    through the ``valued_resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListValuedResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., securitycenter_service.ListValuedResourcesResponse],
        request: securitycenter_service.ListValuedResourcesRequest,
        response: securitycenter_service.ListValuedResourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListValuedResourcesRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListValuedResourcesResponse):
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
        self._request = securitycenter_service.ListValuedResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[securitycenter_service.ListValuedResourcesResponse]:
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

    def __iter__(self) -> Iterator[valued_resource.ValuedResource]:
        for page in self.pages:
            yield from page.valued_resources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListValuedResourcesAsyncPager:
    """A pager for iterating through ``list_valued_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycenter_v2.types.ListValuedResourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``valued_resources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListValuedResources`` requests and continue to iterate
    through the ``valued_resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycenter_v2.types.ListValuedResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[securitycenter_service.ListValuedResourcesResponse]
        ],
        request: securitycenter_service.ListValuedResourcesRequest,
        response: securitycenter_service.ListValuedResourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycenter_v2.types.ListValuedResourcesRequest):
                The initial request object.
            response (google.cloud.securitycenter_v2.types.ListValuedResourcesResponse):
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
        self._request = securitycenter_service.ListValuedResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[securitycenter_service.ListValuedResourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[valued_resource.ValuedResource]:
        async def async_generator():
            async for page in self.pages:
                for response in page.valued_resources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
