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

from google.cloud.bigquery_datatransfer_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore

from google.cloud.bigquery_datatransfer_v1.services.data_transfer_service import pagers
from google.cloud.bigquery_datatransfer_v1.types import datatransfer, transfer

from .client import DataTransferServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DataTransferServiceTransport
from .transports.grpc_asyncio import DataTransferServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DataTransferServiceAsyncClient:
    """This API allows users to manage their data transfers into
    BigQuery.
    """

    _client: DataTransferServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DataTransferServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataTransferServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DataTransferServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DataTransferServiceClient._DEFAULT_UNIVERSE

    data_source_path = staticmethod(DataTransferServiceClient.data_source_path)
    parse_data_source_path = staticmethod(
        DataTransferServiceClient.parse_data_source_path
    )
    run_path = staticmethod(DataTransferServiceClient.run_path)
    parse_run_path = staticmethod(DataTransferServiceClient.parse_run_path)
    transfer_config_path = staticmethod(DataTransferServiceClient.transfer_config_path)
    parse_transfer_config_path = staticmethod(
        DataTransferServiceClient.parse_transfer_config_path
    )
    common_billing_account_path = staticmethod(
        DataTransferServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataTransferServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DataTransferServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DataTransferServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DataTransferServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DataTransferServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DataTransferServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DataTransferServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DataTransferServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DataTransferServiceClient.parse_common_location_path
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
            DataTransferServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DataTransferServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DataTransferServiceAsyncClient, info, *args, **kwargs)

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
            DataTransferServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DataTransferServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DataTransferServiceAsyncClient, filename, *args, **kwargs)

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
        return DataTransferServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> DataTransferServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataTransferServiceTransport: The transport used by the client instance.
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

    get_transport_class = DataTransferServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DataTransferServiceTransport,
                Callable[..., DataTransferServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data transfer service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DataTransferServiceTransport,Callable[..., DataTransferServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DataTransferServiceTransport constructor.
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
        self._client = DataTransferServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.bigquery.datatransfer_v1.DataTransferServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
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
                    "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                    "credentialsType": None,
                },
            )

    async def get_data_source(
        self,
        request: Optional[Union[datatransfer.GetDataSourceRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datatransfer.DataSource:
        r"""Retrieves a supported data source and returns its
        settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_get_data_source():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.GetDataSourceRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_data_source(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.GetDataSourceRequest, dict]]):
                The request object. A request to get data source info.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/dataSources/{data_source_id}``
                or
                ``projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}``

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
            google.cloud.bigquery_datatransfer_v1.types.DataSource:
                Defines the properties and custom
                parameters for a data source.

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
        if not isinstance(request, datatransfer.GetDataSourceRequest):
            request = datatransfer.GetDataSourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_data_source
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

    async def list_data_sources(
        self,
        request: Optional[Union[datatransfer.ListDataSourcesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDataSourcesAsyncPager:
        r"""Lists supported data sources and returns their
        settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_list_data_sources():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListDataSourcesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_data_sources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.ListDataSourcesRequest, dict]]):
                The request object. Request to list supported data
                sources and their data transfer
                settings.
            parent (:class:`str`):
                Required. The BigQuery project id for which data sources
                should be returned. Must be in the form:
                ``projects/{project_id}`` or
                ``projects/{project_id}/locations/{location_id}``

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
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListDataSourcesAsyncPager:
                Returns list of supported data
                sources and their metadata.
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
        if not isinstance(request, datatransfer.ListDataSourcesRequest):
            request = datatransfer.ListDataSourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_data_sources
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
        response = pagers.ListDataSourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_transfer_config(
        self,
        request: Optional[Union[datatransfer.CreateTransferConfigRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        transfer_config: Optional[transfer.TransferConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> transfer.TransferConfig:
        r"""Creates a new data transfer configuration.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_create_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                transfer_config = bigquery_datatransfer_v1.TransferConfig()
                transfer_config.destination_dataset_id = "destination_dataset_id_value"

                request = bigquery_datatransfer_v1.CreateTransferConfigRequest(
                    parent="parent_value",
                    transfer_config=transfer_config,
                )

                # Make the request
                response = await client.create_transfer_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.CreateTransferConfigRequest, dict]]):
                The request object. A request to create a data transfer configuration. If
                new credentials are needed for this transfer
                configuration, authorization info must be provided. If
                authorization info is provided, the transfer
                configuration will be associated with the user id
                corresponding to the authorization info. Otherwise, the
                transfer configuration will be associated with the
                calling user.

                When using a cross project service account for creating
                a transfer config, you must enable cross project service
                account usage. For more information, see `Disable
                attachment of service accounts to resources in other
                projects <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts>`__.
            parent (:class:`str`):
                Required. The BigQuery project id where the transfer
                configuration should be created. Must be in the format
                projects/{project_id}/locations/{location_id} or
                projects/{project_id}. If specified location and
                location of the destination bigquery dataset do not
                match - the request will fail.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            transfer_config (:class:`google.cloud.bigquery_datatransfer_v1.types.TransferConfig`):
                Required. Data transfer configuration
                to create.

                This corresponds to the ``transfer_config`` field
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
            google.cloud.bigquery_datatransfer_v1.types.TransferConfig:
                Represents a data transfer configuration. A transfer configuration
                   contains all metadata needed to perform a data
                   transfer. For example, destination_dataset_id
                   specifies where data should be stored. When a new
                   transfer configuration is created, the specified
                   destination_dataset_id is created when needed and
                   shared with the appropriate data source service
                   account.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, transfer_config]
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
        if not isinstance(request, datatransfer.CreateTransferConfigRequest):
            request = datatransfer.CreateTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if transfer_config is not None:
            request.transfer_config = transfer_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_transfer_config
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

    async def update_transfer_config(
        self,
        request: Optional[Union[datatransfer.UpdateTransferConfigRequest, dict]] = None,
        *,
        transfer_config: Optional[transfer.TransferConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> transfer.TransferConfig:
        r"""Updates a data transfer configuration.
        All fields must be set, even if they are not updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_update_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                transfer_config = bigquery_datatransfer_v1.TransferConfig()
                transfer_config.destination_dataset_id = "destination_dataset_id_value"

                request = bigquery_datatransfer_v1.UpdateTransferConfigRequest(
                    transfer_config=transfer_config,
                )

                # Make the request
                response = await client.update_transfer_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.UpdateTransferConfigRequest, dict]]):
                The request object. A request to update a transfer configuration. To update
                the user id of the transfer configuration, authorization
                info needs to be provided.

                When using a cross project service account for updating
                a transfer config, you must enable cross project service
                account usage. For more information, see `Disable
                attachment of service accounts to resources in other
                projects <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts>`__.
            transfer_config (:class:`google.cloud.bigquery_datatransfer_v1.types.TransferConfig`):
                Required. Data transfer configuration
                to create.

                This corresponds to the ``transfer_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Required list of fields to
                be updated in this request.

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
            google.cloud.bigquery_datatransfer_v1.types.TransferConfig:
                Represents a data transfer configuration. A transfer configuration
                   contains all metadata needed to perform a data
                   transfer. For example, destination_dataset_id
                   specifies where data should be stored. When a new
                   transfer configuration is created, the specified
                   destination_dataset_id is created when needed and
                   shared with the appropriate data source service
                   account.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [transfer_config, update_mask]
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
        if not isinstance(request, datatransfer.UpdateTransferConfigRequest):
            request = datatransfer.UpdateTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if transfer_config is not None:
            request.transfer_config = transfer_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_transfer_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("transfer_config.name", request.transfer_config.name),)
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

    async def delete_transfer_config(
        self,
        request: Optional[Union[datatransfer.DeleteTransferConfigRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a data transfer configuration, including any
        associated transfer runs and logs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_delete_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.DeleteTransferConfigRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_transfer_config(request=request)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.DeleteTransferConfigRequest, dict]]):
                The request object. A request to delete data transfer
                information. All associated transfer
                runs and log messages will be deleted as
                well.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``

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
        if not isinstance(request, datatransfer.DeleteTransferConfigRequest):
            request = datatransfer.DeleteTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_transfer_config
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

    async def get_transfer_config(
        self,
        request: Optional[Union[datatransfer.GetTransferConfigRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> transfer.TransferConfig:
        r"""Returns information about a data transfer config.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_get_transfer_config():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.GetTransferConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_transfer_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.GetTransferConfigRequest, dict]]):
                The request object. A request to get data transfer
                information.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``

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
            google.cloud.bigquery_datatransfer_v1.types.TransferConfig:
                Represents a data transfer configuration. A transfer configuration
                   contains all metadata needed to perform a data
                   transfer. For example, destination_dataset_id
                   specifies where data should be stored. When a new
                   transfer configuration is created, the specified
                   destination_dataset_id is created when needed and
                   shared with the appropriate data source service
                   account.

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
        if not isinstance(request, datatransfer.GetTransferConfigRequest):
            request = datatransfer.GetTransferConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_transfer_config
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

    async def list_transfer_configs(
        self,
        request: Optional[Union[datatransfer.ListTransferConfigsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTransferConfigsAsyncPager:
        r"""Returns information about all transfer configs owned
        by a project in the specified location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_list_transfer_configs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListTransferConfigsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transfer_configs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.ListTransferConfigsRequest, dict]]):
                The request object. A request to list data transfers
                configured for a BigQuery project.
            parent (:class:`str`):
                Required. The BigQuery project id for which transfer
                configs should be returned: ``projects/{project_id}`` or
                ``projects/{project_id}/locations/{location_id}``

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
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListTransferConfigsAsyncPager:
                The returned list of pipelines in the
                project.
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
        if not isinstance(request, datatransfer.ListTransferConfigsRequest):
            request = datatransfer.ListTransferConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_transfer_configs
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
        response = pagers.ListTransferConfigsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def schedule_transfer_runs(
        self,
        request: Optional[Union[datatransfer.ScheduleTransferRunsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        start_time: Optional[timestamp_pb2.Timestamp] = None,
        end_time: Optional[timestamp_pb2.Timestamp] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datatransfer.ScheduleTransferRunsResponse:
        r"""Creates transfer runs for a time range [start_time, end_time].
        For each date - or whatever granularity the data source supports
        - in the range, one transfer run is created. Note that runs are
        created per UTC time in the time range. DEPRECATED: use
        StartManualTransferRuns instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_schedule_transfer_runs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ScheduleTransferRunsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.schedule_transfer_runs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.ScheduleTransferRunsRequest, dict]]):
                The request object. A request to schedule transfer runs
                for a time range.
            parent (:class:`str`):
                Required. Transfer configuration name in the form:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            start_time (:class:`google.protobuf.timestamp_pb2.Timestamp`):
                Required. Start time of the range of transfer runs. For
                example, ``"2017-05-25T00:00:00+00:00"``.

                This corresponds to the ``start_time`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            end_time (:class:`google.protobuf.timestamp_pb2.Timestamp`):
                Required. End time of the range of transfer runs. For
                example, ``"2017-05-30T00:00:00+00:00"``.

                This corresponds to the ``end_time`` field
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
            google.cloud.bigquery_datatransfer_v1.types.ScheduleTransferRunsResponse:
                A response to schedule transfer runs
                for a time range.

        """
        warnings.warn(
            "DataTransferServiceAsyncClient.schedule_transfer_runs is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, start_time, end_time]
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
        if not isinstance(request, datatransfer.ScheduleTransferRunsRequest):
            request = datatransfer.ScheduleTransferRunsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if start_time is not None:
            request.start_time = start_time
        if end_time is not None:
            request.end_time = end_time

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.schedule_transfer_runs
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

    async def start_manual_transfer_runs(
        self,
        request: Optional[
            Union[datatransfer.StartManualTransferRunsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datatransfer.StartManualTransferRunsResponse:
        r"""Start manual transfer runs to be executed now with schedule_time
        equal to current time. The transfer runs can be created for a
        time range where the run_time is between start_time (inclusive)
        and end_time (exclusive), or for a specific run_time.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_start_manual_transfer_runs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.StartManualTransferRunsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.start_manual_transfer_runs(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.StartManualTransferRunsRequest, dict]]):
                The request object. A request to start manual transfer
                runs.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.bigquery_datatransfer_v1.types.StartManualTransferRunsResponse:
                A response to start manual transfer
                runs.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, datatransfer.StartManualTransferRunsRequest):
            request = datatransfer.StartManualTransferRunsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.start_manual_transfer_runs
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

    async def get_transfer_run(
        self,
        request: Optional[Union[datatransfer.GetTransferRunRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> transfer.TransferRun:
        r"""Returns information about the particular transfer
        run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_get_transfer_run():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.GetTransferRunRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_transfer_run(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.GetTransferRunRequest, dict]]):
                The request object. A request to get data transfer run
                information.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
                or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``

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
            google.cloud.bigquery_datatransfer_v1.types.TransferRun:
                Represents a data transfer run.
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
        if not isinstance(request, datatransfer.GetTransferRunRequest):
            request = datatransfer.GetTransferRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_transfer_run
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

    async def delete_transfer_run(
        self,
        request: Optional[Union[datatransfer.DeleteTransferRunRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified transfer run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_delete_transfer_run():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.DeleteTransferRunRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_transfer_run(request=request)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.DeleteTransferRunRequest, dict]]):
                The request object. A request to delete data transfer run
                information.
            name (:class:`str`):
                Required. The field will contain name of the resource
                requested, for example:
                ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
                or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``

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
        if not isinstance(request, datatransfer.DeleteTransferRunRequest):
            request = datatransfer.DeleteTransferRunRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_transfer_run
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

    async def list_transfer_runs(
        self,
        request: Optional[Union[datatransfer.ListTransferRunsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTransferRunsAsyncPager:
        r"""Returns information about running and completed
        transfer runs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_list_transfer_runs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListTransferRunsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transfer_runs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.ListTransferRunsRequest, dict]]):
                The request object. A request to list data transfer runs.
            parent (:class:`str`):
                Required. Name of transfer configuration for which
                transfer runs should be retrieved. Format of transfer
                configuration resource name is:
                ``projects/{project_id}/transferConfigs/{config_id}`` or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}``.

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
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListTransferRunsAsyncPager:
                The returned list of pipelines in the
                project.
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
        if not isinstance(request, datatransfer.ListTransferRunsRequest):
            request = datatransfer.ListTransferRunsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_transfer_runs
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
        response = pagers.ListTransferRunsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_transfer_logs(
        self,
        request: Optional[Union[datatransfer.ListTransferLogsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTransferLogsAsyncPager:
        r"""Returns log messages for the transfer run.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_list_transfer_logs():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.ListTransferLogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_transfer_logs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.ListTransferLogsRequest, dict]]):
                The request object. A request to get user facing log
                messages associated with data transfer
                run.
            parent (:class:`str`):
                Required. Transfer run name in the form:
                ``projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}``
                or
                ``projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}``

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
            google.cloud.bigquery_datatransfer_v1.services.data_transfer_service.pagers.ListTransferLogsAsyncPager:
                The returned list transfer run
                messages.
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
        if not isinstance(request, datatransfer.ListTransferLogsRequest):
            request = datatransfer.ListTransferLogsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_transfer_logs
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
        response = pagers.ListTransferLogsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def check_valid_creds(
        self,
        request: Optional[Union[datatransfer.CheckValidCredsRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datatransfer.CheckValidCredsResponse:
        r"""Returns true if valid credentials exist for the given
        data source and requesting user.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_check_valid_creds():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.CheckValidCredsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.check_valid_creds(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.CheckValidCredsRequest, dict]]):
                The request object. A request to determine whether the
                user has valid credentials. This method
                is used to limit the number of OAuth
                popups in the user interface. The user
                id is inferred from the API call
                context. If the data source has the
                Google+ authorization type, this method
                returns false, as it cannot be
                determined whether the credentials are
                already valid merely based on the user
                id.
            name (:class:`str`):
                Required. The data source in the form:
                ``projects/{project_id}/dataSources/{data_source_id}``
                or
                ``projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}``.

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
            google.cloud.bigquery_datatransfer_v1.types.CheckValidCredsResponse:
                A response indicating whether the
                credentials exist and are valid.

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
        if not isinstance(request, datatransfer.CheckValidCredsRequest):
            request = datatransfer.CheckValidCredsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.check_valid_creds
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

    async def enroll_data_sources(
        self,
        request: Optional[Union[datatransfer.EnrollDataSourcesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Enroll data sources in a user project. This allows users to
        create transfer configurations for these data sources. They will
        also appear in the ListDataSources RPC and as such, will appear
        in the `BigQuery
        UI <https://console.cloud.google.com/bigquery>`__, and the
        documents can be found in the public guide for `BigQuery Web
        UI <https://cloud.google.com/bigquery/bigquery-web-ui>`__ and
        `Data Transfer
        Service <https://cloud.google.com/bigquery/docs/working-with-transfers>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_enroll_data_sources():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.EnrollDataSourcesRequest(
                    name="name_value",
                )

                # Make the request
                await client.enroll_data_sources(request=request)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.EnrollDataSourcesRequest, dict]]):
                The request object. A request to enroll a set of data sources so they are
                visible in the BigQuery UI's ``Transfer`` tab.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, datatransfer.EnrollDataSourcesRequest):
            request = datatransfer.EnrollDataSourcesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.enroll_data_sources
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

    async def unenroll_data_sources(
        self,
        request: Optional[Union[datatransfer.UnenrollDataSourcesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Unenroll data sources in a user project. This allows users to
        remove transfer configurations for these data sources. They will
        no longer appear in the ListDataSources RPC and will also no
        longer appear in the `BigQuery
        UI <https://console.cloud.google.com/bigquery>`__. Data
        transfers configurations of unenrolled data sources will not be
        scheduled.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import bigquery_datatransfer_v1

            async def sample_unenroll_data_sources():
                # Create a client
                client = bigquery_datatransfer_v1.DataTransferServiceAsyncClient()

                # Initialize request argument(s)
                request = bigquery_datatransfer_v1.UnenrollDataSourcesRequest(
                    name="name_value",
                )

                # Make the request
                await client.unenroll_data_sources(request=request)

        Args:
            request (Optional[Union[google.cloud.bigquery_datatransfer_v1.types.UnenrollDataSourcesRequest, dict]]):
                The request object. A request to unenroll a set of data sources so they are
                no longer visible in the BigQuery UI's ``Transfer`` tab.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, datatransfer.UnenrollDataSourcesRequest):
            request = datatransfer.UnenrollDataSourcesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.unenroll_data_sources
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

    async def __aenter__(self) -> "DataTransferServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DataTransferServiceAsyncClient",)
