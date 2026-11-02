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

from google.cloud.bare_metal_solution_v2.types import (
    instance,
    lun,
    network,
    nfs_share,
    osimage,
    provisioning,
    ssh_key,
    volume,
    volume_snapshot,
)


class ListInstancesPager:
    """A pager for iterating through ``list_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListInstancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``instances`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListInstances`` requests and continue to iterate
    through the ``instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., instance.ListInstancesResponse],
        request: instance.ListInstancesRequest,
        response: instance.ListInstancesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListInstancesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListInstancesResponse):
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
        self._request = instance.ListInstancesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[instance.ListInstancesResponse]:
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

    def __iter__(self) -> Iterator[instance.Instance]:
        for page in self.pages:
            yield from page.instances

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListInstancesAsyncPager:
    """A pager for iterating through ``list_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListInstancesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``instances`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListInstances`` requests and continue to iterate
    through the ``instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[instance.ListInstancesResponse]],
        request: instance.ListInstancesRequest,
        response: instance.ListInstancesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListInstancesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListInstancesResponse):
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
        self._request = instance.ListInstancesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[instance.ListInstancesResponse]:
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

    def __aiter__(self) -> AsyncIterator[instance.Instance]:
        async def async_generator():
            async for page in self.pages:
                for response in page.instances:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSSHKeysPager:
    """A pager for iterating through ``list_ssh_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListSSHKeysResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``ssh_keys`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSSHKeys`` requests and continue to iterate
    through the ``ssh_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListSSHKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., ssh_key.ListSSHKeysResponse],
        request: ssh_key.ListSSHKeysRequest,
        response: ssh_key.ListSSHKeysResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListSSHKeysRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListSSHKeysResponse):
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
        self._request = ssh_key.ListSSHKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[ssh_key.ListSSHKeysResponse]:
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

    def __iter__(self) -> Iterator[ssh_key.SSHKey]:
        for page in self.pages:
            yield from page.ssh_keys

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSSHKeysAsyncPager:
    """A pager for iterating through ``list_ssh_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListSSHKeysResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``ssh_keys`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSSHKeys`` requests and continue to iterate
    through the ``ssh_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListSSHKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[ssh_key.ListSSHKeysResponse]],
        request: ssh_key.ListSSHKeysRequest,
        response: ssh_key.ListSSHKeysResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListSSHKeysRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListSSHKeysResponse):
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
        self._request = ssh_key.ListSSHKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[ssh_key.ListSSHKeysResponse]:
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

    def __aiter__(self) -> AsyncIterator[ssh_key.SSHKey]:
        async def async_generator():
            async for page in self.pages:
                for response in page.ssh_keys:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumesPager:
    """A pager for iterating through ``list_volumes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListVolumesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``volumes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVolumes`` requests and continue to iterate
    through the ``volumes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListVolumesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., volume.ListVolumesResponse],
        request: volume.ListVolumesRequest,
        response: volume.ListVolumesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListVolumesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListVolumesResponse):
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
        self._request = volume.ListVolumesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[volume.ListVolumesResponse]:
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

    def __iter__(self) -> Iterator[volume.Volume]:
        for page in self.pages:
            yield from page.volumes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumesAsyncPager:
    """A pager for iterating through ``list_volumes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListVolumesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``volumes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVolumes`` requests and continue to iterate
    through the ``volumes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListVolumesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[volume.ListVolumesResponse]],
        request: volume.ListVolumesRequest,
        response: volume.ListVolumesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListVolumesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListVolumesResponse):
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
        self._request = volume.ListVolumesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[volume.ListVolumesResponse]:
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

    def __aiter__(self) -> AsyncIterator[volume.Volume]:
        async def async_generator():
            async for page in self.pages:
                for response in page.volumes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNetworksPager:
    """A pager for iterating through ``list_networks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListNetworksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``networks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNetworks`` requests and continue to iterate
    through the ``networks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListNetworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., network.ListNetworksResponse],
        request: network.ListNetworksRequest,
        response: network.ListNetworksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListNetworksRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListNetworksResponse):
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
        self._request = network.ListNetworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[network.ListNetworksResponse]:
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

    def __iter__(self) -> Iterator[network.Network]:
        for page in self.pages:
            yield from page.networks

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNetworksAsyncPager:
    """A pager for iterating through ``list_networks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListNetworksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``networks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNetworks`` requests and continue to iterate
    through the ``networks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListNetworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[network.ListNetworksResponse]],
        request: network.ListNetworksRequest,
        response: network.ListNetworksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListNetworksRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListNetworksResponse):
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
        self._request = network.ListNetworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[network.ListNetworksResponse]:
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

    def __aiter__(self) -> AsyncIterator[network.Network]:
        async def async_generator():
            async for page in self.pages:
                for response in page.networks:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumeSnapshotsPager:
    """A pager for iterating through ``list_volume_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``volume_snapshots`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVolumeSnapshots`` requests and continue to iterate
    through the ``volume_snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., volume_snapshot.ListVolumeSnapshotsResponse],
        request: volume_snapshot.ListVolumeSnapshotsRequest,
        response: volume_snapshot.ListVolumeSnapshotsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsResponse):
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
        self._request = volume_snapshot.ListVolumeSnapshotsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[volume_snapshot.ListVolumeSnapshotsResponse]:
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

    def __iter__(self) -> Iterator[volume_snapshot.VolumeSnapshot]:
        for page in self.pages:
            yield from page.volume_snapshots

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVolumeSnapshotsAsyncPager:
    """A pager for iterating through ``list_volume_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``volume_snapshots`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVolumeSnapshots`` requests and continue to iterate
    through the ``volume_snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[volume_snapshot.ListVolumeSnapshotsResponse]],
        request: volume_snapshot.ListVolumeSnapshotsRequest,
        response: volume_snapshot.ListVolumeSnapshotsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListVolumeSnapshotsResponse):
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
        self._request = volume_snapshot.ListVolumeSnapshotsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[volume_snapshot.ListVolumeSnapshotsResponse]:
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

    def __aiter__(self) -> AsyncIterator[volume_snapshot.VolumeSnapshot]:
        async def async_generator():
            async for page in self.pages:
                for response in page.volume_snapshots:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLunsPager:
    """A pager for iterating through ``list_luns`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListLunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``luns`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLuns`` requests and continue to iterate
    through the ``luns`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListLunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., lun.ListLunsResponse],
        request: lun.ListLunsRequest,
        response: lun.ListLunsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListLunsRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListLunsResponse):
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
        self._request = lun.ListLunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[lun.ListLunsResponse]:
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

    def __iter__(self) -> Iterator[lun.Lun]:
        for page in self.pages:
            yield from page.luns

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLunsAsyncPager:
    """A pager for iterating through ``list_luns`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListLunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``luns`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLuns`` requests and continue to iterate
    through the ``luns`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListLunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[lun.ListLunsResponse]],
        request: lun.ListLunsRequest,
        response: lun.ListLunsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListLunsRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListLunsResponse):
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
        self._request = lun.ListLunsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[lun.ListLunsResponse]:
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

    def __aiter__(self) -> AsyncIterator[lun.Lun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.luns:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNfsSharesPager:
    """A pager for iterating through ``list_nfs_shares`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListNfsSharesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``nfs_shares`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNfsShares`` requests and continue to iterate
    through the ``nfs_shares`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListNfsSharesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., nfs_share.ListNfsSharesResponse],
        request: nfs_share.ListNfsSharesRequest,
        response: nfs_share.ListNfsSharesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListNfsSharesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListNfsSharesResponse):
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
        self._request = nfs_share.ListNfsSharesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[nfs_share.ListNfsSharesResponse]:
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

    def __iter__(self) -> Iterator[nfs_share.NfsShare]:
        for page in self.pages:
            yield from page.nfs_shares

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListNfsSharesAsyncPager:
    """A pager for iterating through ``list_nfs_shares`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListNfsSharesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``nfs_shares`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNfsShares`` requests and continue to iterate
    through the ``nfs_shares`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListNfsSharesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[nfs_share.ListNfsSharesResponse]],
        request: nfs_share.ListNfsSharesRequest,
        response: nfs_share.ListNfsSharesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListNfsSharesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListNfsSharesResponse):
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
        self._request = nfs_share.ListNfsSharesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[nfs_share.ListNfsSharesResponse]:
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

    def __aiter__(self) -> AsyncIterator[nfs_share.NfsShare]:
        async def async_generator():
            async for page in self.pages:
                for response in page.nfs_shares:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProvisioningQuotasPager:
    """A pager for iterating through ``list_provisioning_quotas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``provisioning_quotas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProvisioningQuotas`` requests and continue to iterate
    through the ``provisioning_quotas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., provisioning.ListProvisioningQuotasResponse],
        request: provisioning.ListProvisioningQuotasRequest,
        response: provisioning.ListProvisioningQuotasResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasResponse):
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
        self._request = provisioning.ListProvisioningQuotasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[provisioning.ListProvisioningQuotasResponse]:
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

    def __iter__(self) -> Iterator[provisioning.ProvisioningQuota]:
        for page in self.pages:
            yield from page.provisioning_quotas

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProvisioningQuotasAsyncPager:
    """A pager for iterating through ``list_provisioning_quotas`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``provisioning_quotas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProvisioningQuotas`` requests and continue to iterate
    through the ``provisioning_quotas`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[provisioning.ListProvisioningQuotasResponse]],
        request: provisioning.ListProvisioningQuotasRequest,
        response: provisioning.ListProvisioningQuotasResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListProvisioningQuotasResponse):
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
        self._request = provisioning.ListProvisioningQuotasRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[provisioning.ListProvisioningQuotasResponse]:
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

    def __aiter__(self) -> AsyncIterator[provisioning.ProvisioningQuota]:
        async def async_generator():
            async for page in self.pages:
                for response in page.provisioning_quotas:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOSImagesPager:
    """A pager for iterating through ``list_os_images`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListOSImagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``os_images`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOSImages`` requests and continue to iterate
    through the ``os_images`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListOSImagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., osimage.ListOSImagesResponse],
        request: osimage.ListOSImagesRequest,
        response: osimage.ListOSImagesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListOSImagesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListOSImagesResponse):
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
        self._request = osimage.ListOSImagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[osimage.ListOSImagesResponse]:
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

    def __iter__(self) -> Iterator[osimage.OSImage]:
        for page in self.pages:
            yield from page.os_images

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOSImagesAsyncPager:
    """A pager for iterating through ``list_os_images`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.bare_metal_solution_v2.types.ListOSImagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``os_images`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOSImages`` requests and continue to iterate
    through the ``os_images`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.bare_metal_solution_v2.types.ListOSImagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[osimage.ListOSImagesResponse]],
        request: osimage.ListOSImagesRequest,
        response: osimage.ListOSImagesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.bare_metal_solution_v2.types.ListOSImagesRequest):
                The initial request object.
            response (google.cloud.bare_metal_solution_v2.types.ListOSImagesResponse):
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
        self._request = osimage.ListOSImagesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[osimage.ListOSImagesResponse]:
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

    def __aiter__(self) -> AsyncIterator[osimage.OSImage]:
        async def async_generator():
            async for page in self.pages:
                for response in page.os_images:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
