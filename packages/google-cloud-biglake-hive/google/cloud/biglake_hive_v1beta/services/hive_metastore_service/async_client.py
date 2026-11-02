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
    AsyncIterable,
    Awaitable,
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

from google.cloud.biglake_hive_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.biglake_hive_v1beta.services.hive_metastore_service import pagers
from google.cloud.biglake_hive_v1beta.types import hive_metastore

from .client import HiveMetastoreServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, HiveMetastoreServiceTransport
from .transports.grpc_asyncio import HiveMetastoreServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class HiveMetastoreServiceAsyncClient:
    """Hive Metastore Service is a biglake service that allows users to
    manage their external Hive catalogs. Full API compatibility with OSS
    Hive Metastore APIs is not supported. The methods match the Hive
    Metastore API spec mostly except for a few exceptions. These include
    listing resources with pattern, environment context which are
    combined in a single List API, return of ListResponse object instead
    of a list of resources, transactions, locks, etc.

    The BigLake Hive Metastore API defines the following resources:

    - A collection of Google Cloud projects: ``/projects/*``
    - Each project has a collection of catalogs: ``/catalogs/*``
    - Each catalog has a collection of databases: ``/databases/*``
    - Each database has a collection of tables: ``/tables/*``
    """

    _client: HiveMetastoreServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = HiveMetastoreServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = HiveMetastoreServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = HiveMetastoreServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = HiveMetastoreServiceClient._DEFAULT_UNIVERSE

    catalog_path = staticmethod(HiveMetastoreServiceClient.catalog_path)
    parse_catalog_path = staticmethod(HiveMetastoreServiceClient.parse_catalog_path)
    namespace_path = staticmethod(HiveMetastoreServiceClient.namespace_path)
    parse_namespace_path = staticmethod(HiveMetastoreServiceClient.parse_namespace_path)
    table_path = staticmethod(HiveMetastoreServiceClient.table_path)
    parse_table_path = staticmethod(HiveMetastoreServiceClient.parse_table_path)
    common_billing_account_path = staticmethod(
        HiveMetastoreServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        HiveMetastoreServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(HiveMetastoreServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        HiveMetastoreServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        HiveMetastoreServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        HiveMetastoreServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(HiveMetastoreServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        HiveMetastoreServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(HiveMetastoreServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        HiveMetastoreServiceClient.parse_common_location_path
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
            HiveMetastoreServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            HiveMetastoreServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(HiveMetastoreServiceAsyncClient, info, *args, **kwargs)

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
            HiveMetastoreServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            HiveMetastoreServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(HiveMetastoreServiceAsyncClient, filename, *args, **kwargs)

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
        return HiveMetastoreServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> HiveMetastoreServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            HiveMetastoreServiceTransport: The transport used by the client instance.
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

    get_transport_class = HiveMetastoreServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                HiveMetastoreServiceTransport,
                Callable[..., HiveMetastoreServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the hive metastore service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,HiveMetastoreServiceTransport,Callable[..., HiveMetastoreServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the HiveMetastoreServiceTransport constructor.
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
        self._client = HiveMetastoreServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.biglake.hive_v1beta.HiveMetastoreServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
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
                    "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                    "credentialsType": None,
                },
            )

    async def create_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.CreateHiveCatalogRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        hive_catalog: Optional[hive_metastore.HiveCatalog] = None,
        hive_catalog_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveCatalog:
        r"""Creates a new hive catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_create_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                hive_catalog = biglake_hive_v1beta.HiveCatalog()
                hive_catalog.location_uri = "location_uri_value"

                request = biglake_hive_v1beta.CreateHiveCatalogRequest(
                    parent="parent_value",
                    hive_catalog=hive_catalog,
                    hive_catalog_id="hive_catalog_id_value",
                    primary_location="primary_location_value",
                )

                # Make the request
                response = await client.create_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.CreateHiveCatalogRequest, dict]]):
                The request object. Request message for the
                CreateHiveCatalog method.
            parent (:class:`str`):
                Required. The parent resource where this catalog will be
                created. Format: projects/{project_id_or_number}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_catalog (:class:`google.cloud.biglake_hive_v1beta.types.HiveCatalog`):
                Required. The catalog to create. The ``name`` field does
                not need to be provided. Gets copied over from
                catalog_id.

                This corresponds to the ``hive_catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_catalog_id (:class:`str`):
                Required. The Hive Catalog ID to use
                for the catalog that will become the
                final component of the catalog's
                resource name. The maximum length is 256
                characters.

                This corresponds to the ``hive_catalog_id`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveCatalog:
                The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, hive_catalog, hive_catalog_id]
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
        if not isinstance(request, hive_metastore.CreateHiveCatalogRequest):
            request = hive_metastore.CreateHiveCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if hive_catalog is not None:
            request.hive_catalog = hive_catalog
        if hive_catalog_id is not None:
            request.hive_catalog_id = hive_catalog_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_hive_catalog
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

    async def get_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.GetHiveCatalogRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveCatalog:
        r"""Gets the catalog specified by the resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_get_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.GetHiveCatalogRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.GetHiveCatalogRequest, dict]]):
                The request object. Request message for the
                GetHiveCatalog method.
            name (:class:`str`):
                Required. The name of the catalog to retrieve. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

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
            google.cloud.biglake_hive_v1beta.types.HiveCatalog:
                The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

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
        if not isinstance(request, hive_metastore.GetHiveCatalogRequest):
            request = hive_metastore.GetHiveCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_hive_catalog
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

    async def list_hive_catalogs(
        self,
        request: Optional[Union[hive_metastore.ListHiveCatalogsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListHiveCatalogsAsyncPager:
        r"""List all catalogs in a specified project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_list_hive_catalogs():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListHiveCatalogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_hive_catalogs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.ListHiveCatalogsRequest, dict]]):
                The request object. Request message for the
                ListHiveCatalogs method.
            parent (:class:`str`):
                Required. The project to list catalogs from. Format:
                projects/{project_id_or_number}

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
            google.cloud.biglake_hive_v1beta.services.hive_metastore_service.pagers.ListHiveCatalogsAsyncPager:
                Response message for the
                ListHiveCatalogs method.
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
        if not isinstance(request, hive_metastore.ListHiveCatalogsRequest):
            request = hive_metastore.ListHiveCatalogsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_hive_catalogs
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
        response = pagers.ListHiveCatalogsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.UpdateHiveCatalogRequest, dict]] = None,
        *,
        hive_catalog: Optional[hive_metastore.HiveCatalog] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveCatalog:
        r"""Updates an existing catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_update_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                hive_catalog = biglake_hive_v1beta.HiveCatalog()
                hive_catalog.location_uri = "location_uri_value"

                request = biglake_hive_v1beta.UpdateHiveCatalogRequest(
                    hive_catalog=hive_catalog,
                )

                # Make the request
                response = await client.update_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.UpdateHiveCatalogRequest, dict]]):
                The request object. Request message for the
                UpdateHiveCatalog method.
            hive_catalog (:class:`google.cloud.biglake_hive_v1beta.types.HiveCatalog`):
                Required. The hive catalog to update. The name under the
                catalog is used to identify the catalog. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

                This corresponds to the ``hive_catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to update.

                For the ``FieldMask`` definition, see
                https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
                If not set, defaults to all of the fields that are
                allowed to update.

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
            google.cloud.biglake_hive_v1beta.types.HiveCatalog:
                The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [hive_catalog, update_mask]
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
        if not isinstance(request, hive_metastore.UpdateHiveCatalogRequest):
            request = hive_metastore.UpdateHiveCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if hive_catalog is not None:
            request.hive_catalog = hive_catalog
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_hive_catalog
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("hive_catalog.name", request.hive_catalog.name),)
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

    async def delete_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.DeleteHiveCatalogRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing catalog specified by the catalog
        ID. Delete will fail if the catalog is not empty.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_delete_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.DeleteHiveCatalogRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_hive_catalog(request=request)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.DeleteHiveCatalogRequest, dict]]):
                The request object. Request message for the
                DeleteHiveCatalog method.
            name (:class:`str`):
                Required. The name of the catalog to delete. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

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
        if not isinstance(request, hive_metastore.DeleteHiveCatalogRequest):
            request = hive_metastore.DeleteHiveCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_hive_catalog
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

    async def create_hive_database(
        self,
        request: Optional[Union[hive_metastore.CreateHiveDatabaseRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        hive_database: Optional[hive_metastore.HiveDatabase] = None,
        hive_database_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveDatabase:
        r"""Creates a new database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_create_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.CreateHiveDatabaseRequest(
                    parent="parent_value",
                    hive_database_id="hive_database_id_value",
                )

                # Make the request
                response = await client.create_hive_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.CreateHiveDatabaseRequest, dict]]):
                The request object. Request message for the
                CreateHiveDatabase method.
            parent (:class:`str`):
                Required. The parent resource where this database will
                be created. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_database (:class:`google.cloud.biglake_hive_v1beta.types.HiveDatabase`):
                Required. The database to create. The ``name`` field
                does not need to be provided.

                This corresponds to the ``hive_database`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_database_id (:class:`str`):
                Required. The ID to use for the Hive
                Database. The maximum length is 128
                characters.

                This corresponds to the ``hive_database_id`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveDatabase:
                Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, hive_database, hive_database_id]
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
        if not isinstance(request, hive_metastore.CreateHiveDatabaseRequest):
            request = hive_metastore.CreateHiveDatabaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if hive_database is not None:
            request.hive_database = hive_database
        if hive_database_id is not None:
            request.hive_database_id = hive_database_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_hive_database
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

    async def get_hive_database(
        self,
        request: Optional[Union[hive_metastore.GetHiveDatabaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveDatabase:
        r"""Gets the database specified by the resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_get_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.GetHiveDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_hive_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.GetHiveDatabaseRequest, dict]]):
                The request object. Request message for the
                GetHiveDatabase method.
            name (:class:`str`):
                Required. The name of the database to retrieve. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

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
            google.cloud.biglake_hive_v1beta.types.HiveDatabase:
                Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

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
        if not isinstance(request, hive_metastore.GetHiveDatabaseRequest):
            request = hive_metastore.GetHiveDatabaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_hive_database
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

    async def list_hive_databases(
        self,
        request: Optional[Union[hive_metastore.ListHiveDatabasesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListHiveDatabasesAsyncPager:
        r"""List all databases in a specified catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_list_hive_databases():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListHiveDatabasesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_hive_databases(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.ListHiveDatabasesRequest, dict]]):
                The request object. Request message for the
                ListHiveDatabases method.
            parent (:class:`str`):
                Required. The hive catalog to list databases from.
                Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

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
            google.cloud.biglake_hive_v1beta.services.hive_metastore_service.pagers.ListHiveDatabasesAsyncPager:
                Response message for the
                ListHiveDatabases method.
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
        if not isinstance(request, hive_metastore.ListHiveDatabasesRequest):
            request = hive_metastore.ListHiveDatabasesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_hive_databases
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
        response = pagers.ListHiveDatabasesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_hive_database(
        self,
        request: Optional[Union[hive_metastore.UpdateHiveDatabaseRequest, dict]] = None,
        *,
        hive_database: Optional[hive_metastore.HiveDatabase] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveDatabase:
        r"""Updates an existing database specified by the
        database name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_update_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.UpdateHiveDatabaseRequest(
                )

                # Make the request
                response = await client.update_hive_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.UpdateHiveDatabaseRequest, dict]]):
                The request object. Request message for the
                UpdateHiveDatabase method.
            hive_database (:class:`google.cloud.biglake_hive_v1beta.types.HiveDatabase`):
                Required. The database to update.

                The database's ``name`` field is used to identify the
                database to update. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

                This corresponds to the ``hive_database`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveDatabase:
                Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [hive_database, update_mask]
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
        if not isinstance(request, hive_metastore.UpdateHiveDatabaseRequest):
            request = hive_metastore.UpdateHiveDatabaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if hive_database is not None:
            request.hive_database = hive_database
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_hive_database
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("hive_database.name", request.hive_database.name),)
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

    async def delete_hive_database(
        self,
        request: Optional[Union[hive_metastore.DeleteHiveDatabaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing database specified by the
        database name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_delete_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.DeleteHiveDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_hive_database(request=request)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.DeleteHiveDatabaseRequest, dict]]):
                The request object. Request message for the
                DeleteHiveDatabase method.
            name (:class:`str`):
                Required. The name of the database to delete. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

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
        if not isinstance(request, hive_metastore.DeleteHiveDatabaseRequest):
            request = hive_metastore.DeleteHiveDatabaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_hive_database
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

    async def create_hive_table(
        self,
        request: Optional[Union[hive_metastore.CreateHiveTableRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        hive_table: Optional[hive_metastore.HiveTable] = None,
        hive_table_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveTable:
        r"""Creates a new hive table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_create_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                hive_table = biglake_hive_v1beta.HiveTable()
                hive_table.storage_descriptor.columns.name = "name_value"
                hive_table.storage_descriptor.columns.type_ = "type__value"

                request = biglake_hive_v1beta.CreateHiveTableRequest(
                    parent="parent_value",
                    hive_table=hive_table,
                    hive_table_id="hive_table_id_value",
                )

                # Make the request
                response = await client.create_hive_table(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.CreateHiveTableRequest, dict]]):
                The request object. Request message for the
                CreateHiveTable method.
            parent (:class:`str`):
                Required. The parent resource for the table to be
                created. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_table (:class:`google.cloud.biglake_hive_v1beta.types.HiveTable`):
                Required. The Hive Table to create. The ``name`` field
                does not need to be provided.

                This corresponds to the ``hive_table`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_table_id (:class:`str`):
                Required. The Hive Table ID to use
                for the table that will become the final
                component of the table's resource name.
                The maximum length is 256 characters.

                This corresponds to the ``hive_table_id`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveTable:
                Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, hive_table, hive_table_id]
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
        if not isinstance(request, hive_metastore.CreateHiveTableRequest):
            request = hive_metastore.CreateHiveTableRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if hive_table is not None:
            request.hive_table = hive_table
        if hive_table_id is not None:
            request.hive_table_id = hive_table_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_hive_table
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

    async def get_hive_table(
        self,
        request: Optional[Union[hive_metastore.GetHiveTableRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveTable:
        r"""Gets the table specified by the resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_get_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.GetHiveTableRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_hive_table(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.GetHiveTableRequest, dict]]):
                The request object. Request message for the GetHiveTable
                method.
            name (:class:`str`):
                Required. The name of the table to retrieve. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

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
            google.cloud.biglake_hive_v1beta.types.HiveTable:
                Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

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
        if not isinstance(request, hive_metastore.GetHiveTableRequest):
            request = hive_metastore.GetHiveTableRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_hive_table
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

    async def list_hive_tables(
        self,
        request: Optional[Union[hive_metastore.ListHiveTablesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListHiveTablesAsyncPager:
        r"""List all hive tables in a specified project under the
        hive catalog and database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_list_hive_tables():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListHiveTablesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_hive_tables(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.ListHiveTablesRequest, dict]]):
                The request object. Request message for the
                ListHiveTables method.
            parent (:class:`str`):
                Required. The database to list tables from. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

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
            google.cloud.biglake_hive_v1beta.services.hive_metastore_service.pagers.ListHiveTablesAsyncPager:
                Response message for the
                ListHiveTables method.
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
        if not isinstance(request, hive_metastore.ListHiveTablesRequest):
            request = hive_metastore.ListHiveTablesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_hive_tables
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
        response = pagers.ListHiveTablesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_hive_table(
        self,
        request: Optional[Union[hive_metastore.UpdateHiveTableRequest, dict]] = None,
        *,
        hive_table: Optional[hive_metastore.HiveTable] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveTable:
        r"""Updates an existing table specified by the table
        name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_update_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                hive_table = biglake_hive_v1beta.HiveTable()
                hive_table.storage_descriptor.columns.name = "name_value"
                hive_table.storage_descriptor.columns.type_ = "type__value"

                request = biglake_hive_v1beta.UpdateHiveTableRequest(
                    hive_table=hive_table,
                )

                # Make the request
                response = await client.update_hive_table(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.UpdateHiveTableRequest, dict]]):
                The request object. Request message for the
                UpdateHiveTable method.
            hive_table (:class:`google.cloud.biglake_hive_v1beta.types.HiveTable`):
                Required. The table to update.

                The table's ``name`` field is used to identify the table
                to update. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

                This corresponds to the ``hive_table`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveTable:
                Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [hive_table, update_mask]
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
        if not isinstance(request, hive_metastore.UpdateHiveTableRequest):
            request = hive_metastore.UpdateHiveTableRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if hive_table is not None:
            request.hive_table = hive_table
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_hive_table
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("hive_table.name", request.hive_table.name),)
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

    async def delete_hive_table(
        self,
        request: Optional[Union[hive_metastore.DeleteHiveTableRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing table specified by the table
        name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_delete_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.DeleteHiveTableRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_hive_table(request=request)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.DeleteHiveTableRequest, dict]]):
                The request object. Request message for the
                DeleteHiveTable method.
            name (:class:`str`):
                Required. The name of the database to delete. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

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
        if not isinstance(request, hive_metastore.DeleteHiveTableRequest):
            request = hive_metastore.DeleteHiveTableRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_hive_table
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

    async def batch_create_partitions(
        self,
        request: Optional[
            Union[hive_metastore.BatchCreatePartitionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.BatchCreatePartitionsResponse:
        r"""Adds partitions to a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_batch_create_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                requests = biglake_hive_v1beta.CreatePartitionRequest()
                requests.parent = "parent_value"
                requests.partition.values = ['values_value1', 'values_value2']

                request = biglake_hive_v1beta.BatchCreatePartitionsRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = await client.batch_create_partitions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.BatchCreatePartitionsRequest, dict]]):
                The request object. Request message for the
                BatchCreatePartitions method.
            parent (:class:`str`):
                Required. Reference to the table to
                where the partitions to be added, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
            google.cloud.biglake_hive_v1beta.types.BatchCreatePartitionsResponse:
                Response message for
                BatchCreatePartitions.

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
        if not isinstance(request, hive_metastore.BatchCreatePartitionsRequest):
            request = hive_metastore.BatchCreatePartitionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_create_partitions
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

    async def batch_delete_partitions(
        self,
        request: Optional[
            Union[hive_metastore.BatchDeletePartitionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes partitions from a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_batch_delete_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                partition_values = biglake_hive_v1beta.PartitionValues()
                partition_values.values = ['values_value1', 'values_value2']

                request = biglake_hive_v1beta.BatchDeletePartitionsRequest(
                    parent="parent_value",
                    partition_values=partition_values,
                )

                # Make the request
                await client.batch_delete_partitions(request=request)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.BatchDeletePartitionsRequest, dict]]):
                The request object. Request message for
                BatchDeletePartitions. The Partition is
                uniquely identified by values, which is
                an ordered list. Hence, there is no
                separate name or partition id field.
            parent (:class:`str`):
                Required. Reference to the table to
                which these partitions belong, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
        if not isinstance(request, hive_metastore.BatchDeletePartitionsRequest):
            request = hive_metastore.BatchDeletePartitionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_delete_partitions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
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

    async def batch_update_partitions(
        self,
        request: Optional[
            Union[hive_metastore.BatchUpdatePartitionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.BatchUpdatePartitionsResponse:
        r"""Updates partitions in a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_batch_update_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                requests = biglake_hive_v1beta.UpdatePartitionRequest()
                requests.partition.values = ['values_value1', 'values_value2']

                request = biglake_hive_v1beta.BatchUpdatePartitionsRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = await client.batch_update_partitions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.BatchUpdatePartitionsRequest, dict]]):
                The request object. Request message for
                BatchUpdatePartitions.
            parent (:class:`str`):
                Required. Reference to the table to
                which these partitions belong, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
            google.cloud.biglake_hive_v1beta.types.BatchUpdatePartitionsResponse:
                Response message for
                BatchUpdatePartitions.

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
        if not isinstance(request, hive_metastore.BatchUpdatePartitionsRequest):
            request = hive_metastore.BatchUpdatePartitionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_update_partitions
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

    def list_partitions(
        self,
        request: Optional[Union[hive_metastore.ListPartitionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> Awaitable[AsyncIterable[hive_metastore.ListPartitionsResponse]]:
        r"""Streams list of partitions from a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_list_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListPartitionsRequest(
                    parent="parent_value",
                )

                # Make the request
                stream = await client.list_partitions(request=request)

                # Handle the response
                async for response in stream:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.ListPartitionsRequest, dict]]):
                The request object. Request message for ListPartitions.
            parent (:class:`str`):
                Required. Reference to the table to
                which these partitions belong, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
            AsyncIterable[google.cloud.biglake_hive_v1beta.types.ListPartitionsResponse]:
                Response message for ListPartitions.
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
        if not isinstance(request, hive_metastore.ListPartitionsRequest):
            request = hive_metastore.ListPartitionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_partitions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def failover_hive_catalog(
        self,
        request: Optional[
            Union[hive_metastore.FailoverHiveCatalogRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        primary_replica: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.FailoverHiveCatalogResponse:
        r"""Failover the catalog to a new primary replica region.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            async def sample_failover_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceAsyncClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.FailoverHiveCatalogRequest(
                    name="name_value",
                    primary_replica="primary_replica_value",
                )

                # Make the request
                response = await client.failover_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.biglake_hive_v1beta.types.FailoverHiveCatalogRequest, dict]]):
                The request object. Request message for
                FailoverHiveCatalog.
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
            google.cloud.biglake_hive_v1beta.types.FailoverHiveCatalogResponse:
                Response message for
                FailoverHiveCatalog.

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
        if not isinstance(request, hive_metastore.FailoverHiveCatalogRequest):
            request = hive_metastore.FailoverHiveCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if primary_replica is not None:
            request.primary_replica = primary_replica

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.failover_hive_catalog
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

    async def __aenter__(self) -> "HiveMetastoreServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("HiveMetastoreServiceAsyncClient",)
