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

from google.maps.fleetengine_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore

from google.maps.fleetengine_v1.services.vehicle_service import pagers
from google.maps.fleetengine_v1.types import fleetengine, vehicle_api, vehicles

from .client import VehicleServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, VehicleServiceTransport
from .transports.grpc_asyncio import VehicleServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class VehicleServiceAsyncClient:
    """Vehicle management service."""

    _client: VehicleServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = VehicleServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = VehicleServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = VehicleServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = VehicleServiceClient._DEFAULT_UNIVERSE

    vehicle_path = staticmethod(VehicleServiceClient.vehicle_path)
    parse_vehicle_path = staticmethod(VehicleServiceClient.parse_vehicle_path)
    common_billing_account_path = staticmethod(
        VehicleServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        VehicleServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(VehicleServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        VehicleServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        VehicleServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        VehicleServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(VehicleServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        VehicleServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(VehicleServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        VehicleServiceClient.parse_common_location_path
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
            VehicleServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            VehicleServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(VehicleServiceAsyncClient, info, *args, **kwargs)

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
            VehicleServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            VehicleServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(VehicleServiceAsyncClient, filename, *args, **kwargs)

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
        return VehicleServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> VehicleServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            VehicleServiceTransport: The transport used by the client instance.
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

    get_transport_class = VehicleServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, VehicleServiceTransport, Callable[..., VehicleServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the vehicle service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,VehicleServiceTransport,Callable[..., VehicleServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the VehicleServiceTransport constructor.
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
        self._client = VehicleServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `maps.fleetengine_v1.VehicleServiceAsyncClient`.",
                extra={
                    "serviceName": "maps.fleetengine.v1.VehicleService",
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
                    "serviceName": "maps.fleetengine.v1.VehicleService",
                    "credentialsType": None,
                },
            )

    async def create_vehicle(
        self,
        request: Optional[Union[vehicle_api.CreateVehicleRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vehicles.Vehicle:
        r"""Instantiates a new vehicle associated with an on-demand
        rideshare or deliveries provider. Each ``Vehicle`` must have a
        unique vehicle ID.

        The following ``Vehicle`` fields are required when creating a
        ``Vehicle``:

        - ``vehicleState``
        - ``supportedTripTypes``
        - ``maximumCapacity``
        - ``vehicleType``

        The following ``Vehicle`` fields are ignored when creating a
        ``Vehicle``:

        - ``name``
        - ``currentTrips``
        - ``availableCapacity``
        - ``current_route_segment``
        - ``current_route_segment_end_point``
        - ``current_route_segment_version``
        - ``current_route_segment_traffic``
        - ``route``
        - ``waypoints``
        - ``waypoints_version``
        - ``remaining_distance_meters``
        - ``remaining_time_seconds``
        - ``eta_to_next_waypoint``
        - ``navigation_status``

        All other fields are optional and used if provided.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_v1

            async def sample_create_vehicle():
                # Create a client
                client = fleetengine_v1.VehicleServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_v1.CreateVehicleRequest(
                    parent="parent_value",
                    vehicle_id="vehicle_id_value",
                )

                # Make the request
                response = await client.create_vehicle(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_v1.types.CreateVehicleRequest, dict]]):
                The request object. ``CreateVehicle`` request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.maps.fleetengine_v1.types.Vehicle:
                Vehicle metadata.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, vehicle_api.CreateVehicleRequest):
            request = vehicle_api.CreateVehicleRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_vehicle
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("provider_id"):
            header_params["provider_id"] = regex_match.group("provider_id")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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

    async def get_vehicle(
        self,
        request: Optional[Union[vehicle_api.GetVehicleRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vehicles.Vehicle:
        r"""Returns a vehicle from the Fleet Engine.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_v1

            async def sample_get_vehicle():
                # Create a client
                client = fleetengine_v1.VehicleServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_v1.GetVehicleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_vehicle(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_v1.types.GetVehicleRequest, dict]]):
                The request object. ``GetVehicle`` request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.maps.fleetengine_v1.types.Vehicle:
                Vehicle metadata.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, vehicle_api.GetVehicleRequest):
            request = vehicle_api.GetVehicleRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_vehicle
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("provider_id"):
            header_params["provider_id"] = regex_match.group("provider_id")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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

    async def delete_vehicle(
        self,
        request: Optional[Union[vehicle_api.DeleteVehicleRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a Vehicle from the Fleet Engine.

        Returns FAILED_PRECONDITION if the Vehicle has active Trips.
        assigned to it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_v1

            async def sample_delete_vehicle():
                # Create a client
                client = fleetengine_v1.VehicleServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_v1.DeleteVehicleRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_vehicle(request=request)

        Args:
            request (Optional[Union[google.maps.fleetengine_v1.types.DeleteVehicleRequest, dict]]):
                The request object. DeleteVehicle request message.
            name (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}/vehicles/{vehicle}``. The
                {provider} must be the Project ID (for example,
                ``sample-cloud-project``) of the Google Cloud Project of
                which the service account making this call is a member.

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
        if not isinstance(request, vehicle_api.DeleteVehicleRequest):
            request = vehicle_api.DeleteVehicleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_vehicle
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("provider_id"):
            header_params["provider_id"] = regex_match.group("provider_id")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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

    async def update_vehicle(
        self,
        request: Optional[Union[vehicle_api.UpdateVehicleRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vehicles.Vehicle:
        r"""Writes updated vehicle data to the Fleet Engine.

        When updating a ``Vehicle``, the following fields cannot be
        updated since they are managed by the server:

        - ``currentTrips``
        - ``availableCapacity``
        - ``current_route_segment_version``
        - ``waypoints_version``

        The vehicle ``name`` also cannot be updated.

        If the ``attributes`` field is updated, **all** the vehicle's
        attributes are replaced with the attributes provided in the
        request. If you want to update only some attributes, see the
        ``UpdateVehicleAttributes`` method. Likewise, the ``waypoints``
        field can be updated, but must contain all the waypoints
        currently on the vehicle, and no other waypoints.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_v1

            async def sample_update_vehicle():
                # Create a client
                client = fleetengine_v1.VehicleServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_v1.UpdateVehicleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.update_vehicle(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_v1.types.UpdateVehicleRequest, dict]]):
                The request object. \`UpdateVehicle request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.maps.fleetengine_v1.types.Vehicle:
                Vehicle metadata.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, vehicle_api.UpdateVehicleRequest):
            request = vehicle_api.UpdateVehicleRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_vehicle
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("provider_id"):
            header_params["provider_id"] = regex_match.group("provider_id")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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

    async def update_vehicle_attributes(
        self,
        request: Optional[
            Union[vehicle_api.UpdateVehicleAttributesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vehicle_api.UpdateVehicleAttributesResponse:
        r"""Partially updates a vehicle's attributes. Only the attributes
        mentioned in the request will be updated, other attributes will
        NOT be altered. Note: this is different in ``UpdateVehicle``,
        where the whole ``attributes`` field will be replaced by the one
        in ``UpdateVehicleRequest``, attributes not in the request would
        be removed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_v1

            async def sample_update_vehicle_attributes():
                # Create a client
                client = fleetengine_v1.VehicleServiceAsyncClient()

                # Initialize request argument(s)
                attributes = fleetengine_v1.VehicleAttribute()
                attributes.string_value = "string_value_value"

                request = fleetengine_v1.UpdateVehicleAttributesRequest(
                    name="name_value",
                    attributes=attributes,
                )

                # Make the request
                response = await client.update_vehicle_attributes(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_v1.types.UpdateVehicleAttributesRequest, dict]]):
                The request object. ``UpdateVehicleAttributes`` request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.maps.fleetengine_v1.types.UpdateVehicleAttributesResponse:
                UpdateVehicleAttributes response message.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, vehicle_api.UpdateVehicleAttributesRequest):
            request = vehicle_api.UpdateVehicleAttributesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_vehicle_attributes
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("provider_id"):
            header_params["provider_id"] = regex_match.group("provider_id")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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

    async def list_vehicles(
        self,
        request: Optional[Union[vehicle_api.ListVehiclesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListVehiclesAsyncPager:
        r"""Returns a paginated list of vehicles associated with
        a provider that match the request options.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_v1

            async def sample_list_vehicles():
                # Create a client
                client = fleetengine_v1.VehicleServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_v1.ListVehiclesRequest(
                    parent="parent_value",
                    vehicle_type_categories=['PEDESTRIAN'],
                )

                # Make the request
                page_result = client.list_vehicles(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_v1.types.ListVehiclesRequest, dict]]):
                The request object. ``ListVehicles`` request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.maps.fleetengine_v1.services.vehicle_service.pagers.ListVehiclesAsyncPager:
                ListVehicles response message.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, vehicle_api.ListVehiclesRequest):
            request = vehicle_api.ListVehiclesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_vehicles
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("provider_id"):
            header_params["provider_id"] = regex_match.group("provider_id")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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
        response = pagers.ListVehiclesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_vehicles(
        self,
        request: Optional[Union[vehicle_api.SearchVehiclesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> vehicle_api.SearchVehiclesResponse:
        r"""Returns a list of vehicles that match the request
        options.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_v1

            async def sample_search_vehicles():
                # Create a client
                client = fleetengine_v1.VehicleServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_v1.SearchVehiclesRequest(
                    parent="parent_value",
                    pickup_radius_meters=2146,
                    count=553,
                    minimum_capacity=1705,
                    trip_types=['EXCLUSIVE'],
                    order_by="COST",
                )

                # Make the request
                response = await client.search_vehicles(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_v1.types.SearchVehiclesRequest, dict]]):
                The request object. ``SearchVehicles`` request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.maps.fleetengine_v1.types.SearchVehiclesResponse:
                SearchVehicles response message.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, vehicle_api.SearchVehiclesRequest):
            request = vehicle_api.SearchVehiclesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_vehicles
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("provider_id"):
            header_params["provider_id"] = regex_match.group("provider_id")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
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

    async def __aenter__(self) -> "VehicleServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("VehicleServiceAsyncClient",)
