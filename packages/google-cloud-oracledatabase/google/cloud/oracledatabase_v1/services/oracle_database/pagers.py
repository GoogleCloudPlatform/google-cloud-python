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

from google.cloud.oracledatabase_v1.types import (
    autonomous_database,
    autonomous_database_character_set,
    autonomous_db_backup,
    autonomous_db_version,
    database,
    database_character_set,
    db_node,
    db_server,
    db_system,
    db_system_initial_storage_size,
    db_system_shape,
    db_version,
    entitlement,
    exadata_infra,
    exadb_vm_cluster,
    exascale_db_storage_vault,
    gi_version,
    goldengate_connection,
    goldengate_connection_assignment,
    goldengate_connection_type,
    goldengate_deployment,
    goldengate_deployment_environment,
    goldengate_deployment_type,
    goldengate_deployment_version,
    minor_version,
    odb_dns_zone,
    odb_network,
    odb_subnet,
    oracledatabase,
    pluggable_database,
    vm_cluster,
)


class ListCloudExadataInfrastructuresPager:
    """A pager for iterating through ``list_cloud_exadata_infrastructures`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``cloud_exadata_infrastructures`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCloudExadataInfrastructures`` requests and continue to iterate
    through the ``cloud_exadata_infrastructures`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListCloudExadataInfrastructuresResponse],
        request: oracledatabase.ListCloudExadataInfrastructuresRequest,
        response: oracledatabase.ListCloudExadataInfrastructuresResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresResponse):
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
        self._request = oracledatabase.ListCloudExadataInfrastructuresRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListCloudExadataInfrastructuresResponse]:
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

    def __iter__(self) -> Iterator[exadata_infra.CloudExadataInfrastructure]:
        for page in self.pages:
            yield from page.cloud_exadata_infrastructures

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCloudExadataInfrastructuresAsyncPager:
    """A pager for iterating through ``list_cloud_exadata_infrastructures`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``cloud_exadata_infrastructures`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCloudExadataInfrastructures`` requests and continue to iterate
    through the ``cloud_exadata_infrastructures`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[oracledatabase.ListCloudExadataInfrastructuresResponse]
        ],
        request: oracledatabase.ListCloudExadataInfrastructuresRequest,
        response: oracledatabase.ListCloudExadataInfrastructuresResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListCloudExadataInfrastructuresResponse):
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
        self._request = oracledatabase.ListCloudExadataInfrastructuresRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[oracledatabase.ListCloudExadataInfrastructuresResponse]:
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

    def __aiter__(self) -> AsyncIterator[exadata_infra.CloudExadataInfrastructure]:
        async def async_generator():
            async for page in self.pages:
                for response in page.cloud_exadata_infrastructures:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCloudVmClustersPager:
    """A pager for iterating through ``list_cloud_vm_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListCloudVmClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``cloud_vm_clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCloudVmClusters`` requests and continue to iterate
    through the ``cloud_vm_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListCloudVmClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListCloudVmClustersResponse],
        request: oracledatabase.ListCloudVmClustersRequest,
        response: oracledatabase.ListCloudVmClustersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListCloudVmClustersRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListCloudVmClustersResponse):
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
        self._request = oracledatabase.ListCloudVmClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListCloudVmClustersResponse]:
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

    def __iter__(self) -> Iterator[vm_cluster.CloudVmCluster]:
        for page in self.pages:
            yield from page.cloud_vm_clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCloudVmClustersAsyncPager:
    """A pager for iterating through ``list_cloud_vm_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListCloudVmClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``cloud_vm_clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCloudVmClusters`` requests and continue to iterate
    through the ``cloud_vm_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListCloudVmClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[oracledatabase.ListCloudVmClustersResponse]],
        request: oracledatabase.ListCloudVmClustersRequest,
        response: oracledatabase.ListCloudVmClustersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListCloudVmClustersRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListCloudVmClustersResponse):
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
        self._request = oracledatabase.ListCloudVmClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[oracledatabase.ListCloudVmClustersResponse]:
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

    def __aiter__(self) -> AsyncIterator[vm_cluster.CloudVmCluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.cloud_vm_clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntitlementsPager:
    """A pager for iterating through ``list_entitlements`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListEntitlementsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``entitlements`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEntitlements`` requests and continue to iterate
    through the ``entitlements`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListEntitlementsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListEntitlementsResponse],
        request: oracledatabase.ListEntitlementsRequest,
        response: oracledatabase.ListEntitlementsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListEntitlementsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListEntitlementsResponse):
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
        self._request = oracledatabase.ListEntitlementsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListEntitlementsResponse]:
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

    def __iter__(self) -> Iterator[entitlement.Entitlement]:
        for page in self.pages:
            yield from page.entitlements

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListEntitlementsAsyncPager:
    """A pager for iterating through ``list_entitlements`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListEntitlementsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``entitlements`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEntitlements`` requests and continue to iterate
    through the ``entitlements`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListEntitlementsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[oracledatabase.ListEntitlementsResponse]],
        request: oracledatabase.ListEntitlementsRequest,
        response: oracledatabase.ListEntitlementsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListEntitlementsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListEntitlementsResponse):
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
        self._request = oracledatabase.ListEntitlementsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[oracledatabase.ListEntitlementsResponse]:
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

    def __aiter__(self) -> AsyncIterator[entitlement.Entitlement]:
        async def async_generator():
            async for page in self.pages:
                for response in page.entitlements:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbServersPager:
    """A pager for iterating through ``list_db_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbServersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``db_servers`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDbServers`` requests and continue to iterate
    through the ``db_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListDbServersResponse],
        request: oracledatabase.ListDbServersRequest,
        response: oracledatabase.ListDbServersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbServersRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbServersResponse):
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
        self._request = oracledatabase.ListDbServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListDbServersResponse]:
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

    def __iter__(self) -> Iterator[db_server.DbServer]:
        for page in self.pages:
            yield from page.db_servers

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbServersAsyncPager:
    """A pager for iterating through ``list_db_servers`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbServersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``db_servers`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDbServers`` requests and continue to iterate
    through the ``db_servers`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbServersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[oracledatabase.ListDbServersResponse]],
        request: oracledatabase.ListDbServersRequest,
        response: oracledatabase.ListDbServersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbServersRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbServersResponse):
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
        self._request = oracledatabase.ListDbServersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[oracledatabase.ListDbServersResponse]:
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

    def __aiter__(self) -> AsyncIterator[db_server.DbServer]:
        async def async_generator():
            async for page in self.pages:
                for response in page.db_servers:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbNodesPager:
    """A pager for iterating through ``list_db_nodes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbNodesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``db_nodes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDbNodes`` requests and continue to iterate
    through the ``db_nodes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbNodesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListDbNodesResponse],
        request: oracledatabase.ListDbNodesRequest,
        response: oracledatabase.ListDbNodesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbNodesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbNodesResponse):
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
        self._request = oracledatabase.ListDbNodesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListDbNodesResponse]:
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

    def __iter__(self) -> Iterator[db_node.DbNode]:
        for page in self.pages:
            yield from page.db_nodes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbNodesAsyncPager:
    """A pager for iterating through ``list_db_nodes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbNodesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``db_nodes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDbNodes`` requests and continue to iterate
    through the ``db_nodes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbNodesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[oracledatabase.ListDbNodesResponse]],
        request: oracledatabase.ListDbNodesRequest,
        response: oracledatabase.ListDbNodesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbNodesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbNodesResponse):
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
        self._request = oracledatabase.ListDbNodesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[oracledatabase.ListDbNodesResponse]:
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

    def __aiter__(self) -> AsyncIterator[db_node.DbNode]:
        async def async_generator():
            async for page in self.pages:
                for response in page.db_nodes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGiVersionsPager:
    """A pager for iterating through ``list_gi_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGiVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``gi_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGiVersions`` requests and continue to iterate
    through the ``gi_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGiVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListGiVersionsResponse],
        request: oracledatabase.ListGiVersionsRequest,
        response: oracledatabase.ListGiVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGiVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGiVersionsResponse):
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
        self._request = oracledatabase.ListGiVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListGiVersionsResponse]:
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

    def __iter__(self) -> Iterator[gi_version.GiVersion]:
        for page in self.pages:
            yield from page.gi_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGiVersionsAsyncPager:
    """A pager for iterating through ``list_gi_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGiVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``gi_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGiVersions`` requests and continue to iterate
    through the ``gi_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGiVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[oracledatabase.ListGiVersionsResponse]],
        request: oracledatabase.ListGiVersionsRequest,
        response: oracledatabase.ListGiVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGiVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGiVersionsResponse):
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
        self._request = oracledatabase.ListGiVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[oracledatabase.ListGiVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[gi_version.GiVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.gi_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMinorVersionsPager:
    """A pager for iterating through ``list_minor_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListMinorVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``minor_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMinorVersions`` requests and continue to iterate
    through the ``minor_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListMinorVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., minor_version.ListMinorVersionsResponse],
        request: minor_version.ListMinorVersionsRequest,
        response: minor_version.ListMinorVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListMinorVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListMinorVersionsResponse):
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
        self._request = minor_version.ListMinorVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[minor_version.ListMinorVersionsResponse]:
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

    def __iter__(self) -> Iterator[minor_version.MinorVersion]:
        for page in self.pages:
            yield from page.minor_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMinorVersionsAsyncPager:
    """A pager for iterating through ``list_minor_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListMinorVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``minor_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMinorVersions`` requests and continue to iterate
    through the ``minor_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListMinorVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[minor_version.ListMinorVersionsResponse]],
        request: minor_version.ListMinorVersionsRequest,
        response: minor_version.ListMinorVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListMinorVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListMinorVersionsResponse):
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
        self._request = minor_version.ListMinorVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[minor_version.ListMinorVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[minor_version.MinorVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.minor_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbSystemShapesPager:
    """A pager for iterating through ``list_db_system_shapes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbSystemShapesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``db_system_shapes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDbSystemShapes`` requests and continue to iterate
    through the ``db_system_shapes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbSystemShapesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListDbSystemShapesResponse],
        request: oracledatabase.ListDbSystemShapesRequest,
        response: oracledatabase.ListDbSystemShapesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbSystemShapesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbSystemShapesResponse):
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
        self._request = oracledatabase.ListDbSystemShapesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListDbSystemShapesResponse]:
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

    def __iter__(self) -> Iterator[db_system_shape.DbSystemShape]:
        for page in self.pages:
            yield from page.db_system_shapes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbSystemShapesAsyncPager:
    """A pager for iterating through ``list_db_system_shapes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbSystemShapesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``db_system_shapes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDbSystemShapes`` requests and continue to iterate
    through the ``db_system_shapes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbSystemShapesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[oracledatabase.ListDbSystemShapesResponse]],
        request: oracledatabase.ListDbSystemShapesRequest,
        response: oracledatabase.ListDbSystemShapesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbSystemShapesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbSystemShapesResponse):
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
        self._request = oracledatabase.ListDbSystemShapesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[oracledatabase.ListDbSystemShapesResponse]:
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

    def __aiter__(self) -> AsyncIterator[db_system_shape.DbSystemShape]:
        async def async_generator():
            async for page in self.pages:
                for response in page.db_system_shapes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDatabasesPager:
    """A pager for iterating through ``list_autonomous_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``autonomous_databases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutonomousDatabases`` requests and continue to iterate
    through the ``autonomous_databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListAutonomousDatabasesResponse],
        request: oracledatabase.ListAutonomousDatabasesRequest,
        response: oracledatabase.ListAutonomousDatabasesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesResponse):
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
        self._request = oracledatabase.ListAutonomousDatabasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListAutonomousDatabasesResponse]:
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

    def __iter__(self) -> Iterator[autonomous_database.AutonomousDatabase]:
        for page in self.pages:
            yield from page.autonomous_databases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDatabasesAsyncPager:
    """A pager for iterating through ``list_autonomous_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``autonomous_databases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutonomousDatabases`` requests and continue to iterate
    through the ``autonomous_databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[oracledatabase.ListAutonomousDatabasesResponse]
        ],
        request: oracledatabase.ListAutonomousDatabasesRequest,
        response: oracledatabase.ListAutonomousDatabasesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDatabasesResponse):
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
        self._request = oracledatabase.ListAutonomousDatabasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[oracledatabase.ListAutonomousDatabasesResponse]:
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

    def __aiter__(self) -> AsyncIterator[autonomous_database.AutonomousDatabase]:
        async def async_generator():
            async for page in self.pages:
                for response in page.autonomous_databases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDbVersionsPager:
    """A pager for iterating through ``list_autonomous_db_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``autonomous_db_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutonomousDbVersions`` requests and continue to iterate
    through the ``autonomous_db_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListAutonomousDbVersionsResponse],
        request: oracledatabase.ListAutonomousDbVersionsRequest,
        response: oracledatabase.ListAutonomousDbVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse):
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
        self._request = oracledatabase.ListAutonomousDbVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListAutonomousDbVersionsResponse]:
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

    def __iter__(self) -> Iterator[autonomous_db_version.AutonomousDbVersion]:
        for page in self.pages:
            yield from page.autonomous_db_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDbVersionsAsyncPager:
    """A pager for iterating through ``list_autonomous_db_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``autonomous_db_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutonomousDbVersions`` requests and continue to iterate
    through the ``autonomous_db_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[oracledatabase.ListAutonomousDbVersionsResponse]
        ],
        request: oracledatabase.ListAutonomousDbVersionsRequest,
        response: oracledatabase.ListAutonomousDbVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse):
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
        self._request = oracledatabase.ListAutonomousDbVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[oracledatabase.ListAutonomousDbVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[autonomous_db_version.AutonomousDbVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.autonomous_db_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDatabaseCharacterSetsPager:
    """A pager for iterating through ``list_autonomous_database_character_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``autonomous_database_character_sets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutonomousDatabaseCharacterSets`` requests and continue to iterate
    through the ``autonomous_database_character_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., oracledatabase.ListAutonomousDatabaseCharacterSetsResponse
        ],
        request: oracledatabase.ListAutonomousDatabaseCharacterSetsRequest,
        response: oracledatabase.ListAutonomousDatabaseCharacterSetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsResponse):
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
        self._request = oracledatabase.ListAutonomousDatabaseCharacterSetsRequest(
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
    ) -> Iterator[oracledatabase.ListAutonomousDatabaseCharacterSetsResponse]:
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
    ) -> Iterator[autonomous_database_character_set.AutonomousDatabaseCharacterSet]:
        for page in self.pages:
            yield from page.autonomous_database_character_sets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDatabaseCharacterSetsAsyncPager:
    """A pager for iterating through ``list_autonomous_database_character_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``autonomous_database_character_sets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutonomousDatabaseCharacterSets`` requests and continue to iterate
    through the ``autonomous_database_character_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[oracledatabase.ListAutonomousDatabaseCharacterSetsResponse]
        ],
        request: oracledatabase.ListAutonomousDatabaseCharacterSetsRequest,
        response: oracledatabase.ListAutonomousDatabaseCharacterSetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseCharacterSetsResponse):
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
        self._request = oracledatabase.ListAutonomousDatabaseCharacterSetsRequest(
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
    ) -> AsyncIterator[oracledatabase.ListAutonomousDatabaseCharacterSetsResponse]:
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
        autonomous_database_character_set.AutonomousDatabaseCharacterSet
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.autonomous_database_character_sets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDatabaseBackupsPager:
    """A pager for iterating through ``list_autonomous_database_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``autonomous_database_backups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutonomousDatabaseBackups`` requests and continue to iterate
    through the ``autonomous_database_backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListAutonomousDatabaseBackupsResponse],
        request: oracledatabase.ListAutonomousDatabaseBackupsRequest,
        response: oracledatabase.ListAutonomousDatabaseBackupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsResponse):
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
        self._request = oracledatabase.ListAutonomousDatabaseBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListAutonomousDatabaseBackupsResponse]:
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

    def __iter__(self) -> Iterator[autonomous_db_backup.AutonomousDatabaseBackup]:
        for page in self.pages:
            yield from page.autonomous_database_backups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutonomousDatabaseBackupsAsyncPager:
    """A pager for iterating through ``list_autonomous_database_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``autonomous_database_backups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutonomousDatabaseBackups`` requests and continue to iterate
    through the ``autonomous_database_backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[oracledatabase.ListAutonomousDatabaseBackupsResponse]
        ],
        request: oracledatabase.ListAutonomousDatabaseBackupsRequest,
        response: oracledatabase.ListAutonomousDatabaseBackupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListAutonomousDatabaseBackupsResponse):
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
        self._request = oracledatabase.ListAutonomousDatabaseBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[oracledatabase.ListAutonomousDatabaseBackupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[autonomous_db_backup.AutonomousDatabaseBackup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.autonomous_database_backups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOdbNetworksPager:
    """A pager for iterating through ``list_odb_networks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListOdbNetworksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``odb_networks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOdbNetworks`` requests and continue to iterate
    through the ``odb_networks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListOdbNetworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., odb_network.ListOdbNetworksResponse],
        request: odb_network.ListOdbNetworksRequest,
        response: odb_network.ListOdbNetworksResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListOdbNetworksRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListOdbNetworksResponse):
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
        self._request = odb_network.ListOdbNetworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[odb_network.ListOdbNetworksResponse]:
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

    def __iter__(self) -> Iterator[odb_network.OdbNetwork]:
        for page in self.pages:
            yield from page.odb_networks

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOdbNetworksAsyncPager:
    """A pager for iterating through ``list_odb_networks`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListOdbNetworksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``odb_networks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOdbNetworks`` requests and continue to iterate
    through the ``odb_networks`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListOdbNetworksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[odb_network.ListOdbNetworksResponse]],
        request: odb_network.ListOdbNetworksRequest,
        response: odb_network.ListOdbNetworksResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListOdbNetworksRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListOdbNetworksResponse):
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
        self._request = odb_network.ListOdbNetworksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[odb_network.ListOdbNetworksResponse]:
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

    def __aiter__(self) -> AsyncIterator[odb_network.OdbNetwork]:
        async def async_generator():
            async for page in self.pages:
                for response in page.odb_networks:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOdbSubnetsPager:
    """A pager for iterating through ``list_odb_subnets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListOdbSubnetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``odb_subnets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOdbSubnets`` requests and continue to iterate
    through the ``odb_subnets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListOdbSubnetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., odb_subnet.ListOdbSubnetsResponse],
        request: odb_subnet.ListOdbSubnetsRequest,
        response: odb_subnet.ListOdbSubnetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListOdbSubnetsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListOdbSubnetsResponse):
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
        self._request = odb_subnet.ListOdbSubnetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[odb_subnet.ListOdbSubnetsResponse]:
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

    def __iter__(self) -> Iterator[odb_subnet.OdbSubnet]:
        for page in self.pages:
            yield from page.odb_subnets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOdbSubnetsAsyncPager:
    """A pager for iterating through ``list_odb_subnets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListOdbSubnetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``odb_subnets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOdbSubnets`` requests and continue to iterate
    through the ``odb_subnets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListOdbSubnetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[odb_subnet.ListOdbSubnetsResponse]],
        request: odb_subnet.ListOdbSubnetsRequest,
        response: odb_subnet.ListOdbSubnetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListOdbSubnetsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListOdbSubnetsResponse):
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
        self._request = odb_subnet.ListOdbSubnetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[odb_subnet.ListOdbSubnetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[odb_subnet.OdbSubnet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.odb_subnets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOdbDnsZonesPager:
    """A pager for iterating through ``list_odb_dns_zones`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListOdbDnsZonesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``odb_dns_zones`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOdbDnsZones`` requests and continue to iterate
    through the ``odb_dns_zones`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListOdbDnsZonesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., odb_dns_zone.ListOdbDnsZonesResponse],
        request: odb_dns_zone.ListOdbDnsZonesRequest,
        response: odb_dns_zone.ListOdbDnsZonesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListOdbDnsZonesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListOdbDnsZonesResponse):
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
        self._request = odb_dns_zone.ListOdbDnsZonesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[odb_dns_zone.ListOdbDnsZonesResponse]:
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

    def __iter__(self) -> Iterator[odb_dns_zone.OdbDnsZone]:
        for page in self.pages:
            yield from page.odb_dns_zones

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListOdbDnsZonesAsyncPager:
    """A pager for iterating through ``list_odb_dns_zones`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListOdbDnsZonesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``odb_dns_zones`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListOdbDnsZones`` requests and continue to iterate
    through the ``odb_dns_zones`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListOdbDnsZonesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[odb_dns_zone.ListOdbDnsZonesResponse]],
        request: odb_dns_zone.ListOdbDnsZonesRequest,
        response: odb_dns_zone.ListOdbDnsZonesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListOdbDnsZonesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListOdbDnsZonesResponse):
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
        self._request = odb_dns_zone.ListOdbDnsZonesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[odb_dns_zone.ListOdbDnsZonesResponse]:
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

    def __aiter__(self) -> AsyncIterator[odb_dns_zone.OdbDnsZone]:
        async def async_generator():
            async for page in self.pages:
                for response in page.odb_dns_zones:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExadbVmClustersPager:
    """A pager for iterating through ``list_exadb_vm_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListExadbVmClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``exadb_vm_clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExadbVmClusters`` requests and continue to iterate
    through the ``exadb_vm_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListExadbVmClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., oracledatabase.ListExadbVmClustersResponse],
        request: oracledatabase.ListExadbVmClustersRequest,
        response: oracledatabase.ListExadbVmClustersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListExadbVmClustersRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListExadbVmClustersResponse):
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
        self._request = oracledatabase.ListExadbVmClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[oracledatabase.ListExadbVmClustersResponse]:
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

    def __iter__(self) -> Iterator[exadb_vm_cluster.ExadbVmCluster]:
        for page in self.pages:
            yield from page.exadb_vm_clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExadbVmClustersAsyncPager:
    """A pager for iterating through ``list_exadb_vm_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListExadbVmClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``exadb_vm_clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExadbVmClusters`` requests and continue to iterate
    through the ``exadb_vm_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListExadbVmClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[oracledatabase.ListExadbVmClustersResponse]],
        request: oracledatabase.ListExadbVmClustersRequest,
        response: oracledatabase.ListExadbVmClustersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListExadbVmClustersRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListExadbVmClustersResponse):
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
        self._request = oracledatabase.ListExadbVmClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[oracledatabase.ListExadbVmClustersResponse]:
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

    def __aiter__(self) -> AsyncIterator[exadb_vm_cluster.ExadbVmCluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.exadb_vm_clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExascaleDbStorageVaultsPager:
    """A pager for iterating through ``list_exascale_db_storage_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``exascale_db_storage_vaults`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListExascaleDbStorageVaults`` requests and continue to iterate
    through the ``exascale_db_storage_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse
        ],
        request: exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest,
        response: exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsResponse):
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
        self._request = exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest(
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
    ) -> Iterator[exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse]:
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

    def __iter__(self) -> Iterator[exascale_db_storage_vault.ExascaleDbStorageVault]:
        for page in self.pages:
            yield from page.exascale_db_storage_vaults

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListExascaleDbStorageVaultsAsyncPager:
    """A pager for iterating through ``list_exascale_db_storage_vaults`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``exascale_db_storage_vaults`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListExascaleDbStorageVaults`` requests and continue to iterate
    through the ``exascale_db_storage_vaults`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse],
        ],
        request: exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest,
        response: exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsResponse):
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
        self._request = exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest(
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
    ) -> AsyncIterator[exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse]:
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
    ) -> AsyncIterator[exascale_db_storage_vault.ExascaleDbStorageVault]:
        async def async_generator():
            async for page in self.pages:
                for response in page.exascale_db_storage_vaults:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbSystemInitialStorageSizesPager:
    """A pager for iterating through ``list_db_system_initial_storage_sizes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``db_system_initial_storage_sizes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDbSystemInitialStorageSizes`` requests and continue to iterate
    through the ``db_system_initial_storage_sizes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse
        ],
        request: db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest,
        response: db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesResponse):
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
            db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest(
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
        db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse
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
    ) -> Iterator[db_system_initial_storage_size.DbSystemInitialStorageSize]:
        for page in self.pages:
            yield from page.db_system_initial_storage_sizes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbSystemInitialStorageSizesAsyncPager:
    """A pager for iterating through ``list_db_system_initial_storage_sizes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``db_system_initial_storage_sizes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDbSystemInitialStorageSizes`` requests and continue to iterate
    through the ``db_system_initial_storage_sizes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse
            ],
        ],
        request: db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest,
        response: db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbSystemInitialStorageSizesResponse):
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
            db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest(
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
        db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse
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
    ) -> AsyncIterator[db_system_initial_storage_size.DbSystemInitialStorageSize]:
        async def async_generator():
            async for page in self.pages:
                for response in page.db_system_initial_storage_sizes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatabasesPager:
    """A pager for iterating through ``list_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDatabasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``databases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDatabases`` requests and continue to iterate
    through the ``databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., database.ListDatabasesResponse],
        request: database.ListDatabasesRequest,
        response: database.ListDatabasesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDatabasesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDatabasesResponse):
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
        self._request = database.ListDatabasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[database.ListDatabasesResponse]:
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

    def __iter__(self) -> Iterator[database.Database]:
        for page in self.pages:
            yield from page.databases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatabasesAsyncPager:
    """A pager for iterating through ``list_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDatabasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``databases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDatabases`` requests and continue to iterate
    through the ``databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[database.ListDatabasesResponse]],
        request: database.ListDatabasesRequest,
        response: database.ListDatabasesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDatabasesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDatabasesResponse):
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
        self._request = database.ListDatabasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[database.ListDatabasesResponse]:
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

    def __aiter__(self) -> AsyncIterator[database.Database]:
        async def async_generator():
            async for page in self.pages:
                for response in page.databases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPluggableDatabasesPager:
    """A pager for iterating through ``list_pluggable_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListPluggableDatabasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``pluggable_databases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPluggableDatabases`` requests and continue to iterate
    through the ``pluggable_databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListPluggableDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., pluggable_database.ListPluggableDatabasesResponse],
        request: pluggable_database.ListPluggableDatabasesRequest,
        response: pluggable_database.ListPluggableDatabasesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListPluggableDatabasesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListPluggableDatabasesResponse):
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
        self._request = pluggable_database.ListPluggableDatabasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[pluggable_database.ListPluggableDatabasesResponse]:
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

    def __iter__(self) -> Iterator[pluggable_database.PluggableDatabase]:
        for page in self.pages:
            yield from page.pluggable_databases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPluggableDatabasesAsyncPager:
    """A pager for iterating through ``list_pluggable_databases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListPluggableDatabasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``pluggable_databases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListPluggableDatabases`` requests and continue to iterate
    through the ``pluggable_databases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListPluggableDatabasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[pluggable_database.ListPluggableDatabasesResponse]
        ],
        request: pluggable_database.ListPluggableDatabasesRequest,
        response: pluggable_database.ListPluggableDatabasesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListPluggableDatabasesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListPluggableDatabasesResponse):
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
        self._request = pluggable_database.ListPluggableDatabasesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[pluggable_database.ListPluggableDatabasesResponse]:
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

    def __aiter__(self) -> AsyncIterator[pluggable_database.PluggableDatabase]:
        async def async_generator():
            async for page in self.pages:
                for response in page.pluggable_databases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbSystemsPager:
    """A pager for iterating through ``list_db_systems`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbSystemsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``db_systems`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDbSystems`` requests and continue to iterate
    through the ``db_systems`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbSystemsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., db_system.ListDbSystemsResponse],
        request: db_system.ListDbSystemsRequest,
        response: db_system.ListDbSystemsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbSystemsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbSystemsResponse):
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
        self._request = db_system.ListDbSystemsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[db_system.ListDbSystemsResponse]:
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

    def __iter__(self) -> Iterator[db_system.DbSystem]:
        for page in self.pages:
            yield from page.db_systems

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbSystemsAsyncPager:
    """A pager for iterating through ``list_db_systems`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbSystemsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``db_systems`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDbSystems`` requests and continue to iterate
    through the ``db_systems`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbSystemsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[db_system.ListDbSystemsResponse]],
        request: db_system.ListDbSystemsRequest,
        response: db_system.ListDbSystemsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbSystemsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbSystemsResponse):
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
        self._request = db_system.ListDbSystemsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[db_system.ListDbSystemsResponse]:
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

    def __aiter__(self) -> AsyncIterator[db_system.DbSystem]:
        async def async_generator():
            async for page in self.pages:
                for response in page.db_systems:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentsPager:
    """A pager for iterating through ``list_goldengate_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``goldengate_deployments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoldengateDeployments`` requests and continue to iterate
    through the ``goldengate_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., goldengate_deployment.ListGoldengateDeploymentsResponse],
        request: goldengate_deployment.ListGoldengateDeploymentsRequest,
        response: goldengate_deployment.ListGoldengateDeploymentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsResponse):
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
        self._request = goldengate_deployment.ListGoldengateDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[goldengate_deployment.ListGoldengateDeploymentsResponse]:
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

    def __iter__(self) -> Iterator[goldengate_deployment.GoldengateDeployment]:
        for page in self.pages:
            yield from page.goldengate_deployments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentsAsyncPager:
    """A pager for iterating through ``list_goldengate_deployments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``goldengate_deployments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoldengateDeployments`` requests and continue to iterate
    through the ``goldengate_deployments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[goldengate_deployment.ListGoldengateDeploymentsResponse]
        ],
        request: goldengate_deployment.ListGoldengateDeploymentsRequest,
        response: goldengate_deployment.ListGoldengateDeploymentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentsResponse):
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
        self._request = goldengate_deployment.ListGoldengateDeploymentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[goldengate_deployment.ListGoldengateDeploymentsResponse]:
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

    def __aiter__(self) -> AsyncIterator[goldengate_deployment.GoldengateDeployment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.goldengate_deployments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateConnectionsPager:
    """A pager for iterating through ``list_goldengate_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``goldengate_connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoldengateConnections`` requests and continue to iterate
    through the ``goldengate_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., goldengate_connection.ListGoldengateConnectionsResponse],
        request: goldengate_connection.ListGoldengateConnectionsRequest,
        response: goldengate_connection.ListGoldengateConnectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsResponse):
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
        self._request = goldengate_connection.ListGoldengateConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[goldengate_connection.ListGoldengateConnectionsResponse]:
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

    def __iter__(self) -> Iterator[goldengate_connection.GoldengateConnection]:
        for page in self.pages:
            yield from page.goldengate_connections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateConnectionsAsyncPager:
    """A pager for iterating through ``list_goldengate_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``goldengate_connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoldengateConnections`` requests and continue to iterate
    through the ``goldengate_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[goldengate_connection.ListGoldengateConnectionsResponse]
        ],
        request: goldengate_connection.ListGoldengateConnectionsRequest,
        response: goldengate_connection.ListGoldengateConnectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionsResponse):
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
        self._request = goldengate_connection.ListGoldengateConnectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[goldengate_connection.ListGoldengateConnectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[goldengate_connection.GoldengateConnection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.goldengate_connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentVersionsPager:
    """A pager for iterating through ``list_goldengate_deployment_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``goldengate_deployment_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoldengateDeploymentVersions`` requests and continue to iterate
    through the ``goldengate_deployment_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse
        ],
        request: goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest,
        response: goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsResponse):
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
            goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest(
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
        goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse
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
    ) -> Iterator[goldengate_deployment_version.GoldengateDeploymentVersion]:
        for page in self.pages:
            yield from page.goldengate_deployment_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentVersionsAsyncPager:
    """A pager for iterating through ``list_goldengate_deployment_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``goldengate_deployment_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoldengateDeploymentVersions`` requests and continue to iterate
    through the ``goldengate_deployment_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse
            ],
        ],
        request: goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest,
        response: goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentVersionsResponse):
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
            goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest(
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
        goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse
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
    ) -> AsyncIterator[goldengate_deployment_version.GoldengateDeploymentVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.goldengate_deployment_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentTypesPager:
    """A pager for iterating through ``list_goldengate_deployment_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``goldengate_deployment_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoldengateDeploymentTypes`` requests and continue to iterate
    through the ``goldengate_deployment_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., goldengate_deployment_type.ListGoldengateDeploymentTypesResponse
        ],
        request: goldengate_deployment_type.ListGoldengateDeploymentTypesRequest,
        response: goldengate_deployment_type.ListGoldengateDeploymentTypesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesResponse):
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
        self._request = goldengate_deployment_type.ListGoldengateDeploymentTypesRequest(
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
    ) -> Iterator[goldengate_deployment_type.ListGoldengateDeploymentTypesResponse]:
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

    def __iter__(self) -> Iterator[goldengate_deployment_type.GoldengateDeploymentType]:
        for page in self.pages:
            yield from page.goldengate_deployment_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentTypesAsyncPager:
    """A pager for iterating through ``list_goldengate_deployment_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``goldengate_deployment_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoldengateDeploymentTypes`` requests and continue to iterate
    through the ``goldengate_deployment_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[goldengate_deployment_type.ListGoldengateDeploymentTypesResponse],
        ],
        request: goldengate_deployment_type.ListGoldengateDeploymentTypesRequest,
        response: goldengate_deployment_type.ListGoldengateDeploymentTypesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentTypesResponse):
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
        self._request = goldengate_deployment_type.ListGoldengateDeploymentTypesRequest(
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
        goldengate_deployment_type.ListGoldengateDeploymentTypesResponse
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
    ) -> AsyncIterator[goldengate_deployment_type.GoldengateDeploymentType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.goldengate_deployment_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentEnvironmentsPager:
    """A pager for iterating through ``list_goldengate_deployment_environments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``goldengate_deployment_environments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoldengateDeploymentEnvironments`` requests and continue to iterate
    through the ``goldengate_deployment_environments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse,
        ],
        request: goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest,
        response: goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsResponse):
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
        self._request = goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest(
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
        goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse
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
    ) -> Iterator[goldengate_deployment_environment.GoldengateDeploymentEnvironment]:
        for page in self.pages:
            yield from page.goldengate_deployment_environments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateDeploymentEnvironmentsAsyncPager:
    """A pager for iterating through ``list_goldengate_deployment_environments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``goldengate_deployment_environments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoldengateDeploymentEnvironments`` requests and continue to iterate
    through the ``goldengate_deployment_environments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse
            ],
        ],
        request: goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest,
        response: goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateDeploymentEnvironmentsResponse):
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
        self._request = goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest(
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
        goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse
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
        goldengate_deployment_environment.GoldengateDeploymentEnvironment
    ]:
        async def async_generator():
            async for page in self.pages:
                for response in page.goldengate_deployment_environments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateConnectionTypesPager:
    """A pager for iterating through ``list_goldengate_connection_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``goldengate_connection_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoldengateConnectionTypes`` requests and continue to iterate
    through the ``goldengate_connection_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., goldengate_connection_type.ListGoldengateConnectionTypesResponse
        ],
        request: goldengate_connection_type.ListGoldengateConnectionTypesRequest,
        response: goldengate_connection_type.ListGoldengateConnectionTypesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesResponse):
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
        self._request = goldengate_connection_type.ListGoldengateConnectionTypesRequest(
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
    ) -> Iterator[goldengate_connection_type.ListGoldengateConnectionTypesResponse]:
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

    def __iter__(self) -> Iterator[goldengate_connection_type.GoldengateConnectionType]:
        for page in self.pages:
            yield from page.goldengate_connection_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateConnectionTypesAsyncPager:
    """A pager for iterating through ``list_goldengate_connection_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``goldengate_connection_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoldengateConnectionTypes`` requests and continue to iterate
    through the ``goldengate_connection_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[goldengate_connection_type.ListGoldengateConnectionTypesResponse],
        ],
        request: goldengate_connection_type.ListGoldengateConnectionTypesRequest,
        response: goldengate_connection_type.ListGoldengateConnectionTypesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionTypesResponse):
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
        self._request = goldengate_connection_type.ListGoldengateConnectionTypesRequest(
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
        goldengate_connection_type.ListGoldengateConnectionTypesResponse
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
    ) -> AsyncIterator[goldengate_connection_type.GoldengateConnectionType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.goldengate_connection_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbVersionsPager:
    """A pager for iterating through ``list_db_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbVersionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``db_versions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDbVersions`` requests and continue to iterate
    through the ``db_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., db_version.ListDbVersionsResponse],
        request: db_version.ListDbVersionsRequest,
        response: db_version.ListDbVersionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbVersionsResponse):
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
        self._request = db_version.ListDbVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[db_version.ListDbVersionsResponse]:
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

    def __iter__(self) -> Iterator[db_version.DbVersion]:
        for page in self.pages:
            yield from page.db_versions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDbVersionsAsyncPager:
    """A pager for iterating through ``list_db_versions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDbVersionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``db_versions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDbVersions`` requests and continue to iterate
    through the ``db_versions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDbVersionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[db_version.ListDbVersionsResponse]],
        request: db_version.ListDbVersionsRequest,
        response: db_version.ListDbVersionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDbVersionsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDbVersionsResponse):
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
        self._request = db_version.ListDbVersionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[db_version.ListDbVersionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[db_version.DbVersion]:
        async def async_generator():
            async for page in self.pages:
                for response in page.db_versions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatabaseCharacterSetsPager:
    """A pager for iterating through ``list_database_character_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``database_character_sets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDatabaseCharacterSets`` requests and continue to iterate
    through the ``database_character_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., database_character_set.ListDatabaseCharacterSetsResponse],
        request: database_character_set.ListDatabaseCharacterSetsRequest,
        response: database_character_set.ListDatabaseCharacterSetsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsResponse):
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
        self._request = database_character_set.ListDatabaseCharacterSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterator[database_character_set.ListDatabaseCharacterSetsResponse]:
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

    def __iter__(self) -> Iterator[database_character_set.DatabaseCharacterSet]:
        for page in self.pages:
            yield from page.database_character_sets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDatabaseCharacterSetsAsyncPager:
    """A pager for iterating through ``list_database_character_sets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``database_character_sets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDatabaseCharacterSets`` requests and continue to iterate
    through the ``database_character_sets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[database_character_set.ListDatabaseCharacterSetsResponse]
        ],
        request: database_character_set.ListDatabaseCharacterSetsRequest,
        response: database_character_set.ListDatabaseCharacterSetsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListDatabaseCharacterSetsResponse):
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
        self._request = database_character_set.ListDatabaseCharacterSetsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[database_character_set.ListDatabaseCharacterSetsResponse]:
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

    def __aiter__(self) -> AsyncIterator[database_character_set.DatabaseCharacterSet]:
        async def async_generator():
            async for page in self.pages:
                for response in page.database_character_sets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateConnectionAssignmentsPager:
    """A pager for iterating through ``list_goldengate_connection_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``goldengate_connection_assignments`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGoldengateConnectionAssignments`` requests and continue to iterate
    through the ``goldengate_connection_assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse,
        ],
        request: goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest,
        response: goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsResponse):
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
            goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest(
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
        goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse
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
    ) -> Iterator[goldengate_connection_assignment.GoldengateConnectionAssignment]:
        for page in self.pages:
            yield from page.goldengate_connection_assignments

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGoldengateConnectionAssignmentsAsyncPager:
    """A pager for iterating through ``list_goldengate_connection_assignments`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``goldengate_connection_assignments`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGoldengateConnectionAssignments`` requests and continue to iterate
    through the ``goldengate_connection_assignments`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ...,
            Awaitable[
                goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse
            ],
        ],
        request: goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest,
        response: goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsRequest):
                The initial request object.
            response (google.cloud.oracledatabase_v1.types.ListGoldengateConnectionAssignmentsResponse):
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
            goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest(
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
        goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse
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
    ) -> AsyncIterator[goldengate_connection_assignment.GoldengateConnectionAssignment]:
        async def async_generator():
            async for page in self.pages:
                for response in page.goldengate_connection_assignments:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
