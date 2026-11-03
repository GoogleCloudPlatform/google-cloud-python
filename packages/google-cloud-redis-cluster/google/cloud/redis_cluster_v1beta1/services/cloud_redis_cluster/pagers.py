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

from google.cloud.redis_cluster_v1beta1.types import cloud_redis_cluster


class ListClustersPager:
    """A pager for iterating through ``list_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListClusters`` requests and continue to iterate
    through the ``clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_redis_cluster.ListClustersResponse],
        request: cloud_redis_cluster.ListClustersRequest,
        response: cloud_redis_cluster.ListClustersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListClustersRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListClustersResponse):
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
        self._request = cloud_redis_cluster.ListClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_redis_cluster.ListClustersResponse]:
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

    def __iter__(self) -> Iterator[cloud_redis_cluster.Cluster]:
        for page in self.pages:
            yield from page.clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListClustersAsyncPager:
    """A pager for iterating through ``list_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListClusters`` requests and continue to iterate
    through the ``clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_redis_cluster.ListClustersResponse]],
        request: cloud_redis_cluster.ListClustersRequest,
        response: cloud_redis_cluster.ListClustersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListClustersRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListClustersResponse):
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
        self._request = cloud_redis_cluster.ListClustersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_redis_cluster.ListClustersResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_redis_cluster.Cluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAclPoliciesPager:
    """A pager for iterating through ``list_acl_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``acl_policies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAclPolicies`` requests and continue to iterate
    through the ``acl_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_redis_cluster.ListAclPoliciesResponse],
        request: cloud_redis_cluster.ListAclPoliciesRequest,
        response: cloud_redis_cluster.ListAclPoliciesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesResponse):
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
        self._request = cloud_redis_cluster.ListAclPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_redis_cluster.ListAclPoliciesResponse]:
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

    def __iter__(self) -> Iterator[cloud_redis_cluster.AclPolicy]:
        for page in self.pages:
            yield from page.acl_policies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAclPoliciesAsyncPager:
    """A pager for iterating through ``list_acl_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``acl_policies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAclPolicies`` requests and continue to iterate
    through the ``acl_policies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_redis_cluster.ListAclPoliciesResponse]],
        request: cloud_redis_cluster.ListAclPoliciesRequest,
        response: cloud_redis_cluster.ListAclPoliciesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesResponse):
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
        self._request = cloud_redis_cluster.ListAclPoliciesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_redis_cluster.ListAclPoliciesResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_redis_cluster.AclPolicy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.acl_policies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAclPolicyRevisionsPager:
    """A pager for iterating through ``list_acl_policy_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``acl_policy_revisions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAclPolicyRevisions`` requests and continue to iterate
    through the ``acl_policy_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_redis_cluster.ListAclPolicyRevisionsResponse],
        request: cloud_redis_cluster.ListAclPolicyRevisionsRequest,
        response: cloud_redis_cluster.ListAclPolicyRevisionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsResponse):
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
        self._request = cloud_redis_cluster.ListAclPolicyRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_redis_cluster.ListAclPolicyRevisionsResponse]:
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

    def __iter__(self) -> Iterator[cloud_redis_cluster.AclPolicyRevision]:
        for page in self.pages:
            yield from page.acl_policy_revisions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAclPolicyRevisionsAsyncPager:
    """A pager for iterating through ``list_acl_policy_revisions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``acl_policy_revisions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAclPolicyRevisions`` requests and continue to iterate
    through the ``acl_policy_revisions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[cloud_redis_cluster.ListAclPolicyRevisionsResponse]
        ],
        request: cloud_redis_cluster.ListAclPolicyRevisionsRequest,
        response: cloud_redis_cluster.ListAclPolicyRevisionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsResponse):
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
        self._request = cloud_redis_cluster.ListAclPolicyRevisionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[cloud_redis_cluster.ListAclPolicyRevisionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_redis_cluster.AclPolicyRevision]:
        async def async_generator():
            async for page in self.pages:
                for response in page.acl_policy_revisions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupCollectionsPager:
    """A pager for iterating through ``list_backup_collections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backup_collections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackupCollections`` requests and continue to iterate
    through the ``backup_collections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_redis_cluster.ListBackupCollectionsResponse],
        request: cloud_redis_cluster.ListBackupCollectionsRequest,
        response: cloud_redis_cluster.ListBackupCollectionsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse):
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
        self._request = cloud_redis_cluster.ListBackupCollectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_redis_cluster.ListBackupCollectionsResponse]:
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

    def __iter__(self) -> Iterator[cloud_redis_cluster.BackupCollection]:
        for page in self.pages:
            yield from page.backup_collections

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupCollectionsAsyncPager:
    """A pager for iterating through ``list_backup_collections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backup_collections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackupCollections`` requests and continue to iterate
    through the ``backup_collections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[cloud_redis_cluster.ListBackupCollectionsResponse]
        ],
        request: cloud_redis_cluster.ListBackupCollectionsRequest,
        response: cloud_redis_cluster.ListBackupCollectionsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse):
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
        self._request = cloud_redis_cluster.ListBackupCollectionsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[cloud_redis_cluster.ListBackupCollectionsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_redis_cluster.BackupCollection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backup_collections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupsPager:
    """A pager for iterating through ``list_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_redis_cluster.ListBackupsResponse],
        request: cloud_redis_cluster.ListBackupsRequest,
        response: cloud_redis_cluster.ListBackupsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse):
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
        self._request = cloud_redis_cluster.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_redis_cluster.ListBackupsResponse]:
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

    def __iter__(self) -> Iterator[cloud_redis_cluster.Backup]:
        for page in self.pages:
            yield from page.backups

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListBackupsAsyncPager:
    """A pager for iterating through ``list_backups`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``backups`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBackups`` requests and continue to iterate
    through the ``backups`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_redis_cluster.ListBackupsResponse]],
        request: cloud_redis_cluster.ListBackupsRequest,
        response: cloud_redis_cluster.ListBackupsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListBackupsRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse):
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
        self._request = cloud_redis_cluster.ListBackupsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_redis_cluster.ListBackupsResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_redis_cluster.Backup]:
        async def async_generator():
            async for page in self.pages:
                for response in page.backups:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTokenAuthUsersPager:
    """A pager for iterating through ``list_token_auth_users`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``token_auth_users`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTokenAuthUsers`` requests and continue to iterate
    through the ``token_auth_users`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_redis_cluster.ListTokenAuthUsersResponse],
        request: cloud_redis_cluster.ListTokenAuthUsersRequest,
        response: cloud_redis_cluster.ListTokenAuthUsersResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersResponse):
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
        self._request = cloud_redis_cluster.ListTokenAuthUsersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_redis_cluster.ListTokenAuthUsersResponse]:
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

    def __iter__(self) -> Iterator[cloud_redis_cluster.TokenAuthUser]:
        for page in self.pages:
            yield from page.token_auth_users

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTokenAuthUsersAsyncPager:
    """A pager for iterating through ``list_token_auth_users`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``token_auth_users`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTokenAuthUsers`` requests and continue to iterate
    through the ``token_auth_users`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[cloud_redis_cluster.ListTokenAuthUsersResponse]
        ],
        request: cloud_redis_cluster.ListTokenAuthUsersRequest,
        response: cloud_redis_cluster.ListTokenAuthUsersResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersResponse):
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
        self._request = cloud_redis_cluster.ListTokenAuthUsersRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[cloud_redis_cluster.ListTokenAuthUsersResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_redis_cluster.TokenAuthUser]:
        async def async_generator():
            async for page in self.pages:
                for response in page.token_auth_users:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthTokensPager:
    """A pager for iterating through ``list_auth_tokens`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListAuthTokensResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``auth_tokens`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAuthTokens`` requests and continue to iterate
    through the ``auth_tokens`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListAuthTokensResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_redis_cluster.ListAuthTokensResponse],
        request: cloud_redis_cluster.ListAuthTokensRequest,
        response: cloud_redis_cluster.ListAuthTokensResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListAuthTokensRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListAuthTokensResponse):
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
        self._request = cloud_redis_cluster.ListAuthTokensRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_redis_cluster.ListAuthTokensResponse]:
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

    def __iter__(self) -> Iterator[cloud_redis_cluster.AuthToken]:
        for page in self.pages:
            yield from page.auth_tokens

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAuthTokensAsyncPager:
    """A pager for iterating through ``list_auth_tokens`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.redis_cluster_v1beta1.types.ListAuthTokensResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``auth_tokens`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAuthTokens`` requests and continue to iterate
    through the ``auth_tokens`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.redis_cluster_v1beta1.types.ListAuthTokensResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_redis_cluster.ListAuthTokensResponse]],
        request: cloud_redis_cluster.ListAuthTokensRequest,
        response: cloud_redis_cluster.ListAuthTokensResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.redis_cluster_v1beta1.types.ListAuthTokensRequest):
                The initial request object.
            response (google.cloud.redis_cluster_v1beta1.types.ListAuthTokensResponse):
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
        self._request = cloud_redis_cluster.ListAuthTokensRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_redis_cluster.ListAuthTokensResponse]:
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

    def __aiter__(self) -> AsyncIterator[cloud_redis_cluster.AuthToken]:
        async def async_generator():
            async for page in self.pages:
                for response in page.auth_tokens:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
