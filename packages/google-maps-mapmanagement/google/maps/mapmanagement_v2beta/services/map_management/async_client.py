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

from google.maps.mapmanagement_v2beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.maps.mapmanagement_v2beta.services.map_management import pagers
from google.maps.mapmanagement_v2beta.types import map_management_service

from .client import MapManagementClient
from .transports.base import DEFAULT_CLIENT_INFO, MapManagementTransport
from .transports.grpc_asyncio import MapManagementGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class MapManagementAsyncClient:
    """The Map Management API uses your inputs to create and manage Google
    Cloud based styling resources for Google Maps.

    Using this API, you can can create and manage MapConfigs (Map IDs),
    StyleConfigs (JSON-based styling), and MapContextConfigs
    (associations between styles, datasets, and map variants).

    This API offers features through three channels:

    - ``v2alpha``: Experimental features.
    - ``v2beta``: Preview features, recommended for early adoption.
    - ``v2``: General Availability (GA) features.

    Capabilities described here are generally available across both the
    v2alpha and v2beta endpoints.
    """

    _client: MapManagementClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = MapManagementClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = MapManagementClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = MapManagementClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = MapManagementClient._DEFAULT_UNIVERSE

    dataset_path = staticmethod(MapManagementClient.dataset_path)
    parse_dataset_path = staticmethod(MapManagementClient.parse_dataset_path)
    map_config_path = staticmethod(MapManagementClient.map_config_path)
    parse_map_config_path = staticmethod(MapManagementClient.parse_map_config_path)
    map_context_config_path = staticmethod(MapManagementClient.map_context_config_path)
    parse_map_context_config_path = staticmethod(
        MapManagementClient.parse_map_context_config_path
    )
    style_config_path = staticmethod(MapManagementClient.style_config_path)
    parse_style_config_path = staticmethod(MapManagementClient.parse_style_config_path)
    common_billing_account_path = staticmethod(
        MapManagementClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        MapManagementClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(MapManagementClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        MapManagementClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        MapManagementClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        MapManagementClient.parse_common_organization_path
    )
    common_project_path = staticmethod(MapManagementClient.common_project_path)
    parse_common_project_path = staticmethod(
        MapManagementClient.parse_common_project_path
    )
    common_location_path = staticmethod(MapManagementClient.common_location_path)
    parse_common_location_path = staticmethod(
        MapManagementClient.parse_common_location_path
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
            MapManagementAsyncClient: The constructed client.
        """
        sa_info_func = (
            MapManagementClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(MapManagementAsyncClient, info, *args, **kwargs)

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
            MapManagementAsyncClient: The constructed client.
        """
        sa_file_func = (
            MapManagementClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(MapManagementAsyncClient, filename, *args, **kwargs)

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
        return MapManagementClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> MapManagementTransport:
        """Returns the transport used by the client instance.

        Returns:
            MapManagementTransport: The transport used by the client instance.
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

    get_transport_class = MapManagementClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, MapManagementTransport, Callable[..., MapManagementTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the map management async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,MapManagementTransport,Callable[..., MapManagementTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the MapManagementTransport constructor.
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
        self._client = MapManagementClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.maps.mapmanagement_v2beta.MapManagementAsyncClient`.",
                extra={
                    "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
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
                    "serviceName": "google.maps.mapmanagement.v2beta.MapManagement",
                    "credentialsType": None,
                },
            )

    async def create_map_config(
        self,
        request: Optional[
            Union[map_management_service.CreateMapConfigRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        map_config: Optional[map_management_service.MapConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.MapConfig:
        r"""Creates a MapConfig in a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_create_map_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.CreateMapConfigRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_map_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.CreateMapConfigRequest, dict]]):
                The request object. Request to create a MapConfig.
            parent (:class:`str`):
                Required. Parent project that will own the MapConfig.
                Format: ``projects/{$my-project-id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            map_config (:class:`google.maps.mapmanagement_v2beta.types.MapConfig`):
                Required. The MapConfig to create.
                This corresponds to the ``map_config`` field
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
            google.maps.mapmanagement_v2beta.types.MapConfig:
                Represents a single map in a Maps API
                client application. The MapConfig is the
                parent resource of MapContextConfigs and
                enables custom styling in SDKs
                (Mobile/Web). A MapConfig can have
                multiple MapContextConfigs, each
                applying styling to specific map
                variants.
                Next ID = 9;

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, map_config]
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
        if not isinstance(request, map_management_service.CreateMapConfigRequest):
            request = map_management_service.CreateMapConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if map_config is not None:
            request.map_config = map_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_map_config
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

    async def get_map_config(
        self,
        request: Optional[
            Union[map_management_service.GetMapConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.MapConfig:
        r"""Gets a MapConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_get_map_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.GetMapConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_map_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.GetMapConfigRequest, dict]]):
                The request object. Request to get a MapConfig.
            name (:class:`str`):
                Required. Resource name of the MapConfig. Format:
                ``projects/{project}/mapConfigs/{map_config}``

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
            google.maps.mapmanagement_v2beta.types.MapConfig:
                Represents a single map in a Maps API
                client application. The MapConfig is the
                parent resource of MapContextConfigs and
                enables custom styling in SDKs
                (Mobile/Web). A MapConfig can have
                multiple MapContextConfigs, each
                applying styling to specific map
                variants.
                Next ID = 9;

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
        if not isinstance(request, map_management_service.GetMapConfigRequest):
            request = map_management_service.GetMapConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_map_config
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

    async def list_map_configs(
        self,
        request: Optional[
            Union[map_management_service.ListMapConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListMapConfigsAsyncPager:
        r"""Lists MapConfigs for a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_list_map_configs():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.ListMapConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_map_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.ListMapConfigsRequest, dict]]):
                The request object. Request to list MapConfigs.
            parent (:class:`str`):
                Required. Parent project that owns the MapConfigs.
                Format: ``projects/{project}``

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
            google.maps.mapmanagement_v2beta.services.map_management.pagers.ListMapConfigsAsyncPager:
                Response to list MapConfigs.

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
        if not isinstance(request, map_management_service.ListMapConfigsRequest):
            request = map_management_service.ListMapConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_map_configs
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
        response = pagers.ListMapConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_map_config(
        self,
        request: Optional[
            Union[map_management_service.UpdateMapConfigRequest, dict]
        ] = None,
        *,
        map_config: Optional[map_management_service.MapConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.MapConfig:
        r"""Updates a MapConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_update_map_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.UpdateMapConfigRequest(
                )

                # Make the request
                response = await client.update_map_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.UpdateMapConfigRequest, dict]]):
                The request object. Request to update a MapConfig.
            map_config (:class:`google.maps.mapmanagement_v2beta.types.MapConfig`):
                Required. The MapConfig to update.

                The MapConfig's ``name`` field is used to identify the
                MapConfig to update. Format:
                ``projects/{project}/mapConfigs/{map_config}``

                This corresponds to the ``map_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The specific field to update for the
                MapConfig. If not specified, the MapConfig will be
                updated in its entirety. Valid fields are:

                - ``display_name``
                - ``description``
                - ``map_features``

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
            google.maps.mapmanagement_v2beta.types.MapConfig:
                Represents a single map in a Maps API
                client application. The MapConfig is the
                parent resource of MapContextConfigs and
                enables custom styling in SDKs
                (Mobile/Web). A MapConfig can have
                multiple MapContextConfigs, each
                applying styling to specific map
                variants.
                Next ID = 9;

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [map_config, update_mask]
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
        if not isinstance(request, map_management_service.UpdateMapConfigRequest):
            request = map_management_service.UpdateMapConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if map_config is not None:
            request.map_config = map_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_map_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("map_config.name", request.map_config.name),)
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

    async def delete_map_config(
        self,
        request: Optional[
            Union[map_management_service.DeleteMapConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        force: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a MapConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_delete_map_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.DeleteMapConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_map_config(request=request)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.DeleteMapConfigRequest, dict]]):
                The request object. Request to delete a MapConfig. If the
                MapConfig has any child
                MapContextConfigs, those will be deleted
                as well.
            name (:class:`str`):
                Required. Resource name of the MapConfig to delete.
                Format: ``projects/{project}/mapConfigs/{map_config}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            force (:class:`bool`):
                Optional. If set to true, any
                MapContextConfigs from this MapConfig
                will also be deleted. (Otherwise, the
                request will only work if the MapConfig
                has no MapContextConfigs.)

                This corresponds to the ``force`` field
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
        flattened_params = [name, force]
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
        if not isinstance(request, map_management_service.DeleteMapConfigRequest):
            request = map_management_service.DeleteMapConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if force is not None:
            request.force = force

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_map_config
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

    async def create_style_config(
        self,
        request: Optional[
            Union[map_management_service.CreateStyleConfigRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        style_config: Optional[map_management_service.StyleConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.StyleConfig:
        r"""Creates a StyleConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_create_style_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.CreateStyleConfigRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_style_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.CreateStyleConfigRequest, dict]]):
                The request object. Request to create a StyleConfig.
            parent (:class:`str`):
                Required. Parent project that will own the StyleConfig.
                Format: ``projects/{project}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            style_config (:class:`google.maps.mapmanagement_v2beta.types.StyleConfig`):
                Required. The StyleConfig to create.
                This corresponds to the ``style_config`` field
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
            google.maps.mapmanagement_v2beta.types.StyleConfig:
                Represents a single style in a Maps
                API client application. The StyleConfig
                contains the style sheet that defines
                the visual appearance of the map. Next
                ID = 9;

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, style_config]
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
        if not isinstance(request, map_management_service.CreateStyleConfigRequest):
            request = map_management_service.CreateStyleConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if style_config is not None:
            request.style_config = style_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_style_config
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

    async def get_style_config(
        self,
        request: Optional[
            Union[map_management_service.GetStyleConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.StyleConfig:
        r"""Gets a StyleConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_get_style_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.GetStyleConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_style_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.GetStyleConfigRequest, dict]]):
                The request object. Request to get a StyleConfig.
            name (:class:`str`):
                Required. Resource name of the StyleConfig. Format:
                ``projects/{project}/styleConfigs/{style_config}``

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
            google.maps.mapmanagement_v2beta.types.StyleConfig:
                Represents a single style in a Maps
                API client application. The StyleConfig
                contains the style sheet that defines
                the visual appearance of the map. Next
                ID = 9;

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
        if not isinstance(request, map_management_service.GetStyleConfigRequest):
            request = map_management_service.GetStyleConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_style_config
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

    async def list_style_configs(
        self,
        request: Optional[
            Union[map_management_service.ListStyleConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListStyleConfigsAsyncPager:
        r"""Lists StyleConfigs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_list_style_configs():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.ListStyleConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_style_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.ListStyleConfigsRequest, dict]]):
                The request object. Request to list StyleConfigs.
            parent (:class:`str`):
                Required. Parent project that owns the StyleConfigs.
                Format: ``projects/{project}``

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
            google.maps.mapmanagement_v2beta.services.map_management.pagers.ListStyleConfigsAsyncPager:
                Response to list StyleConfigs.

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
        if not isinstance(request, map_management_service.ListStyleConfigsRequest):
            request = map_management_service.ListStyleConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_style_configs
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
        response = pagers.ListStyleConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_style_config(
        self,
        request: Optional[
            Union[map_management_service.UpdateStyleConfigRequest, dict]
        ] = None,
        *,
        style_config: Optional[map_management_service.StyleConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.StyleConfig:
        r"""Updates a StyleConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_update_style_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.UpdateStyleConfigRequest(
                )

                # Make the request
                response = await client.update_style_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.UpdateStyleConfigRequest, dict]]):
                The request object. Request to update a StyleConfig.
            style_config (:class:`google.maps.mapmanagement_v2beta.types.StyleConfig`):
                Required. The StyleConfig to update.

                The StyleConfig's ``name`` field is used to identify the
                StyleConfig to update. Format:
                ``projects/{project}/styleConfigs/{style_config}``

                This corresponds to the ``style_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to update. If not
                specified, the StyleConfig will be updated in its
                entirety. Valid fields are:

                - ``display_name``
                - ``description``
                - ``json_style_sheet``

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
            google.maps.mapmanagement_v2beta.types.StyleConfig:
                Represents a single style in a Maps
                API client application. The StyleConfig
                contains the style sheet that defines
                the visual appearance of the map. Next
                ID = 9;

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [style_config, update_mask]
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
        if not isinstance(request, map_management_service.UpdateStyleConfigRequest):
            request = map_management_service.UpdateStyleConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if style_config is not None:
            request.style_config = style_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_style_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("style_config.name", request.style_config.name),)
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

    async def delete_style_config(
        self,
        request: Optional[
            Union[map_management_service.DeleteStyleConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a StyleConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_delete_style_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.DeleteStyleConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_style_config(request=request)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.DeleteStyleConfigRequest, dict]]):
                The request object. Request to delete a StyleConfig.
            name (:class:`str`):
                Required. Resource name of the StyleConfig to delete.
                Format:
                ``projects/{project}/styleConfigs/{style_config}``

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
        if not isinstance(request, map_management_service.DeleteStyleConfigRequest):
            request = map_management_service.DeleteStyleConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_style_config
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

    async def create_map_context_config(
        self,
        request: Optional[
            Union[map_management_service.CreateMapContextConfigRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        map_context_config: Optional[map_management_service.MapContextConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.MapContextConfig:
        r"""Creates a MapContextConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_create_map_context_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                map_context_config = mapmanagement_v2beta.MapContextConfig()
                map_context_config.map_config = "map_config_value"
                map_context_config.style_config = "style_config_value"
                map_context_config.map_variants = ['PHOTOREALISTIC3D']

                request = mapmanagement_v2beta.CreateMapContextConfigRequest(
                    parent="parent_value",
                    map_context_config=map_context_config,
                )

                # Make the request
                response = await client.create_map_context_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.CreateMapContextConfigRequest, dict]]):
                The request object. Request to create a MapContextConfig.
            parent (:class:`str`):
                Required. Parent MapConfig that will own the
                MapContextConfig. Format:
                ``projects/{project}/mapConfigs/{map_config}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            map_context_config (:class:`google.maps.mapmanagement_v2beta.types.MapContextConfig`):
                Required. The MapContextConfig to
                create.

                This corresponds to the ``map_context_config`` field
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
            google.maps.mapmanagement_v2beta.types.MapContextConfig:
                Encapsulates the styling
                configuration for a map. The
                MapContextConfig associates styling
                components, such as a StyleConfig and
                Datasets, with specific map variants of
                a MapConfig. When the MapConfig is
                loaded in an SDK, the styling and
                dataset information from the
                MapContextConfig are applied to the
                specified map variants.
                Next ID = 10;

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, map_context_config]
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
            request, map_management_service.CreateMapContextConfigRequest
        ):
            request = map_management_service.CreateMapContextConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if map_context_config is not None:
            request.map_context_config = map_context_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_map_context_config
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

    async def get_map_context_config(
        self,
        request: Optional[
            Union[map_management_service.GetMapContextConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.MapContextConfig:
        r"""Gets a MapContextConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_get_map_context_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.GetMapContextConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_map_context_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.GetMapContextConfigRequest, dict]]):
                The request object. Request to get a MapContextConfig.
            name (:class:`str`):
                Required. Resource name of the MapContextConfig. Format:
                ``projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}``

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
            google.maps.mapmanagement_v2beta.types.MapContextConfig:
                Encapsulates the styling
                configuration for a map. The
                MapContextConfig associates styling
                components, such as a StyleConfig and
                Datasets, with specific map variants of
                a MapConfig. When the MapConfig is
                loaded in an SDK, the styling and
                dataset information from the
                MapContextConfig are applied to the
                specified map variants.
                Next ID = 10;

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
        if not isinstance(request, map_management_service.GetMapContextConfigRequest):
            request = map_management_service.GetMapContextConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_map_context_config
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

    async def list_map_context_configs(
        self,
        request: Optional[
            Union[map_management_service.ListMapContextConfigsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListMapContextConfigsAsyncPager:
        r"""Lists MapContextConfigs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_list_map_context_configs():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.ListMapContextConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_map_context_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.ListMapContextConfigsRequest, dict]]):
                The request object. Request to list MapContextConfigs.
            parent (:class:`str`):
                Required. Parent MapConfig that owns the
                MapContextConfigs. Format:
                ``projects/{project}/mapConfigs/{map_config}``

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
            google.maps.mapmanagement_v2beta.services.map_management.pagers.ListMapContextConfigsAsyncPager:
                Response to list MapContextConfigs.

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
        if not isinstance(request, map_management_service.ListMapContextConfigsRequest):
            request = map_management_service.ListMapContextConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_map_context_configs
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
        response = pagers.ListMapContextConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_map_context_config(
        self,
        request: Optional[
            Union[map_management_service.UpdateMapContextConfigRequest, dict]
        ] = None,
        *,
        map_context_config: Optional[map_management_service.MapContextConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> map_management_service.MapContextConfig:
        r"""Updates a MapContextConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_update_map_context_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                map_context_config = mapmanagement_v2beta.MapContextConfig()
                map_context_config.map_config = "map_config_value"
                map_context_config.style_config = "style_config_value"
                map_context_config.map_variants = ['PHOTOREALISTIC3D']

                request = mapmanagement_v2beta.UpdateMapContextConfigRequest(
                    map_context_config=map_context_config,
                )

                # Make the request
                response = await client.update_map_context_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.UpdateMapContextConfigRequest, dict]]):
                The request object. Request to update a MapContextConfig.
            map_context_config (:class:`google.maps.mapmanagement_v2beta.types.MapContextConfig`):
                Required. The MapContextConfig to update.

                The MapContextConfig's ``name`` field is used to
                identify the MapContextConfig to update. Format:
                ``projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}``

                This corresponds to the ``map_context_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to update. If not
                specified, the MapContextConfig will be updated in its
                entirety. Valid fields are:

                - ``display_name``
                - ``alias``
                - ``map_variants``
                - ``style_config``
                - ``dataset``

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
            google.maps.mapmanagement_v2beta.types.MapContextConfig:
                Encapsulates the styling
                configuration for a map. The
                MapContextConfig associates styling
                components, such as a StyleConfig and
                Datasets, with specific map variants of
                a MapConfig. When the MapConfig is
                loaded in an SDK, the styling and
                dataset information from the
                MapContextConfig are applied to the
                specified map variants.
                Next ID = 10;

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [map_context_config, update_mask]
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
            request, map_management_service.UpdateMapContextConfigRequest
        ):
            request = map_management_service.UpdateMapContextConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if map_context_config is not None:
            request.map_context_config = map_context_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_map_context_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("map_context_config.name", request.map_context_config.name),)
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

    async def delete_map_context_config(
        self,
        request: Optional[
            Union[map_management_service.DeleteMapContextConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a MapContextConfig.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.maps import mapmanagement_v2beta

            async def sample_delete_map_context_config():
                # Create a client
                client = mapmanagement_v2beta.MapManagementAsyncClient()

                # Initialize request argument(s)
                request = mapmanagement_v2beta.DeleteMapContextConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_map_context_config(request=request)

        Args:
            request (Optional[Union[google.maps.mapmanagement_v2beta.types.DeleteMapContextConfigRequest, dict]]):
                The request object. Request to delete a MapContextConfig.
            name (:class:`str`):
                Required. Resource name of the MapContextConfig to
                delete. Format:
                ``projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}``

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
            request, map_management_service.DeleteMapContextConfigRequest
        ):
            request = map_management_service.DeleteMapContextConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_map_context_config
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

    async def __aenter__(self) -> "MapManagementAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("MapManagementAsyncClient",)
