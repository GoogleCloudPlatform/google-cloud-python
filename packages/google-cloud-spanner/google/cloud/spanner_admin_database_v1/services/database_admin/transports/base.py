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

from google.cloud.spanner_admin_database_v1 import gapic_version as package_version
from google.cloud.spanner_admin_database_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.spanner_admin_database_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.spanner_admin_database_v1.types import (
    backup,
    backup_schedule,
    spanner_database_admin,
)
from google.cloud.spanner_admin_database_v1.types import backup as gsad_backup
from google.cloud.spanner_admin_database_v1.types import (
    backup_schedule as gsad_backup_schedule,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DatabaseAdminTransport(abc.ABC):
    """Abstract transport class for DatabaseAdmin."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/spanner.admin",
    )

    DEFAULT_HOST: str = "spanner.googleapis.com"

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
                 The hostname to connect to (default: 'spanner.googleapis.com').
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
            self.list_databases: self._wrap_method(
                self.list_databases,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/ListDatabases",
            ),
            self.create_database: self._wrap_method(
                self.create_database,
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/CreateDatabase",
            ),
            self.get_database: self._wrap_method(
                self.get_database,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/GetDatabase",
            ),
            self.update_database: self._wrap_method(
                self.update_database,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/UpdateDatabase",
            ),
            self.update_database_ddl: self._wrap_method(
                self.update_database_ddl,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/UpdateDatabaseDdl",
            ),
            self.drop_database: self._wrap_method(
                self.drop_database,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/DropDatabase",
            ),
            self.get_database_ddl: self._wrap_method(
                self.get_database_ddl,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/GetDatabaseDdl",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/SetIamPolicy",
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/GetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/TestIamPermissions",
            ),
            self.create_backup: self._wrap_method(
                self.create_backup,
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/CreateBackup",
            ),
            self.copy_backup: self._wrap_method(
                self.copy_backup,
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/CopyBackup",
            ),
            self.get_backup: self._wrap_method(
                self.get_backup,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/GetBackup",
            ),
            self.update_backup: self._wrap_method(
                self.update_backup,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/UpdateBackup",
            ),
            self.delete_backup: self._wrap_method(
                self.delete_backup,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/DeleteBackup",
            ),
            self.list_backups: self._wrap_method(
                self.list_backups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/ListBackups",
            ),
            self.restore_database: self._wrap_method(
                self.restore_database,
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/RestoreDatabase",
            ),
            self.list_database_operations: self._wrap_method(
                self.list_database_operations,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/ListDatabaseOperations",
            ),
            self.list_backup_operations: self._wrap_method(
                self.list_backup_operations,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/ListBackupOperations",
            ),
            self.list_database_roles: self._wrap_method(
                self.list_database_roles,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/ListDatabaseRoles",
            ),
            self.add_split_points: self._wrap_method(
                self.add_split_points,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/AddSplitPoints",
            ),
            self.create_backup_schedule: self._wrap_method(
                self.create_backup_schedule,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/CreateBackupSchedule",
            ),
            self.get_backup_schedule: self._wrap_method(
                self.get_backup_schedule,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/GetBackupSchedule",
            ),
            self.update_backup_schedule: self._wrap_method(
                self.update_backup_schedule,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/UpdateBackupSchedule",
            ),
            self.delete_backup_schedule: self._wrap_method(
                self.delete_backup_schedule,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/DeleteBackupSchedule",
            ),
            self.list_backup_schedules: self._wrap_method(
                self.list_backup_schedules,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/ListBackupSchedules",
            ),
            self.internal_update_graph_operation: self._wrap_method(
                self.internal_update_graph_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.spanner.admin.database.v1.DatabaseAdmin/InternalUpdateGraphOperation",
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
    def list_databases(
        self,
    ) -> Callable[
        [spanner_database_admin.ListDatabasesRequest],
        Union[
            spanner_database_admin.ListDatabasesResponse,
            Awaitable[spanner_database_admin.ListDatabasesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_database(
        self,
    ) -> Callable[
        [spanner_database_admin.CreateDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_database(
        self,
    ) -> Callable[
        [spanner_database_admin.GetDatabaseRequest],
        Union[
            spanner_database_admin.Database, Awaitable[spanner_database_admin.Database]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_database(
        self,
    ) -> Callable[
        [spanner_database_admin.UpdateDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_database_ddl(
        self,
    ) -> Callable[
        [spanner_database_admin.UpdateDatabaseDdlRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def drop_database(
        self,
    ) -> Callable[
        [spanner_database_admin.DropDatabaseRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_database_ddl(
        self,
    ) -> Callable[
        [spanner_database_admin.GetDatabaseDdlRequest],
        Union[
            spanner_database_admin.GetDatabaseDdlResponse,
            Awaitable[spanner_database_admin.GetDatabaseDdlResponse],
        ],
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
    def create_backup(
        self,
    ) -> Callable[
        [gsad_backup.CreateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def copy_backup(
        self,
    ) -> Callable[
        [backup.CopyBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [backup.GetBackupRequest], Union[backup.Backup, Awaitable[backup.Backup]]
    ]:
        raise NotImplementedError()

    @property
    def update_backup(
        self,
    ) -> Callable[
        [gsad_backup.UpdateBackupRequest],
        Union[gsad_backup.Backup, Awaitable[gsad_backup.Backup]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [backup.DeleteBackupRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [backup.ListBackupsRequest],
        Union[backup.ListBackupsResponse, Awaitable[backup.ListBackupsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def restore_database(
        self,
    ) -> Callable[
        [spanner_database_admin.RestoreDatabaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_database_operations(
        self,
    ) -> Callable[
        [spanner_database_admin.ListDatabaseOperationsRequest],
        Union[
            spanner_database_admin.ListDatabaseOperationsResponse,
            Awaitable[spanner_database_admin.ListDatabaseOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_operations(
        self,
    ) -> Callable[
        [backup.ListBackupOperationsRequest],
        Union[
            backup.ListBackupOperationsResponse,
            Awaitable[backup.ListBackupOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_database_roles(
        self,
    ) -> Callable[
        [spanner_database_admin.ListDatabaseRolesRequest],
        Union[
            spanner_database_admin.ListDatabaseRolesResponse,
            Awaitable[spanner_database_admin.ListDatabaseRolesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def add_split_points(
        self,
    ) -> Callable[
        [spanner_database_admin.AddSplitPointsRequest],
        Union[
            spanner_database_admin.AddSplitPointsResponse,
            Awaitable[spanner_database_admin.AddSplitPointsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_schedule(
        self,
    ) -> Callable[
        [gsad_backup_schedule.CreateBackupScheduleRequest],
        Union[
            gsad_backup_schedule.BackupSchedule,
            Awaitable[gsad_backup_schedule.BackupSchedule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_schedule(
        self,
    ) -> Callable[
        [backup_schedule.GetBackupScheduleRequest],
        Union[
            backup_schedule.BackupSchedule, Awaitable[backup_schedule.BackupSchedule]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_schedule(
        self,
    ) -> Callable[
        [gsad_backup_schedule.UpdateBackupScheduleRequest],
        Union[
            gsad_backup_schedule.BackupSchedule,
            Awaitable[gsad_backup_schedule.BackupSchedule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_schedule(
        self,
    ) -> Callable[
        [backup_schedule.DeleteBackupScheduleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_schedules(
        self,
    ) -> Callable[
        [backup_schedule.ListBackupSchedulesRequest],
        Union[
            backup_schedule.ListBackupSchedulesResponse,
            Awaitable[backup_schedule.ListBackupSchedulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def internal_update_graph_operation(
        self,
    ) -> Callable[
        [spanner_database_admin.InternalUpdateGraphOperationRequest],
        Union[
            spanner_database_admin.InternalUpdateGraphOperationResponse,
            Awaitable[spanner_database_admin.InternalUpdateGraphOperationResponse],
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
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("DatabaseAdminTransport",)
