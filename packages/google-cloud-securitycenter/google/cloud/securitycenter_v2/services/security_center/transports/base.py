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

from google.cloud.securitycenter_v2 import gapic_version as package_version
from google.cloud.securitycenter_v2._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.securitycenter_v2._compat import (
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

from google.cloud.securitycenter_v2.types import (
    bigquery_export,
    finding,
    mute_config,
    notification_config,
    resource_value_config,
    securitycenter_service,
    simulation,
    source,
    valued_resource,
)
from google.cloud.securitycenter_v2.types import external_system as gcs_external_system
from google.cloud.securitycenter_v2.types import finding as gcs_finding
from google.cloud.securitycenter_v2.types import mute_config as gcs_mute_config
from google.cloud.securitycenter_v2.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v2.types import (
    resource_value_config as gcs_resource_value_config,
)
from google.cloud.securitycenter_v2.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v2.types import source as gcs_source

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class SecurityCenterTransport(abc.ABC):
    """Abstract transport class for SecurityCenter."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "securitycenter.googleapis.com"

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
                 The hostname to connect to (default: 'securitycenter.googleapis.com').
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
            self.batch_create_resource_value_configs: self._wrap_method(
                self.batch_create_resource_value_configs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/BatchCreateResourceValueConfigs",
            ),
            self.bulk_mute_findings: self._wrap_method(
                self.bulk_mute_findings,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/BulkMuteFindings",
            ),
            self.create_big_query_export: self._wrap_method(
                self.create_big_query_export,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/CreateBigQueryExport",
            ),
            self.create_finding: self._wrap_method(
                self.create_finding,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/CreateFinding",
            ),
            self.create_mute_config: self._wrap_method(
                self.create_mute_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/CreateMuteConfig",
            ),
            self.create_notification_config: self._wrap_method(
                self.create_notification_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/CreateNotificationConfig",
            ),
            self.create_source: self._wrap_method(
                self.create_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/CreateSource",
            ),
            self.delete_big_query_export: self._wrap_method(
                self.delete_big_query_export,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/DeleteBigQueryExport",
            ),
            self.delete_mute_config: self._wrap_method(
                self.delete_mute_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/DeleteMuteConfig",
            ),
            self.delete_notification_config: self._wrap_method(
                self.delete_notification_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/DeleteNotificationConfig",
            ),
            self.delete_resource_value_config: self._wrap_method(
                self.delete_resource_value_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/DeleteResourceValueConfig",
            ),
            self.get_big_query_export: self._wrap_method(
                self.get_big_query_export,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetBigQueryExport",
            ),
            self.get_simulation: self._wrap_method(
                self.get_simulation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetSimulation",
            ),
            self.get_valued_resource: self._wrap_method(
                self.get_valued_resource,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetValuedResource",
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetIamPolicy",
            ),
            self.get_mute_config: self._wrap_method(
                self.get_mute_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetMuteConfig",
            ),
            self.get_notification_config: self._wrap_method(
                self.get_notification_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetNotificationConfig",
            ),
            self.get_resource_value_config: self._wrap_method(
                self.get_resource_value_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetResourceValueConfig",
            ),
            self.get_source: self._wrap_method(
                self.get_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GetSource",
            ),
            self.group_findings: self._wrap_method(
                self.group_findings,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/GroupFindings",
            ),
            self.list_attack_paths: self._wrap_method(
                self.list_attack_paths,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListAttackPaths",
            ),
            self.list_big_query_exports: self._wrap_method(
                self.list_big_query_exports,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListBigQueryExports",
            ),
            self.list_findings: self._wrap_method(
                self.list_findings,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListFindings",
            ),
            self.list_mute_configs: self._wrap_method(
                self.list_mute_configs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListMuteConfigs",
            ),
            self.list_notification_configs: self._wrap_method(
                self.list_notification_configs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListNotificationConfigs",
            ),
            self.list_resource_value_configs: self._wrap_method(
                self.list_resource_value_configs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListResourceValueConfigs",
            ),
            self.list_sources: self._wrap_method(
                self.list_sources,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListSources",
            ),
            self.list_valued_resources: self._wrap_method(
                self.list_valued_resources,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/ListValuedResources",
            ),
            self.set_finding_state: self._wrap_method(
                self.set_finding_state,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/SetFindingState",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/SetIamPolicy",
            ),
            self.set_mute: self._wrap_method(
                self.set_mute,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/SetMute",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/TestIamPermissions",
            ),
            self.update_big_query_export: self._wrap_method(
                self.update_big_query_export,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateBigQueryExport",
            ),
            self.update_external_system: self._wrap_method(
                self.update_external_system,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateExternalSystem",
            ),
            self.update_finding: self._wrap_method(
                self.update_finding,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateFinding",
            ),
            self.update_mute_config: self._wrap_method(
                self.update_mute_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateMuteConfig",
            ),
            self.update_notification_config: self._wrap_method(
                self.update_notification_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateNotificationConfig",
            ),
            self.update_resource_value_config: self._wrap_method(
                self.update_resource_value_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateResourceValueConfig",
            ),
            self.update_security_marks: self._wrap_method(
                self.update_security_marks,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateSecurityMarks",
            ),
            self.update_source: self._wrap_method(
                self.update_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v2.SecurityCenter/UpdateSource",
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
    def batch_create_resource_value_configs(
        self,
    ) -> Callable[
        [securitycenter_service.BatchCreateResourceValueConfigsRequest],
        Union[
            securitycenter_service.BatchCreateResourceValueConfigsResponse,
            Awaitable[securitycenter_service.BatchCreateResourceValueConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def bulk_mute_findings(
        self,
    ) -> Callable[
        [securitycenter_service.BulkMuteFindingsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.CreateBigQueryExportRequest],
        Union[
            bigquery_export.BigQueryExport, Awaitable[bigquery_export.BigQueryExport]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_finding(
        self,
    ) -> Callable[
        [securitycenter_service.CreateFindingRequest],
        Union[gcs_finding.Finding, Awaitable[gcs_finding.Finding]],
    ]:
        raise NotImplementedError()

    @property
    def create_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.CreateMuteConfigRequest],
        Union[gcs_mute_config.MuteConfig, Awaitable[gcs_mute_config.MuteConfig]],
    ]:
        raise NotImplementedError()

    @property
    def create_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.CreateNotificationConfigRequest],
        Union[
            gcs_notification_config.NotificationConfig,
            Awaitable[gcs_notification_config.NotificationConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_source(
        self,
    ) -> Callable[
        [securitycenter_service.CreateSourceRequest],
        Union[gcs_source.Source, Awaitable[gcs_source.Source]],
    ]:
        raise NotImplementedError()

    @property
    def delete_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteBigQueryExportRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def delete_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteMuteConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def delete_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteNotificationConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def delete_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteResourceValueConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.GetBigQueryExportRequest],
        Union[
            bigquery_export.BigQueryExport, Awaitable[bigquery_export.BigQueryExport]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_simulation(
        self,
    ) -> Callable[
        [securitycenter_service.GetSimulationRequest],
        Union[simulation.Simulation, Awaitable[simulation.Simulation]],
    ]:
        raise NotImplementedError()

    @property
    def get_valued_resource(
        self,
    ) -> Callable[
        [securitycenter_service.GetValuedResourceRequest],
        Union[
            valued_resource.ValuedResource, Awaitable[valued_resource.ValuedResource]
        ],
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
    def get_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetMuteConfigRequest],
        Union[mute_config.MuteConfig, Awaitable[mute_config.MuteConfig]],
    ]:
        raise NotImplementedError()

    @property
    def get_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetNotificationConfigRequest],
        Union[
            notification_config.NotificationConfig,
            Awaitable[notification_config.NotificationConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetResourceValueConfigRequest],
        Union[
            resource_value_config.ResourceValueConfig,
            Awaitable[resource_value_config.ResourceValueConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_source(
        self,
    ) -> Callable[
        [securitycenter_service.GetSourceRequest],
        Union[source.Source, Awaitable[source.Source]],
    ]:
        raise NotImplementedError()

    @property
    def group_findings(
        self,
    ) -> Callable[
        [securitycenter_service.GroupFindingsRequest],
        Union[
            securitycenter_service.GroupFindingsResponse,
            Awaitable[securitycenter_service.GroupFindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_attack_paths(
        self,
    ) -> Callable[
        [securitycenter_service.ListAttackPathsRequest],
        Union[
            securitycenter_service.ListAttackPathsResponse,
            Awaitable[securitycenter_service.ListAttackPathsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_big_query_exports(
        self,
    ) -> Callable[
        [securitycenter_service.ListBigQueryExportsRequest],
        Union[
            securitycenter_service.ListBigQueryExportsResponse,
            Awaitable[securitycenter_service.ListBigQueryExportsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_findings(
        self,
    ) -> Callable[
        [securitycenter_service.ListFindingsRequest],
        Union[
            securitycenter_service.ListFindingsResponse,
            Awaitable[securitycenter_service.ListFindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_mute_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListMuteConfigsRequest],
        Union[
            securitycenter_service.ListMuteConfigsResponse,
            Awaitable[securitycenter_service.ListMuteConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_notification_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListNotificationConfigsRequest],
        Union[
            securitycenter_service.ListNotificationConfigsResponse,
            Awaitable[securitycenter_service.ListNotificationConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_resource_value_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListResourceValueConfigsRequest],
        Union[
            securitycenter_service.ListResourceValueConfigsResponse,
            Awaitable[securitycenter_service.ListResourceValueConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_sources(
        self,
    ) -> Callable[
        [securitycenter_service.ListSourcesRequest],
        Union[
            securitycenter_service.ListSourcesResponse,
            Awaitable[securitycenter_service.ListSourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_valued_resources(
        self,
    ) -> Callable[
        [securitycenter_service.ListValuedResourcesRequest],
        Union[
            securitycenter_service.ListValuedResourcesResponse,
            Awaitable[securitycenter_service.ListValuedResourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def set_finding_state(
        self,
    ) -> Callable[
        [securitycenter_service.SetFindingStateRequest],
        Union[finding.Finding, Awaitable[finding.Finding]],
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
    def set_mute(
        self,
    ) -> Callable[
        [securitycenter_service.SetMuteRequest],
        Union[finding.Finding, Awaitable[finding.Finding]],
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
    def update_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateBigQueryExportRequest],
        Union[
            bigquery_export.BigQueryExport, Awaitable[bigquery_export.BigQueryExport]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_external_system(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateExternalSystemRequest],
        Union[
            gcs_external_system.ExternalSystem,
            Awaitable[gcs_external_system.ExternalSystem],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_finding(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateFindingRequest],
        Union[gcs_finding.Finding, Awaitable[gcs_finding.Finding]],
    ]:
        raise NotImplementedError()

    @property
    def update_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateMuteConfigRequest],
        Union[gcs_mute_config.MuteConfig, Awaitable[gcs_mute_config.MuteConfig]],
    ]:
        raise NotImplementedError()

    @property
    def update_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateNotificationConfigRequest],
        Union[
            gcs_notification_config.NotificationConfig,
            Awaitable[gcs_notification_config.NotificationConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateResourceValueConfigRequest],
        Union[
            gcs_resource_value_config.ResourceValueConfig,
            Awaitable[gcs_resource_value_config.ResourceValueConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_security_marks(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSecurityMarksRequest],
        Union[
            gcs_security_marks.SecurityMarks,
            Awaitable[gcs_security_marks.SecurityMarks],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_source(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSourceRequest],
        Union[gcs_source.Source, Awaitable[gcs_source.Source]],
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


__all__ = ("SecurityCenterTransport",)
