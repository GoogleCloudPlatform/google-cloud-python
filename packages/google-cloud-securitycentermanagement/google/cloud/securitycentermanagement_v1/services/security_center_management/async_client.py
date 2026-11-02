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

from google.cloud.securitycentermanagement_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore

from google.cloud.securitycentermanagement_v1.services.security_center_management import (
    pagers,
)
from google.cloud.securitycentermanagement_v1.types import security_center_management

from .client import SecurityCenterManagementClient
from .transports.base import DEFAULT_CLIENT_INFO, SecurityCenterManagementTransport
from .transports.grpc_asyncio import SecurityCenterManagementGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class SecurityCenterManagementAsyncClient:
    """Service describing handlers for resources"""

    _client: SecurityCenterManagementClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SecurityCenterManagementClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SecurityCenterManagementClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        SecurityCenterManagementClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = SecurityCenterManagementClient._DEFAULT_UNIVERSE

    effective_event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterManagementClient.effective_event_threat_detection_custom_module_path
    )
    parse_effective_event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterManagementClient.parse_effective_event_threat_detection_custom_module_path
    )
    effective_security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterManagementClient.effective_security_health_analytics_custom_module_path
    )
    parse_effective_security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterManagementClient.parse_effective_security_health_analytics_custom_module_path
    )
    event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterManagementClient.event_threat_detection_custom_module_path
    )
    parse_event_threat_detection_custom_module_path = staticmethod(
        SecurityCenterManagementClient.parse_event_threat_detection_custom_module_path
    )
    finding_path = staticmethod(SecurityCenterManagementClient.finding_path)
    parse_finding_path = staticmethod(SecurityCenterManagementClient.parse_finding_path)
    security_center_service_path = staticmethod(
        SecurityCenterManagementClient.security_center_service_path
    )
    parse_security_center_service_path = staticmethod(
        SecurityCenterManagementClient.parse_security_center_service_path
    )
    security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterManagementClient.security_health_analytics_custom_module_path
    )
    parse_security_health_analytics_custom_module_path = staticmethod(
        SecurityCenterManagementClient.parse_security_health_analytics_custom_module_path
    )
    common_billing_account_path = staticmethod(
        SecurityCenterManagementClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        SecurityCenterManagementClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(SecurityCenterManagementClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        SecurityCenterManagementClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        SecurityCenterManagementClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        SecurityCenterManagementClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        SecurityCenterManagementClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        SecurityCenterManagementClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        SecurityCenterManagementClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        SecurityCenterManagementClient.parse_common_location_path
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
            SecurityCenterManagementAsyncClient: The constructed client.
        """
        sa_info_func = (
            SecurityCenterManagementClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(SecurityCenterManagementAsyncClient, info, *args, **kwargs)

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
            SecurityCenterManagementAsyncClient: The constructed client.
        """
        sa_file_func = (
            SecurityCenterManagementClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            SecurityCenterManagementAsyncClient, filename, *args, **kwargs
        )

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
        return SecurityCenterManagementClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> SecurityCenterManagementTransport:
        """Returns the transport used by the client instance.

        Returns:
            SecurityCenterManagementTransport: The transport used by the client instance.
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

    get_transport_class = SecurityCenterManagementClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                SecurityCenterManagementTransport,
                Callable[..., SecurityCenterManagementTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the security center management async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SecurityCenterManagementTransport,Callable[..., SecurityCenterManagementTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SecurityCenterManagementTransport constructor.
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
        self._client = SecurityCenterManagementClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.securitycentermanagement_v1.SecurityCenterManagementAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
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
                    "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                    "credentialsType": None,
                },
            )

    async def list_effective_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
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
        [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule]
        resources for the given parent. This includes resident modules
        defined at the scope of the parent, and inherited modules,
        inherited from ancestor organizations, folders, and projects (no
        descendants).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_list_effective_security_health_analytics_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_effective_security_health_analytics_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules].
            parent (:class:`str`):
                Required. Name of parent to list effective custom
                modules, in one of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveSecurityHealthAnalyticsCustomModulesAsyncPager:
                Response message for
                   [SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveSecurityHealthAnalyticsCustomModules].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest(
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

    async def get_effective_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EffectiveSecurityHealthAnalyticsCustomModule:
        r"""Gets details of a single
        [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_get_effective_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_effective_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveSecurityHealthAnalyticsCustomModule].
            name (:class:`str`):
                Required. The full resource name of the custom module,
                specified in one of the following formats:

                - ``organizations/organization/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}``
                - ``folders/folder/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}``
                - ``projects/project/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}``

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
            google.cloud.securitycentermanagement_v1.types.EffectiveSecurityHealthAnalyticsCustomModule:
                The representation of a Security Health Analytics custom module at a
                   specified level of the resource hierarchy:
                   organization, folder, or project. If a custom module
                   is inherited from an ancestor organization or folder,
                   then the enablement state is set to the value that is
                   effective in the parent, not to INHERITED. For
                   example, if the module is enabled in an organization
                   or folder, then the effective enablement state for
                   the module is ENABLED in all descendant folders or
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
            security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest(
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

    async def list_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
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
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        resources for the given parent. This includes resident modules
        defined at the scope of the parent, and inherited modules,
        inherited from ancestor organizations, folders, and projects (no
        descendants).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_list_security_health_analytics_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_security_health_analytics_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ListSecurityHealthAnalyticsCustomModulesRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules].
            parent (:class:`str`):
                Required. Name of the parent organization, folder, or
                project in which to list custom modules, in one of the
                following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityHealthAnalyticsCustomModulesAsyncPager:
                Response message for
                   [SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityHealthAnalyticsCustomModules].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest(
                request
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

    async def list_descendant_security_health_analytics_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
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
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        resources under the given organization, folder, or project and
        all of its descendants.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_list_descendant_security_health_analytics_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_descendant_security_health_analytics_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ListDescendantSecurityHealthAnalyticsCustomModulesRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules].
            parent (:class:`str`):
                Required. Name of the parent organization, folder, or
                project in which to list custom modules, in one of the
                following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantSecurityHealthAnalyticsCustomModulesAsyncPager:
                Response message for
                   [SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantSecurityHealthAnalyticsCustomModules].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest,
        ):
            request = security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest(
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

    async def get_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        r"""Retrieves a
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_get_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.GetSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityHealthAnalyticsCustomModule].
            name (:class:`str`):
                Required. Name of the resource, in the format
                ``projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``.

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
            google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the descendant folders and
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
            security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest(
                request
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

    async def create_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        security_health_analytics_custom_module: Optional[
            security_center_management.SecurityHealthAnalyticsCustomModule
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        r"""Creates a resident
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        at the scope of the given organization, folder, or project, and
        also creates inherited ``SecurityHealthAnalyticsCustomModule``
        resources for all folders and projects that are descendants of
        the given parent. These modules are enabled by default.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_create_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.CreateSecurityHealthAnalyticsCustomModuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.CreateSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateSecurityHealthAnalyticsCustomModule].
            parent (:class:`str`):
                Required. Name of the parent organization, folder, or
                project of the module, in one of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_health_analytics_custom_module (:class:`google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule`):
                Required. The resource being created.
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
            google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the descendant folders and
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
            security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest(
                request
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

    async def update_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        security_health_analytics_custom_module: Optional[
            security_center_management.SecurityHealthAnalyticsCustomModule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityHealthAnalyticsCustomModule:
        r"""Updates the
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        under the given name based on the given update mask. Updating
        the enablement state is supported on both resident and inherited
        modules (though resident modules cannot have an enablement state
        of "inherited"). Updating the display name and custom
        configuration of a module is supported on resident modules only.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_update_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.UpdateSecurityHealthAnalyticsCustomModuleRequest(
                )

                # Make the request
                response = await client.update_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.UpdateSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityHealthAnalyticsCustomModule].
            security_health_analytics_custom_module (:class:`google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule`):
                Required. The resource being updated.
                This corresponds to the ``security_health_analytics_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The fields to update. The following values are
                valid:

                - ``custom_config``
                - ``enablement_state``

                If you omit this field or set it to the wildcard value
                ``*``, then all eligible fields are updated.

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
            google.cloud.securitycentermanagement_v1.types.SecurityHealthAnalyticsCustomModule:
                Represents an instance of a Security
                Health Analytics custom module,
                including its full module name, display
                name, enablement state, and last updated
                time. You can create a custom module at
                the organization, folder, or project
                level. Custom modules that you create at
                the organization or folder level are
                inherited by the descendant folders and
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
            security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest(
                request
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

    async def delete_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
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
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        and all of its descendants in the resource hierarchy. This
        method is only supported for resident custom modules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_delete_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.DeleteSecurityHealthAnalyticsCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_security_health_analytics_custom_module(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.DeleteSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteSecurityHealthAnalyticsCustomModule].
            name (:class:`str`):
                Required. The resource name of the SHA custom module, in
                one of the following formats:

                - ``organizations/{organization}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}``

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
            security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest(
                request
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

    async def simulate_security_health_analytics_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        custom_config: Optional[security_center_management.CustomConfig] = None,
        resource: Optional[
            security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse:
        r"""Simulates the result of using a
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        to check a resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_simulate_security_health_analytics_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                resource = securitycentermanagement_v1.SimulatedResource()
                resource.resource_type = "resource_type_value"

                request = securitycentermanagement_v1.SimulateSecurityHealthAnalyticsCustomModuleRequest(
                    parent="parent_value",
                    resource=resource,
                )

                # Make the request
                response = await client.simulate_security_health_analytics_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule].
                The maximum size of the request is 4 MiB.
            parent (:class:`str`):
                Required. The relative resource name of the
                organization, project, or folder. For more information
                about relative resource names, see `AIP-122: Resource
                names <https://google.aip.dev/122>`__. Example:
                ``organizations/{organization_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            custom_config (:class:`google.cloud.securitycentermanagement_v1.types.CustomConfig`):
                Required. The custom configuration
                that you need to test.

                This corresponds to the ``custom_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            resource (:class:`google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource`):
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
            google.cloud.securitycentermanagement_v1.types.SimulateSecurityHealthAnalyticsCustomModuleResponse:
                Response message for
                   [SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.SimulateSecurityHealthAnalyticsCustomModule].

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
            security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest,
        ):
            request = security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest(
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

    async def list_effective_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
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
            from google.cloud import securitycentermanagement_v1

            async def sample_list_effective_event_threat_detection_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListEffectiveEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_effective_event_threat_detection_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ListEffectiveEventThreatDetectionCustomModulesRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules].
            parent (:class:`str`):
                Required. Name of parent to list effective custom
                modules, in one of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEffectiveEventThreatDetectionCustomModulesAsyncPager:
                Response message for
                   [SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEffectiveEventThreatDetectionCustomModules].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest,
        ):
            request = security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest(
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

    async def get_effective_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EffectiveEventThreatDetectionCustomModule:
        r"""Gets the effective Event Threat Detection custom module at the
        given level.

        The difference between an
        [EffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule]
        and an
        [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule]
        is that the fields for an
        ``EffectiveEventThreatDetectionCustomModule`` are computed from
        ancestors if needed. For example, the enablement state for an
        ``EventThreatDetectionCustomModule`` can be ``ENABLED``,
        ``DISABLED``, or ``INHERITED``. In contrast, the enablement
        state for an ``EffectiveEventThreatDetectionCustomModule`` is
        always computed as ``ENABLED`` or ``DISABLED``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_get_effective_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetEffectiveEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_effective_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.GetEffectiveEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEffectiveEventThreatDetectionCustomModule].
            name (:class:`str`):
                Required. The resource name of the Event Threat
                Detection custom module, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}``

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
            google.cloud.securitycentermanagement_v1.types.EffectiveEventThreatDetectionCustomModule:
                The representation of an
                   [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule]
                   at a given level, taking hierarchy into account and
                   resolving various fields accordingly. For example, if
                   the module is enabled at the ancestor level, then
                   effective modules at all descendant levels will have
                   their enablement state set to ENABLED. Similarly, if
                   module.inherited is set, then the effective module's
                   configuration will reflect the ancestor's
                   configuration.

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
            security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest(
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

    async def list_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListEventThreatDetectionCustomModulesRequest,
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
        the given organization, folder, or project. This
        includes resident modules defined at the scope of the
        parent along with modules inherited from ancestors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_list_event_threat_detection_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_event_threat_detection_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ListEventThreatDetectionCustomModulesRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ListEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules].
            parent (:class:`str`):
                Required. Name of parent to list custom modules, in one
                of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListEventThreatDetectionCustomModulesAsyncPager:
                Response message for
                   [SecurityCenterManagement.ListEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListEventThreatDetectionCustomModules].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            security_center_management.ListEventThreatDetectionCustomModulesRequest,
        ):
            request = (
                security_center_management.ListEventThreatDetectionCustomModulesRequest(
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

    async def list_descendant_event_threat_detection_custom_modules(
        self,
        request: Optional[
            Union[
                security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
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
        modules for the given organization, folder, or project
        and its descendants.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_list_descendant_event_threat_detection_custom_modules():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListDescendantEventThreatDetectionCustomModulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_descendant_event_threat_detection_custom_modules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ListDescendantEventThreatDetectionCustomModulesRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules].
            parent (:class:`str`):
                Required. Name of parent to list custom modules, in one
                of the following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListDescendantEventThreatDetectionCustomModulesAsyncPager:
                Response message for
                   [SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListDescendantEventThreatDetectionCustomModules].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest,
        ):
            request = security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest(
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

    async def get_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.GetEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EventThreatDetectionCustomModule:
        r"""Gets an Event Threat Detection custom module.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_get_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.GetEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.GetEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetEventThreatDetectionCustomModule].
            name (:class:`str`):
                Required. The resource name of the Event Threat
                Detection custom module, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``

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
            google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule:
                A Security Command Center resource
                that contains the configuration and
                enablement state of a custom module,
                which enables Event Threat Detection to
                write certain findings to Security
                Command Center.

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
            security_center_management.GetEventThreatDetectionCustomModuleRequest,
        ):
            request = (
                security_center_management.GetEventThreatDetectionCustomModuleRequest(
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

    async def create_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.CreateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        event_threat_detection_custom_module: Optional[
            security_center_management.EventThreatDetectionCustomModule
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EventThreatDetectionCustomModule:
        r"""Creates a resident Event Threat Detection custom
        module at the scope of the given organization, folder,
        or project, and creates inherited custom modules for all
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
            from google.cloud import securitycentermanagement_v1

            async def sample_create_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.CreateEventThreatDetectionCustomModuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.CreateEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.CreateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.CreateEventThreatDetectionCustomModule].
            parent (:class:`str`):
                Required. Name of parent for the module, in one of the
                following formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            event_threat_detection_custom_module (:class:`google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule`):
                Required. The module to create. The
                [EventThreatDetectionCustomModule.name][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule.name]
                field is ignored; Security Command Center generates the
                name.

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
            google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule:
                A Security Command Center resource
                that contains the configuration and
                enablement state of a custom module,
                which enables Event Threat Detection to
                write certain findings to Security
                Command Center.

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
            security_center_management.CreateEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.CreateEventThreatDetectionCustomModuleRequest(
                request
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

    async def update_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        event_threat_detection_custom_module: Optional[
            security_center_management.EventThreatDetectionCustomModule
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.EventThreatDetectionCustomModule:
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
            from google.cloud import securitycentermanagement_v1

            async def sample_update_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.UpdateEventThreatDetectionCustomModuleRequest(
                )

                # Make the request
                response = await client.update_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.UpdateEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Message for updating a
                EventThreatDetectionCustomModule
            event_threat_detection_custom_module (:class:`google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule`):
                Required. The module being updated.
                This corresponds to the ``event_threat_detection_custom_module`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The fields to update. If
                omitted, then all fields are updated.

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
            google.cloud.securitycentermanagement_v1.types.EventThreatDetectionCustomModule:
                A Security Command Center resource
                that contains the configuration and
                enablement state of a custom module,
                which enables Event Threat Detection to
                write certain findings to Security
                Command Center.

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
            security_center_management.UpdateEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.UpdateEventThreatDetectionCustomModuleRequest(
                request
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

    async def delete_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
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
        module and all of its descendants in the resource
        hierarchy. This method is only supported for resident
        custom modules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_delete_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.DeleteEventThreatDetectionCustomModuleRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_event_threat_detection_custom_module(request=request)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.DeleteEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.DeleteEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.DeleteEventThreatDetectionCustomModule].
            name (:class:`str`):
                Required. The resource name of the Event Threat
                Detection custom module, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``
                - ``projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}``

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
            security_center_management.DeleteEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.DeleteEventThreatDetectionCustomModuleRequest(
                request
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

    async def validate_event_threat_detection_custom_module(
        self,
        request: Optional[
            Union[
                security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
                dict,
            ]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.ValidateEventThreatDetectionCustomModuleResponse:
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
            from google.cloud import securitycentermanagement_v1

            async def sample_validate_event_threat_detection_custom_module():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ValidateEventThreatDetectionCustomModuleRequest(
                    parent="parent_value",
                    raw_text="raw_text_value",
                    type_="type__value",
                )

                # Make the request
                response = await client.validate_event_threat_detection_custom_module(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ValidateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.securitycentermanagement_v1.types.ValidateEventThreatDetectionCustomModuleResponse:
                Response message for
                   [SecurityCenterManagement.ValidateEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ValidateEventThreatDetectionCustomModule].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            security_center_management.ValidateEventThreatDetectionCustomModuleRequest,
        ):
            request = security_center_management.ValidateEventThreatDetectionCustomModuleRequest(
                request
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

    async def get_security_center_service(
        self,
        request: Optional[
            Union[security_center_management.GetSecurityCenterServiceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityCenterService:
        r"""Gets service settings for the specified Security
        Command Center service.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_get_security_center_service():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.GetSecurityCenterServiceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_security_center_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.GetSecurityCenterServiceRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.GetSecurityCenterService][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.GetSecurityCenterService].
            name (:class:`str`):
                Required. The Security Command Center service to
                retrieve, in one of the following formats:

                - organizations/{organization}/locations/{location}/securityCenterServices/{service}
                - folders/{folder}/locations/{location}/securityCenterServices/{service}
                - projects/{project}/locations/{location}/securityCenterServices/{service}

                The following values are valid for ``{service}``:

                - ``container-threat-detection``
                - ``event-threat-detection``
                - ``security-health-analytics``
                - ``vm-threat-detection``
                - ``web-security-scanner``

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
            google.cloud.securitycentermanagement_v1.types.SecurityCenterService:
                Represents a particular Security
                Command Center service. This includes
                settings information such as top-level
                enablement in addition to individual
                module settings. Service settings can be
                configured at the organization, folder,
                or project level. Service settings at
                the organization or folder level are
                inherited by those in descendant folders
                and projects.

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
            request, security_center_management.GetSecurityCenterServiceRequest
        ):
            request = security_center_management.GetSecurityCenterServiceRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_security_center_service
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

    async def list_security_center_services(
        self,
        request: Optional[
            Union[security_center_management.ListSecurityCenterServicesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSecurityCenterServicesAsyncPager:
        r"""Returns a list of all Security Command Center
        services for the given parent.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_list_security_center_services():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.ListSecurityCenterServicesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_security_center_services(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.ListSecurityCenterServicesRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.ListSecurityCenterServices][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices].
            parent (:class:`str`):
                Required. The name of the parent to list Security
                Command Center services, in one of the following
                formats:

                - ``organizations/{organization}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``projects/{project}/locations/{location}``

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
            google.cloud.securitycentermanagement_v1.services.security_center_management.pagers.ListSecurityCenterServicesAsyncPager:
                Response message for
                   [SecurityCenterManagement.ListSecurityCenterServices][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
            request, security_center_management.ListSecurityCenterServicesRequest
        ):
            request = security_center_management.ListSecurityCenterServicesRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_security_center_services
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
        response = pagers.ListSecurityCenterServicesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_security_center_service(
        self,
        request: Optional[
            Union[security_center_management.UpdateSecurityCenterServiceRequest, dict]
        ] = None,
        *,
        security_center_service: Optional[
            security_center_management.SecurityCenterService
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> security_center_management.SecurityCenterService:
        r"""Updates a Security Command Center service using the
        given update mask.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import securitycentermanagement_v1

            async def sample_update_security_center_service():
                # Create a client
                client = securitycentermanagement_v1.SecurityCenterManagementAsyncClient()

                # Initialize request argument(s)
                request = securitycentermanagement_v1.UpdateSecurityCenterServiceRequest(
                )

                # Make the request
                response = await client.update_security_center_service(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.securitycentermanagement_v1.types.UpdateSecurityCenterServiceRequest, dict]]):
                The request object. Request message for
                [SecurityCenterManagement.UpdateSecurityCenterService][google.cloud.securitycentermanagement.v1.SecurityCenterManagement.UpdateSecurityCenterService].
            security_center_service (:class:`google.cloud.securitycentermanagement_v1.types.SecurityCenterService`):
                Required. The updated service.
                This corresponds to the ``security_center_service`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The fields to update. Accepts the following
                values:

                - ``intended_enablement_state``
                - ``modules``

                If omitted, then all eligible fields are updated.

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
            google.cloud.securitycentermanagement_v1.types.SecurityCenterService:
                Represents a particular Security
                Command Center service. This includes
                settings information such as top-level
                enablement in addition to individual
                module settings. Service settings can be
                configured at the organization, folder,
                or project level. Service settings at
                the organization or folder level are
                inherited by those in descendant folders
                and projects.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_center_service, update_mask]
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
            request, security_center_management.UpdateSecurityCenterServiceRequest
        ):
            request = security_center_management.UpdateSecurityCenterServiceRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if security_center_service is not None:
            request.security_center_service = security_center_service
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_security_center_service
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "security_center_service.name",
                        request.security_center_service.name,
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

    async def get_location(
        self,
        request: Optional[Union[locations_pb2.GetLocationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.Location:
        r"""Gets information about a location.

        Args:
            request (:class:`~.location_pb2.GetLocationRequest`):
                The request object. Request message for
                `GetLocation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.Location:
                Location object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.GetLocationRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.GetLocationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_location]

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

    async def list_locations(
        self,
        request: Optional[Union[locations_pb2.ListLocationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.ListLocationsResponse:
        r"""Lists information about the supported locations for this service.

        Args:
            request (:class:`~.location_pb2.ListLocationsRequest`):
                The request object. Request message for
                `ListLocations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.ListLocationsResponse:
                Response message for ``ListLocations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.ListLocationsRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.ListLocationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_locations]

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

    async def __aenter__(self) -> "SecurityCenterManagementAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("SecurityCenterManagementAsyncClient",)
