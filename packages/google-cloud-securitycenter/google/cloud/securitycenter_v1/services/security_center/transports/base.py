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

import google.api_core
import google.auth  # type: ignore
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.securitycenter_v1 import gapic_version as package_version
from google.cloud.securitycenter_v1.types import (
    bigquery_export,
    effective_event_threat_detection_custom_module,
    effective_security_health_analytics_custom_module,
    event_threat_detection_custom_module,
    finding,
    mute_config,
    notification_config,
    organization_settings,
    resource_value_config,
    security_health_analytics_custom_module,
    securitycenter_service,
    simulation,
    source,
    valued_resource,
)
from google.cloud.securitycenter_v1.types import (
    event_threat_detection_custom_module as gcs_event_threat_detection_custom_module,
)
from google.cloud.securitycenter_v1.types import external_system as gcs_external_system
from google.cloud.securitycenter_v1.types import finding as gcs_finding
from google.cloud.securitycenter_v1.types import mute_config as gcs_mute_config
from google.cloud.securitycenter_v1.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v1.types import (
    organization_settings as gcs_organization_settings,
)
from google.cloud.securitycenter_v1.types import (
    resource_value_config as gcs_resource_value_config,
)
from google.cloud.securitycenter_v1.types import (
    security_health_analytics_custom_module as gcs_security_health_analytics_custom_module,
)
from google.cloud.securitycenter_v1.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v1.types import source as gcs_source

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

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.bulk_mute_findings: gapic_v1.method.wrap_method(
                self.bulk_mute_findings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.create_security_health_analytics_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_source: gapic_v1.method.wrap_method(
                self.create_source,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_finding: gapic_v1.method.wrap_method(
                self.create_finding,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_mute_config: gapic_v1.method.wrap_method(
                self.create_mute_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_notification_config: gapic_v1.method.wrap_method(
                self.create_notification_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_mute_config: gapic_v1.method.wrap_method(
                self.delete_mute_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_notification_config: gapic_v1.method.wrap_method(
                self.delete_notification_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.delete_security_health_analytics_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_simulation: gapic_v1.method.wrap_method(
                self.get_simulation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_valued_resource: gapic_v1.method.wrap_method(
                self.get_valued_resource,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_big_query_export: gapic_v1.method.wrap_method(
                self.get_big_query_export,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_mute_config: gapic_v1.method.wrap_method(
                self.get_mute_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_notification_config: gapic_v1.method.wrap_method(
                self.get_notification_config,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_organization_settings: gapic_v1.method.wrap_method(
                self.get_organization_settings,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_effective_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.get_effective_security_health_analytics_custom_module,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.get_security_health_analytics_custom_module,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_source: gapic_v1.method.wrap_method(
                self.get_source,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.group_assets: gapic_v1.method.wrap_method(
                self.group_assets,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
            ),
            self.group_findings: gapic_v1.method.wrap_method(
                self.group_findings,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
            ),
            self.list_assets: gapic_v1.method.wrap_method(
                self.list_assets,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
            ),
            self.list_descendant_security_health_analytics_custom_modules: gapic_v1.method.wrap_method(
                self.list_descendant_security_health_analytics_custom_modules,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_findings: gapic_v1.method.wrap_method(
                self.list_findings,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
            ),
            self.list_mute_configs: gapic_v1.method.wrap_method(
                self.list_mute_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_notification_configs: gapic_v1.method.wrap_method(
                self.list_notification_configs,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_effective_security_health_analytics_custom_modules: gapic_v1.method.wrap_method(
                self.list_effective_security_health_analytics_custom_modules,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_security_health_analytics_custom_modules: gapic_v1.method.wrap_method(
                self.list_security_health_analytics_custom_modules,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_sources: gapic_v1.method.wrap_method(
                self.list_sources,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.run_asset_discovery: gapic_v1.method.wrap_method(
                self.run_asset_discovery,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.set_finding_state: gapic_v1.method.wrap_method(
                self.set_finding_state,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.set_mute: gapic_v1.method.wrap_method(
                self.set_mute,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.simulate_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.simulate_security_health_analytics_custom_module,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_external_system: gapic_v1.method.wrap_method(
                self.update_external_system,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_finding: gapic_v1.method.wrap_method(
                self.update_finding,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_mute_config: gapic_v1.method.wrap_method(
                self.update_mute_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_notification_config: gapic_v1.method.wrap_method(
                self.update_notification_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_organization_settings: gapic_v1.method.wrap_method(
                self.update_organization_settings,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.update_security_health_analytics_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_source: gapic_v1.method.wrap_method(
                self.update_source,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_security_marks: gapic_v1.method.wrap_method(
                self.update_security_marks,
                default_timeout=480.0,
                client_info=client_info,
            ),
            self.create_big_query_export: gapic_v1.method.wrap_method(
                self.create_big_query_export,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_big_query_export: gapic_v1.method.wrap_method(
                self.delete_big_query_export,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_big_query_export: gapic_v1.method.wrap_method(
                self.update_big_query_export,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_big_query_exports: gapic_v1.method.wrap_method(
                self.list_big_query_exports,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.create_event_threat_detection_custom_module,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.delete_event_threat_detection_custom_module,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.get_event_threat_detection_custom_module,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_descendant_event_threat_detection_custom_modules: gapic_v1.method.wrap_method(
                self.list_descendant_event_threat_detection_custom_modules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_event_threat_detection_custom_modules: gapic_v1.method.wrap_method(
                self.list_event_threat_detection_custom_modules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.update_event_threat_detection_custom_module,
                default_timeout=None,
                client_info=client_info,
            ),
            self.validate_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.validate_event_threat_detection_custom_module,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_effective_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.get_effective_event_threat_detection_custom_module,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_effective_event_threat_detection_custom_modules: gapic_v1.method.wrap_method(
                self.list_effective_event_threat_detection_custom_modules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_create_resource_value_configs: gapic_v1.method.wrap_method(
                self.batch_create_resource_value_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_resource_value_config: gapic_v1.method.wrap_method(
                self.delete_resource_value_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_resource_value_config: gapic_v1.method.wrap_method(
                self.get_resource_value_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_resource_value_configs: gapic_v1.method.wrap_method(
                self.list_resource_value_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_resource_value_config: gapic_v1.method.wrap_method(
                self.update_resource_value_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_valued_resources: gapic_v1.method.wrap_method(
                self.list_valued_resources,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_attack_paths: gapic_v1.method.wrap_method(
                self.list_attack_paths,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
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
    def bulk_mute_findings(
        self,
    ) -> Callable[
        [securitycenter_service.BulkMuteFindingsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
            Awaitable[
                gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
            ],
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
    def delete_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
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
    def get_organization_settings(
        self,
    ) -> Callable[
        [securitycenter_service.GetOrganizationSettingsRequest],
        Union[
            organization_settings.OrganizationSettings,
            Awaitable[organization_settings.OrganizationSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_effective_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule,
            Awaitable[
                effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
            Awaitable[
                security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
            ],
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
    def group_assets(
        self,
    ) -> Callable[
        [securitycenter_service.GroupAssetsRequest],
        Union[
            securitycenter_service.GroupAssetsResponse,
            Awaitable[securitycenter_service.GroupAssetsResponse],
        ],
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
    def list_assets(
        self,
    ) -> Callable[
        [securitycenter_service.ListAssetsRequest],
        Union[
            securitycenter_service.ListAssetsResponse,
            Awaitable[securitycenter_service.ListAssetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_descendant_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest
        ],
        Union[
            securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
            Awaitable[
                securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesResponse
            ],
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
    def list_effective_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest
        ],
        Union[
            securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
            Awaitable[
                securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest],
        Union[
            securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse,
            Awaitable[
                securitycenter_service.ListSecurityHealthAnalyticsCustomModulesResponse
            ],
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
    def run_asset_discovery(
        self,
    ) -> Callable[
        [securitycenter_service.RunAssetDiscoveryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
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
    def set_mute(
        self,
    ) -> Callable[
        [securitycenter_service.SetMuteRequest],
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
    def simulate_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse,
            Awaitable[
                securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse
            ],
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
    def update_organization_settings(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateOrganizationSettingsRequest],
        Union[
            gcs_organization_settings.OrganizationSettings,
            Awaitable[gcs_organization_settings.OrganizationSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule,
            Awaitable[
                gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
            ],
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
    def delete_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteBigQueryExportRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
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
    def create_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.CreateEventThreatDetectionCustomModuleRequest],
        Union[
            gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
            Awaitable[
                gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetEventThreatDetectionCustomModuleRequest],
        Union[
            event_threat_detection_custom_module.EventThreatDetectionCustomModule,
            Awaitable[
                event_threat_detection_custom_module.EventThreatDetectionCustomModule
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_descendant_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest],
        Union[
            securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse,
            Awaitable[
                securitycenter_service.ListDescendantEventThreatDetectionCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListEventThreatDetectionCustomModulesRequest],
        Union[
            securitycenter_service.ListEventThreatDetectionCustomModulesResponse,
            Awaitable[
                securitycenter_service.ListEventThreatDetectionCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest],
        Union[
            gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule,
            Awaitable[
                gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def validate_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest],
        Union[
            securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse,
            Awaitable[
                securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_effective_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest],
        Union[
            effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule,
            Awaitable[
                effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_effective_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest],
        Union[
            securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse,
            Awaitable[
                securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesResponse
            ],
        ],
    ]:
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
    def delete_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteResourceValueConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
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
