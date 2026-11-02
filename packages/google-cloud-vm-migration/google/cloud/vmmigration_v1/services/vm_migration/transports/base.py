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

from google.cloud.vmmigration_v1 import gapic_version as package_version
from google.cloud.vmmigration_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.vmmigration_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.vmmigration_v1.types import vmmigration

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class VmMigrationTransport(abc.ABC):
    """Abstract transport class for VmMigration."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "vmmigration.googleapis.com"

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
                 The hostname to connect to (default: 'vmmigration.googleapis.com').
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
            self.list_sources: self._wrap_method(
                self.list_sources,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListSources",
            ),
            self.get_source: self._wrap_method(
                self.get_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetSource",
            ),
            self.create_source: self._wrap_method(
                self.create_source,
                default_timeout=900.0,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateSource",
            ),
            self.update_source: self._wrap_method(
                self.update_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/UpdateSource",
            ),
            self.delete_source: self._wrap_method(
                self.delete_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteSource",
            ),
            self.fetch_inventory: self._wrap_method(
                self.fetch_inventory,
                default_timeout=300.0,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/FetchInventory",
            ),
            self.fetch_storage_inventory: self._wrap_method(
                self.fetch_storage_inventory,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/FetchStorageInventory",
            ),
            self.list_utilization_reports: self._wrap_method(
                self.list_utilization_reports,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListUtilizationReports",
            ),
            self.get_utilization_report: self._wrap_method(
                self.get_utilization_report,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetUtilizationReport",
            ),
            self.create_utilization_report: self._wrap_method(
                self.create_utilization_report,
                default_timeout=300.0,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateUtilizationReport",
            ),
            self.delete_utilization_report: self._wrap_method(
                self.delete_utilization_report,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteUtilizationReport",
            ),
            self.list_datacenter_connectors: self._wrap_method(
                self.list_datacenter_connectors,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListDatacenterConnectors",
            ),
            self.get_datacenter_connector: self._wrap_method(
                self.get_datacenter_connector,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetDatacenterConnector",
            ),
            self.create_datacenter_connector: self._wrap_method(
                self.create_datacenter_connector,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateDatacenterConnector",
            ),
            self.delete_datacenter_connector: self._wrap_method(
                self.delete_datacenter_connector,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteDatacenterConnector",
            ),
            self.upgrade_appliance: self._wrap_method(
                self.upgrade_appliance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/UpgradeAppliance",
            ),
            self.create_migrating_vm: self._wrap_method(
                self.create_migrating_vm,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateMigratingVm",
            ),
            self.list_migrating_vms: self._wrap_method(
                self.list_migrating_vms,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListMigratingVms",
            ),
            self.get_migrating_vm: self._wrap_method(
                self.get_migrating_vm,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetMigratingVm",
            ),
            self.update_migrating_vm: self._wrap_method(
                self.update_migrating_vm,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/UpdateMigratingVm",
            ),
            self.delete_migrating_vm: self._wrap_method(
                self.delete_migrating_vm,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteMigratingVm",
            ),
            self.start_migration: self._wrap_method(
                self.start_migration,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/StartMigration",
            ),
            self.resume_migration: self._wrap_method(
                self.resume_migration,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ResumeMigration",
            ),
            self.pause_migration: self._wrap_method(
                self.pause_migration,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/PauseMigration",
            ),
            self.finalize_migration: self._wrap_method(
                self.finalize_migration,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/FinalizeMigration",
            ),
            self.extend_migration: self._wrap_method(
                self.extend_migration,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ExtendMigration",
            ),
            self.create_clone_job: self._wrap_method(
                self.create_clone_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateCloneJob",
            ),
            self.cancel_clone_job: self._wrap_method(
                self.cancel_clone_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CancelCloneJob",
            ),
            self.list_clone_jobs: self._wrap_method(
                self.list_clone_jobs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListCloneJobs",
            ),
            self.get_clone_job: self._wrap_method(
                self.get_clone_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetCloneJob",
            ),
            self.create_cutover_job: self._wrap_method(
                self.create_cutover_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateCutoverJob",
            ),
            self.cancel_cutover_job: self._wrap_method(
                self.cancel_cutover_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CancelCutoverJob",
            ),
            self.list_cutover_jobs: self._wrap_method(
                self.list_cutover_jobs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListCutoverJobs",
            ),
            self.get_cutover_job: self._wrap_method(
                self.get_cutover_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetCutoverJob",
            ),
            self.list_groups: self._wrap_method(
                self.list_groups,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListGroups",
            ),
            self.get_group: self._wrap_method(
                self.get_group,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetGroup",
            ),
            self.create_group: self._wrap_method(
                self.create_group,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateGroup",
            ),
            self.update_group: self._wrap_method(
                self.update_group,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/UpdateGroup",
            ),
            self.delete_group: self._wrap_method(
                self.delete_group,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteGroup",
            ),
            self.add_group_migration: self._wrap_method(
                self.add_group_migration,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/AddGroupMigration",
            ),
            self.remove_group_migration: self._wrap_method(
                self.remove_group_migration,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/RemoveGroupMigration",
            ),
            self.list_target_projects: self._wrap_method(
                self.list_target_projects,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListTargetProjects",
            ),
            self.get_target_project: self._wrap_method(
                self.get_target_project,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetTargetProject",
            ),
            self.create_target_project: self._wrap_method(
                self.create_target_project,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateTargetProject",
            ),
            self.update_target_project: self._wrap_method(
                self.update_target_project,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/UpdateTargetProject",
            ),
            self.delete_target_project: self._wrap_method(
                self.delete_target_project,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteTargetProject",
            ),
            self.list_replication_cycles: self._wrap_method(
                self.list_replication_cycles,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListReplicationCycles",
            ),
            self.get_replication_cycle: self._wrap_method(
                self.get_replication_cycle,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetReplicationCycle",
            ),
            self.list_image_imports: self._wrap_method(
                self.list_image_imports,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListImageImports",
            ),
            self.get_image_import: self._wrap_method(
                self.get_image_import,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetImageImport",
            ),
            self.create_image_import: self._wrap_method(
                self.create_image_import,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateImageImport",
            ),
            self.delete_image_import: self._wrap_method(
                self.delete_image_import,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteImageImport",
            ),
            self.list_image_import_jobs: self._wrap_method(
                self.list_image_import_jobs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListImageImportJobs",
            ),
            self.get_image_import_job: self._wrap_method(
                self.get_image_import_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetImageImportJob",
            ),
            self.cancel_image_import_job: self._wrap_method(
                self.cancel_image_import_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CancelImageImportJob",
            ),
            self.create_disk_migration_job: self._wrap_method(
                self.create_disk_migration_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CreateDiskMigrationJob",
            ),
            self.list_disk_migration_jobs: self._wrap_method(
                self.list_disk_migration_jobs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/ListDiskMigrationJobs",
            ),
            self.get_disk_migration_job: self._wrap_method(
                self.get_disk_migration_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/GetDiskMigrationJob",
            ),
            self.update_disk_migration_job: self._wrap_method(
                self.update_disk_migration_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/UpdateDiskMigrationJob",
            ),
            self.delete_disk_migration_job: self._wrap_method(
                self.delete_disk_migration_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/DeleteDiskMigrationJob",
            ),
            self.run_disk_migration_job: self._wrap_method(
                self.run_disk_migration_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/RunDiskMigrationJob",
            ),
            self.cancel_disk_migration_job: self._wrap_method(
                self.cancel_disk_migration_job,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.vmmigration.v1.VmMigration/CancelDiskMigrationJob",
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
    def list_sources(
        self,
    ) -> Callable[
        [vmmigration.ListSourcesRequest],
        Union[
            vmmigration.ListSourcesResponse, Awaitable[vmmigration.ListSourcesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_source(
        self,
    ) -> Callable[
        [vmmigration.GetSourceRequest],
        Union[vmmigration.Source, Awaitable[vmmigration.Source]],
    ]:
        raise NotImplementedError()

    @property
    def create_source(
        self,
    ) -> Callable[
        [vmmigration.CreateSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_source(
        self,
    ) -> Callable[
        [vmmigration.UpdateSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_source(
        self,
    ) -> Callable[
        [vmmigration.DeleteSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_inventory(
        self,
    ) -> Callable[
        [vmmigration.FetchInventoryRequest],
        Union[
            vmmigration.FetchInventoryResponse,
            Awaitable[vmmigration.FetchInventoryResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_storage_inventory(
        self,
    ) -> Callable[
        [vmmigration.FetchStorageInventoryRequest],
        Union[
            vmmigration.FetchStorageInventoryResponse,
            Awaitable[vmmigration.FetchStorageInventoryResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_utilization_reports(
        self,
    ) -> Callable[
        [vmmigration.ListUtilizationReportsRequest],
        Union[
            vmmigration.ListUtilizationReportsResponse,
            Awaitable[vmmigration.ListUtilizationReportsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.GetUtilizationReportRequest],
        Union[vmmigration.UtilizationReport, Awaitable[vmmigration.UtilizationReport]],
    ]:
        raise NotImplementedError()

    @property
    def create_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.CreateUtilizationReportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.DeleteUtilizationReportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_datacenter_connectors(
        self,
    ) -> Callable[
        [vmmigration.ListDatacenterConnectorsRequest],
        Union[
            vmmigration.ListDatacenterConnectorsResponse,
            Awaitable[vmmigration.ListDatacenterConnectorsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.GetDatacenterConnectorRequest],
        Union[
            vmmigration.DatacenterConnector, Awaitable[vmmigration.DatacenterConnector]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.CreateDatacenterConnectorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.DeleteDatacenterConnectorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def upgrade_appliance(
        self,
    ) -> Callable[
        [vmmigration.UpgradeApplianceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_migrating_vm(
        self,
    ) -> Callable[
        [vmmigration.CreateMigratingVmRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_migrating_vms(
        self,
    ) -> Callable[
        [vmmigration.ListMigratingVmsRequest],
        Union[
            vmmigration.ListMigratingVmsResponse,
            Awaitable[vmmigration.ListMigratingVmsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_migrating_vm(
        self,
    ) -> Callable[
        [vmmigration.GetMigratingVmRequest],
        Union[vmmigration.MigratingVm, Awaitable[vmmigration.MigratingVm]],
    ]:
        raise NotImplementedError()

    @property
    def update_migrating_vm(
        self,
    ) -> Callable[
        [vmmigration.UpdateMigratingVmRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_migrating_vm(
        self,
    ) -> Callable[
        [vmmigration.DeleteMigratingVmRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_migration(
        self,
    ) -> Callable[
        [vmmigration.StartMigrationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def resume_migration(
        self,
    ) -> Callable[
        [vmmigration.ResumeMigrationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def pause_migration(
        self,
    ) -> Callable[
        [vmmigration.PauseMigrationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def finalize_migration(
        self,
    ) -> Callable[
        [vmmigration.FinalizeMigrationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def extend_migration(
        self,
    ) -> Callable[
        [vmmigration.ExtendMigrationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_clone_job(
        self,
    ) -> Callable[
        [vmmigration.CreateCloneJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_clone_job(
        self,
    ) -> Callable[
        [vmmigration.CancelCloneJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_clone_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListCloneJobsRequest],
        Union[
            vmmigration.ListCloneJobsResponse,
            Awaitable[vmmigration.ListCloneJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_clone_job(
        self,
    ) -> Callable[
        [vmmigration.GetCloneJobRequest],
        Union[vmmigration.CloneJob, Awaitable[vmmigration.CloneJob]],
    ]:
        raise NotImplementedError()

    @property
    def create_cutover_job(
        self,
    ) -> Callable[
        [vmmigration.CreateCutoverJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_cutover_job(
        self,
    ) -> Callable[
        [vmmigration.CancelCutoverJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_cutover_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListCutoverJobsRequest],
        Union[
            vmmigration.ListCutoverJobsResponse,
            Awaitable[vmmigration.ListCutoverJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cutover_job(
        self,
    ) -> Callable[
        [vmmigration.GetCutoverJobRequest],
        Union[vmmigration.CutoverJob, Awaitable[vmmigration.CutoverJob]],
    ]:
        raise NotImplementedError()

    @property
    def list_groups(
        self,
    ) -> Callable[
        [vmmigration.ListGroupsRequest],
        Union[
            vmmigration.ListGroupsResponse, Awaitable[vmmigration.ListGroupsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_group(
        self,
    ) -> Callable[
        [vmmigration.GetGroupRequest],
        Union[vmmigration.Group, Awaitable[vmmigration.Group]],
    ]:
        raise NotImplementedError()

    @property
    def create_group(
        self,
    ) -> Callable[
        [vmmigration.CreateGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_group(
        self,
    ) -> Callable[
        [vmmigration.UpdateGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_group(
        self,
    ) -> Callable[
        [vmmigration.DeleteGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def add_group_migration(
        self,
    ) -> Callable[
        [vmmigration.AddGroupMigrationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def remove_group_migration(
        self,
    ) -> Callable[
        [vmmigration.RemoveGroupMigrationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_target_projects(
        self,
    ) -> Callable[
        [vmmigration.ListTargetProjectsRequest],
        Union[
            vmmigration.ListTargetProjectsResponse,
            Awaitable[vmmigration.ListTargetProjectsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_target_project(
        self,
    ) -> Callable[
        [vmmigration.GetTargetProjectRequest],
        Union[vmmigration.TargetProject, Awaitable[vmmigration.TargetProject]],
    ]:
        raise NotImplementedError()

    @property
    def create_target_project(
        self,
    ) -> Callable[
        [vmmigration.CreateTargetProjectRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_target_project(
        self,
    ) -> Callable[
        [vmmigration.UpdateTargetProjectRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_target_project(
        self,
    ) -> Callable[
        [vmmigration.DeleteTargetProjectRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_replication_cycles(
        self,
    ) -> Callable[
        [vmmigration.ListReplicationCyclesRequest],
        Union[
            vmmigration.ListReplicationCyclesResponse,
            Awaitable[vmmigration.ListReplicationCyclesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_replication_cycle(
        self,
    ) -> Callable[
        [vmmigration.GetReplicationCycleRequest],
        Union[vmmigration.ReplicationCycle, Awaitable[vmmigration.ReplicationCycle]],
    ]:
        raise NotImplementedError()

    @property
    def list_image_imports(
        self,
    ) -> Callable[
        [vmmigration.ListImageImportsRequest],
        Union[
            vmmigration.ListImageImportsResponse,
            Awaitable[vmmigration.ListImageImportsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_image_import(
        self,
    ) -> Callable[
        [vmmigration.GetImageImportRequest],
        Union[vmmigration.ImageImport, Awaitable[vmmigration.ImageImport]],
    ]:
        raise NotImplementedError()

    @property
    def create_image_import(
        self,
    ) -> Callable[
        [vmmigration.CreateImageImportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_image_import(
        self,
    ) -> Callable[
        [vmmigration.DeleteImageImportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_image_import_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListImageImportJobsRequest],
        Union[
            vmmigration.ListImageImportJobsResponse,
            Awaitable[vmmigration.ListImageImportJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_image_import_job(
        self,
    ) -> Callable[
        [vmmigration.GetImageImportJobRequest],
        Union[vmmigration.ImageImportJob, Awaitable[vmmigration.ImageImportJob]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_image_import_job(
        self,
    ) -> Callable[
        [vmmigration.CancelImageImportJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.CreateDiskMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_disk_migration_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListDiskMigrationJobsRequest],
        Union[
            vmmigration.ListDiskMigrationJobsResponse,
            Awaitable[vmmigration.ListDiskMigrationJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.GetDiskMigrationJobRequest],
        Union[vmmigration.DiskMigrationJob, Awaitable[vmmigration.DiskMigrationJob]],
    ]:
        raise NotImplementedError()

    @property
    def update_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.UpdateDiskMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.DeleteDiskMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def run_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.RunDiskMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.CancelDiskMigrationJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
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


__all__ = ("VmMigrationTransport",)
