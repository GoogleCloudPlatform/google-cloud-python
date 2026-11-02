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

from google.cloud.certificate_manager_v1.types import (
    certificate_issuance_config,
    certificate_manager,
    trust_config,
)


class ListCertificatesPager:
    """A pager for iterating through ``list_certificates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``certificates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCertificates`` requests and continue to iterate
    through the ``certificates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., certificate_manager.ListCertificatesResponse],
        request: certificate_manager.ListCertificatesRequest,
        response: certificate_manager.ListCertificatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificatesRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificatesResponse):
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
        self._request = certificate_manager.ListCertificatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[certificate_manager.ListCertificatesResponse]:
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

    def __iter__(self) -> Iterator[certificate_manager.Certificate]:
        for page in self.pages:
            yield from page.certificates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificatesAsyncPager:
    """A pager for iterating through ``list_certificates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``certificates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCertificates`` requests and continue to iterate
    through the ``certificates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[certificate_manager.ListCertificatesResponse]],
        request: certificate_manager.ListCertificatesRequest,
        response: certificate_manager.ListCertificatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificatesRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificatesResponse):
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
        self._request = certificate_manager.ListCertificatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[certificate_manager.ListCertificatesResponse]:
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

    def __aiter__(self) -> AsyncIterator[certificate_manager.Certificate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.certificates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateMapsPager:
    """A pager for iterating through ``list_certificate_maps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``certificate_maps`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCertificateMaps`` requests and continue to iterate
    through the ``certificate_maps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., certificate_manager.ListCertificateMapsResponse],
        request: certificate_manager.ListCertificateMapsRequest,
        response: certificate_manager.ListCertificateMapsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificateMapsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificateMapsResponse):
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
        self._request = certificate_manager.ListCertificateMapsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[certificate_manager.ListCertificateMapsResponse]:
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

    def __iter__(self) -> Iterator[certificate_manager.CertificateMap]:
        for page in self.pages:
            yield from page.certificate_maps

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateMapsAsyncPager:
    """A pager for iterating through ``list_certificate_maps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``certificate_maps`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCertificateMaps`` requests and continue to iterate
    through the ``certificate_maps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[certificate_manager.ListCertificateMapsResponse]
        ],
        request: certificate_manager.ListCertificateMapsRequest,
        response: certificate_manager.ListCertificateMapsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificateMapsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificateMapsResponse):
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
        self._request = certificate_manager.ListCertificateMapsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[certificate_manager.ListCertificateMapsResponse]:
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

    def __aiter__(self) -> AsyncIterator[certificate_manager.CertificateMap]:
        async def async_generator():
            async for page in self.pages:
                for response in page.certificate_maps:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateMapEntriesPager:
    """A pager for iterating through ``list_certificate_map_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``certificate_map_entries`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCertificateMapEntries`` requests and continue to iterate
    through the ``certificate_map_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., certificate_manager.ListCertificateMapEntriesResponse],
        request: certificate_manager.ListCertificateMapEntriesRequest,
        response: certificate_manager.ListCertificateMapEntriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesResponse):
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
        self._request = certificate_manager.ListCertificateMapEntriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[certificate_manager.ListCertificateMapEntriesResponse]:
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

    def __iter__(self) -> Iterator[certificate_manager.CertificateMapEntry]:
        for page in self.pages:
            yield from page.certificate_map_entries

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateMapEntriesAsyncPager:
    """A pager for iterating through ``list_certificate_map_entries`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``certificate_map_entries`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCertificateMapEntries`` requests and continue to iterate
    through the ``certificate_map_entries`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[certificate_manager.ListCertificateMapEntriesResponse]
        ],
        request: certificate_manager.ListCertificateMapEntriesRequest,
        response: certificate_manager.ListCertificateMapEntriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificateMapEntriesResponse):
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
        self._request = certificate_manager.ListCertificateMapEntriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[certificate_manager.ListCertificateMapEntriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[certificate_manager.CertificateMapEntry]:
        async def async_generator():
            async for page in self.pages:
                for response in page.certificate_map_entries:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDnsAuthorizationsPager:
    """A pager for iterating through ``list_dns_authorizations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``dns_authorizations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDnsAuthorizations`` requests and continue to iterate
    through the ``dns_authorizations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., certificate_manager.ListDnsAuthorizationsResponse],
        request: certificate_manager.ListDnsAuthorizationsRequest,
        response: certificate_manager.ListDnsAuthorizationsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsResponse):
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
        self._request = certificate_manager.ListDnsAuthorizationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[certificate_manager.ListDnsAuthorizationsResponse]:
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

    def __iter__(self) -> Iterator[certificate_manager.DnsAuthorization]:
        for page in self.pages:
            yield from page.dns_authorizations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDnsAuthorizationsAsyncPager:
    """A pager for iterating through ``list_dns_authorizations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``dns_authorizations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDnsAuthorizations`` requests and continue to iterate
    through the ``dns_authorizations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[certificate_manager.ListDnsAuthorizationsResponse]
        ],
        request: certificate_manager.ListDnsAuthorizationsRequest,
        response: certificate_manager.ListDnsAuthorizationsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListDnsAuthorizationsResponse):
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
        self._request = certificate_manager.ListDnsAuthorizationsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[certificate_manager.ListDnsAuthorizationsResponse]:
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

    def __aiter__(self) -> AsyncIterator[certificate_manager.DnsAuthorization]:
        async def async_generator():
            async for page in self.pages:
                for response in page.dns_authorizations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateIssuanceConfigsPager:
    """A pager for iterating through ``list_certificate_issuance_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``certificate_issuance_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCertificateIssuanceConfigs`` requests and continue to iterate
    through the ``certificate_issuance_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., certificate_issuance_config.ListCertificateIssuanceConfigsResponse
        ],
        request: certificate_issuance_config.ListCertificateIssuanceConfigsRequest,
        response: certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsResponse):
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
            certificate_issuance_config.ListCertificateIssuanceConfigsRequest(request)
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
    ) -> Iterator[certificate_issuance_config.ListCertificateIssuanceConfigsResponse]:
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
    ) -> Iterator[certificate_issuance_config.CertificateIssuanceConfig]:
        for page in self.pages:
            yield from page.certificate_issuance_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCertificateIssuanceConfigsAsyncPager:
    """A pager for iterating through ``list_certificate_issuance_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``certificate_issuance_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCertificateIssuanceConfigs`` requests and continue to iterate
    through the ``certificate_issuance_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                certificate_issuance_config.ListCertificateIssuanceConfigsResponse
            ],
        ],
        request: certificate_issuance_config.ListCertificateIssuanceConfigsRequest,
        response: certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListCertificateIssuanceConfigsResponse):
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
            certificate_issuance_config.ListCertificateIssuanceConfigsRequest(request)
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
        certificate_issuance_config.ListCertificateIssuanceConfigsResponse
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
    ) -> AsyncIterator[certificate_issuance_config.CertificateIssuanceConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.certificate_issuance_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTrustConfigsPager:
    """A pager for iterating through ``list_trust_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListTrustConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``trust_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTrustConfigs`` requests and continue to iterate
    through the ``trust_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListTrustConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., trust_config.ListTrustConfigsResponse],
        request: trust_config.ListTrustConfigsRequest,
        response: trust_config.ListTrustConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListTrustConfigsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListTrustConfigsResponse):
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
        self._request = trust_config.ListTrustConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[trust_config.ListTrustConfigsResponse]:
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

    def __iter__(self) -> Iterator[trust_config.TrustConfig]:
        for page in self.pages:
            yield from page.trust_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTrustConfigsAsyncPager:
    """A pager for iterating through ``list_trust_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.certificate_manager_v1.types.ListTrustConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``trust_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTrustConfigs`` requests and continue to iterate
    through the ``trust_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.certificate_manager_v1.types.ListTrustConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[trust_config.ListTrustConfigsResponse]],
        request: trust_config.ListTrustConfigsRequest,
        response: trust_config.ListTrustConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.certificate_manager_v1.types.ListTrustConfigsRequest):
                The initial request object.
            response (google.cloud.certificate_manager_v1.types.ListTrustConfigsResponse):
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
        self._request = trust_config.ListTrustConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[trust_config.ListTrustConfigsResponse]:
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

    def __aiter__(self) -> AsyncIterator[trust_config.TrustConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.trust_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
