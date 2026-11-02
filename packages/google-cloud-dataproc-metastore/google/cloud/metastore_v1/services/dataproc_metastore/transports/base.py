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

from google.cloud.metastore_v1 import gapic_version as package_version
from google.cloud.metastore_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.metastore_v1._compat import (
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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.metastore_v1.types import metastore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DataprocMetastoreTransport(abc.ABC):
    """Abstract transport class for DataprocMetastore."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "metastore.googleapis.com"

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
                 The hostname to connect to (default: 'metastore.googleapis.com').
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
            self.list_services: self._wrap_method(
                self.list_services,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/ListServices",
            ),
            self.get_service: self._wrap_method(
                self.get_service,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/GetService",
            ),
            self.create_service: self._wrap_method(
                self.create_service,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/CreateService",
            ),
            self.update_service: self._wrap_method(
                self.update_service,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/UpdateService",
            ),
            self.delete_service: self._wrap_method(
                self.delete_service,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/DeleteService",
            ),
            self.list_metadata_imports: self._wrap_method(
                self.list_metadata_imports,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/ListMetadataImports",
            ),
            self.get_metadata_import: self._wrap_method(
                self.get_metadata_import,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/GetMetadataImport",
            ),
            self.create_metadata_import: self._wrap_method(
                self.create_metadata_import,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/CreateMetadataImport",
            ),
            self.update_metadata_import: self._wrap_method(
                self.update_metadata_import,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/UpdateMetadataImport",
            ),
            self.export_metadata: self._wrap_method(
                self.export_metadata,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/ExportMetadata",
            ),
            self.restore_service: self._wrap_method(
                self.restore_service,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/RestoreService",
            ),
            self.list_backups: self._wrap_method(
                self.list_backups,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/ListBackups",
            ),
            self.get_backup: self._wrap_method(
                self.get_backup,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/GetBackup",
            ),
            self.create_backup: self._wrap_method(
                self.create_backup,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/CreateBackup",
            ),
            self.delete_backup: self._wrap_method(
                self.delete_backup,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/DeleteBackup",
            ),
            self.query_metadata: self._wrap_method(
                self.query_metadata,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/QueryMetadata",
            ),
            self.move_table_to_database: self._wrap_method(
                self.move_table_to_database,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/MoveTableToDatabase",
            ),
            self.alter_metadata_resource_location: self._wrap_method(
                self.alter_metadata_resource_location,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.metastore.v1.DataprocMetastore/AlterMetadataResourceLocation",
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
    def list_services(
        self,
    ) -> Callable[
        [metastore.ListServicesRequest],
        Union[
            metastore.ListServicesResponse, Awaitable[metastore.ListServicesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service(
        self,
    ) -> Callable[
        [metastore.GetServiceRequest],
        Union[metastore.Service, Awaitable[metastore.Service]],
    ]:
        raise NotImplementedError()

    @property
    def create_service(
        self,
    ) -> Callable[
        [metastore.CreateServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_service(
        self,
    ) -> Callable[
        [metastore.UpdateServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service(
        self,
    ) -> Callable[
        [metastore.DeleteServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_metadata_imports(
        self,
    ) -> Callable[
        [metastore.ListMetadataImportsRequest],
        Union[
            metastore.ListMetadataImportsResponse,
            Awaitable[metastore.ListMetadataImportsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_metadata_import(
        self,
    ) -> Callable[
        [metastore.GetMetadataImportRequest],
        Union[metastore.MetadataImport, Awaitable[metastore.MetadataImport]],
    ]:
        raise NotImplementedError()

    @property
    def create_metadata_import(
        self,
    ) -> Callable[
        [metastore.CreateMetadataImportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_metadata_import(
        self,
    ) -> Callable[
        [metastore.UpdateMetadataImportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_metadata(
        self,
    ) -> Callable[
        [metastore.ExportMetadataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def restore_service(
        self,
    ) -> Callable[
        [metastore.RestoreServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [metastore.ListBackupsRequest],
        Union[metastore.ListBackupsResponse, Awaitable[metastore.ListBackupsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [metastore.GetBackupRequest],
        Union[metastore.Backup, Awaitable[metastore.Backup]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup(
        self,
    ) -> Callable[
        [metastore.CreateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [metastore.DeleteBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def query_metadata(
        self,
    ) -> Callable[
        [metastore.QueryMetadataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def move_table_to_database(
        self,
    ) -> Callable[
        [metastore.MoveTableToDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def alter_metadata_resource_location(
        self,
    ) -> Callable[
        [metastore.AlterMetadataResourceLocationRequest],
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


__all__ = ("DataprocMetastoreTransport",)
