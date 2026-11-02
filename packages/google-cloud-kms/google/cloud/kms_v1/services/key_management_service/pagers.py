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

from google.cloud.kms_v1.types import resources, service


class ListKeyRingsPager:
    """A pager for iterating through ``list_key_rings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListKeyRingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``key_rings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListKeyRings`` requests and continue to iterate
    through the ``key_rings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListKeyRingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListKeyRingsResponse],
        request: service.ListKeyRingsRequest,
        response: service.ListKeyRingsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListKeyRingsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListKeyRingsResponse):
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
        self._request = service.ListKeyRingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListKeyRingsResponse]:
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

    def __iter__(self) -> Iterator[resources.KeyRing]:
        for page in self.pages:
            yield from page.key_rings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListKeyRingsAsyncPager:
    """A pager for iterating through ``list_key_rings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListKeyRingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``key_rings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListKeyRings`` requests and continue to iterate
    through the ``key_rings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListKeyRingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListKeyRingsResponse]],
        request: service.ListKeyRingsRequest,
        response: service.ListKeyRingsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListKeyRingsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListKeyRingsResponse):
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
        self._request = service.ListKeyRingsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListKeyRingsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.KeyRing]:
        async def async_generator():
            async for page in self.pages:
                for response in page.key_rings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCryptoKeysPager:
    """A pager for iterating through ``list_crypto_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListCryptoKeysResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``crypto_keys`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCryptoKeys`` requests and continue to iterate
    through the ``crypto_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListCryptoKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListCryptoKeysResponse],
        request: service.ListCryptoKeysRequest,
        response: service.ListCryptoKeysResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListCryptoKeysRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListCryptoKeysResponse):
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
        self._request = service.ListCryptoKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListCryptoKeysResponse]:
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

    def __iter__(self) -> Iterator[resources.CryptoKey]:
        for page in self.pages:
            yield from page.crypto_keys

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCryptoKeysAsyncPager:
    """A pager for iterating through ``list_crypto_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListCryptoKeysResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``crypto_keys`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCryptoKeys`` requests and continue to iterate
    through the ``crypto_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListCryptoKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListCryptoKeysResponse]],
        request: service.ListCryptoKeysRequest,
        response: service.ListCryptoKeysResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListCryptoKeysRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListCryptoKeysResponse):
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
        self._request = service.ListCryptoKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListCryptoKeysResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.CryptoKey]:
        async def async_generator():
            async for page in self.pages:
                for response in page.crypto_keys:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCryptoKeyVersionsPager:
    """A pager for iterating through ``list_crypto_key_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListCryptoKeyVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``crypto_key_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCryptoKeyVersions`` requests and continue to iterate
    through the ``crypto_key_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListCryptoKeyVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListCryptoKeyVersionsResponse],
        request: service.ListCryptoKeyVersionsRequest,
        response: service.ListCryptoKeyVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListCryptoKeyVersionsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListCryptoKeyVersionsResponse):
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
        self._request = service.ListCryptoKeyVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListCryptoKeyVersionsResponse]:
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

    def __iter__(self) -> Iterator[resources.CryptoKeyVersion]:
        for page in self.pages:
            yield from page.crypto_key_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCryptoKeyVersionsAsyncPager:
    """A pager for iterating through ``list_crypto_key_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListCryptoKeyVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``crypto_key_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCryptoKeyVersions`` requests and continue to iterate
    through the ``crypto_key_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListCryptoKeyVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListCryptoKeyVersionsResponse]],
        request: service.ListCryptoKeyVersionsRequest,
        response: service.ListCryptoKeyVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListCryptoKeyVersionsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListCryptoKeyVersionsResponse):
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
        self._request = service.ListCryptoKeyVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListCryptoKeyVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.CryptoKeyVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.crypto_key_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImportJobsPager:
    """A pager for iterating through ``list_import_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListImportJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``import_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListImportJobs`` requests and continue to iterate
    through the ``import_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListImportJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListImportJobsResponse],
        request: service.ListImportJobsRequest,
        response: service.ListImportJobsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListImportJobsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListImportJobsResponse):
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
        self._request = service.ListImportJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListImportJobsResponse]:
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

    def __iter__(self) -> Iterator[resources.ImportJob]:
        for page in self.pages:
            yield from page.import_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListImportJobsAsyncPager:
    """A pager for iterating through ``list_import_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListImportJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``import_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListImportJobs`` requests and continue to iterate
    through the ``import_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListImportJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListImportJobsResponse]],
        request: service.ListImportJobsRequest,
        response: service.ListImportJobsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListImportJobsRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListImportJobsResponse):
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
        self._request = service.ListImportJobsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListImportJobsResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.ImportJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.import_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRetiredResourcesPager:
    """A pager for iterating through ``list_retired_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListRetiredResourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``retired_resources`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRetiredResources`` requests and continue to iterate
    through the ``retired_resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListRetiredResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., service.ListRetiredResourcesResponse],
        request: service.ListRetiredResourcesRequest,
        response: service.ListRetiredResourcesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListRetiredResourcesRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListRetiredResourcesResponse):
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
        self._request = service.ListRetiredResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListRetiredResourcesResponse]:
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

    def __iter__(self) -> Iterator[resources.RetiredResource]:
        for page in self.pages:
            yield from page.retired_resources

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRetiredResourcesAsyncPager:
    """A pager for iterating through ``list_retired_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.kms_v1.types.ListRetiredResourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``retired_resources`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRetiredResources`` requests and continue to iterate
    through the ``retired_resources`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.kms_v1.types.ListRetiredResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[service.ListRetiredResourcesResponse]],
        request: service.ListRetiredResourcesRequest,
        response: service.ListRetiredResourcesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.kms_v1.types.ListRetiredResourcesRequest):
                The initial request object.
            response (google.cloud.kms_v1.types.ListRetiredResourcesResponse):
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
        self._request = service.ListRetiredResourcesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListRetiredResourcesResponse]:
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

    def __aiter__(self) -> AsyncIterator[resources.RetiredResource]:
        async def async_generator():
            async for page in self.pages:
                for response in page.retired_resources:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
