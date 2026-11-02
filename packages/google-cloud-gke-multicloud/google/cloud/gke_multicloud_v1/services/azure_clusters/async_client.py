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

from google.cloud.gke_multicloud_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.gke_multicloud_v1.services.azure_clusters import pagers
from google.cloud.gke_multicloud_v1.types import (
    azure_resources,
    azure_service,
    common_resources,
)

from .client import AzureClustersClient
from .transports.base import DEFAULT_CLIENT_INFO, AzureClustersTransport
from .transports.grpc_asyncio import AzureClustersGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AzureClustersAsyncClient:
    """The AzureClusters API provides a single centrally managed
    service to create and manage Anthos clusters that run on Azure
    infrastructure.
    """

    _client: AzureClustersClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AzureClustersClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AzureClustersClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AzureClustersClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AzureClustersClient._DEFAULT_UNIVERSE

    azure_client_path = staticmethod(AzureClustersClient.azure_client_path)
    parse_azure_client_path = staticmethod(AzureClustersClient.parse_azure_client_path)
    azure_cluster_path = staticmethod(AzureClustersClient.azure_cluster_path)
    parse_azure_cluster_path = staticmethod(
        AzureClustersClient.parse_azure_cluster_path
    )
    azure_node_pool_path = staticmethod(AzureClustersClient.azure_node_pool_path)
    parse_azure_node_pool_path = staticmethod(
        AzureClustersClient.parse_azure_node_pool_path
    )
    azure_server_config_path = staticmethod(
        AzureClustersClient.azure_server_config_path
    )
    parse_azure_server_config_path = staticmethod(
        AzureClustersClient.parse_azure_server_config_path
    )
    common_billing_account_path = staticmethod(
        AzureClustersClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AzureClustersClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AzureClustersClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        AzureClustersClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        AzureClustersClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        AzureClustersClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AzureClustersClient.common_project_path)
    parse_common_project_path = staticmethod(
        AzureClustersClient.parse_common_project_path
    )
    common_location_path = staticmethod(AzureClustersClient.common_location_path)
    parse_common_location_path = staticmethod(
        AzureClustersClient.parse_common_location_path
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
            AzureClustersAsyncClient: The constructed client.
        """
        sa_info_func = (
            AzureClustersClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AzureClustersAsyncClient, info, *args, **kwargs)

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
            AzureClustersAsyncClient: The constructed client.
        """
        sa_file_func = (
            AzureClustersClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(AzureClustersAsyncClient, filename, *args, **kwargs)

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
        return AzureClustersClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AzureClustersTransport:
        """Returns the transport used by the client instance.

        Returns:
            AzureClustersTransport: The transport used by the client instance.
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

    get_transport_class = AzureClustersClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, AzureClustersTransport, Callable[..., AzureClustersTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the azure clusters async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AzureClustersTransport,Callable[..., AzureClustersTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AzureClustersTransport constructor.
                If set to None, a transport is chosen automatically.
                NOTE: "rest" transport functionality is currently in a
                beta state (preview). We welcome your feedback via an
                issue in this library's source repository.
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
        self._client = AzureClustersClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.gkemulticloud_v1.AzureClustersAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.gkemulticloud.v1.AzureClusters",
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
                    "serviceName": "google.cloud.gkemulticloud.v1.AzureClusters",
                    "credentialsType": None,
                },
            )

    async def create_azure_client(
        self,
        request: Optional[Union[azure_service.CreateAzureClientRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        azure_client: Optional[azure_resources.AzureClient] = None,
        azure_client_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resource on a given Google Cloud project and region.

        ``AzureClient`` resources hold client authentication information
        needed by the Anthos Multicloud API to manage Azure resources on
        your Azure subscription on your behalf.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_create_azure_client():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                azure_client = gke_multicloud_v1.AzureClient()
                azure_client.tenant_id = "tenant_id_value"
                azure_client.application_id = "application_id_value"

                request = gke_multicloud_v1.CreateAzureClientRequest(
                    parent="parent_value",
                    azure_client=azure_client,
                    azure_client_id="azure_client_id_value",
                )

                # Make the request
                operation = await client.create_azure_client(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.CreateAzureClientRequest, dict]]):
                The request object. Request message for ``AzureClusters.CreateAzureClient``
                method.
            parent (:class:`str`):
                Required. The parent location where this
                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                resource will be created.

                Location names are formatted as
                ``projects/<project-id>/locations/<region>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            azure_client (:class:`google.cloud.gke_multicloud_v1.types.AzureClient`):
                Required. The specification of the
                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                to create.

                This corresponds to the ``azure_client`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            azure_client_id (:class:`str`):
                Required. A client provided ID the resource. Must be
                unique within the parent resource.

                The provided ID will be part of the
                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                resource name formatted as
                ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

                Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
                than 63 characters.

                This corresponds to the ``azure_client_id`` field
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

                The result type for the operation will be :class:`google.cloud.gke_multicloud_v1.types.AzureClient` AzureClient resources hold client authentication information needed by the
                   Anthos Multi-Cloud API to manage Azure resources on
                   your Azure subscription.

                   When an
                   [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                   is created, an AzureClient resource needs to be
                   provided and all operations on Azure resources
                   associated to that cluster will authenticate to Azure
                   services using the given client.

                   AzureClient resources are immutable and cannot be
                   modified upon creation.

                   Each AzureClient resource is bound to a single Azure
                   Active Directory Application and tenant.

        """
        warnings.warn(
            "AzureClustersAsyncClient.create_azure_client is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, azure_client, azure_client_id]
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
        if not isinstance(request, azure_service.CreateAzureClientRequest):
            request = azure_service.CreateAzureClientRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if azure_client is not None:
            request.azure_client = azure_client
        if azure_client_id is not None:
            request.azure_client_id = azure_client_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_azure_client
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
            azure_resources.AzureClient,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_azure_client(
        self,
        request: Optional[Union[azure_service.GetAzureClientRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_resources.AzureClient:
        r"""Describes a specific
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_azure_client():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAzureClientRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_azure_client(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAzureClientRequest, dict]]):
                The request object. Request message for ``AzureClusters.GetAzureClient``
                method.
            name (:class:`str`):
                Required. The name of the
                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                resource to describe.

                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                names are formatted as
                ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.cloud.gke_multicloud_v1.types.AzureClient:
                AzureClient resources hold client authentication information needed by the
                   Anthos Multi-Cloud API to manage Azure resources on
                   your Azure subscription.

                   When an
                   [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                   is created, an AzureClient resource needs to be
                   provided and all operations on Azure resources
                   associated to that cluster will authenticate to Azure
                   services using the given client.

                   AzureClient resources are immutable and cannot be
                   modified upon creation.

                   Each AzureClient resource is bound to a single Azure
                   Active Directory Application and tenant.

        """
        warnings.warn(
            "AzureClustersAsyncClient.get_azure_client is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, azure_service.GetAzureClientRequest):
            request = azure_service.GetAzureClientRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_azure_client
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

    async def list_azure_clients(
        self,
        request: Optional[Union[azure_service.ListAzureClientsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAzureClientsAsyncPager:
        r"""Lists all
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resources on a given Google Cloud project and region.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_list_azure_clients():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.ListAzureClientsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_azure_clients(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.ListAzureClientsRequest, dict]]):
                The request object. Request message for ``AzureClusters.ListAzureClients``
                method.
            parent (:class:`str`):
                Required. The parent location which owns this collection
                of
                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                resources.

                Location names are formatted as
                ``projects/<project-id>/locations/<region>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud Platform resource
                names.

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
            google.cloud.gke_multicloud_v1.services.azure_clusters.pagers.ListAzureClientsAsyncPager:
                Response message for AzureClusters.ListAzureClients
                method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "AzureClustersAsyncClient.list_azure_clients is deprecated",
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
        if not isinstance(request, azure_service.ListAzureClientsRequest):
            request = azure_service.ListAzureClientsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_azure_clients
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
        response = pagers.ListAzureClientsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_azure_client(
        self,
        request: Optional[Union[azure_service.DeleteAzureClientRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a specific
        [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
        resource.

        If the client is used by one or more clusters, deletion will
        fail and a ``FAILED_PRECONDITION`` error will be returned.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_delete_azure_client():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.DeleteAzureClientRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_azure_client(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.DeleteAzureClientRequest, dict]]):
                The request object. Request message for ``AzureClusters.DeleteAzureClient``
                method.
            name (:class:`str`):
                Required. The resource name the
                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                to delete.

                [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
                names are formatted as
                ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        warnings.warn(
            "AzureClustersAsyncClient.delete_azure_client is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, azure_service.DeleteAzureClientRequest):
            request = azure_service.DeleteAzureClientRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_azure_client
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_azure_cluster(
        self,
        request: Optional[Union[azure_service.CreateAzureClusterRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        azure_cluster: Optional[azure_resources.AzureCluster] = None,
        azure_cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource on a given Google Cloud Platform project and region.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_create_azure_cluster():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                azure_cluster = gke_multicloud_v1.AzureCluster()
                azure_cluster.azure_region = "azure_region_value"
                azure_cluster.resource_group_id = "resource_group_id_value"
                azure_cluster.networking.virtual_network_id = "virtual_network_id_value"
                azure_cluster.networking.pod_address_cidr_blocks = ['pod_address_cidr_blocks_value1', 'pod_address_cidr_blocks_value2']
                azure_cluster.networking.service_address_cidr_blocks = ['service_address_cidr_blocks_value1', 'service_address_cidr_blocks_value2']
                azure_cluster.control_plane.version = "version_value"
                azure_cluster.control_plane.ssh_config.authorized_key = "authorized_key_value"
                azure_cluster.fleet.project = "project_value"

                request = gke_multicloud_v1.CreateAzureClusterRequest(
                    parent="parent_value",
                    azure_cluster=azure_cluster,
                    azure_cluster_id="azure_cluster_id_value",
                )

                # Make the request
                operation = await client.create_azure_cluster(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.CreateAzureClusterRequest, dict]]):
                The request object. Request message for ``AzureClusters.CreateAzureCluster``
                method.
            parent (:class:`str`):
                Required. The parent location where this
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                resource will be created.

                Location names are formatted as
                ``projects/<project-id>/locations/<region>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            azure_cluster (:class:`google.cloud.gke_multicloud_v1.types.AzureCluster`):
                Required. The specification of the
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                to create.

                This corresponds to the ``azure_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            azure_cluster_id (:class:`str`):
                Required. A client provided ID the resource. Must be
                unique within the parent resource.

                The provided ID will be part of the
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                resource name formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

                Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
                than 63 characters.

                This corresponds to the ``azure_cluster_id`` field
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
                :class:`google.cloud.gke_multicloud_v1.types.AzureCluster`
                An Anthos cluster running on Azure.

        """
        warnings.warn(
            "AzureClustersAsyncClient.create_azure_cluster is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, azure_cluster, azure_cluster_id]
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
        if not isinstance(request, azure_service.CreateAzureClusterRequest):
            request = azure_service.CreateAzureClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if azure_cluster is not None:
            request.azure_cluster = azure_cluster
        if azure_cluster_id is not None:
            request.azure_cluster_id = azure_cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_azure_cluster
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
            azure_resources.AzureCluster,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_azure_cluster(
        self,
        request: Optional[Union[azure_service.UpdateAzureClusterRequest, dict]] = None,
        *,
        azure_cluster: Optional[azure_resources.AzureCluster] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates an
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_update_azure_cluster():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                azure_cluster = gke_multicloud_v1.AzureCluster()
                azure_cluster.azure_region = "azure_region_value"
                azure_cluster.resource_group_id = "resource_group_id_value"
                azure_cluster.networking.virtual_network_id = "virtual_network_id_value"
                azure_cluster.networking.pod_address_cidr_blocks = ['pod_address_cidr_blocks_value1', 'pod_address_cidr_blocks_value2']
                azure_cluster.networking.service_address_cidr_blocks = ['service_address_cidr_blocks_value1', 'service_address_cidr_blocks_value2']
                azure_cluster.control_plane.version = "version_value"
                azure_cluster.control_plane.ssh_config.authorized_key = "authorized_key_value"
                azure_cluster.fleet.project = "project_value"

                request = gke_multicloud_v1.UpdateAzureClusterRequest(
                    azure_cluster=azure_cluster,
                )

                # Make the request
                operation = await client.update_azure_cluster(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.UpdateAzureClusterRequest, dict]]):
                The request object. Request message for ``AzureClusters.UpdateAzureCluster``
                method.
            azure_cluster (:class:`google.cloud.gke_multicloud_v1.types.AzureCluster`):
                Required. The
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                resource to update.

                This corresponds to the ``azure_cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. The elements of the
                repeated paths field can only include these fields from
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]:

                - ``description``.
                - ``azureClient``.
                - ``control_plane.version``.
                - ``control_plane.vm_size``.
                - ``annotations``.
                - ``authorization.admin_users``.
                - ``authorization.admin_groups``.
                - ``control_plane.root_volume.size_gib``.
                - ``azure_services_authentication``.
                - ``azure_services_authentication.tenant_id``.
                - ``azure_services_authentication.application_id``.
                - ``control_plane.proxy_config``.
                - ``control_plane.proxy_config.resource_group_id``.
                - ``control_plane.proxy_config.secret_id``.
                - ``control_plane.ssh_config.authorized_key``.
                - ``logging_config.component_config.enable_components``
                - ``monitoring_config.managed_prometheus_config.enabled``.

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.gke_multicloud_v1.types.AzureCluster`
                An Anthos cluster running on Azure.

        """
        warnings.warn(
            "AzureClustersAsyncClient.update_azure_cluster is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [azure_cluster, update_mask]
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
        if not isinstance(request, azure_service.UpdateAzureClusterRequest):
            request = azure_service.UpdateAzureClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if azure_cluster is not None:
            request.azure_cluster = azure_cluster
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_azure_cluster
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("azure_cluster.name", request.azure_cluster.name),)
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            azure_resources.AzureCluster,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_azure_cluster(
        self,
        request: Optional[Union[azure_service.GetAzureClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_resources.AzureCluster:
        r"""Describes a specific
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_azure_cluster():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAzureClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_azure_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAzureClusterRequest, dict]]):
                The request object. Request message for ``AzureClusters.GetAzureCluster``
                method.
            name (:class:`str`):
                Required. The name of the
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                resource to describe.

                ``AzureCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud Platform resource
                names.

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
            google.cloud.gke_multicloud_v1.types.AzureCluster:
                An Anthos cluster running on Azure.
        """
        warnings.warn(
            "AzureClustersAsyncClient.get_azure_cluster is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, azure_service.GetAzureClusterRequest):
            request = azure_service.GetAzureClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_azure_cluster
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

    async def list_azure_clusters(
        self,
        request: Optional[Union[azure_service.ListAzureClustersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAzureClustersAsyncPager:
        r"""Lists all
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resources on a given Google Cloud project and region.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_list_azure_clusters():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.ListAzureClustersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_azure_clusters(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.ListAzureClustersRequest, dict]]):
                The request object. Request message for ``AzureClusters.ListAzureClusters``
                method.
            parent (:class:`str`):
                Required. The parent location which owns this collection
                of
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                resources.

                Location names are formatted as
                ``projects/<project-id>/locations/<region>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud Platform resource
                names.

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
            google.cloud.gke_multicloud_v1.services.azure_clusters.pagers.ListAzureClustersAsyncPager:
                Response message for AzureClusters.ListAzureClusters
                method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "AzureClustersAsyncClient.list_azure_clusters is deprecated",
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
        if not isinstance(request, azure_service.ListAzureClustersRequest):
            request = azure_service.ListAzureClustersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_azure_clusters
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
        response = pagers.ListAzureClustersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_azure_cluster(
        self,
        request: Optional[Union[azure_service.DeleteAzureClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a specific
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource.

        Fails if the cluster has one or more associated
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resources.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_delete_azure_cluster():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.DeleteAzureClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_azure_cluster(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.DeleteAzureClusterRequest, dict]]):
                The request object. Request message for ``AzureClusters.DeleteAzureCluster``
                method.
            name (:class:`str`):
                Required. The resource name the
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                to delete.

                ``AzureCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud Platform resource
                names.

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        warnings.warn(
            "AzureClustersAsyncClient.delete_azure_cluster is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, azure_service.DeleteAzureClusterRequest):
            request = azure_service.DeleteAzureClusterRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_azure_cluster
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def generate_azure_cluster_agent_token(
        self,
        request: Optional[
            Union[azure_service.GenerateAzureClusterAgentTokenRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_service.GenerateAzureClusterAgentTokenResponse:
        r"""Generates an access token for a cluster agent.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_generate_azure_cluster_agent_token():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GenerateAzureClusterAgentTokenRequest(
                    azure_cluster="azure_cluster_value",
                    subject_token="subject_token_value",
                    subject_token_type="subject_token_type_value",
                    version="version_value",
                )

                # Make the request
                response = await client.generate_azure_cluster_agent_token(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GenerateAzureClusterAgentTokenRequest, dict]]):
                The request object.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gke_multicloud_v1.types.GenerateAzureClusterAgentTokenResponse:

        """
        warnings.warn(
            "AzureClustersAsyncClient.generate_azure_cluster_agent_token is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, azure_service.GenerateAzureClusterAgentTokenRequest):
            request = azure_service.GenerateAzureClusterAgentTokenRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_azure_cluster_agent_token
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("azure_cluster", request.azure_cluster),)
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

    async def generate_azure_access_token(
        self,
        request: Optional[
            Union[azure_service.GenerateAzureAccessTokenRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_service.GenerateAzureAccessTokenResponse:
        r"""Generates a short-lived access token to authenticate to a given
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_generate_azure_access_token():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GenerateAzureAccessTokenRequest(
                    azure_cluster="azure_cluster_value",
                )

                # Make the request
                response = await client.generate_azure_access_token(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GenerateAzureAccessTokenRequest, dict]]):
                The request object. Request message for
                ``AzureClusters.GenerateAzureAccessToken`` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.gke_multicloud_v1.types.GenerateAzureAccessTokenResponse:
                Response message for
                AzureClusters.GenerateAzureAccessToken method.

        """
        warnings.warn(
            "AzureClustersAsyncClient.generate_azure_access_token is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, azure_service.GenerateAzureAccessTokenRequest):
            request = azure_service.GenerateAzureAccessTokenRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_azure_access_token
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("azure_cluster", request.azure_cluster),)
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

    async def create_azure_node_pool(
        self,
        request: Optional[Union[azure_service.CreateAzureNodePoolRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        azure_node_pool: Optional[azure_resources.AzureNodePool] = None,
        azure_node_pool_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool],
        attached to a given
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_create_azure_node_pool():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                azure_node_pool = gke_multicloud_v1.AzureNodePool()
                azure_node_pool.version = "version_value"
                azure_node_pool.config.ssh_config.authorized_key = "authorized_key_value"
                azure_node_pool.subnet_id = "subnet_id_value"
                azure_node_pool.autoscaling.min_node_count = 1489
                azure_node_pool.autoscaling.max_node_count = 1491
                azure_node_pool.max_pods_constraint.max_pods_per_node = 1798

                request = gke_multicloud_v1.CreateAzureNodePoolRequest(
                    parent="parent_value",
                    azure_node_pool=azure_node_pool,
                    azure_node_pool_id="azure_node_pool_id_value",
                )

                # Make the request
                operation = await client.create_azure_node_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.CreateAzureNodePoolRequest, dict]]):
                The request object. Response message for
                ``AzureClusters.CreateAzureNodePool`` method.
            parent (:class:`str`):
                Required. The
                [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
                resource where this node pool will be created.

                ``AzureCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            azure_node_pool (:class:`google.cloud.gke_multicloud_v1.types.AzureNodePool`):
                Required. The specification of the
                [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
                to create.

                This corresponds to the ``azure_node_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            azure_node_pool_id (:class:`str`):
                Required. A client provided ID the resource. Must be
                unique within the parent resource.

                The provided ID will be part of the
                [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
                resource name formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

                Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
                than 63 characters.

                This corresponds to the ``azure_node_pool_id`` field
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
                :class:`google.cloud.gke_multicloud_v1.types.AzureNodePool`
                An Anthos node pool running on Azure.

        """
        warnings.warn(
            "AzureClustersAsyncClient.create_azure_node_pool is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, azure_node_pool, azure_node_pool_id]
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
        if not isinstance(request, azure_service.CreateAzureNodePoolRequest):
            request = azure_service.CreateAzureNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if azure_node_pool is not None:
            request.azure_node_pool = azure_node_pool
        if azure_node_pool_id is not None:
            request.azure_node_pool_id = azure_node_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_azure_node_pool
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
            azure_resources.AzureNodePool,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_azure_node_pool(
        self,
        request: Optional[Union[azure_service.UpdateAzureNodePoolRequest, dict]] = None,
        *,
        azure_node_pool: Optional[azure_resources.AzureNodePool] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates an
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_update_azure_node_pool():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                azure_node_pool = gke_multicloud_v1.AzureNodePool()
                azure_node_pool.version = "version_value"
                azure_node_pool.config.ssh_config.authorized_key = "authorized_key_value"
                azure_node_pool.subnet_id = "subnet_id_value"
                azure_node_pool.autoscaling.min_node_count = 1489
                azure_node_pool.autoscaling.max_node_count = 1491
                azure_node_pool.max_pods_constraint.max_pods_per_node = 1798

                request = gke_multicloud_v1.UpdateAzureNodePoolRequest(
                    azure_node_pool=azure_node_pool,
                )

                # Make the request
                operation = await client.update_azure_node_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.UpdateAzureNodePoolRequest, dict]]):
                The request object. Request message for
                ``AzureClusters.UpdateAzureNodePool`` method.
            azure_node_pool (:class:`google.cloud.gke_multicloud_v1.types.AzureNodePool`):
                Required. The
                [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
                resource to update.

                This corresponds to the ``azure_node_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. The elements of the
                repeated paths field can only include these fields from
                [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]:

                \*. ``annotations``.

                - ``version``.
                - ``autoscaling.min_node_count``.
                - ``autoscaling.max_node_count``.
                - ``config.ssh_config.authorized_key``.
                - ``management.auto_repair``.
                - ``management``.

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.gke_multicloud_v1.types.AzureNodePool`
                An Anthos node pool running on Azure.

        """
        warnings.warn(
            "AzureClustersAsyncClient.update_azure_node_pool is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [azure_node_pool, update_mask]
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
        if not isinstance(request, azure_service.UpdateAzureNodePoolRequest):
            request = azure_service.UpdateAzureNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if azure_node_pool is not None:
            request.azure_node_pool = azure_node_pool
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_azure_node_pool
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("azure_node_pool.name", request.azure_node_pool.name),)
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            azure_resources.AzureNodePool,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_azure_node_pool(
        self,
        request: Optional[Union[azure_service.GetAzureNodePoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_resources.AzureNodePool:
        r"""Describes a specific
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_azure_node_pool():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAzureNodePoolRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_azure_node_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAzureNodePoolRequest, dict]]):
                The request object. Request message for ``AzureClusters.GetAzureNodePool``
                method.
            name (:class:`str`):
                Required. The name of the
                [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
                resource to describe.

                ``AzureNodePool`` names are formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.cloud.gke_multicloud_v1.types.AzureNodePool:
                An Anthos node pool running on Azure.
        """
        warnings.warn(
            "AzureClustersAsyncClient.get_azure_node_pool is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, azure_service.GetAzureNodePoolRequest):
            request = azure_service.GetAzureNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_azure_node_pool
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

    async def list_azure_node_pools(
        self,
        request: Optional[Union[azure_service.ListAzureNodePoolsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAzureNodePoolsAsyncPager:
        r"""Lists all
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resources on a given
        [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_list_azure_node_pools():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.ListAzureNodePoolsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_azure_node_pools(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.ListAzureNodePoolsRequest, dict]]):
                The request object. Request message for ``AzureClusters.ListAzureNodePools``
                method.
            parent (:class:`str`):
                Required. The parent ``AzureCluster`` which owns this
                collection of
                [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
                resources.

                ``AzureCluster`` names are formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.cloud.gke_multicloud_v1.services.azure_clusters.pagers.ListAzureNodePoolsAsyncPager:
                Response message for AzureClusters.ListAzureNodePools
                method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "AzureClustersAsyncClient.list_azure_node_pools is deprecated",
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
        if not isinstance(request, azure_service.ListAzureNodePoolsRequest):
            request = azure_service.ListAzureNodePoolsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_azure_node_pools
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
        response = pagers.ListAzureNodePoolsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_azure_node_pool(
        self,
        request: Optional[Union[azure_service.DeleteAzureNodePoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a specific
        [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
        resource.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_delete_azure_node_pool():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.DeleteAzureNodePoolRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_azure_node_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.DeleteAzureNodePoolRequest, dict]]):
                The request object. Request message for
                ``AzureClusters.DeleteAzureNodePool`` method.
            name (:class:`str`):
                Required. The resource name the
                [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
                to delete.

                ``AzureNodePool`` names are formatted as
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        warnings.warn(
            "AzureClustersAsyncClient.delete_azure_node_pool is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, azure_service.DeleteAzureNodePoolRequest):
            request = azure_service.DeleteAzureNodePoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_azure_node_pool
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

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=common_resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_azure_open_id_config(
        self,
        request: Optional[
            Union[azure_service.GetAzureOpenIdConfigRequest, dict]
        ] = None,
        *,
        azure_cluster: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_resources.AzureOpenIdConfig:
        r"""Gets the OIDC discovery document for the cluster. See the
        `OpenID Connect Discovery 1.0
        specification <https://openid.net/specs/openid-connect-discovery-1_0.html>`__
        for details.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_azure_open_id_config():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAzureOpenIdConfigRequest(
                    azure_cluster="azure_cluster_value",
                )

                # Make the request
                response = await client.get_azure_open_id_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAzureOpenIdConfigRequest, dict]]):
                The request object. GetAzureOpenIdConfigRequest gets the
                OIDC discovery document for the cluster.
                See the OpenID Connect Discovery 1.0
                specification for details.
            azure_cluster (:class:`str`):
                Required. The AzureCluster, which
                owns the OIDC discovery document.
                Format:

                projects/<project-id>/locations/<region>/azureClusters/<cluster-id>

                This corresponds to the ``azure_cluster`` field
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
            google.cloud.gke_multicloud_v1.types.AzureOpenIdConfig:
                AzureOpenIdConfig is an OIDC
                discovery document for the cluster. See
                the OpenID Connect Discovery 1.0
                specification for details.

        """
        warnings.warn(
            "AzureClustersAsyncClient.get_azure_open_id_config is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [azure_cluster]
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
        if not isinstance(request, azure_service.GetAzureOpenIdConfigRequest):
            request = azure_service.GetAzureOpenIdConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if azure_cluster is not None:
            request.azure_cluster = azure_cluster

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_azure_open_id_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("azure_cluster", request.azure_cluster),)
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

    async def get_azure_json_web_keys(
        self,
        request: Optional[Union[azure_service.GetAzureJsonWebKeysRequest, dict]] = None,
        *,
        azure_cluster: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_resources.AzureJsonWebKeys:
        r"""Gets the public component of the cluster signing keys
        in JSON Web Key format.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_azure_json_web_keys():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAzureJsonWebKeysRequest(
                    azure_cluster="azure_cluster_value",
                )

                # Make the request
                response = await client.get_azure_json_web_keys(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAzureJsonWebKeysRequest, dict]]):
                The request object. GetAzureJsonWebKeysRequest gets the public component of
                the keys used by the cluster to sign token requests.
                This will be the jwks_uri for the discover document
                returned by getOpenIDConfig. See the OpenID Connect
                Discovery 1.0 specification for details.
            azure_cluster (:class:`str`):
                Required. The AzureCluster, which owns the JsonWebKeys.
                Format:
                ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``

                This corresponds to the ``azure_cluster`` field
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
            google.cloud.gke_multicloud_v1.types.AzureJsonWebKeys:
                AzureJsonWebKeys is a valid JSON Web
                Key Set as specififed in RFC 7517.

        """
        warnings.warn(
            "AzureClustersAsyncClient.get_azure_json_web_keys is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [azure_cluster]
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
        if not isinstance(request, azure_service.GetAzureJsonWebKeysRequest):
            request = azure_service.GetAzureJsonWebKeysRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if azure_cluster is not None:
            request.azure_cluster = azure_cluster

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_azure_json_web_keys
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("azure_cluster", request.azure_cluster),)
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

    async def get_azure_server_config(
        self,
        request: Optional[
            Union[azure_service.GetAzureServerConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> azure_resources.AzureServerConfig:
        r"""Returns information, such as supported Azure regions
        and Kubernetes versions, on a given Google Cloud
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import gke_multicloud_v1

            async def sample_get_azure_server_config():
                # Create a client
                client = gke_multicloud_v1.AzureClustersAsyncClient()

                # Initialize request argument(s)
                request = gke_multicloud_v1.GetAzureServerConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_azure_server_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.gke_multicloud_v1.types.GetAzureServerConfigRequest, dict]]):
                The request object. GetAzureServerConfigRequest gets the
                server config of GKE cluster on Azure.
            name (:class:`str`):
                Required. The name of the
                [AzureServerConfig][google.cloud.gkemulticloud.v1.AzureServerConfig]
                resource to describe.

                ``AzureServerConfig`` names are formatted as
                ``projects/<project-id>/locations/<region>/azureServerConfig``.

                See `Resource
                Names <https://cloud.google.com/apis/design/resource_names>`__
                for more details on Google Cloud resource names.

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
            google.cloud.gke_multicloud_v1.types.AzureServerConfig:
                AzureServerConfig contains
                information about a Google Cloud
                location, such as supported Azure
                regions and Kubernetes versions.

        """
        warnings.warn(
            "AzureClustersAsyncClient.get_azure_server_config is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, azure_service.GetAzureServerConfigRequest):
            request = azure_service.GetAzureServerConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_azure_server_config
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

    async def __aenter__(self) -> "AzureClustersAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AzureClustersAsyncClient",)
