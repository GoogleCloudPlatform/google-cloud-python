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

from google.cloud.designcenter_v1.types import (
    assessment,
    authoring,
    authoring_messages,
    best_practices,
    best_practices_messages,
    catalog_management,
    catalog_management_messages,
    deployment_messages,
    deployment_resources,
    sharing,
    sharing_messages,
)


class ListSpacesPager:
    """A pager for iterating through ``list_spaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSpacesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``spaces`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSpaces`` requests and continue to iterate
    through the ``spaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSpacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog_management_messages.ListSpacesResponse],
        request: catalog_management_messages.ListSpacesRequest,
        response: catalog_management_messages.ListSpacesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSpacesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSpacesResponse):
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
        self._request = catalog_management_messages.ListSpacesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[catalog_management_messages.ListSpacesResponse]:
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

    def __iter__(self) -> Iterator[catalog_management.Space]:
        for page in self.pages:
            yield from page.spaces

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSpacesAsyncPager:
    """A pager for iterating through ``list_spaces`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSpacesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``spaces`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSpaces`` requests and continue to iterate
    through the ``spaces`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSpacesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[catalog_management_messages.ListSpacesResponse]
        ],
        request: catalog_management_messages.ListSpacesRequest,
        response: catalog_management_messages.ListSpacesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSpacesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSpacesResponse):
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
        self._request = catalog_management_messages.ListSpacesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[catalog_management_messages.ListSpacesResponse]:
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

    def __aiter__(self) -> AsyncIterator[catalog_management.Space]:
        async def async_generator():
            async for page in self.pages:
                for response in page.spaces:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationTemplatesPager:
    """A pager for iterating through ``list_application_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationTemplatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``application_templates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApplicationTemplates`` requests and continue to iterate
    through the ``application_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., authoring_messages.ListApplicationTemplatesResponse],
        request: authoring_messages.ListApplicationTemplatesRequest,
        response: authoring_messages.ListApplicationTemplatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationTemplatesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationTemplatesResponse):
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
        self._request = authoring_messages.ListApplicationTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[authoring_messages.ListApplicationTemplatesResponse]:
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

    def __iter__(self) -> Iterator[authoring.ApplicationTemplate]:
        for page in self.pages:
            yield from page.application_templates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationTemplatesAsyncPager:
    """A pager for iterating through ``list_application_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationTemplatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``application_templates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApplicationTemplates`` requests and continue to iterate
    through the ``application_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[authoring_messages.ListApplicationTemplatesResponse]
        ],
        request: authoring_messages.ListApplicationTemplatesRequest,
        response: authoring_messages.ListApplicationTemplatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationTemplatesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationTemplatesResponse):
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
        self._request = authoring_messages.ListApplicationTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[authoring_messages.ListApplicationTemplatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[authoring.ApplicationTemplate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.application_templates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListComponentsPager:
    """A pager for iterating through ``list_components`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListComponentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``components`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListComponents`` requests and continue to iterate
    through the ``components`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListComponentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., authoring_messages.ListComponentsResponse],
        request: authoring_messages.ListComponentsRequest,
        response: authoring_messages.ListComponentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListComponentsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListComponentsResponse):
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
        self._request = authoring_messages.ListComponentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[authoring_messages.ListComponentsResponse]:
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

    def __iter__(self) -> Iterator[authoring.Component]:
        for page in self.pages:
            yield from page.components

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListComponentsAsyncPager:
    """A pager for iterating through ``list_components`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListComponentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``components`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListComponents`` requests and continue to iterate
    through the ``components`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListComponentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[authoring_messages.ListComponentsResponse]],
        request: authoring_messages.ListComponentsRequest,
        response: authoring_messages.ListComponentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListComponentsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListComponentsResponse):
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
        self._request = authoring_messages.ListComponentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[authoring_messages.ListComponentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[authoring.Component]:
        async def async_generator():
            async for page in self.pages:
                for response in page.components:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionsPager:
    """A pager for iterating through ``list_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., authoring_messages.ListConnectionsResponse],
        request: authoring_messages.ListConnectionsRequest,
        response: authoring_messages.ListConnectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListConnectionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListConnectionsResponse):
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
        self._request = authoring_messages.ListConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[authoring_messages.ListConnectionsResponse]:
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

    def __iter__(self) -> Iterator[authoring.Connection]:
        for page in self.pages:
            yield from page.connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConnectionsAsyncPager:
    """A pager for iterating through ``list_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConnections`` requests and continue to iterate
    through the ``connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[authoring_messages.ListConnectionsResponse]],
        request: authoring_messages.ListConnectionsRequest,
        response: authoring_messages.ListConnectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListConnectionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListConnectionsResponse):
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
        self._request = authoring_messages.ListConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[authoring_messages.ListConnectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[authoring.Connection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationTemplateRevisionsPager:
    """A pager for iterating through ``list_application_template_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``application_template_revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApplicationTemplateRevisions`` requests and continue to iterate
    through the ``application_template_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., authoring_messages.ListApplicationTemplateRevisionsResponse
        ],
        request: authoring_messages.ListApplicationTemplateRevisionsRequest,
        response: authoring_messages.ListApplicationTemplateRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsResponse):
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
        self._request = authoring_messages.ListApplicationTemplateRevisionsRequest(
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
    ) -> Iterator[authoring_messages.ListApplicationTemplateRevisionsResponse]:
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

    def __iter__(self) -> Iterator[authoring.ApplicationTemplateRevision]:
        for page in self.pages:
            yield from page.application_template_revisions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationTemplateRevisionsAsyncPager:
    """A pager for iterating through ``list_application_template_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``application_template_revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApplicationTemplateRevisions`` requests and continue to iterate
    through the ``application_template_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[authoring_messages.ListApplicationTemplateRevisionsResponse]
        ],
        request: authoring_messages.ListApplicationTemplateRevisionsRequest,
        response: authoring_messages.ListApplicationTemplateRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsResponse):
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
        self._request = authoring_messages.ListApplicationTemplateRevisionsRequest(
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
    ) -> AsyncIterator[authoring_messages.ListApplicationTemplateRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[authoring.ApplicationTemplateRevision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.application_template_revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCatalogsPager:
    """A pager for iterating through ``list_catalogs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListCatalogsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``catalogs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCatalogs`` requests and continue to iterate
    through the ``catalogs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListCatalogsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog_management_messages.ListCatalogsResponse],
        request: catalog_management_messages.ListCatalogsRequest,
        response: catalog_management_messages.ListCatalogsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListCatalogsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListCatalogsResponse):
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
        self._request = catalog_management_messages.ListCatalogsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[catalog_management_messages.ListCatalogsResponse]:
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

    def __iter__(self) -> Iterator[catalog_management.Catalog]:
        for page in self.pages:
            yield from page.catalogs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCatalogsAsyncPager:
    """A pager for iterating through ``list_catalogs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListCatalogsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``catalogs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCatalogs`` requests and continue to iterate
    through the ``catalogs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListCatalogsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[catalog_management_messages.ListCatalogsResponse]
        ],
        request: catalog_management_messages.ListCatalogsRequest,
        response: catalog_management_messages.ListCatalogsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListCatalogsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListCatalogsResponse):
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
        self._request = catalog_management_messages.ListCatalogsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[catalog_management_messages.ListCatalogsResponse]:
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

    def __aiter__(self) -> AsyncIterator[catalog_management.Catalog]:
        async def async_generator():
            async for page in self.pages:
                for response in page.catalogs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCatalogTemplatesPager:
    """A pager for iterating through ``list_catalog_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListCatalogTemplatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``catalog_templates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCatalogTemplates`` requests and continue to iterate
    through the ``catalog_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListCatalogTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., catalog_management_messages.ListCatalogTemplatesResponse],
        request: catalog_management_messages.ListCatalogTemplatesRequest,
        response: catalog_management_messages.ListCatalogTemplatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListCatalogTemplatesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListCatalogTemplatesResponse):
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
        self._request = catalog_management_messages.ListCatalogTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[catalog_management_messages.ListCatalogTemplatesResponse]:
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

    def __iter__(self) -> Iterator[catalog_management.CatalogTemplate]:
        for page in self.pages:
            yield from page.catalog_templates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCatalogTemplatesAsyncPager:
    """A pager for iterating through ``list_catalog_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListCatalogTemplatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``catalog_templates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCatalogTemplates`` requests and continue to iterate
    through the ``catalog_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListCatalogTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[catalog_management_messages.ListCatalogTemplatesResponse]
        ],
        request: catalog_management_messages.ListCatalogTemplatesRequest,
        response: catalog_management_messages.ListCatalogTemplatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListCatalogTemplatesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListCatalogTemplatesResponse):
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
        self._request = catalog_management_messages.ListCatalogTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[catalog_management_messages.ListCatalogTemplatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[catalog_management.CatalogTemplate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.catalog_templates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSharesPager:
    """A pager for iterating through ``list_shares`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSharesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``shares`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListShares`` requests and continue to iterate
    through the ``shares`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSharesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., sharing_messages.ListSharesResponse],
        request: sharing_messages.ListSharesRequest,
        response: sharing_messages.ListSharesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSharesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSharesResponse):
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
        self._request = sharing_messages.ListSharesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[sharing_messages.ListSharesResponse]:
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

    def __iter__(self) -> Iterator[sharing.Share]:
        for page in self.pages:
            yield from page.shares

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSharesAsyncPager:
    """A pager for iterating through ``list_shares`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSharesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``shares`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListShares`` requests and continue to iterate
    through the ``shares`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSharesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[sharing_messages.ListSharesResponse]],
        request: sharing_messages.ListSharesRequest,
        response: sharing_messages.ListSharesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSharesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSharesResponse):
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
        self._request = sharing_messages.ListSharesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[sharing_messages.ListSharesResponse]:
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

    def __aiter__(self) -> AsyncIterator[sharing.Share]:
        async def async_generator():
            async for page in self.pages:
                for response in page.shares:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSharedTemplatesPager:
    """A pager for iterating through ``list_shared_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSharedTemplatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``shared_templates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSharedTemplates`` requests and continue to iterate
    through the ``shared_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSharedTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., sharing_messages.ListSharedTemplatesResponse],
        request: sharing_messages.ListSharedTemplatesRequest,
        response: sharing_messages.ListSharedTemplatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSharedTemplatesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSharedTemplatesResponse):
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
        self._request = sharing_messages.ListSharedTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[sharing_messages.ListSharedTemplatesResponse]:
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

    def __iter__(self) -> Iterator[sharing.SharedTemplate]:
        for page in self.pages:
            yield from page.shared_templates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSharedTemplatesAsyncPager:
    """A pager for iterating through ``list_shared_templates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSharedTemplatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``shared_templates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSharedTemplates`` requests and continue to iterate
    through the ``shared_templates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSharedTemplatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[sharing_messages.ListSharedTemplatesResponse]],
        request: sharing_messages.ListSharedTemplatesRequest,
        response: sharing_messages.ListSharedTemplatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSharedTemplatesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSharedTemplatesResponse):
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
        self._request = sharing_messages.ListSharedTemplatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[sharing_messages.ListSharedTemplatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[sharing.SharedTemplate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.shared_templates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSharedTemplateRevisionsPager:
    """A pager for iterating through ``list_shared_template_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``shared_template_revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSharedTemplateRevisions`` requests and continue to iterate
    through the ``shared_template_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., sharing_messages.ListSharedTemplateRevisionsResponse],
        request: sharing_messages.ListSharedTemplateRevisionsRequest,
        response: sharing_messages.ListSharedTemplateRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsResponse):
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
        self._request = sharing_messages.ListSharedTemplateRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[sharing_messages.ListSharedTemplateRevisionsResponse]:
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

    def __iter__(self) -> Iterator[sharing.SharedTemplateRevision]:
        for page in self.pages:
            yield from page.shared_template_revisions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSharedTemplateRevisionsAsyncPager:
    """A pager for iterating through ``list_shared_template_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``shared_template_revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSharedTemplateRevisions`` requests and continue to iterate
    through the ``shared_template_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[sharing_messages.ListSharedTemplateRevisionsResponse]
        ],
        request: sharing_messages.ListSharedTemplateRevisionsRequest,
        response: sharing_messages.ListSharedTemplateRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsResponse):
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
        self._request = sharing_messages.ListSharedTemplateRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[sharing_messages.ListSharedTemplateRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[sharing.SharedTemplateRevision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.shared_template_revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCatalogTemplateRevisionsPager:
    """A pager for iterating through ``list_catalog_template_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``catalog_template_revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCatalogTemplateRevisions`` requests and continue to iterate
    through the ``catalog_template_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., catalog_management_messages.ListCatalogTemplateRevisionsResponse
        ],
        request: catalog_management_messages.ListCatalogTemplateRevisionsRequest,
        response: catalog_management_messages.ListCatalogTemplateRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsResponse):
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
        self._request = catalog_management_messages.ListCatalogTemplateRevisionsRequest(
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
    ) -> Iterator[catalog_management_messages.ListCatalogTemplateRevisionsResponse]:
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

    def __iter__(self) -> Iterator[catalog_management.CatalogTemplateRevision]:
        for page in self.pages:
            yield from page.catalog_template_revisions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCatalogTemplateRevisionsAsyncPager:
    """A pager for iterating through ``list_catalog_template_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``catalog_template_revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCatalogTemplateRevisions`` requests and continue to iterate
    through the ``catalog_template_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[catalog_management_messages.ListCatalogTemplateRevisionsResponse],
        ],
        request: catalog_management_messages.ListCatalogTemplateRevisionsRequest,
        response: catalog_management_messages.ListCatalogTemplateRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsResponse):
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
        self._request = catalog_management_messages.ListCatalogTemplateRevisionsRequest(
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
        catalog_management_messages.ListCatalogTemplateRevisionsResponse
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

    def __aiter__(self) -> AsyncIterator[catalog_management.CatalogTemplateRevision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.catalog_template_revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationsPager:
    """A pager for iterating through ``list_applications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``applications`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApplications`` requests and continue to iterate
    through the ``applications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., deployment_messages.ListApplicationsResponse],
        request: deployment_messages.ListApplicationsRequest,
        response: deployment_messages.ListApplicationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationsResponse):
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
        self._request = deployment_messages.ListApplicationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[deployment_messages.ListApplicationsResponse]:
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

    def __iter__(self) -> Iterator[deployment_resources.Application]:
        for page in self.pages:
            yield from page.applications

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationsAsyncPager:
    """A pager for iterating through ``list_applications`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``applications`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApplications`` requests and continue to iterate
    through the ``applications`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[deployment_messages.ListApplicationsResponse]],
        request: deployment_messages.ListApplicationsRequest,
        response: deployment_messages.ListApplicationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationsResponse):
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
        self._request = deployment_messages.ListApplicationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[deployment_messages.ListApplicationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[deployment_resources.Application]:
        async def async_generator():
            async for page in self.pages:
                for response in page.applications:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPoliciesPager:
    """A pager for iterating through ``list_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPolicies`` requests and continue to iterate
    through the ``policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., best_practices_messages.ListPoliciesResponse],
        request: best_practices_messages.ListPoliciesRequest,
        response: best_practices_messages.ListPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListPoliciesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListPoliciesResponse):
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
        self._request = best_practices_messages.ListPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[best_practices_messages.ListPoliciesResponse]:
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

    def __iter__(self) -> Iterator[best_practices.Policy]:
        for page in self.pages:
            yield from page.policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPoliciesAsyncPager:
    """A pager for iterating through ``list_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPolicies`` requests and continue to iterate
    through the ``policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[best_practices_messages.ListPoliciesResponse]],
        request: best_practices_messages.ListPoliciesRequest,
        response: best_practices_messages.ListPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListPoliciesRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListPoliciesResponse):
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
        self._request = best_practices_messages.ListPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[best_practices_messages.ListPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[best_practices.Policy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchFrameworksPager:
    """A pager for iterating through ``fetch_frameworks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.FetchFrameworksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``frameworks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``FetchFrameworks`` requests and continue to iterate
    through the ``frameworks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.FetchFrameworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., best_practices_messages.FetchFrameworksResponse],
        request: best_practices_messages.FetchFrameworksRequest,
        response: best_practices_messages.FetchFrameworksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.FetchFrameworksRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.FetchFrameworksResponse):
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
        self._request = best_practices_messages.FetchFrameworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[best_practices_messages.FetchFrameworksResponse]:
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

    def __iter__(self) -> Iterator[assessment.Framework]:
        for page in self.pages:
            yield from page.frameworks

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class FetchFrameworksAsyncPager:
    """A pager for iterating through ``fetch_frameworks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.FetchFrameworksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``frameworks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``FetchFrameworks`` requests and continue to iterate
    through the ``frameworks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.FetchFrameworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[best_practices_messages.FetchFrameworksResponse]
        ],
        request: best_practices_messages.FetchFrameworksRequest,
        response: best_practices_messages.FetchFrameworksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.FetchFrameworksRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.FetchFrameworksResponse):
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
        self._request = best_practices_messages.FetchFrameworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[best_practices_messages.FetchFrameworksResponse]:
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

    def __aiter__(self) -> AsyncIterator[assessment.Framework]:
        async def async_generator():
            async for page in self.pages:
                for response in page.frameworks:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationTemplateSystemRevisionsPager:
    """A pager for iterating through ``list_application_template_system_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``application_template_system_revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListApplicationTemplateSystemRevisions`` requests and continue to iterate
    through the ``application_template_system_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., authoring_messages.ListApplicationTemplateSystemRevisionsResponse
        ],
        request: authoring_messages.ListApplicationTemplateSystemRevisionsRequest,
        response: authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsResponse):
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
            authoring_messages.ListApplicationTemplateSystemRevisionsRequest(request)
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
    ) -> Iterator[authoring_messages.ListApplicationTemplateSystemRevisionsResponse]:
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

    def __iter__(self) -> Iterator[authoring.ApplicationTemplateSystemRevision]:
        for page in self.pages:
            yield from page.application_template_system_revisions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListApplicationTemplateSystemRevisionsAsyncPager:
    """A pager for iterating through ``list_application_template_system_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``application_template_system_revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListApplicationTemplateSystemRevisions`` requests and continue to iterate
    through the ``application_template_system_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                authoring_messages.ListApplicationTemplateSystemRevisionsResponse
            ],
        ],
        request: authoring_messages.ListApplicationTemplateSystemRevisionsRequest,
        response: authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsRequest):
                The initial request object.
            response (google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsResponse):
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
            authoring_messages.ListApplicationTemplateSystemRevisionsRequest(request)
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
        authoring_messages.ListApplicationTemplateSystemRevisionsResponse
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

    def __aiter__(self) -> AsyncIterator[authoring.ApplicationTemplateSystemRevision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.application_template_system_revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
