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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

from google.cloud.managedkafka_v1 import gapic_version as package_version
from google.cloud.managedkafka_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.managedkafka_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.managedkafka_v1.types import managed_kafka, resources

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ManagedKafkaTransport(abc.ABC):
    """Abstract transport class for ManagedKafka."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "managedkafka.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'managedkafka.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._client_options = client_options
        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _wrap_method(self, func, *args, **kwargs):
        """Wrap an RPC method with common client-level features.

        Applies retry, timeout, metadata, and tracing wrappers to the
        underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method.wrap_method(func, *args, **kwargs)

    def _wrap_async_method(self, func, *args, **kwargs):
        """Wrap an async RPC method with common client-level features.

        Applies asynchronous retry, timeout, metadata, and tracing wrappers
        to the underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _ASYNC_WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method_async.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _ASYNC_WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for RPC dispatch."""
        self._wrapped_methods = {
            self.list_clusters: self._wrap_method(
                self.list_clusters,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/ListClusters",
            ),
            self.get_cluster: self._wrap_method(
                self.get_cluster,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/GetCluster",
            ),
            self.create_cluster: self._wrap_method(
                self.create_cluster,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/CreateCluster",
            ),
            self.update_cluster: self._wrap_method(
                self.update_cluster,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/UpdateCluster",
            ),
            self.delete_cluster: self._wrap_method(
                self.delete_cluster,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/DeleteCluster",
            ),
            self.list_topics: self._wrap_method(
                self.list_topics,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/ListTopics",
            ),
            self.get_topic: self._wrap_method(
                self.get_topic,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/GetTopic",
            ),
            self.create_topic: self._wrap_method(
                self.create_topic,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/CreateTopic",
            ),
            self.update_topic: self._wrap_method(
                self.update_topic,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/UpdateTopic",
            ),
            self.delete_topic: self._wrap_method(
                self.delete_topic,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/DeleteTopic",
            ),
            self.list_consumer_groups: self._wrap_method(
                self.list_consumer_groups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/ListConsumerGroups",
            ),
            self.get_consumer_group: self._wrap_method(
                self.get_consumer_group,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/GetConsumerGroup",
            ),
            self.update_consumer_group: self._wrap_method(
                self.update_consumer_group,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/UpdateConsumerGroup",
            ),
            self.delete_consumer_group: self._wrap_method(
                self.delete_consumer_group,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/DeleteConsumerGroup",
            ),
            self.list_acls: self._wrap_method(
                self.list_acls,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/ListAcls",
            ),
            self.get_acl: self._wrap_method(
                self.get_acl,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/GetAcl",
            ),
            self.create_acl: self._wrap_method(
                self.create_acl,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/CreateAcl",
            ),
            self.update_acl: self._wrap_method(
                self.update_acl,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/UpdateAcl",
            ),
            self.delete_acl: self._wrap_method(
                self.delete_acl,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/DeleteAcl",
            ),
            self.add_acl_entry: self._wrap_method(
                self.add_acl_entry,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/AddAclEntry",
            ),
            self.remove_acl_entry: self._wrap_method(
                self.remove_acl_entry,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.managedkafka.v1.ManagedKafka/RemoveAclEntry",
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/GetLocation",
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/ListLocations",
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/CancelOperation",
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/DeleteOperation",
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/ListOperations",
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [managed_kafka.ListClustersRequest],
        Union[
            managed_kafka.ListClustersResponse,
            Awaitable[managed_kafka.ListClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [managed_kafka.GetClusterRequest],
        Union[resources.Cluster, Awaitable[resources.Cluster]],
    ]:
        raise NotImplementedError()

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [managed_kafka.CreateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [managed_kafka.UpdateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [managed_kafka.DeleteClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_topics(
        self,
    ) -> Callable[
        [managed_kafka.ListTopicsRequest],
        Union[
            managed_kafka.ListTopicsResponse,
            Awaitable[managed_kafka.ListTopicsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_topic(
        self,
    ) -> Callable[
        [managed_kafka.GetTopicRequest],
        Union[resources.Topic, Awaitable[resources.Topic]],
    ]:
        raise NotImplementedError()

    @property
    def create_topic(
        self,
    ) -> Callable[
        [managed_kafka.CreateTopicRequest],
        Union[resources.Topic, Awaitable[resources.Topic]],
    ]:
        raise NotImplementedError()

    @property
    def update_topic(
        self,
    ) -> Callable[
        [managed_kafka.UpdateTopicRequest],
        Union[resources.Topic, Awaitable[resources.Topic]],
    ]:
        raise NotImplementedError()

    @property
    def delete_topic(
        self,
    ) -> Callable[
        [managed_kafka.DeleteTopicRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_consumer_groups(
        self,
    ) -> Callable[
        [managed_kafka.ListConsumerGroupsRequest],
        Union[
            managed_kafka.ListConsumerGroupsResponse,
            Awaitable[managed_kafka.ListConsumerGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_consumer_group(
        self,
    ) -> Callable[
        [managed_kafka.GetConsumerGroupRequest],
        Union[resources.ConsumerGroup, Awaitable[resources.ConsumerGroup]],
    ]:
        raise NotImplementedError()

    @property
    def update_consumer_group(
        self,
    ) -> Callable[
        [managed_kafka.UpdateConsumerGroupRequest],
        Union[resources.ConsumerGroup, Awaitable[resources.ConsumerGroup]],
    ]:
        raise NotImplementedError()

    @property
    def delete_consumer_group(
        self,
    ) -> Callable[
        [managed_kafka.DeleteConsumerGroupRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_acls(
        self,
    ) -> Callable[
        [managed_kafka.ListAclsRequest],
        Union[
            managed_kafka.ListAclsResponse, Awaitable[managed_kafka.ListAclsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_acl(
        self,
    ) -> Callable[
        [managed_kafka.GetAclRequest], Union[resources.Acl, Awaitable[resources.Acl]]
    ]:
        raise NotImplementedError()

    @property
    def create_acl(
        self,
    ) -> Callable[
        [managed_kafka.CreateAclRequest], Union[resources.Acl, Awaitable[resources.Acl]]
    ]:
        raise NotImplementedError()

    @property
    def update_acl(
        self,
    ) -> Callable[
        [managed_kafka.UpdateAclRequest], Union[resources.Acl, Awaitable[resources.Acl]]
    ]:
        raise NotImplementedError()

    @property
    def delete_acl(
        self,
    ) -> Callable[
        [managed_kafka.DeleteAclRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def add_acl_entry(
        self,
    ) -> Callable[
        [managed_kafka.AddAclEntryRequest],
        Union[
            managed_kafka.AddAclEntryResponse,
            Awaitable[managed_kafka.AddAclEntryResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def remove_acl_entry(
        self,
    ) -> Callable[
        [managed_kafka.RemoveAclEntryRequest],
        Union[
            managed_kafka.RemoveAclEntryResponse,
            Awaitable[managed_kafka.RemoveAclEntryResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("ManagedKafkaTransport",)
