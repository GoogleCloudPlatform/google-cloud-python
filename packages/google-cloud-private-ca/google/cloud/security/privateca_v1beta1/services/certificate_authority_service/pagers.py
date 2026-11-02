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

from google.cloud.security.privateca_v1beta1.types import resources, service


class ListCertificatesPager:
    """A pager for iterating through ``list_certificates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListCertificatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``certificates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCertificates`` requests and continue to iterate
    through the ``certificates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListCertificatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListCertificatesResponse],
        request: service.ListCertificatesRequest,
        response: service.ListCertificatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListCertificatesRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListCertificatesResponse):
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
        self._request = service.ListCertificatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListCertificatesResponse]:
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

    def __iter__(self) -> Iterator[resources.Certificate]:
        for page in self.pages:
            yield from page.certificates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificatesAsyncPager:
    """A pager for iterating through ``list_certificates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListCertificatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``certificates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCertificates`` requests and continue to iterate
    through the ``certificates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListCertificatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListCertificatesResponse]],
        request: service.ListCertificatesRequest,
        response: service.ListCertificatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListCertificatesRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListCertificatesResponse):
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
        self._request = service.ListCertificatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListCertificatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.Certificate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.certificates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateAuthoritiesPager:
    """A pager for iterating through ``list_certificate_authorities`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``certificate_authorities`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCertificateAuthorities`` requests and continue to iterate
    through the ``certificate_authorities`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListCertificateAuthoritiesResponse],
        request: service.ListCertificateAuthoritiesRequest,
        response: service.ListCertificateAuthoritiesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesResponse):
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
        self._request = service.ListCertificateAuthoritiesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListCertificateAuthoritiesResponse]:
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

    def __iter__(self) -> Iterator[resources.CertificateAuthority]:
        for page in self.pages:
            yield from page.certificate_authorities

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateAuthoritiesAsyncPager:
    """A pager for iterating through ``list_certificate_authorities`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``certificate_authorities`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCertificateAuthorities`` requests and continue to iterate
    through the ``certificate_authorities`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListCertificateAuthoritiesResponse]],
        request: service.ListCertificateAuthoritiesRequest,
        response: service.ListCertificateAuthoritiesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListCertificateAuthoritiesResponse):
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
        self._request = service.ListCertificateAuthoritiesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListCertificateAuthoritiesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.CertificateAuthority]:
        async def async_generator():
            async for page in self.pages:
                for response in page.certificate_authorities:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateRevocationListsPager:
    """A pager for iterating through ``list_certificate_revocation_lists`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``certificate_revocation_lists`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCertificateRevocationLists`` requests and continue to iterate
    through the ``certificate_revocation_lists`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListCertificateRevocationListsResponse],
        request: service.ListCertificateRevocationListsRequest,
        response: service.ListCertificateRevocationListsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsResponse):
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
        self._request = service.ListCertificateRevocationListsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListCertificateRevocationListsResponse]:
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

    def __iter__(self) -> Iterator[resources.CertificateRevocationList]:
        for page in self.pages:
            yield from page.certificate_revocation_lists

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateRevocationListsAsyncPager:
    """A pager for iterating through ``list_certificate_revocation_lists`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``certificate_revocation_lists`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCertificateRevocationLists`` requests and continue to iterate
    through the ``certificate_revocation_lists`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[service.ListCertificateRevocationListsResponse]
        ],
        request: service.ListCertificateRevocationListsRequest,
        response: service.ListCertificateRevocationListsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListCertificateRevocationListsResponse):
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
        self._request = service.ListCertificateRevocationListsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[service.ListCertificateRevocationListsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.CertificateRevocationList]:
        async def async_generator():
            async for page in self.pages:
                for response in page.certificate_revocation_lists:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReusableConfigsPager:
    """A pager for iterating through ``list_reusable_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListReusableConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``reusable_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReusableConfigs`` requests and continue to iterate
    through the ``reusable_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListReusableConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListReusableConfigsResponse],
        request: service.ListReusableConfigsRequest,
        response: service.ListReusableConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListReusableConfigsRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListReusableConfigsResponse):
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
        self._request = service.ListReusableConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListReusableConfigsResponse]:
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

    def __iter__(self) -> Iterator[resources.ReusableConfig]:
        for page in self.pages:
            yield from page.reusable_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReusableConfigsAsyncPager:
    """A pager for iterating through ``list_reusable_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.security.privateca_v1beta1.types.ListReusableConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``reusable_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReusableConfigs`` requests and continue to iterate
    through the ``reusable_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.security.privateca_v1beta1.types.ListReusableConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListReusableConfigsResponse]],
        request: service.ListReusableConfigsRequest,
        response: service.ListReusableConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.security.privateca_v1beta1.types.ListReusableConfigsRequest):
                The initial request object.
            response (google.cloud.security.privateca_v1beta1.types.ListReusableConfigsResponse):
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
        self._request = service.ListReusableConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListReusableConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.ReusableConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.reusable_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
