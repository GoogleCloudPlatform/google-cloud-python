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
import logging as std_logging
import re
import warnings
from collections import OrderedDict
from typing import (
    Callable,
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.securitycenter_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.securitycenter_v1.services.security_center import pagers
from google.cloud.securitycenter_v1.types import (
    access,
    agent,
    agent_anomaly,
    agent_session,
    application,
    attack_exposure,
    attack_path,
    backup_disaster_recovery,
    bigquery_export,
    chokepoint,
    cloud_armor,
    cloud_dlp_data_profile,
    cloud_dlp_inspection,
    compliance,
    connection,
    container,
    database,
    effective_event_threat_detection_custom_module,
    effective_security_health_analytics_custom_module,
    event_threat_detection_custom_module,
    event_threat_detection_custom_module_validation_errors,
    exfiltration,
    external_exposure,
    file,
    finding,
    group_membership,
    iam_binding,
    indicator,
    kernel_rootkit,
    kubernetes,
    load_balancer,
    log_entry,
    mitre_attack,
    mute_config,
    notebook,
    notification_config,
    org_policy,
    organization_settings,
    process,
    resource,
    resource_value_config,
    run_asset_discovery_response,
    security_health_analytics_custom_config,
    security_health_analytics_custom_module,
    security_marks,
    security_posture,
    securitycenter_service,
    simulation,
    source,
    toxic_combination,
    valued_resource,
    vulnerability,
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

from .client import SecurityCenterClient
from .transports.base import DEFAULT_CLIENT_INFO, SecurityCenterTransport
from .transports.grpc_asyncio import SecurityCenterGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class SecurityCenterAsyncClient:
    """V1 APIs for Security Center service."""

    _client: SecurityCenterClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SecurityCenterClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SecurityCenterClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = SecurityCenterClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = SecurityCenterClient._DEFAULT_UNIVERSE

    asset_path = staticmethod(SecurityCenterClient.asset_path)
    parse_asset_path = staticmethod(SecurityCenterClient.parse_asset_path)
    attack_path_path = staticmethod(SecurityCenterClient.attack_path_path)
    parse_attack_path_path = staticmethod(SecurityCenterClient.parse_attack_path_path)
    big_query_export_path = staticmethod(SecurityCenterClient.big_query_export_path)
    parse_big_query_export_path = staticmethod(
        SecurityCenterClient.parse_big_query_export_path
    )
    dlp_job_path = staticmethod(SecurityCenterClient.dlp_job_path)
    parse_dlp_job_path = staticmethod(SecurityCenterClient.parse_dlp_job_path)
    effective_event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterClient.effective_event_threat_detection_custom_module_path
    )
    parse_effective_event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterClient.parse_effective_event_threat_detection_custom_module_path
    )
    effective_security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterClient.effective_security_health_analytics_custom_module_path
    )
    parse_effective_security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterClient.parse_effective_security_health_analytics_custom_module_path
    )
    event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterClient.event_threat_detection_custom_module_path
    )
    parse_event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterClient.parse_event_threat_detection_custom_module_path
    )
    external_system_path = staticmethod(SecurityCenterClient.external_system_path)
    parse_external_system_path = staticmethod(
        SecurityCenterClient.parse_external_system_path
    )
    finding_path = staticmethod(SecurityCenterClient.finding_path)
    parse_finding_path = staticmethod(SecurityCenterClient.parse_finding_path)
    mute_config_path = staticmethod(SecurityCenterClient.mute_config_path)
    parse_mute_config_path = staticmethod(SecurityCenterClient.parse_mute_config_path)
    notification_config_path = staticmethod(
        SecurityCenterClient.notification_config_path
    )
    parse_notification_config_path = staticmethod(
        SecurityCenterClient.parse_notification_config_path
    )
    organization_settings_path = staticmethod(
        SecurityCenterClient.organization_settings_path
    )
    parse_organization_settings_path = staticmethod(
        SecurityCenterClient.parse_organization_settings_path
    )
    policy_path = staticmethod(SecurityCenterClient.policy_path)
    parse_policy_path = staticmethod(SecurityCenterClient.parse_policy_path)
    resource_value_config_path = staticmethod(
        SecurityCenterClient.resource_value_config_path
    )
    parse_resource_value_config_path = staticmethod(
        SecurityCenterClient.parse_resource_value_config_path
    )
    security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterClient.security_health_analytics_custom_module_path
    )
    parse_security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterClient.parse_security_health_analytics_custom_module_path
    )
    security_marks_path = staticmethod(SecurityCenterClient.security_marks_path)
    parse_security_marks_path = staticmethod(
        SecurityCenterClient.parse_security_marks_path
    )
    simulation_path = staticmethod(SecurityCenterClient.simulation_path)
    parse_simulation_path = staticmethod(SecurityCenterClient.parse_simulation_path)
    source_path = staticmethod(SecurityCenterClient.source_path)
    parse_source_path = staticmethod(SecurityCenterClient.parse_source_path)
    table_data_profile_path = staticmethod(SecurityCenterClient.table_data_profile_path)
    parse_table_data_profile_path = staticmethod(
        SecurityCenterClient.parse_table_data_profile_path
    )
    topic_path = staticmethod(SecurityCenterClient.topic_path)
    parse_topic_path = staticmethod(SecurityCenterClient.parse_topic_path)
    valued_resource_path = staticmethod(SecurityCenterClient.valued_resource_path)
    parse_valued_resource_path = staticmethod(
        SecurityCenterClient.parse_valued_resource_path
    )
    common_billing_account_path = staticmethod(
        SecurityCenterClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        SecurityCenterClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(SecurityCenterClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        SecurityCenterClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        SecurityCenterClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        SecurityCenterClient.parse_common_organization_path
    )
    common_project_path = staticmethod(SecurityCenterClient.common_project_path)
    parse_common_project_path = staticmethod(
        SecurityCenterClient.parse_common_project_path
    )
    common_location_path = staticmethod(SecurityCenterClient.common_location_path)
    parse_common_location_path = staticmethod(
        SecurityCenterClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            SecurityCenterAsyncClient: The constructed client.
        """
        sa_info_func = (
            SecurityCenterClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(SecurityCenterAsyncClient, info, *args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            SecurityCenterAsyncClient: The constructed client.
        """
        sa_file_func = (
            SecurityCenterClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(SecurityCenterAsyncClient, filename, *args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return SecurityCenterClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> SecurityCenterTransport:
        """Returns the transport used by the client instance.

        Returns:
            SecurityCenterTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = SecurityCenterClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, SecurityCenterTransport, Callable[..., SecurityCenterTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the security center async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SecurityCenterTransport,Callable[..., SecurityCenterTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SecurityCenterTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = SecurityCenterClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.securitycenter_v1.SecurityCenterAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                    "universeDomain": getattr(
                        self._client._transport._credentials, "universe_domain", ""
                    ),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(
                        self.transport._credentials, "get_cred_info", lambda: None
                    )(),
                }
                if hasattr(self._client._transport, "_credentials")
                else {
                    "serviceName": "google.cloud.securitycenter.v1.SecurityCenter",
                    "credentialsType": None,
                },
            )

    async def bulk_mute_findings(
        self,
        request: Optional[
            Union[securitycenter_service.BulkMuteFindingsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Kicks off an LRO to bulk mute findings for a parent
        based on a filter. The parent can be either an
        organization, folder or project. The findings matched by
        the filter will be muted after the LRO is done.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_bulk_mute_findings():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.BulkMuteFindingsRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = await client.bulk_mute_findings(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.BulkMuteFindingsRequest, dict]]):
                The request object. Request message for bulk findings
                update.
                Note:

                1. If multiple bulk update requests
                    match the same resource, the order
                    in which they get executed is not
                    defined.
                2. Once a bulk operation is started,
                    there is no way to stop it.
            parent (:class:`str`):
                Required. The parent, at which bulk action needs to be
                applied. Its format is
                ``organizations/[organization_id]``,
                ``folders/[folder_id]``, ``projects/[project_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.securitycenter_v1.types.BulkMuteFindingsResponse`
                The response to a BulkMute request. Contains the LRO
                information.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.BulkMuteFindingsRequest):
            request = securitycenter_service.BulkMuteFindingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.bulk_mute_findings
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            securitycenter_service.BulkMuteFindingsResponse,
            metadata_type=empty_pb2.Empty,
        )

        # Done; return the response.
        return response

    async def create_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        security_health_analytics_custom_module: Optional[
            gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> (
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    ):
        r"""Creates a resident
        SecurityHealthAnalyticsCustomModule at the scope of the
        given CRM parent, and also creates inherited
        SecurityHealthAnalyticsCustomModules for all CRM
        descendants of the given parent. These modules are
        enabled by default.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_create_security_health_analytics_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.CreateSecurityHealthAnalyticsCustomModuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for creating Security
                Health Analytics custom modules.
            parent (:class:`str`):
                Required. Resource name of the new custom module's
                parent. Its format is
                ``organizations/{organization}/securityHealthAnalyticsSettings``,
                ``folders/{folder}/securityHealthAnalyticsSettings``, or
                ``projects/{project}/securityHealthAnalyticsSettings``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_health_analytics_custom_module (:class:`google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule`):
                Required. SecurityHealthAnalytics
                custom module to create. The provided
                name is ignored and reset with provided
                parent information and server-generated
                ID.

                This corresponds to the ``security_health_analytics_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the child folders and
                projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, security_health_analytics_custom_module]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = (
                securitycenter_service.CreateSecurityHealthAnalyticsCustomModuleRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if security_health_analytics_custom_module is not None:
            request.security_health_analytics_custom_module = (
                security_health_analytics_custom_module
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_source(
        self,
        request: Optional[
            Union[securitycenter_service.CreateSourceRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        source: Optional[gcs_source.Source] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_source.Source:
        r"""Creates a source.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_create_source():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.CreateSourceRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_source(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.CreateSourceRequest, dict]]):
                The request object. Request message for creating a
                source.
            parent (:class:`str`):
                Required. Resource name of the new source's parent. Its
                format should be ``organizations/[organization_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            source (:class:`google.cloud.securitycenter_v1.types.Source`):
                Required. The Source being created, only the
                display_name and description will be used. All other
                fields will be ignored.

                This corresponds to the ``source`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Source:
                Security Command Center finding
                source. A finding source is an entity or
                a mechanism that can produce a finding.
                A source is like a container of findings
                that come from the same scanner, logger,
                monitor, and other tools.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, source]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.CreateSourceRequest):
            request = securitycenter_service.CreateSourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if source is not None:
            request.source = source

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_source
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_finding(
        self,
        request: Optional[
            Union[securitycenter_service.CreateFindingRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        finding_id: Optional[str] = None,
        finding: Optional[gcs_finding.Finding] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_finding.Finding:
        r"""Creates a finding. The corresponding source must
        exist for finding creation to succeed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_create_finding():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.CreateFindingRequest(
                    parent="parent_value",
                    finding_id="finding_id_value",
                )

                # Make the request
                response = await client.create_finding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.CreateFindingRequest, dict]]):
                The request object. Request message for creating a
                finding.
            parent (:class:`str`):
                Required. Resource name of the new finding's parent. Its
                format should be
                ``organizations/[organization_id]/sources/[source_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            finding_id (:class:`str`):
                Required. Unique identifier provided
                by the client within the parent scope.
                It must be alphanumeric and less than or
                equal to 32 characters and greater than
                0 characters in length.

                This corresponds to the ``finding_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            finding (:class:`google.cloud.securitycenter_v1.types.Finding`):
                Required. The Finding being created. The name and
                security_marks will be ignored as they are both output
                only fields on this resource.

                This corresponds to the ``finding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Finding:
                Security Command Center finding.

                A finding is a record of assessment data
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, finding_id, finding]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.CreateFindingRequest):
            request = securitycenter_service.CreateFindingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if finding_id is not None:
            request.finding_id = finding_id
        if finding is not None:
            request.finding = finding

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_finding
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_mute_config(
        self,
        request: Optional[
            Union[securitycenter_service.CreateMuteConfigRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        mute_config: Optional[gcs_mute_config.MuteConfig] = None,
        mute_config_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_mute_config.MuteConfig:
        r"""Creates a mute config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_create_mute_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                mute_config = securitycenter_v1.MuteConfig()
                mute_config.filter = "filter_value"

                request = securitycenter_v1.CreateMuteConfigRequest(
                    parent="parent_value",
                    mute_config=mute_config,
                    mute_config_id="mute_config_id_value",
                )

                # Make the request
                response = await client.create_mute_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.CreateMuteConfigRequest, dict]]):
                The request object. Request message for creating a mute
                config.
            parent (:class:`str`):
                Required. Resource name of the new mute configs's
                parent. Its format is
                ``organizations/[organization_id]``,
                ``folders/[folder_id]``, or ``projects/[project_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            mute_config (:class:`google.cloud.securitycenter_v1.types.MuteConfig`):
                Required. The mute config being
                created.

                This corresponds to the ``mute_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            mute_config_id (:class:`str`):
                Required. Unique identifier provided
                by the client within the parent scope.
                It must consist of only lowercase
                letters, numbers, and hyphens, must
                start with a letter, must end with
                either a letter or a number, and must be
                63 characters or less.

                This corresponds to the ``mute_config_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.MuteConfig:
                A mute config is a Cloud SCC resource
                that contains the configuration to mute
                create/update events of findings.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, mute_config, mute_config_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.CreateMuteConfigRequest):
            request = securitycenter_service.CreateMuteConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if mute_config is not None:
            request.mute_config = mute_config
        if mute_config_id is not None:
            request.mute_config_id = mute_config_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_mute_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_notification_config(
        self,
        request: Optional[
            Union[securitycenter_service.CreateNotificationConfigRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        config_id: Optional[str] = None,
        notification_config: Optional[
            gcs_notification_config.NotificationConfig
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_notification_config.NotificationConfig:
        r"""Creates a notification config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_create_notification_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.CreateNotificationConfigRequest(
                    parent="parent_value",
                    config_id="config_id_value",
                )

                # Make the request
                response = await client.create_notification_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.CreateNotificationConfigRequest, dict]]):
                The request object. Request message for creating a
                notification config.
            parent (:class:`str`):
                Required. Resource name of the new notification config's
                parent. Its format is
                ``organizations/[organization_id]``,
                ``folders/[folder_id]``, or ``projects/[project_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            config_id (:class:`str`):
                Required.
                Unique identifier provided by the client
                within the parent scope. It must be
                between 1 and 128 characters and contain
                alphanumeric characters, underscores, or
                hyphens only.

                This corresponds to the ``config_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            notification_config (:class:`google.cloud.securitycenter_v1.types.NotificationConfig`):
                Required. The notification config
                being created. The name and the service
                account will be ignored as they are both
                output only fields on this resource.

                This corresponds to the ``notification_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.NotificationConfig:
                Cloud Security Command Center (Cloud
                SCC) notification configs.
                A notification config is a Cloud SCC
                resource that contains the configuration
                to send notifications for create/update
                events of findings, assets and etc.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, config_id, notification_config]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.CreateNotificationConfigRequest
        ):
            request = securitycenter_service.CreateNotificationConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if config_id is not None:
            request.config_id = config_id
        if notification_config is not None:
            request.notification_config = notification_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_notification_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_mute_config(
        self,
        request: Optional[
            Union[securitycenter_service.DeleteMuteConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing mute config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_delete_mute_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.DeleteMuteConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_mute_config(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.DeleteMuteConfigRequest, dict]]):
                The request object. Request message for deleting a mute
                config.
            name (:class:`str`):
                Required. Name of the mute config to delete. Its format
                is
                ``organizations/{organization}/muteConfigs/{config_id}``,
                ``folders/{folder}/muteConfigs/{config_id}``,
                ``projects/{project}/muteConfigs/{config_id}``,
                ``organizations/{organization}/locations/global/muteConfigs/{config_id}``,
                ``folders/{folder}/locations/global/muteConfigs/{config_id}``,
                or
                ``projects/{project}/locations/global/muteConfigs/{config_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.DeleteMuteConfigRequest):
            request = securitycenter_service.DeleteMuteConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_mute_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def delete_notification_config(
        self,
        request: Optional[
            Union[securitycenter_service.DeleteNotificationConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a notification config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_delete_notification_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.DeleteNotificationConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_notification_config(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.DeleteNotificationConfigRequest, dict]]):
                The request object. Request message for deleting a
                notification config.
            name (:class:`str`):
                Required. Name of the notification config to delete. Its
                format is
                ``organizations/[organization_id]/notificationConfigs/[config_id]``,
                ``folders/[folder_id]/notificationConfigs/[config_id]``,
                or
                ``projects/[project_id]/notificationConfigs/[config_id]``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.DeleteNotificationConfigRequest
        ):
            request = securitycenter_service.DeleteNotificationConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_notification_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def delete_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified
        SecurityHealthAnalyticsCustomModule and all of its
        descendants in the CRM hierarchy. This method is only
        supported for resident custom modules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_delete_security_health_analytics_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.DeleteSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_security_health_analytics_custom_module(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for deleting Security
                Health Analytics custom modules.
            name (:class:`str`):
                Required. Name of the custom module to delete. Its
                format is
                ``organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}``,
                ``folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}``,
                or
                ``projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = (
                securitycenter_service.DeleteSecurityHealthAnalyticsCustomModuleRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_simulation(
        self,
        request: Optional[
            Union[securitycenter_service.GetSimulationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> simulation.Simulation:
        r"""Get the simulation by name or the latest simulation
        for the given organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_simulation():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetSimulationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_simulation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetSimulationRequest, dict]]):
                The request object. Request message for getting
                simulation. Simulation name can include
                "latest" to retrieve the latest
                simulation For example,
                "organizations/123/simulations/latest".
            name (:class:`str`):
                Required. The organization name or simulation name of
                this simulation

                Valid format:
                ``organizations/{organization}/simulations/latest``
                ``organizations/{organization}/simulations/{simulation}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Simulation:
                Attack path simulation
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GetSimulationRequest):
            request = securitycenter_service.GetSimulationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_simulation
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_valued_resource(
        self,
        request: Optional[
            Union[securitycenter_service.GetValuedResourceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> valued_resource.ValuedResource:
        r"""Get the valued resource by name

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_valued_resource():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetValuedResourceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_valued_resource(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetValuedResourceRequest, dict]]):
                The request object. Request message for getting a valued
                resource.
            name (:class:`str`):
                Required. The name of this valued resource

                Valid format:
                ``organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.ValuedResource:
                A resource that is determined to have
                value to a user's system

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GetValuedResourceRequest):
            request = securitycenter_service.GetValuedResourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_valued_resource
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_big_query_export(
        self,
        request: Optional[
            Union[securitycenter_service.GetBigQueryExportRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> bigquery_export.BigQueryExport:
        r"""Gets a BigQuery export.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_big_query_export():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetBigQueryExportRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_big_query_export(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetBigQueryExportRequest, dict]]):
                The request object. Request message for retrieving a
                BigQuery export.
            name (:class:`str`):
                Required. Name of the BigQuery export to retrieve. Its
                format is
                ``organizations/{organization}/bigQueryExports/{export_id}``,
                ``folders/{folder}/bigQueryExports/{export_id}``, or
                ``projects/{project}/bigQueryExports/{export_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.BigQueryExport:
                Configures how to deliver Findings to
                BigQuery Instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GetBigQueryExportRequest):
            request = securitycenter_service.GetBigQueryExportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_big_query_export
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.GetIamPolicyRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the access control policy on the specified
        Source.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            async def sample_get_iam_policy():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.GetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.get_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]]):
                The request object. Request message for ``GetIamPolicy`` method.
            resource (:class:`str`):
                REQUIRED: The resource for which the
                policy is being requested. See the
                operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time <             timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

                   **YAML example:**

                   :literal:``     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\ \`

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - The request isn't a proto-plus wrapped type,
        #   so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.GetIamPolicyRequest(**request)
        elif not request:
            request = iam_policy_pb2.GetIamPolicyRequest(resource=resource)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_iam_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_mute_config(
        self,
        request: Optional[
            Union[securitycenter_service.GetMuteConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> mute_config.MuteConfig:
        r"""Gets a mute config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_mute_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetMuteConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_mute_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetMuteConfigRequest, dict]]):
                The request object. Request message for retrieving a mute
                config.
            name (:class:`str`):
                Required. Name of the mute config to retrieve. Its
                format is
                ``organizations/{organization}/muteConfigs/{config_id}``,
                ``folders/{folder}/muteConfigs/{config_id}``,
                ``projects/{project}/muteConfigs/{config_id}``,
                ``organizations/{organization}/locations/global/muteConfigs/{config_id}``,
                ``folders/{folder}/locations/global/muteConfigs/{config_id}``,
                or
                ``projects/{project}/locations/global/muteConfigs/{config_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.MuteConfig:
                A mute config is a Cloud SCC resource
                that contains the configuration to mute
                create/update events of findings.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GetMuteConfigRequest):
            request = securitycenter_service.GetMuteConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_mute_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_notification_config(
        self,
        request: Optional[
            Union[securitycenter_service.GetNotificationConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> notification_config.NotificationConfig:
        r"""Gets a notification config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_notification_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetNotificationConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_notification_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetNotificationConfigRequest, dict]]):
                The request object. Request message for getting a
                notification config.
            name (:class:`str`):
                Required. Name of the notification config to get. Its
                format is
                ``organizations/[organization_id]/notificationConfigs/[config_id]``,
                ``folders/[folder_id]/notificationConfigs/[config_id]``,
                or
                ``projects/[project_id]/notificationConfigs/[config_id]``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.NotificationConfig:
                Cloud Security Command Center (Cloud
                SCC) notification configs.
                A notification config is a Cloud SCC
                resource that contains the configuration
                to send notifications for create/update
                events of findings, assets and etc.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GetNotificationConfigRequest):
            request = securitycenter_service.GetNotificationConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_notification_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_organization_settings(
        self,
        request: Optional[
            Union[securitycenter_service.GetOrganizationSettingsRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> organization_settings.OrganizationSettings:
        r"""Gets the settings for an organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_organization_settings():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetOrganizationSettingsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_organization_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetOrganizationSettingsRequest, dict]]):
                The request object. Request message for getting
                organization settings.
            name (:class:`str`):
                Required. Name of the organization to get organization
                settings for. Its format is
                ``organizations/[organization_id]/organizationSettings``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.OrganizationSettings:
                User specified settings that are
                attached to the Security Command Center
                organization.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.GetOrganizationSettingsRequest
        ):
            request = securitycenter_service.GetOrganizationSettingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_organization_settings
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_effective_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> effective_security_health_analytics_custom_module.EffectiveSecurityHealthAnalyticsCustomModule:
        r"""Retrieves an
        EffectiveSecurityHealthAnalyticsCustomModule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_effective_security_health_analytics_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_effective_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for getting effective
                Security Health Analytics custom
                modules.
            name (:class:`str`):
                Required. Name of the effective custom module to get.
                Its format is
                ``organizations/{organization}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}``,
                ``folders/{folder}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}``,
                or
                ``projects/{project}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.EffectiveSecurityHealthAnalyticsCustomModule:
                An EffectiveSecurityHealthAnalyticsCustomModule is the representation of
                   a Security Health Analytics custom module at a
                   specified level of the resource hierarchy:
                   organization, folder, or project. If a custom module
                   is inherited from a parent organization or folder,
                   the value of the enablementState property in
                   EffectiveSecurityHealthAnalyticsCustomModule is set
                   to the value that is effective in the parent, instead
                   of INHERITED. For example, if the module is enabled
                   in a parent organization or folder, the effective
                   enablement_state for the module in all child folders
                   or projects is also enabled.
                   EffectiveSecurityHealthAnalyticsCustomModule is
                   read-only.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = securitycenter_service.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_effective_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule:
        r"""Retrieves a SecurityHealthAnalyticsCustomModule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_security_health_analytics_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for getting Security
                Health Analytics custom modules.
            name (:class:`str`):
                Required. Name of the custom module to get. Its format
                is
                ``organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}``,
                ``folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}``,
                or
                ``projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the child folders and
                projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = (
                securitycenter_service.GetSecurityHealthAnalyticsCustomModuleRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_source(
        self,
        request: Optional[Union[securitycenter_service.GetSourceRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> source.Source:
        r"""Gets a source.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_source():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetSourceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_source(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetSourceRequest, dict]]):
                The request object. Request message for getting a source.
            name (:class:`str`):
                Required. Relative resource name of the source. Its
                format is
                ``organizations/[organization_id]/source/[source_id]``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Source:
                Security Command Center finding
                source. A finding source is an entity or
                a mechanism that can produce a finding.
                A source is like a container of findings
                that come from the same scanner, logger,
                monitor, and other tools.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GetSourceRequest):
            request = securitycenter_service.GetSourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_source
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def group_assets(
        self,
        request: Optional[
            Union[securitycenter_service.GroupAssetsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.GroupAssetsAsyncPager:
        r"""Filters an organization's assets and  groups them by
        their specified properties.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_group_assets():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GroupAssetsRequest(
                    parent="parent_value",
                    group_by="group_by_value",
                )

                # Make the request
                page_result = client.group_assets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GroupAssetsRequest, dict]]):
                The request object. Request message for grouping by
                assets.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.GroupAssetsAsyncPager:
                Response message for grouping by
                assets.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        warnings.warn(
            "SecurityCenterAsyncClient.group_assets is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GroupAssetsRequest):
            request = securitycenter_service.GroupAssetsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.group_assets
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.GroupAssetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def group_findings(
        self,
        request: Optional[
            Union[securitycenter_service.GroupFindingsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        group_by: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.GroupFindingsAsyncPager:
        r"""Filters an organization or source's findings and groups them by
        their specified properties.

        To group across all sources provide a ``-`` as the source id.
        Example: /v1/organizations/{organization_id}/sources/-/findings,
        /v1/folders/{folder_id}/sources/-/findings,
        /v1/projects/{project_id}/sources/-/findings

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_group_findings():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GroupFindingsRequest(
                    parent="parent_value",
                    group_by="group_by_value",
                )

                # Make the request
                page_result = client.group_findings(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GroupFindingsRequest, dict]]):
                The request object. Request message for grouping by
                findings.
            parent (:class:`str`):
                Required. Name of the source to groupBy. Its format is
                ``organizations/[organization_id]/sources/[source_id]``,
                ``folders/[folder_id]/sources/[source_id]``, or
                ``projects/[project_id]/sources/[source_id]``. To
                groupBy across all sources provide a source_id of ``-``.
                For example:
                ``organizations/{organization_id}/sources/-, folders/{folder_id}/sources/-``,
                or ``projects/{project_id}/sources/-``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            group_by (:class:`str`):
                Required. Expression that defines what assets fields to
                use for grouping (including ``state_change``). The
                string value should follow SQL syntax: comma separated
                list of fields. For example: "parent,resource_name".

                The following fields are supported when compare_duration
                is set:

                - state_change

                This corresponds to the ``group_by`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.GroupFindingsAsyncPager:
                Response message for group by
                findings.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, group_by]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.GroupFindingsRequest):
            request = securitycenter_service.GroupFindingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if group_by is not None:
            request.group_by = group_by

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.group_findings
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.GroupFindingsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_assets(
        self,
        request: Optional[Union[securitycenter_service.ListAssetsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAssetsAsyncPager:
        r"""Lists an organization's assets.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_assets():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListAssetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_assets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListAssetsRequest, dict]]):
                The request object. Request message for listing assets.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListAssetsAsyncPager:
                Response message for listing assets.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        warnings.warn(
            "SecurityCenterAsyncClient.list_assets is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.ListAssetsRequest):
            request = securitycenter_service.ListAssetsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_assets
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListAssetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_descendant_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager:
        r"""Returns a list of all resident
        SecurityHealthAnalyticsCustomModules under the given CRM
        parent and all of the parent’s CRM descendants.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_descendant_security_health_analytics_custom_modules():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_descendant_security_health_analytics_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest, dict]]):
                The request object. Request message for listing
                descendant Security Health Analytics
                custom modules.
            parent (:class:`str`):
                Required. Name of parent to list descendant custom
                modules. Its format is
                ``organizations/{organization}/securityHealthAnalyticsSettings``,
                ``folders/{folder}/securityHealthAnalyticsSettings``, or
                ``projects/{project}/securityHealthAnalyticsSettings``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager:
                Response message for listing
                descendant Security Health Analytics
                custom modules.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = securitycenter_service.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_descendant_security_health_analytics_custom_modules
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_findings(
        self,
        request: Optional[
            Union[securitycenter_service.ListFindingsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListFindingsAsyncPager:
        r"""Lists an organization or source's findings.

        To list across all sources provide a ``-`` as the source id.
        Example: /v1/organizations/{organization_id}/sources/-/findings

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_findings():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListFindingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_findings(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListFindingsRequest, dict]]):
                The request object. Request message for listing findings.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListFindingsAsyncPager:
                Response message for listing
                findings.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.ListFindingsRequest):
            request = securitycenter_service.ListFindingsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_findings
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListFindingsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_mute_configs(
        self,
        request: Optional[
            Union[securitycenter_service.ListMuteConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListMuteConfigsAsyncPager:
        r"""Lists mute configs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_mute_configs():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListMuteConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_mute_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListMuteConfigsRequest, dict]]):
                The request object. Request message for listing  mute
                configs at a given scope e.g.
                organization, folder or project.
            parent (:class:`str`):
                Required. The parent, which owns the collection of mute
                configs. Its format is
                ``organizations/[organization_id]``,
                ``folders/[folder_id]``, ``projects/[project_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListMuteConfigsAsyncPager:
                Response message for listing mute
                configs.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.ListMuteConfigsRequest):
            request = securitycenter_service.ListMuteConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_mute_configs
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListMuteConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_notification_configs(
        self,
        request: Optional[
            Union[securitycenter_service.ListNotificationConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListNotificationConfigsAsyncPager:
        r"""Lists notification configs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_notification_configs():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListNotificationConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_notification_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListNotificationConfigsRequest, dict]]):
                The request object. Request message for listing
                notification configs.
            parent (:class:`str`):
                Required. The name of the parent in which to list the
                notification configurations. Its format is
                "organizations/[organization_id]",
                "folders/[folder_id]", or "projects/[project_id]".

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListNotificationConfigsAsyncPager:
                Response message for listing
                notification configs.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.ListNotificationConfigsRequest
        ):
            request = securitycenter_service.ListNotificationConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_notification_configs
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListNotificationConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_effective_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager:
        r"""Returns a list of all
        EffectiveSecurityHealthAnalyticsCustomModules for the
        given parent. This includes resident modules defined at
        the scope of the parent, and inherited modules,
        inherited from CRM ancestors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_effective_security_health_analytics_custom_modules():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_effective_security_health_analytics_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest, dict]]):
                The request object. Request message for listing effective
                Security Health Analytics custom
                modules.
            parent (:class:`str`):
                Required. Name of parent to list effective custom
                modules. Its format is
                ``organizations/{organization}/securityHealthAnalyticsSettings``,
                ``folders/{folder}/securityHealthAnalyticsSettings``, or
                ``projects/{project}/securityHealthAnalyticsSettings``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager:
                Response message for listing
                effective Security Health Analytics
                custom modules.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = securitycenter_service.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_effective_security_health_analytics_custom_modules
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSecurityHealthAnalyticsCustomModulesAsyncPager:
        r"""Returns a list of all
        SecurityHealthAnalyticsCustomModules for the given
        parent. This includes resident modules defined at the
        scope of the parent, and inherited modules, inherited
        from CRM ancestors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_security_health_analytics_custom_modules():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_security_health_analytics_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest, dict]]):
                The request object. Request message for listing Security
                Health Analytics custom modules.
            parent (:class:`str`):
                Required. Name of parent to list custom modules. Its
                format is
                ``organizations/{organization}/securityHealthAnalyticsSettings``,
                ``folders/{folder}/securityHealthAnalyticsSettings``, or
                ``projects/{project}/securityHealthAnalyticsSettings``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListSecurityHealthAnalyticsCustomModulesAsyncPager:
                Response message for listing Security
                Health Analytics custom modules.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = (
                securitycenter_service.ListSecurityHealthAnalyticsCustomModulesRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_security_health_analytics_custom_modules
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListSecurityHealthAnalyticsCustomModulesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_sources(
        self,
        request: Optional[
            Union[securitycenter_service.ListSourcesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSourcesAsyncPager:
        r"""Lists all sources belonging to an organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_sources():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListSourcesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_sources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListSourcesRequest, dict]]):
                The request object. Request message for listing sources.
            parent (:class:`str`):
                Required. Resource name of the parent of sources to
                list. Its format should be
                ``organizations/[organization_id]``,
                ``folders/[folder_id]``, or ``projects/[project_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListSourcesAsyncPager:
                Response message for listing sources.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.ListSourcesRequest):
            request = securitycenter_service.ListSourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_sources
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListSourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def run_asset_discovery(
        self,
        request: Optional[
            Union[securitycenter_service.RunAssetDiscoveryRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Runs asset discovery. The discovery is tracked with a
        long-running operation.

        This API can only be called with limited frequency for an
        organization. If it is called too frequently the caller will
        receive a TOO_MANY_REQUESTS error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_run_asset_discovery():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.RunAssetDiscoveryRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = await client.run_asset_discovery(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.RunAssetDiscoveryRequest, dict]]):
                The request object. Request message for running asset
                discovery for an organization.
            parent (:class:`str`):
                Required. Name of the organization to run asset
                discovery for. Its format is
                ``organizations/[organization_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.securitycenter_v1.types.RunAssetDiscoveryResponse`
                Response of asset discovery run

        """
        warnings.warn(
            "SecurityCenterAsyncClient.run_asset_discovery is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.RunAssetDiscoveryRequest):
            request = securitycenter_service.RunAssetDiscoveryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_asset_discovery
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            run_asset_discovery_response.RunAssetDiscoveryResponse,
            metadata_type=empty_pb2.Empty,
        )

        # Done; return the response.
        return response

    async def set_finding_state(
        self,
        request: Optional[
            Union[securitycenter_service.SetFindingStateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        state: Optional[finding.Finding.State] = None,
        start_time: Optional[timestamp_pb2.Timestamp] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> finding.Finding:
        r"""Updates the state of a finding.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_set_finding_state():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.SetFindingStateRequest(
                    name="name_value",
                    state="INACTIVE",
                )

                # Make the request
                response = await client.set_finding_state(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.SetFindingStateRequest, dict]]):
                The request object. Request message for updating a
                finding's state.
            name (:class:`str`):
                Required. The `relative resource
                name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
                of the finding. Example:
                ``organizations/{organization_id}/sources/{source_id}/findings/{finding_id}``,
                ``folders/{folder_id}/sources/{source_id}/findings/{finding_id}``,
                ``projects/{project_id}/sources/{source_id}/findings/{finding_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            state (:class:`google.cloud.securitycenter_v1.types.Finding.State`):
                Required. The desired State of the
                finding.

                This corresponds to the ``state`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            start_time (:class:`google.protobuf.timestamp_pb2.Timestamp`):
                Required. The time at which the
                updated state takes effect.

                This corresponds to the ``start_time`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Finding:
                Security Command Center finding.

                A finding is a record of assessment data
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, state, start_time]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.SetFindingStateRequest):
            request = securitycenter_service.SetFindingStateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if state is not None:
            request.state = state
        if start_time is not None:
            request.start_time = start_time

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.set_finding_state
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_mute(
        self,
        request: Optional[Union[securitycenter_service.SetMuteRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        mute: Optional[finding.Finding.Mute] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> finding.Finding:
        r"""Updates the mute state of a finding.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_set_mute():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.SetMuteRequest(
                    name="name_value",
                    mute="UNDEFINED",
                )

                # Make the request
                response = await client.set_mute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.SetMuteRequest, dict]]):
                The request object. Request message for updating a
                finding's mute status.
            name (:class:`str`):
                Required. The `relative resource
                name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
                of the finding. Example:
                ``organizations/{organization_id}/sources/{source_id}/findings/{finding_id}``,
                ``folders/{folder_id}/sources/{source_id}/findings/{finding_id}``,
                ``projects/{project_id}/sources/{source_id}/findings/{finding_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            mute (:class:`google.cloud.securitycenter_v1.types.Finding.Mute`):
                Required. The desired state of the
                Mute.

                This corresponds to the ``mute`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Finding:
                Security Command Center finding.

                A finding is a record of assessment data
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, mute]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.SetMuteRequest):
            request = securitycenter_service.SetMuteRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if mute is not None:
            request.mute = mute

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.set_mute]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.SetIamPolicyRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the access control policy on the specified
        Source.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            async def sample_set_iam_policy():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.SetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.set_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]]):
                The request object. Request message for ``SetIamPolicy`` method.
            resource (:class:`str`):
                REQUIRED: The resource for which the
                policy is being specified. See the
                operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time <             timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

                   **YAML example:**

                   :literal:``     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\ \`

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - The request isn't a proto-plus wrapped type,
        #   so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.SetIamPolicyRequest(**request)
        elif not request:
            request = iam_policy_pb2.SetIamPolicyRequest(resource=resource)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.set_iam_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def test_iam_permissions(
        self,
        request: Optional[Union[iam_policy_pb2.TestIamPermissionsRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        permissions: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Returns the permissions that a caller has on the
        specified source.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            async def sample_test_iam_permissions():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.TestIamPermissionsRequest(
                    resource="resource_value",
                    permissions=['permissions_value1', 'permissions_value2'],
                )

                # Make the request
                response = await client.test_iam_permissions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]]):
                The request object. Request message for ``TestIamPermissions`` method.
            resource (:class:`str`):
                REQUIRED: The resource for which the
                policy detail is being requested. See
                the operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            permissions (:class:`MutableSequence[str]`):
                The set of permissions to check for the ``resource``.
                Permissions with wildcards (such as '*' or 'storage.*')
                are not allowed. For more information see `IAM
                Overview <https://cloud.google.com/iam/docs/overview#permissions>`__.

                This corresponds to the ``permissions`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for TestIamPermissions method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource, permissions]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - The request isn't a proto-plus wrapped type,
        #   so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.TestIamPermissionsRequest(**request)
        elif not request:
            request = iam_policy_pb2.TestIamPermissionsRequest(
                resource=resource, permissions=permissions
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.test_iam_permissions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def simulate_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        custom_config: Optional[
            security_health_analytics_custom_config.CustomConfig
        ] = None,
        resource: Optional[
            securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleResponse:
        r"""Simulates a given SecurityHealthAnalyticsCustomModule
        and Resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_simulate_security_health_analytics_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                resource = securitycenter_v1.SimulatedResource()
                resource.resource_type = "resource_type_value"

                request = securitycenter_v1.SimulateSecurityHealthAnalyticsCustomModuleRequest(
                    parent="parent_value",
                    resource=resource,
                )

                # Make the request
                response = await client.simulate_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message to simulate a
                CustomConfig against a given test
                resource. Maximum size of the request is
                4 MB by default.
            parent (:class:`str`):
                Required. The relative resource name of the
                organization, project, or folder. For more information
                about relative resource names, see `Relative Resource
                Name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
                Example: ``organizations/{organization_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            custom_config (:class:`google.cloud.securitycenter_v1.types.CustomConfig`):
                Required. The custom configuration
                that you need to test.

                This corresponds to the ``custom_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            resource (:class:`google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource`):
                Required. Resource data to simulate
                custom module against.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse:
                Response message for simulating a SecurityHealthAnalyticsCustomModule
                   against a given resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, custom_config, resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = securitycenter_service.SimulateSecurityHealthAnalyticsCustomModuleRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if custom_config is not None:
            request.custom_config = custom_config
        if resource is not None:
            request.resource = resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.simulate_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_external_system(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateExternalSystemRequest, dict]
        ] = None,
        *,
        external_system: Optional[gcs_external_system.ExternalSystem] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_external_system.ExternalSystem:
        r"""Updates external system. This is for a given finding.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_external_system():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateExternalSystemRequest(
                )

                # Make the request
                response = await client.update_external_system(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateExternalSystemRequest, dict]]):
                The request object. Request message for updating a
                ExternalSystem resource.
            external_system (:class:`google.cloud.securitycenter_v1.types.ExternalSystem`):
                Required. The external system
                resource to update.

                This corresponds to the ``external_system`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The FieldMask to use when updating
                the external system resource.
                If empty all mutable fields will be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.ExternalSystem:
                Representation of third party
                SIEM/SOAR fields within SCC.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [external_system, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.UpdateExternalSystemRequest):
            request = securitycenter_service.UpdateExternalSystemRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if external_system is not None:
            request.external_system = external_system
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_external_system
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("external_system.name", request.external_system.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_finding(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateFindingRequest, dict]
        ] = None,
        *,
        finding: Optional[gcs_finding.Finding] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_finding.Finding:
        r"""Creates or updates a finding. The corresponding
        source must exist for a finding creation to succeed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_finding():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateFindingRequest(
                )

                # Make the request
                response = await client.update_finding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateFindingRequest, dict]]):
                The request object. Request message for updating or
                creating a finding.
            finding (:class:`google.cloud.securitycenter_v1.types.Finding`):
                Required. The finding resource to update or create if it
                does not already exist. parent, security_marks, and
                update_time will be ignored.

                In the case of creation, the finding id portion of the
                name must be alphanumeric and less than or equal to 32
                characters and greater than 0 characters in length.

                This corresponds to the ``finding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Finding:
                Security Command Center finding.

                A finding is a record of assessment data
                like security, risk, health, or privacy,
                that is ingested into Security Command
                Center for presentation, notification,
                analysis, policy testing, and
                enforcement. For example, a cross-site
                scripting (XSS) vulnerability in an App
                Engine application is a finding.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [finding]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.UpdateFindingRequest):
            request = securitycenter_service.UpdateFindingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if finding is not None:
            request.finding = finding

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_finding
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("finding.name", request.finding.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_mute_config(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateMuteConfigRequest, dict]
        ] = None,
        *,
        mute_config: Optional[gcs_mute_config.MuteConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_mute_config.MuteConfig:
        r"""Updates a mute config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_mute_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                mute_config = securitycenter_v1.MuteConfig()
                mute_config.filter = "filter_value"

                request = securitycenter_v1.UpdateMuteConfigRequest(
                    mute_config=mute_config,
                )

                # Make the request
                response = await client.update_mute_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateMuteConfigRequest, dict]]):
                The request object. Request message for updating a mute
                config.
            mute_config (:class:`google.cloud.securitycenter_v1.types.MuteConfig`):
                Required. The mute config being
                updated.

                This corresponds to the ``mute_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                If empty all mutable fields will be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.MuteConfig:
                A mute config is a Cloud SCC resource
                that contains the configuration to mute
                create/update events of findings.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [mute_config, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.UpdateMuteConfigRequest):
            request = securitycenter_service.UpdateMuteConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if mute_config is not None:
            request.mute_config = mute_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_mute_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("mute_config.name", request.mute_config.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_notification_config(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateNotificationConfigRequest, dict]
        ] = None,
        *,
        notification_config: Optional[
            gcs_notification_config.NotificationConfig
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_notification_config.NotificationConfig:
        r"""Updates a notification config. The following update fields are
        allowed: description, pubsub_topic, streaming_config.filter

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_notification_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateNotificationConfigRequest(
                )

                # Make the request
                response = await client.update_notification_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateNotificationConfigRequest, dict]]):
                The request object. Request message for updating a
                notification config.
            notification_config (:class:`google.cloud.securitycenter_v1.types.NotificationConfig`):
                Required. The notification config to
                update.

                This corresponds to the ``notification_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The FieldMask to use when updating
                the notification config.
                If empty all mutable fields will be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.NotificationConfig:
                Cloud Security Command Center (Cloud
                SCC) notification configs.
                A notification config is a Cloud SCC
                resource that contains the configuration
                to send notifications for create/update
                events of findings, assets and etc.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [notification_config, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.UpdateNotificationConfigRequest
        ):
            request = securitycenter_service.UpdateNotificationConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if notification_config is not None:
            request.notification_config = notification_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_notification_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("notification_config.name", request.notification_config.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_organization_settings(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateOrganizationSettingsRequest, dict]
        ] = None,
        *,
        organization_settings: Optional[
            gcs_organization_settings.OrganizationSettings
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_organization_settings.OrganizationSettings:
        r"""Updates an organization's settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_organization_settings():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateOrganizationSettingsRequest(
                )

                # Make the request
                response = await client.update_organization_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateOrganizationSettingsRequest, dict]]):
                The request object. Request message for updating an
                organization's settings.
            organization_settings (:class:`google.cloud.securitycenter_v1.types.OrganizationSettings`):
                Required. The organization settings
                resource to update.

                This corresponds to the ``organization_settings`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.OrganizationSettings:
                User specified settings that are
                attached to the Security Command Center
                organization.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [organization_settings]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.UpdateOrganizationSettingsRequest
        ):
            request = securitycenter_service.UpdateOrganizationSettingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if organization_settings is not None:
            request.organization_settings = organization_settings

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_organization_settings
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("organization_settings.name", request.organization_settings.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        security_health_analytics_custom_module: Optional[
            gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> (
        gcs_security_health_analytics_custom_module.SecurityHealthAnalyticsCustomModule
    ):
        r"""Updates the SecurityHealthAnalyticsCustomModule under
        the given name based on the given update mask. Updating
        the enablement state is supported on both resident and
        inherited modules (though resident modules cannot have
        an enablement state of "inherited"). Updating the
        display name and custom config of a module is supported
        on resident modules only.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_security_health_analytics_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateSecurityHealthAnalyticsCustomModuleRequest(
                )

                # Make the request
                response = await client.update_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for updating Security
                Health Analytics custom modules.
            security_health_analytics_custom_module (:class:`google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule`):
                Required. The SecurityHealthAnalytics
                custom module to update.

                This corresponds to the ``security_health_analytics_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated. The only fields that
                can be updated are ``enablement_state`` and
                ``custom_config``. If empty or set to the wildcard value
                ``*``, both ``enablement_state`` and ``custom_config``
                are updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the child folders and
                projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_health_analytics_custom_module, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = (
                securitycenter_service.UpdateSecurityHealthAnalyticsCustomModuleRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if security_health_analytics_custom_module is not None:
            request.security_health_analytics_custom_module = (
                security_health_analytics_custom_module
            )
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_security_health_analytics_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "security_health_analytics_custom_module.name",
                        request.security_health_analytics_custom_module.name,
                    ),
                )
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_source(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateSourceRequest, dict]
        ] = None,
        *,
        source: Optional[gcs_source.Source] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_source.Source:
        r"""Updates a source.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_source():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateSourceRequest(
                )

                # Make the request
                response = await client.update_source(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateSourceRequest, dict]]):
                The request object. Request message for updating a
                source.
            source (:class:`google.cloud.securitycenter_v1.types.Source`):
                Required. The source resource to
                update.

                This corresponds to the ``source`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.Source:
                Security Command Center finding
                source. A finding source is an entity or
                a mechanism that can produce a finding.
                A source is like a container of findings
                that come from the same scanner, logger,
                monitor, and other tools.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [source]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.UpdateSourceRequest):
            request = securitycenter_service.UpdateSourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if source is not None:
            request.source = source

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_source
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("source.name", request.source.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_security_marks(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateSecurityMarksRequest, dict]
        ] = None,
        *,
        security_marks: Optional[gcs_security_marks.SecurityMarks] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_security_marks.SecurityMarks:
        r"""Updates security marks.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_security_marks():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateSecurityMarksRequest(
                )

                # Make the request
                response = await client.update_security_marks(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateSecurityMarksRequest, dict]]):
                The request object. Request message for updating a
                SecurityMarks resource.
            security_marks (:class:`google.cloud.securitycenter_v1.types.SecurityMarks`):
                Required. The security marks resource
                to update.

                This corresponds to the ``security_marks`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.SecurityMarks:
                User specified security marks that
                are attached to the parent Security
                Command Center resource. Security marks
                are scoped within a Security Command
                Center organization -- they can be
                modified and viewed by all users who
                have proper permissions on the
                organization.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_marks]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.UpdateSecurityMarksRequest):
            request = securitycenter_service.UpdateSecurityMarksRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if security_marks is not None:
            request.security_marks = security_marks

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_security_marks
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_marks.name", request.security_marks.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_big_query_export(
        self,
        request: Optional[
            Union[securitycenter_service.CreateBigQueryExportRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        big_query_export: Optional[bigquery_export.BigQueryExport] = None,
        big_query_export_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> bigquery_export.BigQueryExport:
        r"""Creates a BigQuery export.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_create_big_query_export():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.CreateBigQueryExportRequest(
                    parent="parent_value",
                    big_query_export_id="big_query_export_id_value",
                )

                # Make the request
                response = await client.create_big_query_export(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.CreateBigQueryExportRequest, dict]]):
                The request object. Request message for creating a
                BigQuery export.
            parent (:class:`str`):
                Required. The name of the parent resource of the new
                BigQuery export. Its format is
                ``organizations/[organization_id]``,
                ``folders/[folder_id]``, or ``projects/[project_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            big_query_export (:class:`google.cloud.securitycenter_v1.types.BigQueryExport`):
                Required. The BigQuery export being
                created.

                This corresponds to the ``big_query_export`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            big_query_export_id (:class:`str`):
                Required. Unique identifier provided
                by the client within the parent scope.
                It must consist of only lowercase
                letters, numbers, and hyphens, must
                start with a letter, must end with
                either a letter or a number, and must be
                63 characters or less.

                This corresponds to the ``big_query_export_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.BigQueryExport:
                Configures how to deliver Findings to
                BigQuery Instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, big_query_export, big_query_export_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.CreateBigQueryExportRequest):
            request = securitycenter_service.CreateBigQueryExportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if big_query_export is not None:
            request.big_query_export = big_query_export
        if big_query_export_id is not None:
            request.big_query_export_id = big_query_export_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_big_query_export
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_big_query_export(
        self,
        request: Optional[
            Union[securitycenter_service.DeleteBigQueryExportRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing BigQuery export.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_delete_big_query_export():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.DeleteBigQueryExportRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_big_query_export(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.DeleteBigQueryExportRequest, dict]]):
                The request object. Request message for deleting a
                BigQuery export.
            name (:class:`str`):
                Required. The name of the BigQuery export to delete. Its
                format is
                ``organizations/{organization}/bigQueryExports/{export_id}``,
                ``folders/{folder}/bigQueryExports/{export_id}``, or
                ``projects/{project}/bigQueryExports/{export_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.DeleteBigQueryExportRequest):
            request = securitycenter_service.DeleteBigQueryExportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_big_query_export
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def update_big_query_export(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateBigQueryExportRequest, dict]
        ] = None,
        *,
        big_query_export: Optional[bigquery_export.BigQueryExport] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> bigquery_export.BigQueryExport:
        r"""Updates a BigQuery export.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_big_query_export():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateBigQueryExportRequest(
                )

                # Make the request
                response = await client.update_big_query_export(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateBigQueryExportRequest, dict]]):
                The request object. Request message for updating a
                BigQuery export.
            big_query_export (:class:`google.cloud.securitycenter_v1.types.BigQueryExport`):
                Required. The BigQuery export being
                updated.

                This corresponds to the ``big_query_export`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                If empty all mutable fields will be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.BigQueryExport:
                Configures how to deliver Findings to
                BigQuery Instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [big_query_export, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.UpdateBigQueryExportRequest):
            request = securitycenter_service.UpdateBigQueryExportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if big_query_export is not None:
            request.big_query_export = big_query_export
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_big_query_export
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("big_query_export.name", request.big_query_export.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_big_query_exports(
        self,
        request: Optional[
            Union[securitycenter_service.ListBigQueryExportsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBigQueryExportsAsyncPager:
        r"""Lists BigQuery exports. Note that when requesting
        BigQuery exports at a given level all exports under that
        level are also returned e.g. if requesting BigQuery
        exports under a folder, then all BigQuery exports
        immediately under the folder plus the ones created under
        the projects within the folder are returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_big_query_exports():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListBigQueryExportsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_big_query_exports(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListBigQueryExportsRequest, dict]]):
                The request object. Request message for listing BigQuery
                exports at a given scope e.g.
                organization, folder or project.
            parent (:class:`str`):
                Required. The parent, which owns the collection of
                BigQuery exports. Its format is
                ``organizations/[organization_id]``,
                ``folders/[folder_id]``, ``projects/[project_id]``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListBigQueryExportsAsyncPager:
                Response message for listing BigQuery
                exports.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.ListBigQueryExportsRequest):
            request = securitycenter_service.ListBigQueryExportsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_big_query_exports
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListBigQueryExportsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.CreateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        event_threat_detection_custom_module: Optional[
            gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
        r"""Creates a resident Event Threat Detection custom
        module at the scope of the given Resource Manager
        parent, and also creates inherited custom modules for
        all descendants of the given parent. These modules are
        enabled by default.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_create_event_threat_detection_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.CreateEventThreatDetectionCustomModuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.CreateEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request to create an Event Threat
                Detection custom module.
            parent (:class:`str`):
                Required. The new custom module's parent.

                Its format is:

                - ``organizations/{organization}/eventThreatDetectionSettings``.
                - ``folders/{folder}/eventThreatDetectionSettings``.
                - ``projects/{project}/eventThreatDetectionSettings``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            event_threat_detection_custom_module (:class:`google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule`):
                Required. The module to create. The
                event_threat_detection_custom_module.name will be
                ignored and server generated.

                This corresponds to the ``event_threat_detection_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule:
                Represents an instance of an Event
                Threat Detection custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by child folders and projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, event_threat_detection_custom_module]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.CreateEventThreatDetectionCustomModuleRequest,
        ):
            request = (
                securitycenter_service.CreateEventThreatDetectionCustomModuleRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if event_threat_detection_custom_module is not None:
            request.event_threat_detection_custom_module = (
                event_threat_detection_custom_module
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified Event Threat Detection custom
        module and all of its descendants in the Resource
        Manager hierarchy. This method is only supported for
        resident custom modules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_delete_event_threat_detection_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.DeleteEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_event_threat_detection_custom_module(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.DeleteEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request to delete an Event Threat
                Detection custom module.
            name (:class:`str`):
                Required. Name of the custom module to delete.

                Its format is:

                - ``organizations/{organization}/eventThreatDetectionSettings/customModules/{module}``.
                - ``folders/{folder}/eventThreatDetectionSettings/customModules/{module}``.
                - ``projects/{project}/eventThreatDetectionSettings/customModules/{module}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest,
        ):
            request = (
                securitycenter_service.DeleteEventThreatDetectionCustomModuleRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.GetEventThreatDetectionCustomModuleRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> event_threat_detection_custom_module.EventThreatDetectionCustomModule:
        r"""Gets an Event Threat Detection custom module.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_event_threat_detection_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request to get an Event Threat
                Detection custom module.
            name (:class:`str`):
                Required. Name of the custom module to get.

                Its format is:

                - ``organizations/{organization}/eventThreatDetectionSettings/customModules/{module}``.
                - ``folders/{folder}/eventThreatDetectionSettings/customModules/{module}``.
                - ``projects/{project}/eventThreatDetectionSettings/customModules/{module}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule:
                Represents an instance of an Event
                Threat Detection custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by child folders and projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.GetEventThreatDetectionCustomModuleRequest
        ):
            request = securitycenter_service.GetEventThreatDetectionCustomModuleRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_descendant_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDescendantEventThreatDetectionCustomModulesAsyncPager:
        r"""Lists all resident Event Threat Detection custom
        modules under the given Resource Manager parent and its
        descendants.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_descendant_event_threat_detection_custom_modules():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListDescendantEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_descendant_event_threat_detection_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest, dict]]):
                The request object. Request to list current and
                descendant resident Event Threat
                Detection custom modules.
            parent (:class:`str`):
                Required. Name of the parent to list custom modules
                under.

                Its format is:

                - ``organizations/{organization}/eventThreatDetectionSettings``.
                - ``folders/{folder}/eventThreatDetectionSettings``.
                - ``projects/{project}/eventThreatDetectionSettings``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListDescendantEventThreatDetectionCustomModulesAsyncPager:
                Response for listing current and
                descendant resident Event Threat
                Detection custom modules.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest,
        ):
            request = securitycenter_service.ListDescendantEventThreatDetectionCustomModulesRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_descendant_event_threat_detection_custom_modules
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListDescendantEventThreatDetectionCustomModulesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                securitycenter_service.ListEventThreatDetectionCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEventThreatDetectionCustomModulesAsyncPager:
        r"""Lists all Event Threat Detection custom modules for
        the given Resource Manager parent. This includes
        resident modules defined at the scope of the parent
        along with modules inherited from ancestors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_event_threat_detection_custom_modules():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_event_threat_detection_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListEventThreatDetectionCustomModulesRequest, dict]]):
                The request object. Request to list Event Threat
                Detection custom modules.
            parent (:class:`str`):
                Required. Name of the parent to list custom modules
                under.

                Its format is:

                - ``organizations/{organization}/eventThreatDetectionSettings``.
                - ``folders/{folder}/eventThreatDetectionSettings``.
                - ``projects/{project}/eventThreatDetectionSettings``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListEventThreatDetectionCustomModulesAsyncPager:
                Response for listing Event Threat
                Detection custom modules.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.ListEventThreatDetectionCustomModulesRequest
        ):
            request = (
                securitycenter_service.ListEventThreatDetectionCustomModulesRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_event_threat_detection_custom_modules
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEventThreatDetectionCustomModulesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        event_threat_detection_custom_module: Optional[
            gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_event_threat_detection_custom_module.EventThreatDetectionCustomModule:
        r"""Updates the Event Threat Detection custom module with
        the given name based on the given update mask. Updating
        the enablement state is supported for both resident and
        inherited modules (though resident modules cannot have
        an enablement state of "inherited"). Updating the
        display name or configuration of a module is supported
        for resident modules only. The type of a module cannot
        be changed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_event_threat_detection_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.UpdateEventThreatDetectionCustomModuleRequest(
                )

                # Make the request
                response = await client.update_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request to update an Event Threat
                Detection custom module.
            event_threat_detection_custom_module (:class:`google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule`):
                Required. The module being updated.
                This corresponds to the ``event_threat_detection_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                If empty all mutable fields will be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule:
                Represents an instance of an Event
                Threat Detection custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by child folders and projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [event_threat_detection_custom_module, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest,
        ):
            request = (
                securitycenter_service.UpdateEventThreatDetectionCustomModuleRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if event_threat_detection_custom_module is not None:
            request.event_threat_detection_custom_module = (
                event_threat_detection_custom_module
            )
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "event_threat_detection_custom_module.name",
                        request.event_threat_detection_custom_module.name,
                    ),
                )
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def validate_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> securitycenter_service.ValidateEventThreatDetectionCustomModuleResponse:
        r"""Validates the given Event Threat Detection custom
        module.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_validate_event_threat_detection_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ValidateEventThreatDetectionCustomModuleRequest(
                    parent="parent_value",
                    raw_text="raw_text_value",
                    type_="type__value",
                )

                # Make the request
                response = await client.validate_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ValidateEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request to validate an Event Threat
                Detection custom module.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.ValidateEventThreatDetectionCustomModuleResponse:
                Response to validating an Event
                Threat Detection custom module.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest,
        ):
            request = (
                securitycenter_service.ValidateEventThreatDetectionCustomModuleRequest(
                    request
                )
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.validate_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_effective_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> effective_event_threat_detection_custom_module.EffectiveEventThreatDetectionCustomModule:
        r"""Gets an effective Event Threat Detection custom
        module at the given level.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_effective_event_threat_detection_custom_module():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetEffectiveEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_effective_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request to get an
                EffectiveEventThreatDetectionCustomModule.
            name (:class:`str`):
                Required. The resource name of the effective Event
                Threat Detection custom module.

                Its format is:

                - ``organizations/{organization}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
                - ``folders/{folder}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
                - ``projects/{project}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.EffectiveEventThreatDetectionCustomModule:
                An EffectiveEventThreatDetectionCustomModule is the representation of
                   an Event Threat Detection custom module at a
                   specified level of the resource hierarchy:
                   organization, folder, or project. If a custom module
                   is inherited from a parent organization or folder,
                   the value of the enablement_state property in
                   EffectiveEventThreatDetectionCustomModule is set to
                   the value that is effective in the parent, instead of
                   INHERITED. For example, if the module is enabled in a
                   parent organization or folder, the effective
                   enablement_state for the module in all child folders
                   or projects is also enabled.
                   EffectiveEventThreatDetectionCustomModule is
                   read-only.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest,
        ):
            request = securitycenter_service.GetEffectiveEventThreatDetectionCustomModuleRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_effective_event_threat_detection_custom_module
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_effective_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEffectiveEventThreatDetectionCustomModulesAsyncPager:
        r"""Lists all effective Event Threat Detection custom
        modules for the given parent. This includes resident
        modules defined at the scope of the parent along with
        modules inherited from its ancestors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_effective_event_threat_detection_custom_modules():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListEffectiveEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_effective_event_threat_detection_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest, dict]]):
                The request object. Request to list effective Event
                Threat Detection custom modules.
            parent (:class:`str`):
                Required. Name of the parent to list custom modules for.

                Its format is:

                - ``organizations/{organization}/eventThreatDetectionSettings``.
                - ``folders/{folder}/eventThreatDetectionSettings``.
                - ``projects/{project}/eventThreatDetectionSettings``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListEffectiveEventThreatDetectionCustomModulesAsyncPager:
                Response for listing
                EffectiveEventThreatDetectionCustomModules.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest,
        ):
            request = securitycenter_service.ListEffectiveEventThreatDetectionCustomModulesRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_effective_event_threat_detection_custom_modules
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEffectiveEventThreatDetectionCustomModulesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def batch_create_resource_value_configs(
        self,
        request: Optional[
            Union[securitycenter_service.BatchCreateResourceValueConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[
            MutableSequence[securitycenter_service.CreateResourceValueConfigRequest]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> securitycenter_service.BatchCreateResourceValueConfigsResponse:
        r"""Creates a ResourceValueConfig for an organization.
        Maps user's tags to difference resource values for use
        by the attack path simulation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_batch_create_resource_value_configs():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                requests = securitycenter_v1.CreateResourceValueConfigRequest()
                requests.parent = "parent_value"
                requests.resource_value_config.resource_value = "NONE"
                requests.resource_value_config.tag_values = ['tag_values_value1', 'tag_values_value2']

                request = securitycenter_v1.BatchCreateResourceValueConfigsRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = await client.batch_create_resource_value_configs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.BatchCreateResourceValueConfigsRequest, dict]]):
                The request object. Request message to create multiple
                resource value configs
            parent (:class:`str`):
                Required. Resource name of the new
                ResourceValueConfig's parent. The parent
                field in the
                CreateResourceValueConfigRequest
                messages must either be empty or match
                this field.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (:class:`MutableSequence[google.cloud.securitycenter_v1.types.CreateResourceValueConfigRequest]`):
                Required. The resource value configs
                to be created.

                This corresponds to the ``requests`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.BatchCreateResourceValueConfigsResponse:
                Response message for
                BatchCreateResourceValueConfigs

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, requests]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.BatchCreateResourceValueConfigsRequest
        ):
            request = securitycenter_service.BatchCreateResourceValueConfigsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if requests:
            request.requests.extend(requests)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_create_resource_value_configs
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_resource_value_config(
        self,
        request: Optional[
            Union[securitycenter_service.DeleteResourceValueConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a ResourceValueConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_delete_resource_value_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.DeleteResourceValueConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_resource_value_config(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.DeleteResourceValueConfigRequest, dict]]):
                The request object. Request message to delete resource
                value config
            name (:class:`str`):
                Required. Name of the
                ResourceValueConfig to delete

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.DeleteResourceValueConfigRequest
        ):
            request = securitycenter_service.DeleteResourceValueConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_resource_value_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_resource_value_config(
        self,
        request: Optional[
            Union[securitycenter_service.GetResourceValueConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resource_value_config.ResourceValueConfig:
        r"""Gets a ResourceValueConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_get_resource_value_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.GetResourceValueConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_resource_value_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.GetResourceValueConfigRequest, dict]]):
                The request object. Request message to get resource value
                config
            name (:class:`str`):
                Required. Name of the resource value config to retrieve.
                Its format is
                ``organizations/{organization}/resourceValueConfigs/{config_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.ResourceValueConfig:
                A resource value configuration (RVC)
                is a mapping configuration of user's
                resources to resource values. Used in
                Attack path simulations.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.GetResourceValueConfigRequest
        ):
            request = securitycenter_service.GetResourceValueConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_resource_value_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_resource_value_configs(
        self,
        request: Optional[
            Union[securitycenter_service.ListResourceValueConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListResourceValueConfigsAsyncPager:
        r"""Lists all ResourceValueConfigs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_resource_value_configs():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListResourceValueConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_resource_value_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListResourceValueConfigsRequest, dict]]):
                The request object. Request message to list resource
                value configs of a parent
            parent (:class:`str`):
                Required. The parent, which owns the collection of
                resource value configs. Its format is
                ``organizations/[organization_id]``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListResourceValueConfigsAsyncPager:
                Response message to list resource
                value configs
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.ListResourceValueConfigsRequest
        ):
            request = securitycenter_service.ListResourceValueConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_resource_value_configs
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListResourceValueConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_resource_value_config(
        self,
        request: Optional[
            Union[securitycenter_service.UpdateResourceValueConfigRequest, dict]
        ] = None,
        *,
        resource_value_config: Optional[
            gcs_resource_value_config.ResourceValueConfig
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_resource_value_config.ResourceValueConfig:
        r"""Updates an existing ResourceValueConfigs with new
        rules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_update_resource_value_config():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                resource_value_config = securitycenter_v1.ResourceValueConfig()
                resource_value_config.resource_value = "NONE"
                resource_value_config.tag_values = ['tag_values_value1', 'tag_values_value2']

                request = securitycenter_v1.UpdateResourceValueConfigRequest(
                    resource_value_config=resource_value_config,
                )

                # Make the request
                response = await client.update_resource_value_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.UpdateResourceValueConfigRequest, dict]]):
                The request object. Request message to update resource
                value config
            resource_value_config (:class:`google.cloud.securitycenter_v1.types.ResourceValueConfig`):
                Required. The resource value config
                being updated.

                This corresponds to the ``resource_value_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to be updated.
                If empty all mutable fields will be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.types.ResourceValueConfig:
                A resource value configuration (RVC)
                is a mapping configuration of user's
                resources to resource values. Used in
                Attack path simulations.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource_value_config, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, securitycenter_service.UpdateResourceValueConfigRequest
        ):
            request = securitycenter_service.UpdateResourceValueConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if resource_value_config is not None:
            request.resource_value_config = resource_value_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_resource_value_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource_value_config.name", request.resource_value_config.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_valued_resources(
        self,
        request: Optional[
            Union[securitycenter_service.ListValuedResourcesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListValuedResourcesAsyncPager:
        r"""Lists the valued resources for a set of simulation
        results and filter.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_valued_resources():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListValuedResourcesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_valued_resources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListValuedResourcesRequest, dict]]):
                The request object. Request message for listing the
                valued resources for a given simulation.
            parent (:class:`str`):
                Required. Name of parent to list valued resources.

                Valid formats: ``organizations/{organization}``,
                ``organizations/{organization}/simulations/{simulation}``
                ``organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListValuedResourcesAsyncPager:
                Response message for listing the
                valued resources for a given simulation.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.ListValuedResourcesRequest):
            request = securitycenter_service.ListValuedResourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_valued_resources
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListValuedResourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_attack_paths(
        self,
        request: Optional[
            Union[securitycenter_service.ListAttackPathsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAttackPathsAsyncPager:
        r"""Lists the attack paths for a set of simulation
        results or valued resources and filter.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycenter_v1

            async def sample_list_attack_paths():
                # Create a client
                client = securitycenter_v1.SecurityCenterAsyncClient()

                # Initialize request argument(s)
                request = securitycenter_v1.ListAttackPathsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_attack_paths(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycenter_v1.types.ListAttackPathsRequest, dict]]):
                The request object. Request message for listing the
                attack paths for a given simulation or
                valued resource.
            parent (:class:`str`):
                Required. Name of parent to list attack paths.

                Valid formats: ``organizations/{organization}``,
                ``organizations/{organization}/simulations/{simulation}``
                ``organizations/{organization}/simulations/{simulation}/attackExposureResults/{attack_exposure_result_v2}``
                ``organizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycenter_v1.services.security_center.pagers.ListAttackPathsAsyncPager:
                Response message for listing the
                attack paths for a given simulation or
                valued resource.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, securitycenter_service.ListAttackPathsRequest):
            request = securitycenter_service.ListAttackPathsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_attack_paths
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListAttackPathsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: Optional[Union[operations_pb2.ListOperationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.ListOperationsRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.ListOperationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_operations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[Union[operations_pb2.GetOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.GetOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.GetOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_operation(
        self,
        request: Optional[Union[operations_pb2.DeleteOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.DeleteOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.DeleteOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.delete_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def cancel_operation(
        self,
        request: Optional[Union[operations_pb2.CancelOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.CancelOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.CancelOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self) -> "SecurityCenterAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("SecurityCenterAsyncClient",)
