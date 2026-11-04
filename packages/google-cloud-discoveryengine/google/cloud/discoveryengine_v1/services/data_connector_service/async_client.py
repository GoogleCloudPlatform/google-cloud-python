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

from google.cloud.discoveryengine_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.discoveryengine_v1.types import (
    common,
    data_connector,
    data_connector_service,
)
from google.cloud.discoveryengine_v1.types import data_connector as gcd_data_connector

from .client import DataConnectorServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DataConnectorServiceTransport
from .transports.grpc_asyncio import DataConnectorServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DataConnectorServiceAsyncClient:
    """Service for data connector management."""

    _client: DataConnectorServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DataConnectorServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataConnectorServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DataConnectorServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DataConnectorServiceClient._DEFAULT_UNIVERSE

    content_policy_path = staticmethod(DataConnectorServiceClient.content_policy_path)
    parse_content_policy_path = staticmethod(
        DataConnectorServiceClient.parse_content_policy_path
    )
    data_connector_path = staticmethod(DataConnectorServiceClient.data_connector_path)
    parse_data_connector_path = staticmethod(
        DataConnectorServiceClient.parse_data_connector_path
    )
    data_store_path = staticmethod(DataConnectorServiceClient.data_store_path)
    parse_data_store_path = staticmethod(
        DataConnectorServiceClient.parse_data_store_path
    )
    location_path = staticmethod(DataConnectorServiceClient.location_path)
    parse_location_path = staticmethod(DataConnectorServiceClient.parse_location_path)
    schema_path = staticmethod(DataConnectorServiceClient.schema_path)
    parse_schema_path = staticmethod(DataConnectorServiceClient.parse_schema_path)
    service_path = staticmethod(DataConnectorServiceClient.service_path)
    parse_service_path = staticmethod(DataConnectorServiceClient.parse_service_path)
    common_billing_account_path = staticmethod(
        DataConnectorServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataConnectorServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DataConnectorServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DataConnectorServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DataConnectorServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DataConnectorServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DataConnectorServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DataConnectorServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DataConnectorServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DataConnectorServiceClient.parse_common_location_path
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
            DataConnectorServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DataConnectorServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DataConnectorServiceAsyncClient, info, *args, **kwargs)

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
            DataConnectorServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DataConnectorServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DataConnectorServiceAsyncClient, filename, *args, **kwargs)

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
        return DataConnectorServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> DataConnectorServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataConnectorServiceTransport: The transport used by the client instance.
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

    get_transport_class = DataConnectorServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DataConnectorServiceTransport,
                Callable[..., DataConnectorServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data connector service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DataConnectorServiceTransport,Callable[..., DataConnectorServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DataConnectorServiceTransport constructor.
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
        self._client = DataConnectorServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.discoveryengine_v1.DataConnectorServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.discoveryengine.v1.DataConnectorService",
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
                    "serviceName": "google.cloud.discoveryengine.v1.DataConnectorService",
                    "credentialsType": None,
                },
            )

    async def set_up_data_connector(
        self,
        request: Optional[
            Union[data_connector_service.SetUpDataConnectorRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        collection_id: Optional[str] = None,
        collection_display_name: Optional[str] = None,
        data_connector: Optional[gcd_data_connector.DataConnector] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a
        [Collection][google.cloud.discoveryengine.v1.Collection] and
        sets up the
        [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
        for it. To stop a
        [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
        after setup, use the
        [CollectionService.DeleteCollection][google.cloud.discoveryengine.v1.CollectionService.DeleteCollection]
        method.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1

            async def sample_set_up_data_connector():
                # Create a client
                client = discoveryengine_v1.DataConnectorServiceAsyncClient()

                # Initialize request argument(s)
                data_connector = discoveryengine_v1.DataConnector()
                data_connector.data_source = "data_source_value"

                request = discoveryengine_v1.SetUpDataConnectorRequest(
                    parent="parent_value",
                    collection_id="collection_id_value",
                    collection_display_name="collection_display_name_value",
                    data_connector=data_connector,
                )

                # Make the request
                operation = await client.set_up_data_connector(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1.types.SetUpDataConnectorRequest, dict]]):
                The request object. Request for
                [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
                method.
            parent (:class:`str`):
                Required. The parent of
                [Collection][google.cloud.discoveryengine.v1.Collection],
                in the format of
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            collection_id (:class:`str`):
                Required. The ID to use for the
                [Collection][google.cloud.discoveryengine.v1.Collection],
                which will become the final component of the
                [Collection][google.cloud.discoveryengine.v1.Collection]'s
                resource name. A new
                [Collection][google.cloud.discoveryengine.v1.Collection]
                is created as part of the
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                setup.
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                is a singleton resource under
                [Collection][google.cloud.discoveryengine.v1.Collection],
                managing all
                [DataStore][google.cloud.discoveryengine.v1.DataStore]s
                of the
                [Collection][google.cloud.discoveryengine.v1.Collection].

                Should conform to
                `RFC-1034 <https://tools.ietf.org/html/rfc1034>`__
                standard with a length limit of 63 characters.
                Otherwise, an ``INVALID_ARGUMENT`` error is returned.

                This corresponds to the ``collection_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            collection_display_name (:class:`str`):
                Required. The display name of the
                [Collection][google.cloud.discoveryengine.v1.Collection].

                Should be human readable, used to display collections in
                the Console Dashboard. UTF-8 encoded string with limit
                of 1024 characters.

                This corresponds to the ``collection_display_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            data_connector (:class:`google.cloud.discoveryengine_v1.types.DataConnector`):
                Required. The
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                to initialize in the newly created
                [Collection][google.cloud.discoveryengine.v1.Collection].

                This corresponds to the ``data_connector`` field
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

                The result type for the operation will be :class:`google.cloud.discoveryengine_v1.types.DataConnector` Manages the connection to external data sources for all data stores grouped
                   under a
                   [Collection][google.cloud.discoveryengine.v1.Collection].
                   It's a singleton resource of
                   [Collection][google.cloud.discoveryengine.v1.Collection].
                   The initialization is only supported through
                   [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
                   method, which will create a new
                   [Collection][google.cloud.discoveryengine.v1.Collection]
                   and initialize its
                   [DataConnector][google.cloud.discoveryengine.v1.DataConnector].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            collection_id,
            collection_display_name,
            data_connector,
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
        if not isinstance(request, data_connector_service.SetUpDataConnectorRequest):
            request = data_connector_service.SetUpDataConnectorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if collection_id is not None:
            request.collection_id = collection_id
        if collection_display_name is not None:
            request.collection_display_name = collection_display_name
        if data_connector is not None:
            request.data_connector = data_connector

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.set_up_data_connector
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
            gcd_data_connector.DataConnector,
            metadata_type=data_connector_service.SetUpDataConnectorMetadata,
        )

        # Done; return the response.
        return response

    async def get_data_connector(
        self,
        request: Optional[
            Union[data_connector_service.GetDataConnectorRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> data_connector.DataConnector:
        r"""Gets the
        [DataConnector][google.cloud.discoveryengine.v1.DataConnector].
        [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
        is a singleton resource for each
        [Collection][google.cloud.discoveryengine.v1.Collection].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1

            async def sample_get_data_connector():
                # Create a client
                client = discoveryengine_v1.DataConnectorServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1.GetDataConnectorRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_data_connector(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1.types.GetDataConnectorRequest, dict]]):
                The request object. Request for
                [DataConnectorService.GetDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector]
                method.
            name (:class:`str`):
                Required. Full resource name of
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector],
                such as
                ``projects/{project}/locations/{location}/collections/{collection_id}/dataConnector``.

                If the caller does not have permission to access the
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector],
                regardless of whether or not it exists, a
                ``PERMISSION_DENIED`` error is returned.

                If the requested
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                does not exist, a ``NOT_FOUND`` error is returned.

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
            google.cloud.discoveryengine_v1.types.DataConnector:
                Manages the connection to external data sources for all data stores grouped
                   under a
                   [Collection][google.cloud.discoveryengine.v1.Collection].
                   It's a singleton resource of
                   [Collection][google.cloud.discoveryengine.v1.Collection].
                   The initialization is only supported through
                   [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
                   method, which will create a new
                   [Collection][google.cloud.discoveryengine.v1.Collection]
                   and initialize its
                   [DataConnector][google.cloud.discoveryengine.v1.DataConnector].

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
        if not isinstance(request, data_connector_service.GetDataConnectorRequest):
            request = data_connector_service.GetDataConnectorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_data_connector
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

    async def update_data_connector(
        self,
        request: Optional[
            Union[data_connector_service.UpdateDataConnectorRequest, dict]
        ] = None,
        *,
        data_connector: Optional[gcd_data_connector.DataConnector] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_data_connector.DataConnector:
        r"""Updates a
        [DataConnector][google.cloud.discoveryengine.v1.DataConnector].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1

            async def sample_update_data_connector():
                # Create a client
                client = discoveryengine_v1.DataConnectorServiceAsyncClient()

                # Initialize request argument(s)
                data_connector = discoveryengine_v1.DataConnector()
                data_connector.data_source = "data_source_value"

                request = discoveryengine_v1.UpdateDataConnectorRequest(
                    data_connector=data_connector,
                )

                # Make the request
                response = await client.update_data_connector(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1.types.UpdateDataConnectorRequest, dict]]):
                The request object. Request message for
                [DataConnectorService.UpdateDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector]
                method.
            data_connector (:class:`google.cloud.discoveryengine_v1.types.DataConnector`):
                Required. The
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                to update.

                If the caller does not have permission to update the
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector],
                regardless of whether or not it exists, a
                ``PERMISSION_DENIED`` error is returned.

                If the
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                does not exist, a ``NOT_FOUND`` error is returned.

                This corresponds to the ``data_connector`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which fields in the provided
                [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
                to update.

                Supported field paths include:

                - ``refresh_interval``
                - ``params``
                - ``auto_run_disabled``
                - ``action_config``
                - ``action_config.action_params``
                - ``action_config.service_name``
                - ``destination_configs``
                - ``blocking_reasons``
                - ``sync_mode``
                - ``incremental_sync_disabled``
                - ``incremental_refresh_interval``
                - ``data_protection_policy``

                Note: Support for these fields may vary depending on the
                connector type. For example, not all connectors support
                ``destination_configs``.

                If an unsupported or unknown field path is provided, the
                request will return an ``INVALID_ARGUMENT`` error.

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
            google.cloud.discoveryengine_v1.types.DataConnector:
                Manages the connection to external data sources for all data stores grouped
                   under a
                   [Collection][google.cloud.discoveryengine.v1.Collection].
                   It's a singleton resource of
                   [Collection][google.cloud.discoveryengine.v1.Collection].
                   The initialization is only supported through
                   [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
                   method, which will create a new
                   [Collection][google.cloud.discoveryengine.v1.Collection]
                   and initialize its
                   [DataConnector][google.cloud.discoveryengine.v1.DataConnector].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [data_connector, update_mask]
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
        if not isinstance(request, data_connector_service.UpdateDataConnectorRequest):
            request = data_connector_service.UpdateDataConnectorRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if data_connector is not None:
            request.data_connector = data_connector
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_data_connector
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("data_connector.name", request.data_connector.name),)
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

    async def __aenter__(self) -> "DataConnectorServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DataConnectorServiceAsyncClient",)
