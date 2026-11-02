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

from google.cloud.gke_backup_v1 import gapic_version as package_version
from google.cloud.gke_backup_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.gke_backup_v1._compat import (
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

from google.cloud.gke_backup_v1.types import (
    backup,
    backup_channel,
    backup_plan,
    backup_plan_binding,
    gkebackup,
    restore,
    restore_channel,
    restore_plan,
    restore_plan_binding,
    volume,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class BackupForGKETransport(abc.ABC):
    """Abstract transport class for BackupForGKE."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "gkebackup.googleapis.com"

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
                 The hostname to connect to (default: 'gkebackup.googleapis.com').
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
            self.create_backup_plan: self._wrap_method(
                self.create_backup_plan,
                default_timeout=300.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/CreateBackupPlan",
            ),
            self.list_backup_plans: self._wrap_method(
                self.list_backup_plans,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListBackupPlans",
            ),
            self.get_backup_plan: self._wrap_method(
                self.get_backup_plan,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetBackupPlan",
            ),
            self.update_backup_plan: self._wrap_method(
                self.update_backup_plan,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/UpdateBackupPlan",
            ),
            self.delete_backup_plan: self._wrap_method(
                self.delete_backup_plan,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/DeleteBackupPlan",
            ),
            self.create_backup_channel: self._wrap_method(
                self.create_backup_channel,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/CreateBackupChannel",
            ),
            self.list_backup_channels: self._wrap_method(
                self.list_backup_channels,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListBackupChannels",
            ),
            self.get_backup_channel: self._wrap_method(
                self.get_backup_channel,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetBackupChannel",
            ),
            self.update_backup_channel: self._wrap_method(
                self.update_backup_channel,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/UpdateBackupChannel",
            ),
            self.delete_backup_channel: self._wrap_method(
                self.delete_backup_channel,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/DeleteBackupChannel",
            ),
            self.list_backup_plan_bindings: self._wrap_method(
                self.list_backup_plan_bindings,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListBackupPlanBindings",
            ),
            self.get_backup_plan_binding: self._wrap_method(
                self.get_backup_plan_binding,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetBackupPlanBinding",
            ),
            self.create_backup: self._wrap_method(
                self.create_backup,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/CreateBackup",
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListBackups",
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetBackup",
            ),
            self.update_backup: self._wrap_method(
                self.update_backup,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/UpdateBackup",
            ),
            self.delete_backup: self._wrap_method(
                self.delete_backup,
                default_timeout=300.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/DeleteBackup",
            ),
            self.list_volume_backups: self._wrap_method(
                self.list_volume_backups,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListVolumeBackups",
            ),
            self.get_volume_backup: self._wrap_method(
                self.get_volume_backup,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetVolumeBackup",
            ),
            self.create_restore_plan: self._wrap_method(
                self.create_restore_plan,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/CreateRestorePlan",
            ),
            self.list_restore_plans: self._wrap_method(
                self.list_restore_plans,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListRestorePlans",
            ),
            self.get_restore_plan: self._wrap_method(
                self.get_restore_plan,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetRestorePlan",
            ),
            self.update_restore_plan: self._wrap_method(
                self.update_restore_plan,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/UpdateRestorePlan",
            ),
            self.delete_restore_plan: self._wrap_method(
                self.delete_restore_plan,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/DeleteRestorePlan",
            ),
            self.create_restore_channel: self._wrap_method(
                self.create_restore_channel,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/CreateRestoreChannel",
            ),
            self.list_restore_channels: self._wrap_method(
                self.list_restore_channels,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListRestoreChannels",
            ),
            self.get_restore_channel: self._wrap_method(
                self.get_restore_channel,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetRestoreChannel",
            ),
            self.update_restore_channel: self._wrap_method(
                self.update_restore_channel,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/UpdateRestoreChannel",
            ),
            self.delete_restore_channel: self._wrap_method(
                self.delete_restore_channel,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/DeleteRestoreChannel",
            ),
            self.list_restore_plan_bindings: self._wrap_method(
                self.list_restore_plan_bindings,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListRestorePlanBindings",
            ),
            self.get_restore_plan_binding: self._wrap_method(
                self.get_restore_plan_binding,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetRestorePlanBinding",
            ),
            self.create_restore: self._wrap_method(
                self.create_restore,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/CreateRestore",
            ),
            self.list_restores: self._wrap_method(
                self.list_restores,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListRestores",
            ),
            self.get_restore: self._wrap_method(
                self.get_restore,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetRestore",
            ),
            self.update_restore: self._wrap_method(
                self.update_restore,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/UpdateRestore",
            ),
            self.delete_restore: self._wrap_method(
                self.delete_restore,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gkebackup.v1.BackupForGKE/DeleteRestore",
            ),
            self.list_volume_restores: self._wrap_method(
                self.list_volume_restores,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/ListVolumeRestores",
            ),
            self.get_volume_restore: self._wrap_method(
                self.get_volume_restore,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetVolumeRestore",
            ),
            self.get_backup_index_download_url: self._wrap_method(
                self.get_backup_index_download_url,
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
                method_name="google.cloud.gkebackup.v1.BackupForGKE/GetBackupIndexDownloadUrl",
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
    def create_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.CreateBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_plans(
        self,
    ) -> Callable[
        [gkebackup.ListBackupPlansRequest],
        Union[
            gkebackup.ListBackupPlansResponse,
            Awaitable[gkebackup.ListBackupPlansResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.GetBackupPlanRequest],
        Union[backup_plan.BackupPlan, Awaitable[backup_plan.BackupPlan]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.UpdateBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_plan(
        self,
    ) -> Callable[
        [gkebackup.DeleteBackupPlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.CreateBackupChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_channels(
        self,
    ) -> Callable[
        [gkebackup.ListBackupChannelsRequest],
        Union[
            gkebackup.ListBackupChannelsResponse,
            Awaitable[gkebackup.ListBackupChannelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.GetBackupChannelRequest],
        Union[backup_channel.BackupChannel, Awaitable[backup_channel.BackupChannel]],
    ]:
        raise NotImplementedError()

    @property
    def update_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.UpdateBackupChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup_channel(
        self,
    ) -> Callable[
        [gkebackup.DeleteBackupChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backup_plan_bindings(
        self,
    ) -> Callable[
        [gkebackup.ListBackupPlanBindingsRequest],
        Union[
            gkebackup.ListBackupPlanBindingsResponse,
            Awaitable[gkebackup.ListBackupPlanBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_plan_binding(
        self,
    ) -> Callable[
        [gkebackup.GetBackupPlanBindingRequest],
        Union[
            backup_plan_binding.BackupPlanBinding,
            Awaitable[backup_plan_binding.BackupPlanBinding],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_backup(
        self,
    ) -> Callable[
        [gkebackup.CreateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backups(
        self,
    ) -> Callable[
        [gkebackup.ListBackupsRequest],
        Union[gkebackup.ListBackupsResponse, Awaitable[gkebackup.ListBackupsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup(
        self,
    ) -> Callable[
        [gkebackup.GetBackupRequest], Union[backup.Backup, Awaitable[backup.Backup]]
    ]:
        raise NotImplementedError()

    @property
    def update_backup(
        self,
    ) -> Callable[
        [gkebackup.UpdateBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [gkebackup.DeleteBackupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_volume_backups(
        self,
    ) -> Callable[
        [gkebackup.ListVolumeBackupsRequest],
        Union[
            gkebackup.ListVolumeBackupsResponse,
            Awaitable[gkebackup.ListVolumeBackupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_volume_backup(
        self,
    ) -> Callable[
        [gkebackup.GetVolumeBackupRequest],
        Union[volume.VolumeBackup, Awaitable[volume.VolumeBackup]],
    ]:
        raise NotImplementedError()

    @property
    def create_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.CreateRestorePlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restore_plans(
        self,
    ) -> Callable[
        [gkebackup.ListRestorePlansRequest],
        Union[
            gkebackup.ListRestorePlansResponse,
            Awaitable[gkebackup.ListRestorePlansResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.GetRestorePlanRequest],
        Union[restore_plan.RestorePlan, Awaitable[restore_plan.RestorePlan]],
    ]:
        raise NotImplementedError()

    @property
    def update_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.UpdateRestorePlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_restore_plan(
        self,
    ) -> Callable[
        [gkebackup.DeleteRestorePlanRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.CreateRestoreChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restore_channels(
        self,
    ) -> Callable[
        [gkebackup.ListRestoreChannelsRequest],
        Union[
            gkebackup.ListRestoreChannelsResponse,
            Awaitable[gkebackup.ListRestoreChannelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.GetRestoreChannelRequest],
        Union[
            restore_channel.RestoreChannel, Awaitable[restore_channel.RestoreChannel]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.UpdateRestoreChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_restore_channel(
        self,
    ) -> Callable[
        [gkebackup.DeleteRestoreChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restore_plan_bindings(
        self,
    ) -> Callable[
        [gkebackup.ListRestorePlanBindingsRequest],
        Union[
            gkebackup.ListRestorePlanBindingsResponse,
            Awaitable[gkebackup.ListRestorePlanBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore_plan_binding(
        self,
    ) -> Callable[
        [gkebackup.GetRestorePlanBindingRequest],
        Union[
            restore_plan_binding.RestorePlanBinding,
            Awaitable[restore_plan_binding.RestorePlanBinding],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_restore(
        self,
    ) -> Callable[
        [gkebackup.CreateRestoreRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_restores(
        self,
    ) -> Callable[
        [gkebackup.ListRestoresRequest],
        Union[
            gkebackup.ListRestoresResponse, Awaitable[gkebackup.ListRestoresResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_restore(
        self,
    ) -> Callable[
        [gkebackup.GetRestoreRequest],
        Union[restore.Restore, Awaitable[restore.Restore]],
    ]:
        raise NotImplementedError()

    @property
    def update_restore(
        self,
    ) -> Callable[
        [gkebackup.UpdateRestoreRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_restore(
        self,
    ) -> Callable[
        [gkebackup.DeleteRestoreRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_volume_restores(
        self,
    ) -> Callable[
        [gkebackup.ListVolumeRestoresRequest],
        Union[
            gkebackup.ListVolumeRestoresResponse,
            Awaitable[gkebackup.ListVolumeRestoresResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_volume_restore(
        self,
    ) -> Callable[
        [gkebackup.GetVolumeRestoreRequest],
        Union[volume.VolumeRestore, Awaitable[volume.VolumeRestore]],
    ]:
        raise NotImplementedError()

    @property
    def get_backup_index_download_url(
        self,
    ) -> Callable[
        [gkebackup.GetBackupIndexDownloadUrlRequest],
        Union[
            gkebackup.GetBackupIndexDownloadUrlResponse,
            Awaitable[gkebackup.GetBackupIndexDownloadUrlResponse],
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


__all__ = ("BackupForGKETransport",)
