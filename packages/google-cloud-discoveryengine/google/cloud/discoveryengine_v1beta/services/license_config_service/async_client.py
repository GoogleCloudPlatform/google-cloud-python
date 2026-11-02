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

from google.cloud.discoveryengine_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.discoveryengine_v1beta.services.license_config_service import pagers
from google.cloud.discoveryengine_v1beta.types import (
    common,
    license_config,
    license_config_service,
)
from google.cloud.discoveryengine_v1beta.types import (
    license_config as gcd_license_config,
)

from .client import LicenseConfigServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, LicenseConfigServiceTransport
from .transports.grpc_asyncio import LicenseConfigServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class LicenseConfigServiceAsyncClient:
    """Service for managing license config related resources."""

    _client: LicenseConfigServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = LicenseConfigServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = LicenseConfigServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = LicenseConfigServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = LicenseConfigServiceClient._DEFAULT_UNIVERSE

    billing_account_license_config_path = staticmethod(
        LicenseConfigServiceClient.billing_account_license_config_path
    )
    parse_billing_account_license_config_path = staticmethod(
        LicenseConfigServiceClient.parse_billing_account_license_config_path
    )
    license_config_path = staticmethod(LicenseConfigServiceClient.license_config_path)
    parse_license_config_path = staticmethod(
        LicenseConfigServiceClient.parse_license_config_path
    )
    location_path = staticmethod(LicenseConfigServiceClient.location_path)
    parse_location_path = staticmethod(LicenseConfigServiceClient.parse_location_path)
    common_billing_account_path = staticmethod(
        LicenseConfigServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        LicenseConfigServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(LicenseConfigServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        LicenseConfigServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        LicenseConfigServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        LicenseConfigServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(LicenseConfigServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        LicenseConfigServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(LicenseConfigServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        LicenseConfigServiceClient.parse_common_location_path
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
            LicenseConfigServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            LicenseConfigServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(LicenseConfigServiceAsyncClient, info, *args, **kwargs)

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
            LicenseConfigServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            LicenseConfigServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(LicenseConfigServiceAsyncClient, filename, *args, **kwargs)

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
        return LicenseConfigServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> LicenseConfigServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            LicenseConfigServiceTransport: The transport used by the client instance.
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

    get_transport_class = LicenseConfigServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                LicenseConfigServiceTransport,
                Callable[..., LicenseConfigServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the license config service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,LicenseConfigServiceTransport,Callable[..., LicenseConfigServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the LicenseConfigServiceTransport constructor.
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
        self._client = LicenseConfigServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.discoveryengine_v1beta.LicenseConfigServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
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
                    "serviceName": "google.cloud.discoveryengine.v1beta.LicenseConfigService",
                    "credentialsType": None,
                },
            )

    async def create_license_config(
        self,
        request: Optional[
            Union[license_config_service.CreateLicenseConfigRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        license_config: Optional[gcd_license_config.LicenseConfig] = None,
        license_config_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_license_config.LicenseConfig:
        r"""Creates a
        [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
        This method should only be used for creating NotebookLm licenses
        or Gemini Enterprise free trial licenses.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_create_license_config():
                # Create a client
                client = discoveryengine_v1beta.LicenseConfigServiceAsyncClient()

                # Initialize request argument(s)
                license_config = discoveryengine_v1beta.LicenseConfig()
                license_config.license_count = 1387
                license_config.subscription_tier = "SUBSCRIPTION_TIER_FRONTLINE_STARTER"
                license_config.subscription_term = "SUBSCRIPTION_TERM_CUSTOM"

                request = discoveryengine_v1beta.CreateLicenseConfigRequest(
                    parent="parent_value",
                    license_config=license_config,
                )

                # Make the request
                response = await client.create_license_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.CreateLicenseConfigRequest, dict]]):
                The request object. Request message for
                [LicenseConfigService.CreateLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig]
                method.
            parent (:class:`str`):
                Required. The parent resource name, such as
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            license_config (:class:`google.cloud.discoveryengine_v1beta.types.LicenseConfig`):
                Required. The
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
                to create.

                This corresponds to the ``license_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            license_config_id (:class:`str`):
                Optional. The ID to use for the
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig],
                which will become the final component of the
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]'s
                resource name. We are using the tier (product edition)
                name as the license config id such as ``search`` or
                ``search_and_assistant``.

                This corresponds to the ``license_config_id`` field
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
            google.cloud.discoveryengine_v1beta.types.LicenseConfig:
                Information about users' licenses.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, license_config, license_config_id]
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
        if not isinstance(request, license_config_service.CreateLicenseConfigRequest):
            request = license_config_service.CreateLicenseConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if license_config is not None:
            request.license_config = license_config
        if license_config_id is not None:
            request.license_config_id = license_config_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_license_config
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

    async def update_license_config(
        self,
        request: Optional[
            Union[license_config_service.UpdateLicenseConfigRequest, dict]
        ] = None,
        *,
        license_config: Optional[gcd_license_config.LicenseConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_license_config.LicenseConfig:
        r"""Updates the
        [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_update_license_config():
                # Create a client
                client = discoveryengine_v1beta.LicenseConfigServiceAsyncClient()

                # Initialize request argument(s)
                license_config = discoveryengine_v1beta.LicenseConfig()
                license_config.license_count = 1387
                license_config.subscription_tier = "SUBSCRIPTION_TIER_FRONTLINE_STARTER"
                license_config.subscription_term = "SUBSCRIPTION_TERM_CUSTOM"

                request = discoveryengine_v1beta.UpdateLicenseConfigRequest(
                    license_config=license_config,
                )

                # Make the request
                response = await client.update_license_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.UpdateLicenseConfigRequest, dict]]):
                The request object. Request message for
                [LicenseConfigService.UpdateLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig]
                method.
            license_config (:class:`google.cloud.discoveryengine_v1beta.types.LicenseConfig`):
                Required. The
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
                to update.

                This corresponds to the ``license_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Indicates which fields in the provided
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
                to update.

                If an unsupported or unknown field is provided, an
                INVALID_ARGUMENT error is returned.

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
            google.cloud.discoveryengine_v1beta.types.LicenseConfig:
                Information about users' licenses.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [license_config, update_mask]
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
        if not isinstance(request, license_config_service.UpdateLicenseConfigRequest):
            request = license_config_service.UpdateLicenseConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if license_config is not None:
            request.license_config = license_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_license_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("license_config.name", request.license_config.name),)
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

    async def get_license_config(
        self,
        request: Optional[
            Union[license_config_service.GetLicenseConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> license_config.LicenseConfig:
        r"""Gets a
        [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_get_license_config():
                # Create a client
                client = discoveryengine_v1beta.LicenseConfigServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.GetLicenseConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_license_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.GetLicenseConfigRequest, dict]]):
                The request object. Request message for
                [LicenseConfigService.GetLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig]
                method.
            name (:class:`str`):
                Required. Full resource name of
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig],
                such as
                ``projects/{project}/locations/{location}/licenseConfigs/*``.

                If the caller does not have permission to access the
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                If the requested
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
                does not exist, a NOT_FOUND error is returned.

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
            google.cloud.discoveryengine_v1beta.types.LicenseConfig:
                Information about users' licenses.
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
        if not isinstance(request, license_config_service.GetLicenseConfigRequest):
            request = license_config_service.GetLicenseConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_license_config
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

    async def list_license_configs(
        self,
        request: Optional[
            Union[license_config_service.ListLicenseConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListLicenseConfigsAsyncPager:
        r"""Lists all the
        [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]s
        associated with the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_list_license_configs():
                # Create a client
                client = discoveryengine_v1beta.LicenseConfigServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.ListLicenseConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_license_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsRequest, dict]]):
                The request object. Request message for
                [LicenseConfigService.ListLicenseConfigs][google.cloud.discoveryengine.v1beta.LicenseConfigService.ListLicenseConfigs]
                method.
            parent (:class:`str`):
                Required. The parent branch resource name, such as
                ``projects/{project}/locations/{location}``.

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
            google.cloud.discoveryengine_v1beta.services.license_config_service.pagers.ListLicenseConfigsAsyncPager:
                Response message for
                   [LicenseConfigService.ListLicenseConfigs][google.cloud.discoveryengine.v1beta.LicenseConfigService.ListLicenseConfigs]
                   method.

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
        if not isinstance(request, license_config_service.ListLicenseConfigsRequest):
            request = license_config_service.ListLicenseConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_license_configs
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
        response = pagers.ListLicenseConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def distribute_license_config(
        self,
        request: Optional[
            Union[license_config_service.DistributeLicenseConfigRequest, dict]
        ] = None,
        *,
        billing_account_license_config: Optional[str] = None,
        project_number: Optional[int] = None,
        location: Optional[str] = None,
        license_count: Optional[int] = None,
        license_config_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> license_config_service.DistributeLicenseConfigResponse:
        r"""Distributes a
        [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
        from billing account level to project level.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_distribute_license_config():
                # Create a client
                client = discoveryengine_v1beta.LicenseConfigServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.DistributeLicenseConfigRequest(
                    billing_account_license_config="billing_account_license_config_value",
                    project_number=1503,
                    location="location_value",
                    license_count=1387,
                )

                # Make the request
                response = await client.distribute_license_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.DistributeLicenseConfigRequest, dict]]):
                The request object. Request message for
                [LicenseConfigService.DistributeLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig]
                method.
            billing_account_license_config (:class:`str`):
                Required. Full resource name of
                [BillingAccountLicenseConfig][].

                Format:
                ``billingAccounts/{billing_account}/billingAccountLicenseConfigs/{billing_account_license_config_id}``.

                This corresponds to the ``billing_account_license_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            project_number (:class:`int`):
                Required. The target GCP project
                number to distribute the license config
                to.

                This corresponds to the ``project_number`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            location (:class:`str`):
                Required. The target GCP project
                region to distribute the license config
                to.

                This corresponds to the ``location`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            license_count (:class:`int`):
                Required. The number of licenses to
                distribute.

                This corresponds to the ``license_count`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            license_config_id (:class:`str`):
                Optional. Distribute seats to this
                license config instead of creating a new
                one. If not specified, a new license
                config will be created from the billing
                account license config.

                This corresponds to the ``license_config_id`` field
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
            google.cloud.discoveryengine_v1beta.types.DistributeLicenseConfigResponse:
                Response message for
                   [LicenseConfigService.DistributeLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig]
                   method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            billing_account_license_config,
            project_number,
            location,
            license_count,
            license_config_id,
        ]
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
            request, license_config_service.DistributeLicenseConfigRequest
        ):
            request = license_config_service.DistributeLicenseConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if billing_account_license_config is not None:
            request.billing_account_license_config = billing_account_license_config
        if project_number is not None:
            request.project_number = project_number
        if location is not None:
            request.location = location
        if license_count is not None:
            request.license_count = license_count
        if license_config_id is not None:
            request.license_config_id = license_config_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.distribute_license_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "billing_account_license_config",
                        request.billing_account_license_config,
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

    async def retract_license_config(
        self,
        request: Optional[
            Union[license_config_service.RetractLicenseConfigRequest, dict]
        ] = None,
        *,
        billing_account_license_config: Optional[str] = None,
        license_config: Optional[str] = None,
        full_retract: Optional[bool] = None,
        license_count: Optional[int] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> license_config_service.RetractLicenseConfigResponse:
        r"""This method is called from the billing account side to retract
        the
        [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
        from the given project back to the billing account.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_retract_license_config():
                # Create a client
                client = discoveryengine_v1beta.LicenseConfigServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.RetractLicenseConfigRequest(
                    billing_account_license_config="billing_account_license_config_value",
                    license_config="license_config_value",
                )

                # Make the request
                response = await client.retract_license_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.RetractLicenseConfigRequest, dict]]):
                The request object. Request message for
                [LicenseConfigService.RetractLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig]
                method.
            billing_account_license_config (:class:`str`):
                Required. Full resource name of
                [BillingAccountLicenseConfig][].

                Format:
                ``billingAccounts/{billing_account}/billingAccountLicenseConfigs/{billing_account_license_config_id}``.

                This corresponds to the ``billing_account_license_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            license_config (:class:`str`):
                Required. Full resource name of
                [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig].

                Format:
                ``projects/{project}/locations/{location}/licenseConfigs/{license_config_id}``.

                This corresponds to the ``license_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            full_retract (:class:`bool`):
                Optional. If set to true, retract the
                entire license config. Otherwise,
                retract the specified license count.

                This corresponds to the ``full_retract`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            license_count (:class:`int`):
                Optional. The number of licenses to retract. Only used
                when full_retract is false.

                This corresponds to the ``license_count`` field
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
            google.cloud.discoveryengine_v1beta.types.RetractLicenseConfigResponse:
                Response message for
                   [LicenseConfigService.RetractLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig]
                   method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            billing_account_license_config,
            license_config,
            full_retract,
            license_count,
        ]
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
        if not isinstance(request, license_config_service.RetractLicenseConfigRequest):
            request = license_config_service.RetractLicenseConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if billing_account_license_config is not None:
            request.billing_account_license_config = billing_account_license_config
        if license_config is not None:
            request.license_config = license_config
        if full_retract is not None:
            request.full_retract = full_retract
        if license_count is not None:
            request.license_count = license_count

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.retract_license_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "billing_account_license_config",
                        request.billing_account_license_config,
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

    async def __aenter__(self) -> "LicenseConfigServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("LicenseConfigServiceAsyncClient",)
