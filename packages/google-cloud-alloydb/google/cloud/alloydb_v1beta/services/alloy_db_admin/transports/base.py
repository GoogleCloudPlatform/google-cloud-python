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

from google.cloud.alloydb_v1beta import gapic_version as package_version
from google.cloud.alloydb_v1beta._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.alloydb_v1beta._compat import (
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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.alloydb_v1beta.types import resources, service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AlloyDBAdminTransport(abc.ABC):
    """Abstract transport class for AlloyDBAdmin."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "alloydb.googleapis.com"

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
                 The hostname to connect to (default: 'alloydb.googleapis.com').
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
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ListClusters",
            ),
            self.get_cluster: self._wrap_method(
                self.get_cluster,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/GetCluster",
            ),
            self.create_cluster: self._wrap_method(
                self.create_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/CreateCluster",
            ),
            self.update_cluster: self._wrap_method(
                self.update_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/UpdateCluster",
            ),
            self.export_cluster: self._wrap_method(
                self.export_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ExportCluster",
            ),
            self.import_cluster: self._wrap_method(
                self.import_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ImportCluster",
            ),
            self.upgrade_cluster: self._wrap_method(
                self.upgrade_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/UpgradeCluster",
            ),
            self.delete_cluster: self._wrap_method(
                self.delete_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/DeleteCluster",
            ),
            self.promote_cluster: self._wrap_method(
                self.promote_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/PromoteCluster",
            ),
            self.switchover_cluster: self._wrap_method(
                self.switchover_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/SwitchoverCluster",
            ),
            self.restore_cluster: self._wrap_method(
                self.restore_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/RestoreCluster",
            ),
            self.create_secondary_cluster: self._wrap_method(
                self.create_secondary_cluster,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/CreateSecondaryCluster",
            ),
            self.list_instances: self._wrap_method(
                self.list_instances,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ListInstances",
            ),
            self.get_instance: self._wrap_method(
                self.get_instance,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/GetInstance",
            ),
            self.create_instance: self._wrap_method(
                self.create_instance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/CreateInstance",
            ),
            self.create_secondary_instance: self._wrap_method(
                self.create_secondary_instance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/CreateSecondaryInstance",
            ),
            self.batch_create_instances: self._wrap_method(
                self.batch_create_instances,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/BatchCreateInstances",
            ),
            self.update_instance: self._wrap_method(
                self.update_instance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/UpdateInstance",
            ),
            self.delete_instance: self._wrap_method(
                self.delete_instance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/DeleteInstance",
            ),
            self.failover_instance: self._wrap_method(
                self.failover_instance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/FailoverInstance",
            ),
            self.inject_fault: self._wrap_method(
                self.inject_fault,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/InjectFault",
            ),
            self.restart_instance: self._wrap_method(
                self.restart_instance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/RestartInstance",
            ),
            self.execute_sql: self._wrap_method(
                self.execute_sql,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ExecuteSql",
            ),
            self.list_backups: self._wrap_method(
                self.list_backups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ListBackups",
            ),
            self.get_backup: self._wrap_method(
                self.get_backup,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/GetBackup",
            ),
            self.create_backup: self._wrap_method(
                self.create_backup,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/CreateBackup",
            ),
            self.update_backup: self._wrap_method(
                self.update_backup,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/UpdateBackup",
            ),
            self.delete_backup: self._wrap_method(
                self.delete_backup,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/DeleteBackup",
            ),
            self.list_supported_database_flags: self._wrap_method(
                self.list_supported_database_flags,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ListSupportedDatabaseFlags",
            ),
            self.generate_client_certificate: self._wrap_method(
                self.generate_client_certificate,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/GenerateClientCertificate",
            ),
            self.get_connection_info: self._wrap_method(
                self.get_connection_info,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/GetConnectionInfo",
            ),
            self.list_users: self._wrap_method(
                self.list_users,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ListUsers",
            ),
            self.get_user: self._wrap_method(
                self.get_user,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/GetUser",
            ),
            self.create_user: self._wrap_method(
                self.create_user,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/CreateUser",
            ),
            self.update_user: self._wrap_method(
                self.update_user,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/UpdateUser",
            ),
            self.delete_user: self._wrap_method(
                self.delete_user,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/DeleteUser",
            ),
            self.list_databases: self._wrap_method(
                self.list_databases,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/ListDatabases",
            ),
            self.create_database: self._wrap_method(
                self.create_database,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.alloydb.v1beta.AlloyDBAdmin/CreateDatabase",
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
        [service.ListClustersRequest],
        Union[service.ListClustersResponse, Awaitable[service.ListClustersResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [service.GetClusterRequest],
        Union[resources.Cluster, Awaitable[resources.Cluster]],
    ]:
        raise NotImplementedError()

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [service.CreateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [service.UpdateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_cluster(
        self,
    ) -> Callable[
        [service.ExportClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_cluster(
        self,
    ) -> Callable[
        [service.ImportClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def upgrade_cluster(
        self,
    ) -> Callable[
        [service.UpgradeClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [service.DeleteClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def promote_cluster(
        self,
    ) -> Callable[
        [service.PromoteClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def switchover_cluster(
        self,
    ) -> Callable[
        [service.SwitchoverClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restore_cluster(
        self,
    ) -> Callable[
        [service.RestoreClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_secondary_cluster(
        self,
    ) -> Callable[
        [service.CreateSecondaryClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_instances(
        self,
    ) -> Callable[
        [service.ListInstancesRequest],
        Union[service.ListInstancesResponse, Awaitable[service.ListInstancesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_instance(
        self,
    ) -> Callable[
        [service.GetInstanceRequest],
        Union[resources.Instance, Awaitable[resources.Instance]],
    ]:
        raise NotImplementedError()

    @property
    def create_instance(
        self,
    ) -> Callable[
        [service.CreateInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_secondary_instance(
        self,
    ) -> Callable[
        [service.CreateSecondaryInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_instances(
        self,
    ) -> Callable[
        [service.BatchCreateInstancesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_instance(
        self,
    ) -> Callable[
        [service.UpdateInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_instance(
        self,
    ) -> Callable[
        [service.DeleteInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def failover_instance(
        self,
    ) -> Callable[
        [service.FailoverInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def inject_fault(
        self,
    ) -> Callable[
        [service.InjectFaultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restart_instance(
        self,
    ) -> Callable[
        [service.RestartInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def execute_sql(
        self,
    ) -> Callable[
        [service.ExecuteSqlRequest],
        Union[service.ExecuteSqlResponse, Awaitable[service.ExecuteSqlResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [service.ListBackupsRequest],
        Union[service.ListBackupsResponse, Awaitable[service.ListBackupsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [service.GetBackupRequest], Union[resources.Backup, Awaitable[resources.Backup]]
    ]:
        raise NotImplementedError()

    @property
    def create_backup(
        self,
    ) -> Callable[
        [service.CreateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup(
        self,
    ) -> Callable[
        [service.UpdateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [service.DeleteBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_supported_database_flags(
        self,
    ) -> Callable[
        [service.ListSupportedDatabaseFlagsRequest],
        Union[
            service.ListSupportedDatabaseFlagsResponse,
            Awaitable[service.ListSupportedDatabaseFlagsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def generate_client_certificate(
        self,
    ) -> Callable[
        [service.GenerateClientCertificateRequest],
        Union[
            service.GenerateClientCertificateResponse,
            Awaitable[service.GenerateClientCertificateResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_connection_info(
        self,
    ) -> Callable[
        [service.GetConnectionInfoRequest],
        Union[resources.ConnectionInfo, Awaitable[resources.ConnectionInfo]],
    ]:
        raise NotImplementedError()

    @property
    def list_users(
        self,
    ) -> Callable[
        [service.ListUsersRequest],
        Union[service.ListUsersResponse, Awaitable[service.ListUsersResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_user(
        self,
    ) -> Callable[
        [service.GetUserRequest], Union[resources.User, Awaitable[resources.User]]
    ]:
        raise NotImplementedError()

    @property
    def create_user(
        self,
    ) -> Callable[
        [service.CreateUserRequest], Union[resources.User, Awaitable[resources.User]]
    ]:
        raise NotImplementedError()

    @property
    def update_user(
        self,
    ) -> Callable[
        [service.UpdateUserRequest], Union[resources.User, Awaitable[resources.User]]
    ]:
        raise NotImplementedError()

    @property
    def delete_user(
        self,
    ) -> Callable[
        [service.DeleteUserRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def list_databases(
        self,
    ) -> Callable[
        [service.ListDatabasesRequest],
        Union[service.ListDatabasesResponse, Awaitable[service.ListDatabasesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_database(
        self,
    ) -> Callable[
        [service.CreateDatabaseRequest],
        Union[resources.Database, Awaitable[resources.Database]],
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


__all__ = ("AlloyDBAdminTransport",)
