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

from google.cloud.artifactregistry_v1.types import (
    artifact,
    attachment,
    file,
    package,
    repository,
    rule,
    tag,
    version,
)


class ListDockerImagesPager:
    """A pager for iterating through ``list_docker_images`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListDockerImagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``docker_images`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDockerImages`` requests and continue to iterate
    through the ``docker_images`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListDockerImagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., artifact.ListDockerImagesResponse],
        request: artifact.ListDockerImagesRequest,
        response: artifact.ListDockerImagesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListDockerImagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListDockerImagesResponse):
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
        self._request = artifact.ListDockerImagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[artifact.ListDockerImagesResponse]:
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

    def __iter__(self) -> Iterator[artifact.DockerImage]:
        for page in self.pages:
            yield from page.docker_images

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDockerImagesAsyncPager:
    """A pager for iterating through ``list_docker_images`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListDockerImagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``docker_images`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDockerImages`` requests and continue to iterate
    through the ``docker_images`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListDockerImagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[artifact.ListDockerImagesResponse]],
        request: artifact.ListDockerImagesRequest,
        response: artifact.ListDockerImagesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListDockerImagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListDockerImagesResponse):
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
        self._request = artifact.ListDockerImagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[artifact.ListDockerImagesResponse]:
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

    def __aiter__(self) -> AsyncIterator[artifact.DockerImage]:
        async def async_generator():
            async for page in self.pages:
                for response in page.docker_images:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMavenArtifactsPager:
    """A pager for iterating through ``list_maven_artifacts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListMavenArtifactsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``maven_artifacts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMavenArtifacts`` requests and continue to iterate
    through the ``maven_artifacts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListMavenArtifactsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., artifact.ListMavenArtifactsResponse],
        request: artifact.ListMavenArtifactsRequest,
        response: artifact.ListMavenArtifactsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListMavenArtifactsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListMavenArtifactsResponse):
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
        self._request = artifact.ListMavenArtifactsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[artifact.ListMavenArtifactsResponse]:
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

    def __iter__(self) -> Iterator[artifact.MavenArtifact]:
        for page in self.pages:
            yield from page.maven_artifacts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMavenArtifactsAsyncPager:
    """A pager for iterating through ``list_maven_artifacts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListMavenArtifactsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``maven_artifacts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMavenArtifacts`` requests and continue to iterate
    through the ``maven_artifacts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListMavenArtifactsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[artifact.ListMavenArtifactsResponse]],
        request: artifact.ListMavenArtifactsRequest,
        response: artifact.ListMavenArtifactsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListMavenArtifactsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListMavenArtifactsResponse):
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
        self._request = artifact.ListMavenArtifactsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[artifact.ListMavenArtifactsResponse]:
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

    def __aiter__(self) -> AsyncIterator[artifact.MavenArtifact]:
        async def async_generator():
            async for page in self.pages:
                for response in page.maven_artifacts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNpmPackagesPager:
    """A pager for iterating through ``list_npm_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListNpmPackagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``npm_packages`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNpmPackages`` requests and continue to iterate
    through the ``npm_packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListNpmPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., artifact.ListNpmPackagesResponse],
        request: artifact.ListNpmPackagesRequest,
        response: artifact.ListNpmPackagesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListNpmPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListNpmPackagesResponse):
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
        self._request = artifact.ListNpmPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[artifact.ListNpmPackagesResponse]:
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

    def __iter__(self) -> Iterator[artifact.NpmPackage]:
        for page in self.pages:
            yield from page.npm_packages

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNpmPackagesAsyncPager:
    """A pager for iterating through ``list_npm_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListNpmPackagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``npm_packages`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNpmPackages`` requests and continue to iterate
    through the ``npm_packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListNpmPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[artifact.ListNpmPackagesResponse]],
        request: artifact.ListNpmPackagesRequest,
        response: artifact.ListNpmPackagesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListNpmPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListNpmPackagesResponse):
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
        self._request = artifact.ListNpmPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[artifact.ListNpmPackagesResponse]:
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

    def __aiter__(self) -> AsyncIterator[artifact.NpmPackage]:
        async def async_generator():
            async for page in self.pages:
                for response in page.npm_packages:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPythonPackagesPager:
    """A pager for iterating through ``list_python_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListPythonPackagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``python_packages`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPythonPackages`` requests and continue to iterate
    through the ``python_packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListPythonPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., artifact.ListPythonPackagesResponse],
        request: artifact.ListPythonPackagesRequest,
        response: artifact.ListPythonPackagesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListPythonPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListPythonPackagesResponse):
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
        self._request = artifact.ListPythonPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[artifact.ListPythonPackagesResponse]:
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

    def __iter__(self) -> Iterator[artifact.PythonPackage]:
        for page in self.pages:
            yield from page.python_packages

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPythonPackagesAsyncPager:
    """A pager for iterating through ``list_python_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListPythonPackagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``python_packages`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPythonPackages`` requests and continue to iterate
    through the ``python_packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListPythonPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[artifact.ListPythonPackagesResponse]],
        request: artifact.ListPythonPackagesRequest,
        response: artifact.ListPythonPackagesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListPythonPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListPythonPackagesResponse):
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
        self._request = artifact.ListPythonPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[artifact.ListPythonPackagesResponse]:
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

    def __aiter__(self) -> AsyncIterator[artifact.PythonPackage]:
        async def async_generator():
            async for page in self.pages:
                for response in page.python_packages:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRepositoriesPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListRepositoriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., repository.ListRepositoriesResponse],
        request: repository.ListRepositoriesRequest,
        response: repository.ListRepositoriesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListRepositoriesResponse):
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
        self._request = repository.ListRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[repository.ListRepositoriesResponse]:
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

    def __iter__(self) -> Iterator[repository.Repository]:
        for page in self.pages:
            yield from page.repositories

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRepositoriesAsyncPager:
    """A pager for iterating through ``list_repositories`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListRepositoriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``repositories`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRepositories`` requests and continue to iterate
    through the ``repositories`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListRepositoriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[repository.ListRepositoriesResponse]],
        request: repository.ListRepositoriesRequest,
        response: repository.ListRepositoriesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListRepositoriesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListRepositoriesResponse):
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
        self._request = repository.ListRepositoriesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[repository.ListRepositoriesResponse]:
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

    def __aiter__(self) -> AsyncIterator[repository.Repository]:
        async def async_generator():
            async for page in self.pages:
                for response in page.repositories:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPackagesPager:
    """A pager for iterating through ``list_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListPackagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``packages`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPackages`` requests and continue to iterate
    through the ``packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., package.ListPackagesResponse],
        request: package.ListPackagesRequest,
        response: package.ListPackagesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListPackagesResponse):
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
        self._request = package.ListPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[package.ListPackagesResponse]:
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

    def __iter__(self) -> Iterator[package.Package]:
        for page in self.pages:
            yield from page.packages

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPackagesAsyncPager:
    """A pager for iterating through ``list_packages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListPackagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``packages`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPackages`` requests and continue to iterate
    through the ``packages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListPackagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[package.ListPackagesResponse]],
        request: package.ListPackagesRequest,
        response: package.ListPackagesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListPackagesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListPackagesResponse):
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
        self._request = package.ListPackagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[package.ListPackagesResponse]:
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

    def __aiter__(self) -> AsyncIterator[package.Package]:
        async def async_generator():
            async for page in self.pages:
                for response in page.packages:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVersionsPager:
    """A pager for iterating through ``list_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVersions`` requests and continue to iterate
    through the ``versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., version.ListVersionsResponse],
        request: version.ListVersionsRequest,
        response: version.ListVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListVersionsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListVersionsResponse):
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
        self._request = version.ListVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[version.ListVersionsResponse]:
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

    def __iter__(self) -> Iterator[version.Version]:
        for page in self.pages:
            yield from page.versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVersionsAsyncPager:
    """A pager for iterating through ``list_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVersions`` requests and continue to iterate
    through the ``versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[version.ListVersionsResponse]],
        request: version.ListVersionsRequest,
        response: version.ListVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListVersionsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListVersionsResponse):
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
        self._request = version.ListVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[version.ListVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[version.Version]:
        async def async_generator():
            async for page in self.pages:
                for response in page.versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFilesPager:
    """A pager for iterating through ``list_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListFilesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``files`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFiles`` requests and continue to iterate
    through the ``files`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., file.ListFilesResponse],
        request: file.ListFilesRequest,
        response: file.ListFilesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListFilesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListFilesResponse):
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
        self._request = file.ListFilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[file.ListFilesResponse]:
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

    def __iter__(self) -> Iterator[file.File]:
        for page in self.pages:
            yield from page.files

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFilesAsyncPager:
    """A pager for iterating through ``list_files`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListFilesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``files`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFiles`` requests and continue to iterate
    through the ``files`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListFilesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[file.ListFilesResponse]],
        request: file.ListFilesRequest,
        response: file.ListFilesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListFilesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListFilesResponse):
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
        self._request = file.ListFilesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[file.ListFilesResponse]:
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

    def __aiter__(self) -> AsyncIterator[file.File]:
        async def async_generator():
            async for page in self.pages:
                for response in page.files:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTagsPager:
    """A pager for iterating through ``list_tags`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListTagsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``tags`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTags`` requests and continue to iterate
    through the ``tags`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListTagsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., tag.ListTagsResponse],
        request: tag.ListTagsRequest,
        response: tag.ListTagsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListTagsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListTagsResponse):
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
        self._request = tag.ListTagsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[tag.ListTagsResponse]:
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

    def __iter__(self) -> Iterator[tag.Tag]:
        for page in self.pages:
            yield from page.tags

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTagsAsyncPager:
    """A pager for iterating through ``list_tags`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListTagsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``tags`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTags`` requests and continue to iterate
    through the ``tags`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListTagsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[tag.ListTagsResponse]],
        request: tag.ListTagsRequest,
        response: tag.ListTagsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListTagsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListTagsResponse):
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
        self._request = tag.ListTagsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[tag.ListTagsResponse]:
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

    def __aiter__(self) -> AsyncIterator[tag.Tag]:
        async def async_generator():
            async for page in self.pages:
                for response in page.tags:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRulesPager:
    """A pager for iterating through ``list_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListRulesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rules`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRules`` requests and continue to iterate
    through the ``rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., rule.ListRulesResponse],
        request: rule.ListRulesRequest,
        response: rule.ListRulesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListRulesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListRulesResponse):
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
        self._request = rule.ListRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[rule.ListRulesResponse]:
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

    def __iter__(self) -> Iterator[rule.Rule]:
        for page in self.pages:
            yield from page.rules

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRulesAsyncPager:
    """A pager for iterating through ``list_rules`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListRulesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rules`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRules`` requests and continue to iterate
    through the ``rules`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListRulesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[rule.ListRulesResponse]],
        request: rule.ListRulesRequest,
        response: rule.ListRulesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListRulesRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListRulesResponse):
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
        self._request = rule.ListRulesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[rule.ListRulesResponse]:
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

    def __aiter__(self) -> AsyncIterator[rule.Rule]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rules:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAttachmentsPager:
    """A pager for iterating through ``list_attachments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListAttachmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``attachments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAttachments`` requests and continue to iterate
    through the ``attachments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListAttachmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., attachment.ListAttachmentsResponse],
        request: attachment.ListAttachmentsRequest,
        response: attachment.ListAttachmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListAttachmentsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListAttachmentsResponse):
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
        self._request = attachment.ListAttachmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[attachment.ListAttachmentsResponse]:
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

    def __iter__(self) -> Iterator[attachment.Attachment]:
        for page in self.pages:
            yield from page.attachments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAttachmentsAsyncPager:
    """A pager for iterating through ``list_attachments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.artifactregistry_v1.types.ListAttachmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``attachments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAttachments`` requests and continue to iterate
    through the ``attachments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.artifactregistry_v1.types.ListAttachmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[attachment.ListAttachmentsResponse]],
        request: attachment.ListAttachmentsRequest,
        response: attachment.ListAttachmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.artifactregistry_v1.types.ListAttachmentsRequest):
                The initial request object.
            response (google.cloud.artifactregistry_v1.types.ListAttachmentsResponse):
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
        self._request = attachment.ListAttachmentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[attachment.ListAttachmentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[attachment.Attachment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.attachments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
