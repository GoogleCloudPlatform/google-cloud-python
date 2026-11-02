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

from google.cloud.securitycentermanagement_v1.types import security_center_management


class ListEffectiveSecurityHealthAnalyticsCustomModulesPager:
    """A pager for iterating through ``list_effective_security_health_analytics_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``effective_security_health_analytics_custom_modules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEffectiveSecurityHealthAnalyticsCustomModules`` requests and continue to iterate
    through the ``effective_security_health_analytics_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
        ],
        request: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        response: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse):
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
        self._request = security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
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
    ) -> Iterator[
        security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse
    ]:
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
        security_center_management.EffectiveSecurityHealthAnalyticsCustomModule
    ]:
        for page in self.pages:
            yield from page.effective_security_health_analytics_custom_modules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager:
    """A pager for iterating through ``list_effective_security_health_analytics_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``effective_security_health_analytics_custom_modules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEffectiveSecurityHealthAnalyticsCustomModules`` requests and continue to iterate
    through the ``effective_security_health_analytics_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse
            ],
        ],
        request: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        response: security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse):
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
        self._request = security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
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
        security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse
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
    ) -> AsyncIterator[
        security_center_management.EffectiveSecurityHealthAnalyticsCustomModule
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.effective_security_health_analytics_custom_modules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSecurityHealthAnalyticsCustomModulesPager:
    """A pager for iterating through ``list_security_health_analytics_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``security_health_analytics_custom_modules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSecurityHealthAnalyticsCustomModules`` requests and continue to iterate
    through the ``security_health_analytics_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
        ],
        request: security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
        response: security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesResponse):
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
            security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest(
                request
            )
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
    ) -> Iterator[
        security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse
    ]:
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
    ) -> Iterator[security_center_management.SecurityHealthAnalyticsCustomModule]:
        for page in self.pages:
            yield from page.security_health_analytics_custom_modules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSecurityHealthAnalyticsCustomModulesAsyncPager:
    """A pager for iterating through ``list_security_health_analytics_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``security_health_analytics_custom_modules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSecurityHealthAnalyticsCustomModules`` requests and continue to iterate
    through the ``security_health_analytics_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse
            ],
        ],
        request: security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
        response: security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesResponse):
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
            security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest(
                request
            )
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
        security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse
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
    ) -> AsyncIterator[security_center_management.SecurityHealthAnalyticsCustomModule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.security_health_analytics_custom_modules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDescendantSecurityHealthAnalyticsCustomModulesPager:
    """A pager for iterating through ``list_descendant_security_health_analytics_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``security_health_analytics_custom_modules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDescendantSecurityHealthAnalyticsCustomModules`` requests and continue to iterate
    through the ``security_health_analytics_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
        ],
        request: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        response: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesResponse):
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
        self._request = security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
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
    ) -> Iterator[
        security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse
    ]:
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
    ) -> Iterator[security_center_management.SecurityHealthAnalyticsCustomModule]:
        for page in self.pages:
            yield from page.security_health_analytics_custom_modules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager:
    """A pager for iterating through ``list_descendant_security_health_analytics_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``security_health_analytics_custom_modules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDescendantSecurityHealthAnalyticsCustomModules`` requests and continue to iterate
    through the ``security_health_analytics_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse
            ],
        ],
        request: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        response: security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesResponse):
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
        self._request = security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
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
        security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse
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
    ) -> AsyncIterator[security_center_management.SecurityHealthAnalyticsCustomModule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.security_health_analytics_custom_modules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEffectiveEventThreatDetectionCustomModulesPager:
    """A pager for iterating through ``list_effective_event_threat_detection_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``effective_event_threat_detection_custom_modules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEffectiveEventThreatDetectionCustomModules`` requests and continue to iterate
    through the ``effective_event_threat_detection_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
        ],
        request: security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
        response: security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesResponse):
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
        self._request = security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest(
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
    ) -> Iterator[
        security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse
    ]:
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
    ) -> Iterator[security_center_management.EffectiveEventThreatDetectionCustomModule]:
        for page in self.pages:
            yield from page.effective_event_threat_detection_custom_modules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEffectiveEventThreatDetectionCustomModulesAsyncPager:
    """A pager for iterating through ``list_effective_event_threat_detection_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``effective_event_threat_detection_custom_modules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEffectiveEventThreatDetectionCustomModules`` requests and continue to iterate
    through the ``effective_event_threat_detection_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse
            ],
        ],
        request: security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
        response: security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesResponse):
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
        self._request = security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest(
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
        security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse
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
    ) -> AsyncIterator[
        security_center_management.EffectiveEventThreatDetectionCustomModule
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.effective_event_threat_detection_custom_modules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEventThreatDetectionCustomModulesPager:
    """A pager for iterating through ``list_event_threat_detection_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``event_threat_detection_custom_modules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEventThreatDetectionCustomModules`` requests and continue to iterate
    through the ``event_threat_detection_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            security_center_management.ListEventThreatDetectionCustomModulesResponse,
        ],
        request: security_center_management.ListEventThreatDetectionCustomModulesRequest,
        response: security_center_management.ListEventThreatDetectionCustomModulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesResponse):
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
            security_center_management.ListEventThreatDetectionCustomModulesRequest(
                request
            )
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
    ) -> Iterator[
        security_center_management.ListEventThreatDetectionCustomModulesResponse
    ]:
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
    ) -> Iterator[security_center_management.EventThreatDetectionCustomModule]:
        for page in self.pages:
            yield from page.event_threat_detection_custom_modules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEventThreatDetectionCustomModulesAsyncPager:
    """A pager for iterating through ``list_event_threat_detection_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``event_threat_detection_custom_modules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEventThreatDetectionCustomModules`` requests and continue to iterate
    through the ``event_threat_detection_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                security_center_management.ListEventThreatDetectionCustomModulesResponse
            ],
        ],
        request: security_center_management.ListEventThreatDetectionCustomModulesRequest,
        response: security_center_management.ListEventThreatDetectionCustomModulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesResponse):
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
            security_center_management.ListEventThreatDetectionCustomModulesRequest(
                request
            )
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
        security_center_management.ListEventThreatDetectionCustomModulesResponse
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
    ) -> AsyncIterator[security_center_management.EventThreatDetectionCustomModule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.event_threat_detection_custom_modules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDescendantEventThreatDetectionCustomModulesPager:
    """A pager for iterating through ``list_descendant_event_threat_detection_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``event_threat_detection_custom_modules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDescendantEventThreatDetectionCustomModules`` requests and continue to iterate
    through the ``event_threat_detection_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
        ],
        request: security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
        response: security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesResponse):
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
        self._request = security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest(
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
    ) -> Iterator[
        security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse
    ]:
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
    ) -> Iterator[security_center_management.EventThreatDetectionCustomModule]:
        for page in self.pages:
            yield from page.event_threat_detection_custom_modules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDescendantEventThreatDetectionCustomModulesAsyncPager:
    """A pager for iterating through ``list_descendant_event_threat_detection_custom_modules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``event_threat_detection_custom_modules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDescendantEventThreatDetectionCustomModules`` requests and continue to iterate
    through the ``event_threat_detection_custom_modules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse
            ],
        ],
        request: security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
        response: security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesResponse):
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
        self._request = security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest(
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
        security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse
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
    ) -> AsyncIterator[security_center_management.EventThreatDetectionCustomModule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.event_threat_detection_custom_modules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSecurityCenterServicesPager:
    """A pager for iterating through ``list_security_center_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``security_center_services`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSecurityCenterServices`` requests and continue to iterate
    through the ``security_center_services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., security_center_management.ListSecurityCenterServicesResponse
        ],
        request: security_center_management.ListSecurityCenterServicesRequest,
        response: security_center_management.ListSecurityCenterServicesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesResponse):
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
        self._request = security_center_management.ListSecurityCenterServicesRequest(
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
    ) -> Iterator[security_center_management.ListSecurityCenterServicesResponse]:
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

    def __iter__(self) -> Iterator[security_center_management.SecurityCenterService]:
        for page in self.pages:
            yield from page.security_center_services

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSecurityCenterServicesAsyncPager:
    """A pager for iterating through ``list_security_center_services`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``security_center_services`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSecurityCenterServices`` requests and continue to iterate
    through the ``security_center_services`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[security_center_management.ListSecurityCenterServicesResponse],
        ],
        request: security_center_management.ListSecurityCenterServicesRequest,
        response: security_center_management.ListSecurityCenterServicesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesRequest):
                The initial request object.
            response (google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesResponse):
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
        self._request = security_center_management.ListSecurityCenterServicesRequest(
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
    ) -> AsyncIterator[security_center_management.ListSecurityCenterServicesResponse]:
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
    ) -> AsyncIterator[security_center_management.SecurityCenterService]:
        async def async_generator():
            async for page in self.pages:
                for response in page.security_center_services:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
