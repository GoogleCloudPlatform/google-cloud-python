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

from google.cloud.clouddms_v1 import gapic_version as package_version
from google.cloud.clouddms_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.clouddms_v1._compat import (
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

from google.cloud.clouddms_v1.types import (
    clouddms,
    clouddms_resources,
    conversionworkspace_resources,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DataMigrationServiceTransport(abc.ABC):
    """Abstract transport class for DataMigrationService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "datamigration.googleapis.com"

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
                 The hostname to connect to (default: 'datamigration.googleapis.com').
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
            self.list_migration_jobs: self._wrap_method(
                self.list_migration_jobs,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ListMigrationJobs",
            ),
            self.get_migration_job: self._wrap_method(
                self.get_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/GetMigrationJob",
            ),
            self.create_migration_job: self._wrap_method(
                self.create_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/CreateMigrationJob",
            ),
            self.update_migration_job: self._wrap_method(
                self.update_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/UpdateMigrationJob",
            ),
            self.delete_migration_job: self._wrap_method(
                self.delete_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/DeleteMigrationJob",
            ),
            self.start_migration_job: self._wrap_method(
                self.start_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/StartMigrationJob",
            ),
            self.stop_migration_job: self._wrap_method(
                self.stop_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/StopMigrationJob",
            ),
            self.resume_migration_job: self._wrap_method(
                self.resume_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ResumeMigrationJob",
            ),
            self.promote_migration_job: self._wrap_method(
                self.promote_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/PromoteMigrationJob",
            ),
            self.verify_migration_job: self._wrap_method(
                self.verify_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/VerifyMigrationJob",
            ),
            self.restart_migration_job: self._wrap_method(
                self.restart_migration_job,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/RestartMigrationJob",
            ),
            self.generate_ssh_script: self._wrap_method(
                self.generate_ssh_script,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/GenerateSshScript",
            ),
            self.generate_tcp_proxy_script: self._wrap_method(
                self.generate_tcp_proxy_script,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/GenerateTcpProxyScript",
            ),
            self.list_connection_profiles: self._wrap_method(
                self.list_connection_profiles,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ListConnectionProfiles",
            ),
            self.get_connection_profile: self._wrap_method(
                self.get_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/GetConnectionProfile",
            ),
            self.create_connection_profile: self._wrap_method(
                self.create_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/CreateConnectionProfile",
            ),
            self.update_connection_profile: self._wrap_method(
                self.update_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/UpdateConnectionProfile",
            ),
            self.delete_connection_profile: self._wrap_method(
                self.delete_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/DeleteConnectionProfile",
            ),
            self.create_private_connection: self._wrap_method(
                self.create_private_connection,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/CreatePrivateConnection",
            ),
            self.get_private_connection: self._wrap_method(
                self.get_private_connection,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/GetPrivateConnection",
            ),
            self.list_private_connections: self._wrap_method(
                self.list_private_connections,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ListPrivateConnections",
            ),
            self.delete_private_connection: self._wrap_method(
                self.delete_private_connection,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/DeletePrivateConnection",
            ),
            self.get_conversion_workspace: self._wrap_method(
                self.get_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/GetConversionWorkspace",
            ),
            self.list_conversion_workspaces: self._wrap_method(
                self.list_conversion_workspaces,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ListConversionWorkspaces",
            ),
            self.create_conversion_workspace: self._wrap_method(
                self.create_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/CreateConversionWorkspace",
            ),
            self.update_conversion_workspace: self._wrap_method(
                self.update_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/UpdateConversionWorkspace",
            ),
            self.delete_conversion_workspace: self._wrap_method(
                self.delete_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/DeleteConversionWorkspace",
            ),
            self.create_mapping_rule: self._wrap_method(
                self.create_mapping_rule,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/CreateMappingRule",
            ),
            self.delete_mapping_rule: self._wrap_method(
                self.delete_mapping_rule,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/DeleteMappingRule",
            ),
            self.list_mapping_rules: self._wrap_method(
                self.list_mapping_rules,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ListMappingRules",
            ),
            self.get_mapping_rule: self._wrap_method(
                self.get_mapping_rule,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/GetMappingRule",
            ),
            self.seed_conversion_workspace: self._wrap_method(
                self.seed_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/SeedConversionWorkspace",
            ),
            self.import_mapping_rules: self._wrap_method(
                self.import_mapping_rules,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ImportMappingRules",
            ),
            self.convert_conversion_workspace: self._wrap_method(
                self.convert_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ConvertConversionWorkspace",
            ),
            self.commit_conversion_workspace: self._wrap_method(
                self.commit_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/CommitConversionWorkspace",
            ),
            self.rollback_conversion_workspace: self._wrap_method(
                self.rollback_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/RollbackConversionWorkspace",
            ),
            self.apply_conversion_workspace: self._wrap_method(
                self.apply_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/ApplyConversionWorkspace",
            ),
            self.describe_database_entities: self._wrap_method(
                self.describe_database_entities,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/DescribeDatabaseEntities",
            ),
            self.search_background_jobs: self._wrap_method(
                self.search_background_jobs,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/SearchBackgroundJobs",
            ),
            self.describe_conversion_workspace_revisions: self._wrap_method(
                self.describe_conversion_workspace_revisions,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/DescribeConversionWorkspaceRevisions",
            ),
            self.fetch_static_ips: self._wrap_method(
                self.fetch_static_ips,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.clouddms.v1.DataMigrationService/FetchStaticIps",
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
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/GetIamPolicy",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/SetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/TestIamPermissions",
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
    def list_migration_jobs(
        self,
    ) -> Callable[
        [clouddms.ListMigrationJobsRequest],
        Union[
            clouddms.ListMigrationJobsResponse,
            Awaitable[clouddms.ListMigrationJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_migration_job(
        self,
    ) -> Callable[
        [clouddms.GetMigrationJobRequest],
        Union[
            clouddms_resources.MigrationJob, Awaitable[clouddms_resources.MigrationJob]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_migration_job(
        self,
    ) -> Callable[
        [clouddms.CreateMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_migration_job(
        self,
    ) -> Callable[
        [clouddms.UpdateMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_migration_job(
        self,
    ) -> Callable[
        [clouddms.DeleteMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_migration_job(
        self,
    ) -> Callable[
        [clouddms.StartMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop_migration_job(
        self,
    ) -> Callable[
        [clouddms.StopMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def resume_migration_job(
        self,
    ) -> Callable[
        [clouddms.ResumeMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def promote_migration_job(
        self,
    ) -> Callable[
        [clouddms.PromoteMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def verify_migration_job(
        self,
    ) -> Callable[
        [clouddms.VerifyMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restart_migration_job(
        self,
    ) -> Callable[
        [clouddms.RestartMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_ssh_script(
        self,
    ) -> Callable[
        [clouddms.GenerateSshScriptRequest],
        Union[clouddms.SshScript, Awaitable[clouddms.SshScript]],
    ]:
        raise NotImplementedError()

    @property
    def generate_tcp_proxy_script(
        self,
    ) -> Callable[
        [clouddms.GenerateTcpProxyScriptRequest],
        Union[clouddms.TcpProxyScript, Awaitable[clouddms.TcpProxyScript]],
    ]:
        raise NotImplementedError()

    @property
    def list_connection_profiles(
        self,
    ) -> Callable[
        [clouddms.ListConnectionProfilesRequest],
        Union[
            clouddms.ListConnectionProfilesResponse,
            Awaitable[clouddms.ListConnectionProfilesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_connection_profile(
        self,
    ) -> Callable[
        [clouddms.GetConnectionProfileRequest],
        Union[
            clouddms_resources.ConnectionProfile,
            Awaitable[clouddms_resources.ConnectionProfile],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_connection_profile(
        self,
    ) -> Callable[
        [clouddms.CreateConnectionProfileRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_connection_profile(
        self,
    ) -> Callable[
        [clouddms.UpdateConnectionProfileRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_connection_profile(
        self,
    ) -> Callable[
        [clouddms.DeleteConnectionProfileRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_private_connection(
        self,
    ) -> Callable[
        [clouddms.CreatePrivateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_private_connection(
        self,
    ) -> Callable[
        [clouddms.GetPrivateConnectionRequest],
        Union[
            clouddms_resources.PrivateConnection,
            Awaitable[clouddms_resources.PrivateConnection],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_private_connections(
        self,
    ) -> Callable[
        [clouddms.ListPrivateConnectionsRequest],
        Union[
            clouddms.ListPrivateConnectionsResponse,
            Awaitable[clouddms.ListPrivateConnectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_private_connection(
        self,
    ) -> Callable[
        [clouddms.DeletePrivateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.GetConversionWorkspaceRequest],
        Union[
            conversionworkspace_resources.ConversionWorkspace,
            Awaitable[conversionworkspace_resources.ConversionWorkspace],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_conversion_workspaces(
        self,
    ) -> Callable[
        [clouddms.ListConversionWorkspacesRequest],
        Union[
            clouddms.ListConversionWorkspacesResponse,
            Awaitable[clouddms.ListConversionWorkspacesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.CreateConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.UpdateConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.DeleteConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_mapping_rule(
        self,
    ) -> Callable[
        [clouddms.CreateMappingRuleRequest],
        Union[
            conversionworkspace_resources.MappingRule,
            Awaitable[conversionworkspace_resources.MappingRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_mapping_rule(
        self,
    ) -> Callable[
        [clouddms.DeleteMappingRuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_mapping_rules(
        self,
    ) -> Callable[
        [clouddms.ListMappingRulesRequest],
        Union[
            clouddms.ListMappingRulesResponse,
            Awaitable[clouddms.ListMappingRulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_mapping_rule(
        self,
    ) -> Callable[
        [clouddms.GetMappingRuleRequest],
        Union[
            conversionworkspace_resources.MappingRule,
            Awaitable[conversionworkspace_resources.MappingRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def seed_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.SeedConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_mapping_rules(
        self,
    ) -> Callable[
        [clouddms.ImportMappingRulesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def convert_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.ConvertConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def commit_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.CommitConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rollback_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.RollbackConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def apply_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.ApplyConversionWorkspaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def describe_database_entities(
        self,
    ) -> Callable[
        [clouddms.DescribeDatabaseEntitiesRequest],
        Union[
            clouddms.DescribeDatabaseEntitiesResponse,
            Awaitable[clouddms.DescribeDatabaseEntitiesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_background_jobs(
        self,
    ) -> Callable[
        [clouddms.SearchBackgroundJobsRequest],
        Union[
            clouddms.SearchBackgroundJobsResponse,
            Awaitable[clouddms.SearchBackgroundJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def describe_conversion_workspace_revisions(
        self,
    ) -> Callable[
        [clouddms.DescribeConversionWorkspaceRevisionsRequest],
        Union[
            clouddms.DescribeConversionWorkspaceRevisionsResponse,
            Awaitable[clouddms.DescribeConversionWorkspaceRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_static_ips(
        self,
    ) -> Callable[
        [clouddms.FetchStaticIpsRequest],
        Union[
            clouddms.FetchStaticIpsResponse, Awaitable[clouddms.FetchStaticIpsResponse]
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
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
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


__all__ = ("DataMigrationServiceTransport",)
