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

from google.cloud.orchestration.airflow.service_v1.types import environments


class ListEnvironmentsPager:
    """A pager for iterating through ``list_environments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``environments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEnvironments`` requests and continue to iterate
    through the ``environments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., environments.ListEnvironmentsResponse],
        request: environments.ListEnvironmentsRequest,
        response: environments.ListEnvironmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsResponse):
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
        self._request = environments.ListEnvironmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[environments.ListEnvironmentsResponse]:
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

    def __iter__(self) -> Iterator[environments.Environment]:
        for page in self.pages:
            yield from page.environments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEnvironmentsAsyncPager:
    """A pager for iterating through ``list_environments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``environments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEnvironments`` requests and continue to iterate
    through the ``environments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[environments.ListEnvironmentsResponse]],
        request: environments.ListEnvironmentsRequest,
        response: environments.ListEnvironmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListEnvironmentsResponse):
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
        self._request = environments.ListEnvironmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[environments.ListEnvironmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[environments.Environment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.environments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkloadsPager:
    """A pager for iterating through ``list_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``workloads`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListWorkloads`` requests and continue to iterate
    through the ``workloads`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., environments.ListWorkloadsResponse],
        request: environments.ListWorkloadsRequest,
        response: environments.ListWorkloadsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsResponse):
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
        self._request = environments.ListWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[environments.ListWorkloadsResponse]:
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

    def __iter__(self) -> Iterator[environments.ListWorkloadsResponse.ComposerWorkload]:
        for page in self.pages:
            yield from page.workloads

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListWorkloadsAsyncPager:
    """A pager for iterating through ``list_workloads`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``workloads`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListWorkloads`` requests and continue to iterate
    through the ``workloads`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[environments.ListWorkloadsResponse]],
        request: environments.ListWorkloadsRequest,
        response: environments.ListWorkloadsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListWorkloadsResponse):
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
        self._request = environments.ListWorkloadsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[environments.ListWorkloadsResponse]:
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
    ) -> AsyncIterator[environments.ListWorkloadsResponse.ComposerWorkload]:
        async def async_generator():
            async for page in self.pages:
                for response in page.workloads:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserWorkloadsSecretsPager:
    """A pager for iterating through ``list_user_workloads_secrets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``user_workloads_secrets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUserWorkloadsSecrets`` requests and continue to iterate
    through the ``user_workloads_secrets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., environments.ListUserWorkloadsSecretsResponse],
        request: environments.ListUserWorkloadsSecretsRequest,
        response: environments.ListUserWorkloadsSecretsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsResponse):
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
        self._request = environments.ListUserWorkloadsSecretsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[environments.ListUserWorkloadsSecretsResponse]:
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

    def __iter__(self) -> Iterator[environments.UserWorkloadsSecret]:
        for page in self.pages:
            yield from page.user_workloads_secrets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserWorkloadsSecretsAsyncPager:
    """A pager for iterating through ``list_user_workloads_secrets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``user_workloads_secrets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUserWorkloadsSecrets`` requests and continue to iterate
    through the ``user_workloads_secrets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[environments.ListUserWorkloadsSecretsResponse]],
        request: environments.ListUserWorkloadsSecretsRequest,
        response: environments.ListUserWorkloadsSecretsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsSecretsResponse):
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
        self._request = environments.ListUserWorkloadsSecretsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[environments.ListUserWorkloadsSecretsResponse]:
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

    def __aiter__(self) -> AsyncIterator[environments.UserWorkloadsSecret]:
        async def async_generator():
            async for page in self.pages:
                for response in page.user_workloads_secrets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserWorkloadsConfigMapsPager:
    """A pager for iterating through ``list_user_workloads_config_maps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``user_workloads_config_maps`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListUserWorkloadsConfigMaps`` requests and continue to iterate
    through the ``user_workloads_config_maps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., environments.ListUserWorkloadsConfigMapsResponse],
        request: environments.ListUserWorkloadsConfigMapsRequest,
        response: environments.ListUserWorkloadsConfigMapsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsResponse):
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
        self._request = environments.ListUserWorkloadsConfigMapsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[environments.ListUserWorkloadsConfigMapsResponse]:
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

    def __iter__(self) -> Iterator[environments.UserWorkloadsConfigMap]:
        for page in self.pages:
            yield from page.user_workloads_config_maps

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListUserWorkloadsConfigMapsAsyncPager:
    """A pager for iterating through ``list_user_workloads_config_maps`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``user_workloads_config_maps`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListUserWorkloadsConfigMaps`` requests and continue to iterate
    through the ``user_workloads_config_maps`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[environments.ListUserWorkloadsConfigMapsResponse]
        ],
        request: environments.ListUserWorkloadsConfigMapsRequest,
        response: environments.ListUserWorkloadsConfigMapsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsRequest):
                The initial request object.
            response (google.cloud.orchestration.airflow.service_v1.types.ListUserWorkloadsConfigMapsResponse):
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
        self._request = environments.ListUserWorkloadsConfigMapsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[environments.ListUserWorkloadsConfigMapsResponse]:
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

    def __aiter__(self) -> AsyncIterator[environments.UserWorkloadsConfigMap]:
        async def async_generator():
            async for page in self.pages:
                for response in page.user_workloads_config_maps:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
