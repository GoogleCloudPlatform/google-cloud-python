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
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.securitycentermanagement_v1 import gapic_version as package_version
from google.cloud.securitycentermanagement_v1.types import security_center_management

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class SecurityCenterManagementTransport(abc.ABC):
    """Abstract transport class for SecurityCenterManagement."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "securitycentermanagement.googleapis.com"

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
                 The hostname to connect to (default: 'securitycentermanagement.googleapis.com').
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
            self.create_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.create_security_health_analytics_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.update_security_health_analytics_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.delete_security_health_analytics_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.simulate_security_health_analytics_custom_module: gapic_v1.method.wrap_method(
                self.simulate_security_health_analytics_custom_module,
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
            self.list_effective_event_threat_detection_custom_modules: gapic_v1.method.wrap_method(
                self.list_effective_event_threat_detection_custom_modules,
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
            self.get_effective_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.get_effective_event_threat_detection_custom_module,
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
            self.list_event_threat_detection_custom_modules: gapic_v1.method.wrap_method(
                self.list_event_threat_detection_custom_modules,
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
            self.list_descendant_event_threat_detection_custom_modules: gapic_v1.method.wrap_method(
                self.list_descendant_event_threat_detection_custom_modules,
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
            self.get_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.get_event_threat_detection_custom_module,
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
            self.create_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.create_event_threat_detection_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.update_event_threat_detection_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.delete_event_threat_detection_custom_module,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.validate_event_threat_detection_custom_module: gapic_v1.method.wrap_method(
                self.validate_event_threat_detection_custom_module,
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
            self.get_security_center_service: gapic_v1.method.wrap_method(
                self.get_security_center_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_security_center_services: gapic_v1.method.wrap_method(
                self.list_security_center_services,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_security_center_service: gapic_v1.method.wrap_method(
                self.update_security_center_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
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
    def list_effective_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest
        ],
        Union[
            security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
            Awaitable[
                security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_effective_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [
            security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest
        ],
        Union[
            security_center_management.EffectiveSecurityHealthAnalyticsCustomModule,
            Awaitable[
                security_center_management.EffectiveSecurityHealthAnalyticsCustomModule
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest],
        Union[
            security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
            Awaitable[
                security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_descendant_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest
        ],
        Union[
            security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
            Awaitable[
                security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            security_center_management.SecurityHealthAnalyticsCustomModule,
            Awaitable[security_center_management.SecurityHealthAnalyticsCustomModule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            security_center_management.SecurityHealthAnalyticsCustomModule,
            Awaitable[security_center_management.SecurityHealthAnalyticsCustomModule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            security_center_management.SecurityHealthAnalyticsCustomModule,
            Awaitable[security_center_management.SecurityHealthAnalyticsCustomModule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def simulate_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest],
        Union[
            security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse,
            Awaitable[
                security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_effective_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest
        ],
        Union[
            security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
            Awaitable[
                security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_effective_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [
            security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest
        ],
        Union[
            security_center_management.EffectiveEventThreatDetectionCustomModule,
            Awaitable[
                security_center_management.EffectiveEventThreatDetectionCustomModule
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [security_center_management.ListEventThreatDetectionCustomModulesRequest],
        Union[
            security_center_management.ListEventThreatDetectionCustomModulesResponse,
            Awaitable[
                security_center_management.ListEventThreatDetectionCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_descendant_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest
        ],
        Union[
            security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
            Awaitable[
                security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.GetEventThreatDetectionCustomModuleRequest],
        Union[
            security_center_management.EventThreatDetectionCustomModule,
            Awaitable[security_center_management.EventThreatDetectionCustomModule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.CreateEventThreatDetectionCustomModuleRequest],
        Union[
            security_center_management.EventThreatDetectionCustomModule,
            Awaitable[security_center_management.EventThreatDetectionCustomModule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.UpdateEventThreatDetectionCustomModuleRequest],
        Union[
            security_center_management.EventThreatDetectionCustomModule,
            Awaitable[security_center_management.EventThreatDetectionCustomModule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.DeleteEventThreatDetectionCustomModuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def validate_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.ValidateEventThreatDetectionCustomModuleRequest],
        Union[
            security_center_management.ValidateEventThreatDetectionCustomModuleResponse,
            Awaitable[
                security_center_management.ValidateEventThreatDetectionCustomModuleResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_security_center_service(
        self,
    ) -> Callable[
        [security_center_management.GetSecurityCenterServiceRequest],
        Union[
            security_center_management.SecurityCenterService,
            Awaitable[security_center_management.SecurityCenterService],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_security_center_services(
        self,
    ) -> Callable[
        [security_center_management.ListSecurityCenterServicesRequest],
        Union[
            security_center_management.ListSecurityCenterServicesResponse,
            Awaitable[security_center_management.ListSecurityCenterServicesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_security_center_service(
        self,
    ) -> Callable[
        [security_center_management.UpdateSecurityCenterServiceRequest],
        Union[
            security_center_management.SecurityCenterService,
            Awaitable[security_center_management.SecurityCenterService],
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


__all__ = ("SecurityCenterManagementTransport",)
