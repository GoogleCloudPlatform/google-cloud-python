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

from google.cloud.biglake_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.biglake_v1.services.iceberg_catalog_service import pagers
from google.cloud.biglake_v1.types import iceberg_rest_catalog

from .client import IcebergCatalogServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, IcebergCatalogServiceTransport
from .transports.grpc_asyncio import IcebergCatalogServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class IcebergCatalogServiceAsyncClient:
    """Lakehouse runtime catalog supports the following catalog
    management methods:

    - GetIcebergCatalog
    - ListIcebergCatalogs
    - DeleteIcebergCatalog
    - UpdateIcebergCatalog
    - CreateIcebergCatalog
    - FailoverIcebergCatalog
    """

    _client: IcebergCatalogServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = IcebergCatalogServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = IcebergCatalogServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = IcebergCatalogServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = IcebergCatalogServiceClient._DEFAULT_UNIVERSE

    catalog_path = staticmethod(IcebergCatalogServiceClient.catalog_path)
    parse_catalog_path = staticmethod(IcebergCatalogServiceClient.parse_catalog_path)
    secret_path = staticmethod(IcebergCatalogServiceClient.secret_path)
    parse_secret_path = staticmethod(IcebergCatalogServiceClient.parse_secret_path)
    service_path = staticmethod(IcebergCatalogServiceClient.service_path)
    parse_service_path = staticmethod(IcebergCatalogServiceClient.parse_service_path)
    common_billing_account_path = staticmethod(
        IcebergCatalogServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        IcebergCatalogServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(IcebergCatalogServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        IcebergCatalogServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        IcebergCatalogServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        IcebergCatalogServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(IcebergCatalogServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        IcebergCatalogServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        IcebergCatalogServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        IcebergCatalogServiceClient.parse_common_location_path
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
            IcebergCatalogServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            IcebergCatalogServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(IcebergCatalogServiceAsyncClient, info, *args, **kwargs)

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
            IcebergCatalogServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            IcebergCatalogServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(IcebergCatalogServiceAsyncClient, filename, *args, **kwargs)

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
        return IcebergCatalogServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> IcebergCatalogServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            IcebergCatalogServiceTransport: The transport used by the client instance.
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

    get_transport_class = IcebergCatalogServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                IcebergCatalogServiceTransport,
                Callable[..., IcebergCatalogServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the iceberg catalog service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,IcebergCatalogServiceTransport,Callable[..., IcebergCatalogServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the IcebergCatalogServiceTransport constructor.
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
        self._client = IcebergCatalogServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.biglake_v1.IcebergCatalogServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
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
                    "serviceName": "google.cloud.biglake.v1.IcebergCatalogService",
                    "credentialsType": None,
                },
            )

    async def get_iceberg_catalog(
        self,
        request: Optional[
            Union[iceberg_rest_catalog.GetIcebergCatalogRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iceberg_rest_catalog.IcebergCatalog:
        r"""Returns the Iceberg REST Catalog configuration
        options.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_v1

            async def sample_get_iceberg_catalog():
                # Create a client
                client = biglake_v1.IcebergCatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_v1.GetIcebergCatalogRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_iceberg_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_v1.types.GetIcebergCatalogRequest, dict]]):
                The request object. The request message for the ``GetIcebergCatalog`` API.
            name (:class:`str`):
                Required. The catalog to get.
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
            google.cloud.biglake_v1.types.IcebergCatalog:
                The Iceberg REST Catalog information.
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
        if not isinstance(request, iceberg_rest_catalog.GetIcebergCatalogRequest):
            request = iceberg_rest_catalog.GetIcebergCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_iceberg_catalog
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

    async def list_iceberg_catalogs(
        self,
        request: Optional[
            Union[iceberg_rest_catalog.ListIcebergCatalogsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListIcebergCatalogsAsyncPager:
        r"""Lists the Iceberg REST Catalogs.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_v1

            async def sample_list_iceberg_catalogs():
                # Create a client
                client = biglake_v1.IcebergCatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_v1.ListIcebergCatalogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_iceberg_catalogs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_v1.types.ListIcebergCatalogsRequest, dict]]):
                The request object. The request message for the ``ListIcebergCatalogs`` API.
            parent (:class:`str`):
                Required. The parent resource where this catalog will be
                created. Format: projects/{project_id}

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
            google.cloud.biglake_v1.services.iceberg_catalog_service.pagers.ListIcebergCatalogsAsyncPager:
                The response message for the ListIcebergCatalogs API.

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
        if not isinstance(request, iceberg_rest_catalog.ListIcebergCatalogsRequest):
            request = iceberg_rest_catalog.ListIcebergCatalogsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_iceberg_catalogs
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
        response = pagers.ListIcebergCatalogsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_iceberg_catalog(
        self,
        request: Optional[
            Union[iceberg_rest_catalog.UpdateIcebergCatalogRequest, dict]
        ] = None,
        *,
        iceberg_catalog: Optional[iceberg_rest_catalog.IcebergCatalog] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iceberg_rest_catalog.IcebergCatalog:
        r"""Update the Iceberg REST Catalog configuration
        options.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_v1

            async def sample_update_iceberg_catalog():
                # Create a client
                client = biglake_v1.IcebergCatalogServiceAsyncClient()

                # Initialize request argument(s)
                iceberg_catalog = biglake_v1.IcebergCatalog()
                iceberg_catalog.catalog_type = "CATALOG_TYPE_FEDERATED"

                request = biglake_v1.UpdateIcebergCatalogRequest(
                    iceberg_catalog=iceberg_catalog,
                )

                # Make the request
                response = await client.update_iceberg_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_v1.types.UpdateIcebergCatalogRequest, dict]]):
                The request object. The request message for the ``UpdateIcebergCatalog``
                API.
            iceberg_catalog (:class:`google.cloud.biglake_v1.types.IcebergCatalog`):
                Required. The catalog to update.
                This corresponds to the ``iceberg_catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to
                update.

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
            google.cloud.biglake_v1.types.IcebergCatalog:
                The Iceberg REST Catalog information.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [iceberg_catalog, update_mask]
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
        if not isinstance(request, iceberg_rest_catalog.UpdateIcebergCatalogRequest):
            request = iceberg_rest_catalog.UpdateIcebergCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if iceberg_catalog is not None:
            request.iceberg_catalog = iceberg_catalog
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_iceberg_catalog
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("iceberg_catalog.name", request.iceberg_catalog.name),)
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

    async def create_iceberg_catalog(
        self,
        request: Optional[
            Union[iceberg_rest_catalog.CreateIcebergCatalogRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        iceberg_catalog: Optional[iceberg_rest_catalog.IcebergCatalog] = None,
        iceberg_catalog_id: Optional[str] = None,
        primary_location: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iceberg_rest_catalog.IcebergCatalog:
        r"""Creates the Iceberg REST Catalog. Google Cloud Storage Bucket
        catalog id is the bucket for which the catalog is created (e.g.
        ``my-catalog`` for ``gs://my-catalog``).

        If the bucket does not exist, of the caller does not have bucket
        metadata permissions, the catalog will not be created.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_v1

            async def sample_create_iceberg_catalog():
                # Create a client
                client = biglake_v1.IcebergCatalogServiceAsyncClient()

                # Initialize request argument(s)
                iceberg_catalog = biglake_v1.IcebergCatalog()
                iceberg_catalog.catalog_type = "CATALOG_TYPE_FEDERATED"

                request = biglake_v1.CreateIcebergCatalogRequest(
                    parent="parent_value",
                    iceberg_catalog_id="iceberg_catalog_id_value",
                    iceberg_catalog=iceberg_catalog,
                )

                # Make the request
                response = await client.create_iceberg_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_v1.types.CreateIcebergCatalogRequest, dict]]):
                The request object. The request message for the ``CreateIcebergCatalog``
                API.
            parent (:class:`str`):
                Required. The parent resource where this catalog will be
                created. Format: projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            iceberg_catalog (:class:`google.cloud.biglake_v1.types.IcebergCatalog`):
                Required. The catalog to create. The required fields for
                creation are:

                - catalog_type. Optionally: credential_mode can be
                  provided, if Credential Vending is desired.

                This corresponds to the ``iceberg_catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            iceberg_catalog_id (:class:`str`):
                Required. The name of the catalog.
                This corresponds to the ``iceberg_catalog_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            primary_location (:class:`str`):
                Optional. The primary location where the catalog
                metadata will be stored.

                For Google Cloud Storage bucket catalogs and BigLake
                catalogs, if this is not specified, then the region is
                inferred from the bucket's region (``default_location``
                bucket for BigLake catalogs). If specified, the region
                must be in jurisdiction (near the ``default_location``
                bucket's region and the ``restricted_locations``
                buckets' regions for BigLake catalogs).

                For federated catalogs, this must be specified and be a
                Lakehouse-supported location
                (https://docs.cloud.google.com/lakehouse/docs/locations).
                It should be close to the remote catalog's location for
                the best performance and cost.

                This corresponds to the ``primary_location`` field
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
            google.cloud.biglake_v1.types.IcebergCatalog:
                The Iceberg REST Catalog information.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            iceberg_catalog,
            iceberg_catalog_id,
            primary_location,
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
        if not isinstance(request, iceberg_rest_catalog.CreateIcebergCatalogRequest):
            request = iceberg_rest_catalog.CreateIcebergCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if iceberg_catalog is not None:
            request.iceberg_catalog = iceberg_catalog
        if iceberg_catalog_id is not None:
            request.iceberg_catalog_id = iceberg_catalog_id
        if primary_location is not None:
            request.primary_location = primary_location

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_iceberg_catalog
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

    async def failover_iceberg_catalog(
        self,
        request: Optional[
            Union[iceberg_rest_catalog.FailoverIcebergCatalogRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        primary_replica: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iceberg_rest_catalog.FailoverIcebergCatalogResponse:
        r"""Failover the catalog to a new primary replica region.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_v1

            async def sample_failover_iceberg_catalog():
                # Create a client
                client = biglake_v1.IcebergCatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_v1.FailoverIcebergCatalogRequest(
                    name="name_value",
                    primary_replica="primary_replica_value",
                )

                # Make the request
                response = await client.failover_iceberg_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_v1.types.FailoverIcebergCatalogRequest, dict]]):
                The request object. Request message for
                FailoverIcebergCatalog.
            name (:class:`str`):
                Required. The name of the catalog in the form
                "projects/{project_id}/catalogs/{catalog_id}"

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            primary_replica (:class:`str`):
                Required. The region being assigned
                as the new primary replica region. For
                example "us-east1". This must be one of
                the replica regions in the catalog's
                list of replicas marked as a
                "secondary".

                This corresponds to the ``primary_replica`` field
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
            google.cloud.biglake_v1.types.FailoverIcebergCatalogResponse:
                Response message for
                FailoverIcebergCatalog.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, primary_replica]
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
        if not isinstance(request, iceberg_rest_catalog.FailoverIcebergCatalogRequest):
            request = iceberg_rest_catalog.FailoverIcebergCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if primary_replica is not None:
            request.primary_replica = primary_replica

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.failover_iceberg_catalog
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

    async def __aenter__(self) -> "IcebergCatalogServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("IcebergCatalogServiceAsyncClient",)
