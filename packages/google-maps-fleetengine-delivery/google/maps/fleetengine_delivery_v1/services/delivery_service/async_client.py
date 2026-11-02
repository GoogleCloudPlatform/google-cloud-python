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

from google.maps.fleetengine_delivery_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore

from google.maps.fleetengine_delivery_v1.services.delivery_service import pagers
from google.maps.fleetengine_delivery_v1.types import (
    common,
    delivery_api,
    delivery_vehicles,
    task_tracking_info,
    tasks,
)

from .client import DeliveryServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DeliveryServiceTransport
from .transports.grpc_asyncio import DeliveryServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DeliveryServiceAsyncClient:
    """The Last Mile Delivery service."""

    _client: DeliveryServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DeliveryServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DeliveryServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DeliveryServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DeliveryServiceClient._DEFAULT_UNIVERSE

    delivery_vehicle_path = staticmethod(DeliveryServiceClient.delivery_vehicle_path)
    parse_delivery_vehicle_path = staticmethod(
        DeliveryServiceClient.parse_delivery_vehicle_path
    )
    task_path = staticmethod(DeliveryServiceClient.task_path)
    parse_task_path = staticmethod(DeliveryServiceClient.parse_task_path)
    task_tracking_info_path = staticmethod(
        DeliveryServiceClient.task_tracking_info_path
    )
    parse_task_tracking_info_path = staticmethod(
        DeliveryServiceClient.parse_task_tracking_info_path
    )
    common_billing_account_path = staticmethod(
        DeliveryServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DeliveryServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DeliveryServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DeliveryServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DeliveryServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DeliveryServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DeliveryServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DeliveryServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DeliveryServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DeliveryServiceClient.parse_common_location_path
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
            DeliveryServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DeliveryServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DeliveryServiceAsyncClient, info, *args, **kwargs)

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
            DeliveryServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DeliveryServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DeliveryServiceAsyncClient, filename, *args, **kwargs)

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
        return DeliveryServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DeliveryServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DeliveryServiceTransport: The transport used by the client instance.
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

    get_transport_class = DeliveryServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str, DeliveryServiceTransport, Callable[..., DeliveryServiceTransport]
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the delivery service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DeliveryServiceTransport,Callable[..., DeliveryServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DeliveryServiceTransport constructor.
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
        self._client = DeliveryServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `maps.fleetengine.delivery_v1.DeliveryServiceAsyncClient`.",
                extra={
                    "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
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
                    "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                    "credentialsType": None,
                },
            )

    async def create_delivery_vehicle(
        self,
        request: Optional[
            Union[delivery_api.CreateDeliveryVehicleRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        delivery_vehicle: Optional[delivery_vehicles.DeliveryVehicle] = None,
        delivery_vehicle_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> delivery_vehicles.DeliveryVehicle:
        r"""Creates and returns a new ``DeliveryVehicle``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_create_delivery_vehicle():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.CreateDeliveryVehicleRequest(
                    parent="parent_value",
                    delivery_vehicle_id="delivery_vehicle_id_value",
                )

                # Make the request
                response = await client.create_delivery_vehicle(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.CreateDeliveryVehicleRequest, dict]]):
                The request object. The ``CreateDeliveryVehicle`` request message.
            parent (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}``. The provider must be the
                Google Cloud Project ID. For example,
                ``sample-cloud-project``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            delivery_vehicle (:class:`google.maps.fleetengine_delivery_v1.types.DeliveryVehicle`):
                Required. The ``DeliveryVehicle`` entity to create. When
                creating a new delivery vehicle, you may set the
                following optional fields:

                - type
                - last_location
                - attributes

                Note: The DeliveryVehicle's ``name`` field is ignored.
                All other DeliveryVehicle fields must not be set;
                otherwise, an error is returned.

                This corresponds to the ``delivery_vehicle`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            delivery_vehicle_id (:class:`str`):
                Required. The Delivery Vehicle ID must be unique and
                subject to the following restrictions:

                - Must be a valid Unicode string.
                - Limited to a maximum length of 64 characters.
                - Normalized according to [Unicode Normalization Form C]
                  (http://www.unicode.org/reports/tr15/).
                - May not contain any of the following ASCII characters:
                  '/', ':', '?', ',', or '#'.

                This corresponds to the ``delivery_vehicle_id`` field
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
            google.maps.fleetengine_delivery_v1.types.DeliveryVehicle:
                The DeliveryVehicle message. A delivery vehicle transports shipments from a
                   depot to a delivery location, and from a pickup
                   location to the depot. In some cases, delivery
                   vehicles also transport shipments directly from the
                   pickup location to the delivery location.

                   Note: gRPC and REST APIs use different field naming
                   conventions. For example, the
                   DeliveryVehicle.current_route_segment field in the
                   gRPC API and the DeliveryVehicle.currentRouteSegment
                   field in the REST API refer to the same field.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, delivery_vehicle, delivery_vehicle_id]
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
        if not isinstance(request, delivery_api.CreateDeliveryVehicleRequest):
            request = delivery_api.CreateDeliveryVehicleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if delivery_vehicle is not None:
            request.delivery_vehicle = delivery_vehicle
        if delivery_vehicle_id is not None:
            request.delivery_vehicle_id = delivery_vehicle_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_delivery_vehicle
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

    async def get_delivery_vehicle(
        self,
        request: Optional[Union[delivery_api.GetDeliveryVehicleRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> delivery_vehicles.DeliveryVehicle:
        r"""Returns the specified ``DeliveryVehicle`` instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_get_delivery_vehicle():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.GetDeliveryVehicleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_delivery_vehicle(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.GetDeliveryVehicleRequest, dict]]):
                The request object. The ``GetDeliveryVehicle`` request message.
            name (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}/deliveryVehicles/{delivery_vehicle}``.
                The ``provider`` must be the Google Cloud Project ID.
                For example, ``sample-cloud-project``.

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
            google.maps.fleetengine_delivery_v1.types.DeliveryVehicle:
                The DeliveryVehicle message. A delivery vehicle transports shipments from a
                   depot to a delivery location, and from a pickup
                   location to the depot. In some cases, delivery
                   vehicles also transport shipments directly from the
                   pickup location to the delivery location.

                   Note: gRPC and REST APIs use different field naming
                   conventions. For example, the
                   DeliveryVehicle.current_route_segment field in the
                   gRPC API and the DeliveryVehicle.currentRouteSegment
                   field in the REST API refer to the same field.

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
        if not isinstance(request, delivery_api.GetDeliveryVehicleRequest):
            request = delivery_api.GetDeliveryVehicleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_delivery_vehicle
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

    async def delete_delivery_vehicle(
        self,
        request: Optional[
            Union[delivery_api.DeleteDeliveryVehicleRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a DeliveryVehicle from the Fleet Engine.

        Returns FAILED_PRECONDITION if the DeliveryVehicle has OPEN
        Tasks assigned to it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_delete_delivery_vehicle():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.DeleteDeliveryVehicleRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_delivery_vehicle(request=request)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.DeleteDeliveryVehicleRequest, dict]]):
                The request object. DeleteDeliveryVehicle request
                message.
            name (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}/deliveryVehicles/{delivery_vehicle}``.
                The ``provider`` must be the Google Cloud Project ID.
                For example, ``sample-cloud-project``.

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
        if not isinstance(request, delivery_api.DeleteDeliveryVehicleRequest):
            request = delivery_api.DeleteDeliveryVehicleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_delivery_vehicle
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

    async def update_delivery_vehicle(
        self,
        request: Optional[
            Union[delivery_api.UpdateDeliveryVehicleRequest, dict]
        ] = None,
        *,
        delivery_vehicle: Optional[delivery_vehicles.DeliveryVehicle] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> delivery_vehicles.DeliveryVehicle:
        r"""Writes updated ``DeliveryVehicle`` data to Fleet Engine, and
        assigns ``Tasks`` to the ``DeliveryVehicle``. You cannot update
        the name of the ``DeliveryVehicle``. You *can* update
        ``remaining_vehicle_journey_segments``, but it must contain all
        of the ``VehicleJourneySegment``\ s to be persisted on the
        ``DeliveryVehicle``. The ``task_id``\ s are retrieved from
        ``remaining_vehicle_journey_segments``, and their corresponding
        ``Tasks`` are assigned to the ``DeliveryVehicle`` if they have
        not yet been assigned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_update_delivery_vehicle():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.UpdateDeliveryVehicleRequest(
                )

                # Make the request
                response = await client.update_delivery_vehicle(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.UpdateDeliveryVehicleRequest, dict]]):
                The request object. The ``UpdateDeliveryVehicle`` request message.
            delivery_vehicle (:class:`google.maps.fleetengine_delivery_v1.types.DeliveryVehicle`):
                Required. The ``DeliveryVehicle`` entity update to
                apply. Note: You cannot update the name of the
                ``DeliveryVehicle``.

                This corresponds to the ``delivery_vehicle`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. A field mask that indicates which
                ``DeliveryVehicle`` fields to update. Note that the
                update_mask must contain at least one field.

                This is a comma-separated list of fully qualified names
                of fields. Example:
                ``"remaining_vehicle_journey_segments"``.

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
            google.maps.fleetengine_delivery_v1.types.DeliveryVehicle:
                The DeliveryVehicle message. A delivery vehicle transports shipments from a
                   depot to a delivery location, and from a pickup
                   location to the depot. In some cases, delivery
                   vehicles also transport shipments directly from the
                   pickup location to the delivery location.

                   Note: gRPC and REST APIs use different field naming
                   conventions. For example, the
                   DeliveryVehicle.current_route_segment field in the
                   gRPC API and the DeliveryVehicle.currentRouteSegment
                   field in the REST API refer to the same field.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [delivery_vehicle, update_mask]
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
        if not isinstance(request, delivery_api.UpdateDeliveryVehicleRequest):
            request = delivery_api.UpdateDeliveryVehicleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if delivery_vehicle is not None:
            request.delivery_vehicle = delivery_vehicle
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_delivery_vehicle
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.delivery_vehicle.name)
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

    async def batch_create_tasks(
        self,
        request: Optional[Union[delivery_api.BatchCreateTasksRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> delivery_api.BatchCreateTasksResponse:
        r"""Creates and returns a batch of new ``Task`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_batch_create_tasks():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                requests = fleetengine_delivery_v1.CreateTaskRequest()
                requests.parent = "parent_value"
                requests.task_id = "task_id_value"
                requests.task.type_ = "UNAVAILABLE"
                requests.task.state = "CLOSED"

                request = fleetengine_delivery_v1.BatchCreateTasksRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = await client.batch_create_tasks(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.BatchCreateTasksRequest, dict]]):
                The request object. The ``BatchCreateTask`` request message.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.maps.fleetengine_delivery_v1.types.BatchCreateTasksResponse:
                The BatchCreateTask response message.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, delivery_api.BatchCreateTasksRequest):
            request = delivery_api.BatchCreateTasksRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_create_tasks
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

    async def create_task(
        self,
        request: Optional[Union[delivery_api.CreateTaskRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        task: Optional[tasks.Task] = None,
        task_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tasks.Task:
        r"""Creates and returns a new ``Task`` object.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_create_task():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                task = fleetengine_delivery_v1.Task()
                task.type_ = "UNAVAILABLE"
                task.state = "CLOSED"

                request = fleetengine_delivery_v1.CreateTaskRequest(
                    parent="parent_value",
                    task_id="task_id_value",
                    task=task,
                )

                # Make the request
                response = await client.create_task(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.CreateTaskRequest, dict]]):
                The request object. The ``CreateTask`` request message.
            parent (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}``. The ``provider`` must be the
                Google Cloud Project ID. For example,
                ``sample-cloud-project``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            task (:class:`google.maps.fleetengine_delivery_v1.types.Task`):
                Required. The Task entity to create. When creating a
                Task, the following fields are required:

                - ``type``
                - ``state`` (must be set to ``OPEN``)
                - ``tracking_id`` (must not be set for ``UNAVAILABLE``
                  or ``SCHEDULED_STOP`` tasks, but required for all
                  other task types)
                - ``planned_location`` (optional for ``UNAVAILABLE``
                  tasks)
                - ``task_duration``

                The following fields can be optionally set:

                - ``target_time_window``
                - ``task_tracking_view_config``
                - ``attributes``

                Note: The Task's ``name`` field is ignored. All other
                Task fields must not be set; otherwise, an error is
                returned.

                This corresponds to the ``task`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            task_id (:class:`str`):
                Required. The Task ID must be unique, but it should be
                not a shipment tracking ID. To store a shipment tracking
                ID, use the ``tracking_id`` field. Note that multiple
                tasks can have the same ``tracking_id``. Task IDs are
                subject to the following restrictions:

                - Must be a valid Unicode string.
                - Limited to a maximum length of 64 characters.
                - Normalized according to [Unicode Normalization Form C]
                  (http://www.unicode.org/reports/tr15/).
                - May not contain any of the following ASCII characters:
                  '/', ':', '?', ',', or '#'.

                This corresponds to the ``task_id`` field
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
            google.maps.fleetengine_delivery_v1.types.Task:
                A Task in the Delivery API represents a single action to track. In general,
                   there is a distinction between shipment-related Tasks
                   and break Tasks. A shipment can have multiple Tasks
                   associated with it. For example, there could be one
                   Task for the pickup, and one for the drop-off or
                   transfer. Also, different Tasks for a given shipment
                   can be handled by different vehicles. For example,
                   one vehicle could handle the pickup, driving the
                   shipment to the hub, while another vehicle drives the
                   same shipment from the hub to the drop-off location.

                   Note: gRPC and REST APIs use different field naming
                   conventions. For example, the
                   Task.journey_sharing_info field in the gRPC API and
                   the Task.journeySharingInfo field in the REST API
                   refer to the same field.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, task, task_id]
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
        if not isinstance(request, delivery_api.CreateTaskRequest):
            request = delivery_api.CreateTaskRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if task is not None:
            request.task = task
        if task_id is not None:
            request.task_id = task_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_task
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

    async def get_task(
        self,
        request: Optional[Union[delivery_api.GetTaskRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tasks.Task:
        r"""Gets information about a ``Task``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_get_task():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.GetTaskRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_task(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.GetTaskRequest, dict]]):
                The request object. The ``GetTask`` request message.
            name (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}/tasks/{task}``. The ``provider``
                must be the Google Cloud Project ID. For example,
                ``sample-cloud-project``.

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
            google.maps.fleetengine_delivery_v1.types.Task:
                A Task in the Delivery API represents a single action to track. In general,
                   there is a distinction between shipment-related Tasks
                   and break Tasks. A shipment can have multiple Tasks
                   associated with it. For example, there could be one
                   Task for the pickup, and one for the drop-off or
                   transfer. Also, different Tasks for a given shipment
                   can be handled by different vehicles. For example,
                   one vehicle could handle the pickup, driving the
                   shipment to the hub, while another vehicle drives the
                   same shipment from the hub to the drop-off location.

                   Note: gRPC and REST APIs use different field naming
                   conventions. For example, the
                   Task.journey_sharing_info field in the gRPC API and
                   the Task.journeySharingInfo field in the REST API
                   refer to the same field.

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
        if not isinstance(request, delivery_api.GetTaskRequest):
            request = delivery_api.GetTaskRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_task]

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

    async def delete_task(
        self,
        request: Optional[Union[delivery_api.DeleteTaskRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a single Task.

        Returns FAILED_PRECONDITION if the Task is OPEN and assigned to
        a DeliveryVehicle.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_delete_task():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.DeleteTaskRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_task(request=request)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.DeleteTaskRequest, dict]]):
                The request object. DeleteTask request message.
            name (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}/tasks/{task}``. The ``provider``
                must be the Google Cloud Project ID. For example,
                ``sample-cloud-project``.

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
        if not isinstance(request, delivery_api.DeleteTaskRequest):
            request = delivery_api.DeleteTaskRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_task
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

    async def update_task(
        self,
        request: Optional[Union[delivery_api.UpdateTaskRequest, dict]] = None,
        *,
        task: Optional[tasks.Task] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tasks.Task:
        r"""Updates ``Task`` data.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_update_task():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                task = fleetengine_delivery_v1.Task()
                task.type_ = "UNAVAILABLE"
                task.state = "CLOSED"

                request = fleetengine_delivery_v1.UpdateTaskRequest(
                    task=task,
                )

                # Make the request
                response = await client.update_task(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.UpdateTaskRequest, dict]]):
                The request object. The ``UpdateTask`` request message.
            task (:class:`google.maps.fleetengine_delivery_v1.types.Task`):
                Required. The Task associated with the update. The
                following fields are maintained by Fleet Engine. Do not
                update them using ``Task.update``.

                - ``last_location``.
                - ``last_location_snappable``.
                - ``name``.
                - ``remaining_vehicle_journey_segments``.
                - ``task_outcome_location_source``.

                Note: You cannot change the value of ``task_outcome``
                once you set it.

                If the Task has been assigned to a delivery vehicle,
                then don't set the Task state to CLOSED using
                ``Task.update``. Instead, remove the ``VehicleStop``
                that contains the Task from the delivery vehicle, which
                automatically sets the Task state to CLOSED.

                This corresponds to the ``task`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The field mask that indicates which Task
                fields to update. Note: The ``update_mask`` must contain
                at least one field.

                This is a comma-separated list of fully qualified names
                of fields. Example:
                ``"task_outcome,task_outcome_time,task_outcome_location"``.

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
            google.maps.fleetengine_delivery_v1.types.Task:
                A Task in the Delivery API represents a single action to track. In general,
                   there is a distinction between shipment-related Tasks
                   and break Tasks. A shipment can have multiple Tasks
                   associated with it. For example, there could be one
                   Task for the pickup, and one for the drop-off or
                   transfer. Also, different Tasks for a given shipment
                   can be handled by different vehicles. For example,
                   one vehicle could handle the pickup, driving the
                   shipment to the hub, while another vehicle drives the
                   same shipment from the hub to the drop-off location.

                   Note: gRPC and REST APIs use different field naming
                   conventions. For example, the
                   Task.journey_sharing_info field in the gRPC API and
                   the Task.journeySharingInfo field in the REST API
                   refer to the same field.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [task, update_mask]
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
        if not isinstance(request, delivery_api.UpdateTaskRequest):
            request = delivery_api.UpdateTaskRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if task is not None:
            request.task = task
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_task
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<provider_id>providers/[^/]+)$")
        regex_match = routing_param_regex.match(request.task.name)
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

    async def list_tasks(
        self,
        request: Optional[Union[delivery_api.ListTasksRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTasksAsyncPager:
        r"""Gets all ``Task``\ s that meet the specified filtering criteria.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_list_tasks():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.ListTasksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_tasks(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.ListTasksRequest, dict]]):
                The request object. The ``ListTasks`` request message.
            parent (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}``. The ``provider`` must be the
                Google Cloud Project ID. For example,
                ``sample-cloud-project``.

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
            google.maps.fleetengine_delivery_v1.services.delivery_service.pagers.ListTasksAsyncPager:
                The ListTasks response that contains the set of Tasks that meet the filter
                   criteria in the ListTasksRequest.

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
        if not isinstance(request, delivery_api.ListTasksRequest):
            request = delivery_api.ListTasksRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_tasks
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
        response = pagers.ListTasksAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_task_tracking_info(
        self,
        request: Optional[Union[delivery_api.GetTaskTrackingInfoRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> task_tracking_info.TaskTrackingInfo:
        r"""Returns the specified ``TaskTrackingInfo`` instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_get_task_tracking_info():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.GetTaskTrackingInfoRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_task_tracking_info(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.GetTaskTrackingInfoRequest, dict]]):
                The request object. The ``GetTaskTrackingInfoRequest`` request message.
            name (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}/taskTrackingInfo/{tracking_id}``.
                The ``provider`` must be the Google Cloud Project ID,
                and the ``tracking_id`` must be the tracking ID
                associated with the task. An example name can be
                ``providers/sample-cloud-project/taskTrackingInfo/sample-tracking-id``.

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
            google.maps.fleetengine_delivery_v1.types.TaskTrackingInfo:
                The TaskTrackingInfo message. The message contains task tracking
                   information which will be used for display. If a
                   tracking ID is associated with multiple Tasks, Fleet
                   Engine uses a heuristic to decide which Task's
                   TaskTrackingInfo to select.

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
        if not isinstance(request, delivery_api.GetTaskTrackingInfoRequest):
            request = delivery_api.GetTaskTrackingInfoRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_task_tracking_info
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

    async def list_delivery_vehicles(
        self,
        request: Optional[Union[delivery_api.ListDeliveryVehiclesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDeliveryVehiclesAsyncPager:
        r"""Gets all ``DeliveryVehicle``\ s that meet the specified
        filtering criteria.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import fleetengine_delivery_v1

            async def sample_list_delivery_vehicles():
                # Create a client
                client = fleetengine_delivery_v1.DeliveryServiceAsyncClient()

                # Initialize request argument(s)
                request = fleetengine_delivery_v1.ListDeliveryVehiclesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_delivery_vehicles(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.maps.fleetengine_delivery_v1.types.ListDeliveryVehiclesRequest, dict]]):
                The request object. The ``ListDeliveryVehicles`` request message.
            parent (:class:`str`):
                Required. Must be in the format
                ``providers/{provider}``. The ``provider`` must be the
                Google Cloud Project ID. For example,
                ``sample-cloud-project``.

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
            google.maps.fleetengine_delivery_v1.services.delivery_service.pagers.ListDeliveryVehiclesAsyncPager:
                The ListDeliveryVehicles response message.

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
        if not isinstance(request, delivery_api.ListDeliveryVehiclesRequest):
            request = delivery_api.ListDeliveryVehiclesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_delivery_vehicles
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
        response = pagers.ListDeliveryVehiclesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "DeliveryServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DeliveryServiceAsyncClient",)
