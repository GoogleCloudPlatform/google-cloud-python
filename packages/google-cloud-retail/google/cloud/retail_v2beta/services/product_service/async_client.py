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

from google.cloud.retail_v2beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.retail_v2beta.services.product_service import pagers
from google.cloud.retail_v2beta.types import (
    common,
    export_config,
    import_config,
    product,
    product_service,
    promotion,
    purge_config,
)
from google.cloud.retail_v2beta.types import product as gcr_product

from .client import ProductServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, ProductServiceTransport
from .transports.grpc_asyncio import ProductServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ProductServiceAsyncClient:
    """Service for ingesting [Product][google.cloud.retail.v2beta.Product]
    information of the customer's website.
    """

    _client: ProductServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ProductServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ProductServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = ProductServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = ProductServiceClient._DEFAULT_UNIVERSE

    branch_path = staticmethod(ProductServiceClient.branch_path)
    parse_branch_path = staticmethod(ProductServiceClient.parse_branch_path)
    product_path = staticmethod(ProductServiceClient.product_path)
    parse_product_path = staticmethod(ProductServiceClient.parse_product_path)
    common_billing_account_path = staticmethod(
        ProductServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ProductServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ProductServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ProductServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ProductServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ProductServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ProductServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        ProductServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(ProductServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        ProductServiceClient.parse_common_location_path
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
            ProductServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            ProductServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(ProductServiceAsyncClient, info, *args, **kwargs)

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
            ProductServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            ProductServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(ProductServiceAsyncClient, filename, *args, **kwargs)

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
        return ProductServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ProductServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ProductServiceTransport: The transport used by the client instance.
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

    get_transport_class = ProductServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, ProductServiceTransport, Callable[..., ProductServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the product service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ProductServiceTransport,Callable[..., ProductServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ProductServiceTransport constructor.
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
        self._client = ProductServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.retail_v2beta.ProductServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.retail.v2beta.ProductService",
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
                    "serviceName": "google.cloud.retail.v2beta.ProductService",
                    "credentialsType": None,
                },
            )

    async def create_product(
        self,
        request: Optional[Union[product_service.CreateProductRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        product: Optional[gcr_product.Product] = None,
        product_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcr_product.Product:
        r"""Creates a [Product][google.cloud.retail.v2beta.Product].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_create_product():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                product = retail_v2beta.Product()
                product.title = "title_value"

                request = retail_v2beta.CreateProductRequest(
                    parent="parent_value",
                    product=product,
                    product_id="product_id_value",
                )

                # Make the request
                response = await client.create_product(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.CreateProductRequest, dict]]):
                The request object. Request message for
                [ProductService.CreateProduct][google.cloud.retail.v2beta.ProductService.CreateProduct]
                method.
            parent (:class:`str`):
                Required. The parent catalog resource name, such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product (:class:`google.cloud.retail_v2beta.types.Product`):
                Required. The
                [Product][google.cloud.retail.v2beta.Product] to create.

                This corresponds to the ``product`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product_id (:class:`str`):
                Required. The ID to use for the
                [Product][google.cloud.retail.v2beta.Product], which
                will become the final component of the
                [Product.name][google.cloud.retail.v2beta.Product.name].

                If the caller does not have permission to create the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                This field must be unique among all
                [Product][google.cloud.retail.v2beta.Product]s with the
                same
                [parent][google.cloud.retail.v2beta.CreateProductRequest.parent].
                Otherwise, an ALREADY_EXISTS error is returned.

                This field must be a UTF-8 encoded string with a length
                limit of 128 characters. Otherwise, an INVALID_ARGUMENT
                error is returned.

                This corresponds to the ``product_id`` field
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
            google.cloud.retail_v2beta.types.Product:
                Product captures all metadata
                information of items to be recommended
                or searched.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, product, product_id]
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
        if not isinstance(request, product_service.CreateProductRequest):
            request = product_service.CreateProductRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if product is not None:
            request.product = product
        if product_id is not None:
            request.product_id = product_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_product
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

    async def get_product(
        self,
        request: Optional[Union[product_service.GetProductRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> product.Product:
        r"""Gets a [Product][google.cloud.retail.v2beta.Product].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_get_product():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.GetProductRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_product(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.GetProductRequest, dict]]):
                The request object. Request message for
                [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct]
                method.
            name (:class:`str`):
                Required. Full resource name of
                [Product][google.cloud.retail.v2beta.Product], such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

                If the caller does not have permission to access the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                If the requested
                [Product][google.cloud.retail.v2beta.Product] does not
                exist, a NOT_FOUND error is returned.

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
            google.cloud.retail_v2beta.types.Product:
                Product captures all metadata
                information of items to be recommended
                or searched.

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
        if not isinstance(request, product_service.GetProductRequest):
            request = product_service.GetProductRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_product
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

    async def list_products(
        self,
        request: Optional[Union[product_service.ListProductsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListProductsAsyncPager:
        r"""Gets a list of [Product][google.cloud.retail.v2beta.Product]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_list_products():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.ListProductsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_products(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.ListProductsRequest, dict]]):
                The request object. Request message for
                [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts]
                method.
            parent (:class:`str`):
                Required. The parent branch resource name, such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/0``.
                Use ``default_branch`` as the branch ID, to list
                products under the default branch.

                If the caller does not have permission to list
                [Product][google.cloud.retail.v2beta.Product]s under
                this branch, regardless of whether or not this branch
                exists, a PERMISSION_DENIED error is returned.

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
            google.cloud.retail_v2beta.services.product_service.pagers.ListProductsAsyncPager:
                Response message for
                   [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts]
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
        if not isinstance(request, product_service.ListProductsRequest):
            request = product_service.ListProductsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_products
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
        response = pagers.ListProductsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_product(
        self,
        request: Optional[Union[product_service.UpdateProductRequest, dict]] = None,
        *,
        product: Optional[gcr_product.Product] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcr_product.Product:
        r"""Updates a [Product][google.cloud.retail.v2beta.Product].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_update_product():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                product = retail_v2beta.Product()
                product.title = "title_value"

                request = retail_v2beta.UpdateProductRequest(
                    product=product,
                )

                # Make the request
                response = await client.update_product(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.UpdateProductRequest, dict]]):
                The request object. Request message for
                [ProductService.UpdateProduct][google.cloud.retail.v2beta.ProductService.UpdateProduct]
                method.
            product (:class:`google.cloud.retail_v2beta.types.Product`):
                Required. The product to update/create.

                If the caller does not have permission to update the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                If the [Product][google.cloud.retail.v2beta.Product] to
                update does not exist and
                [allow_missing][google.cloud.retail.v2beta.UpdateProductRequest.allow_missing]
                is not set, a NOT_FOUND error is returned.

                This corresponds to the ``product`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which fields in the provided
                [Product][google.cloud.retail.v2beta.Product] to update.
                The immutable and output only fields are NOT supported.
                If not set, all supported fields (the fields that are
                neither immutable nor output only) are updated.

                If an unsupported or unknown field is provided, an
                INVALID_ARGUMENT error is returned.

                The attribute key can be updated by setting the mask
                path as "attributes.${key_name}". If a key name is
                present in the mask but not in the patching product from
                the request, this key will be deleted after the update.

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
            google.cloud.retail_v2beta.types.Product:
                Product captures all metadata
                information of items to be recommended
                or searched.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [product, update_mask]
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
        if not isinstance(request, product_service.UpdateProductRequest):
            request = product_service.UpdateProductRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if product is not None:
            request.product = product
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_product
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("product.name", request.product.name),)
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

    async def delete_product(
        self,
        request: Optional[Union[product_service.DeleteProductRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a [Product][google.cloud.retail.v2beta.Product].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_delete_product():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.DeleteProductRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_product(request=request)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.DeleteProductRequest, dict]]):
                The request object. Request message for
                [ProductService.DeleteProduct][google.cloud.retail.v2beta.ProductService.DeleteProduct]
                method.
            name (:class:`str`):
                Required. Full resource name of
                [Product][google.cloud.retail.v2beta.Product], such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

                If the caller does not have permission to delete the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                If the [Product][google.cloud.retail.v2beta.Product] to
                delete does not exist, a NOT_FOUND error is returned.

                The [Product][google.cloud.retail.v2beta.Product] to
                delete can neither be a
                [Product.Type.COLLECTION][google.cloud.retail.v2beta.Product.Type.COLLECTION]
                [Product][google.cloud.retail.v2beta.Product] member nor
                a
                [Product.Type.PRIMARY][google.cloud.retail.v2beta.Product.Type.PRIMARY]
                [Product][google.cloud.retail.v2beta.Product] with more
                than one
                [variants][google.cloud.retail.v2beta.Product.Type.VARIANT].
                Otherwise, an INVALID_ARGUMENT error is returned.

                All inventory information for the named
                [Product][google.cloud.retail.v2beta.Product] will be
                deleted.

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
        if not isinstance(request, product_service.DeleteProductRequest):
            request = product_service.DeleteProductRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_product
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

    async def purge_products(
        self,
        request: Optional[Union[purge_config.PurgeProductsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Permanently deletes all selected
        [Product][google.cloud.retail.v2beta.Product]s under a branch.

        This process is asynchronous. If the request is valid, the
        removal will be enqueued and processed offline. Depending on the
        number of [Product][google.cloud.retail.v2beta.Product]s, this
        operation could take hours to complete. Before the operation
        completes, some [Product][google.cloud.retail.v2beta.Product]s
        may still be returned by
        [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct]
        or
        [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts].

        Depending on the number of
        [Product][google.cloud.retail.v2beta.Product]s, this operation
        could take hours to complete. To get a sample of
        [Product][google.cloud.retail.v2beta.Product]s that would be
        deleted, set
        [PurgeProductsRequest.force][google.cloud.retail.v2beta.PurgeProductsRequest.force]
        to false.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_purge_products():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.PurgeProductsRequest(
                    parent="parent_value",
                    filter="filter_value",
                )

                # Make the request
                operation = await client.purge_products(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.PurgeProductsRequest, dict]]):
                The request object. Request message for PurgeProducts
                method.
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.PurgeProductsResponse` Response of the PurgeProductsRequest. If the long running operation is
                   successfully done, then this message is returned by
                   the google.longrunning.Operations.response field.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, purge_config.PurgeProductsRequest):
            request = purge_config.PurgeProductsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.purge_products
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
            purge_config.PurgeProductsResponse,
            metadata_type=purge_config.PurgeProductsMetadata,
        )

        # Done; return the response.
        return response

    async def import_products(
        self,
        request: Optional[Union[import_config.ImportProductsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Bulk import of multiple
        [Product][google.cloud.retail.v2beta.Product]s.

        Request processing may be synchronous. Non-existing items are
        created.

        Note that it is possible for a subset of the
        [Product][google.cloud.retail.v2beta.Product]s to be
        successfully updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_import_products():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                input_config = retail_v2beta.ProductInputConfig()
                input_config.product_inline_source.products.title = "title_value"

                request = retail_v2beta.ImportProductsRequest(
                    parent="parent_value",
                    input_config=input_config,
                )

                # Make the request
                operation = await client.import_products(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.ImportProductsRequest, dict]]):
                The request object. Request message for Import methods.
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.ImportProductsResponse` Response of the
                   [ImportProductsRequest][google.cloud.retail.v2beta.ImportProductsRequest].
                   If the long running operation is done, then this
                   message is returned by the
                   google.longrunning.Operations.response field if the
                   operation was successful.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, import_config.ImportProductsRequest):
            request = import_config.ImportProductsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.import_products
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
            import_config.ImportProductsResponse,
            metadata_type=import_config.ImportMetadata,
        )

        # Done; return the response.
        return response

    async def export_products(
        self,
        request: Optional[Union[export_config.ExportProductsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports multiple [Product][google.cloud.retail.v2beta.Product]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_export_products():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                output_config = retail_v2beta.OutputConfig()
                output_config.gcs_destination.output_uri_prefix = "output_uri_prefix_value"

                request = retail_v2beta.ExportProductsRequest(
                    parent="parent_value",
                    output_config=output_config,
                )

                # Make the request
                operation = await client.export_products(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.ExportProductsRequest, dict]]):
                The request object. Request message for ExportProducts
                method.
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.ExportProductsResponse` Response of the ExportProductsRequest. If the long running
                   operation is done, then this message is returned by
                   the google.longrunning.Operations.response field if
                   the operation was successful.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, export_config.ExportProductsRequest):
            request = export_config.ExportProductsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_products
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
            export_config.ExportProductsResponse,
            metadata_type=export_config.ExportMetadata,
        )

        # Done; return the response.
        return response

    async def set_inventory(
        self,
        request: Optional[Union[product_service.SetInventoryRequest, dict]] = None,
        *,
        inventory: Optional[product.Product] = None,
        set_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates inventory information for a
        [Product][google.cloud.retail.v2beta.Product] while respecting
        the last update timestamps of each inventory field.

        This process is asynchronous and does not require the
        [Product][google.cloud.retail.v2beta.Product] to exist before
        updating fulfillment information. If the request is valid, the
        update is enqueued and processed downstream. As a consequence,
        when a response is returned, updates are not immediately
        manifested in the [Product][google.cloud.retail.v2beta.Product]
        queried by
        [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct]
        or
        [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts].

        When inventory is updated with
        [ProductService.CreateProduct][google.cloud.retail.v2beta.ProductService.CreateProduct]
        and
        [ProductService.UpdateProduct][google.cloud.retail.v2beta.ProductService.UpdateProduct],
        the specified inventory field value(s) overwrite any existing
        value(s) while ignoring the last update time for this field.
        Furthermore, the last update times for the specified inventory
        fields are overwritten by the times of the
        [ProductService.CreateProduct][google.cloud.retail.v2beta.ProductService.CreateProduct]
        or
        [ProductService.UpdateProduct][google.cloud.retail.v2beta.ProductService.UpdateProduct]
        request.

        If no inventory fields are set in
        [CreateProductRequest.product][google.cloud.retail.v2beta.CreateProductRequest.product],
        then any pre-existing inventory information for this product is
        used.

        If no inventory fields are set in
        [SetInventoryRequest.set_mask][google.cloud.retail.v2beta.SetInventoryRequest.set_mask],
        then any existing inventory information is preserved.

        Pre-existing inventory information can only be updated with
        [ProductService.SetInventory][google.cloud.retail.v2beta.ProductService.SetInventory],
        [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces],
        and
        [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.RemoveFulfillmentPlaces].

        The returned [Operation][google.longrunning.Operation]s is
        obsolete after one day, and the
        [GetOperation][google.longrunning.Operations.GetOperation] API
        returns ``NOT_FOUND`` afterwards.

        If conflicting updates are issued, the
        [Operation][google.longrunning.Operation]s associated with the
        stale updates are not marked as
        [done][google.longrunning.Operation.done] until they are
        obsolete.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_set_inventory():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                inventory = retail_v2beta.Product()
                inventory.title = "title_value"

                request = retail_v2beta.SetInventoryRequest(
                    inventory=inventory,
                )

                # Make the request
                operation = await client.set_inventory(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.SetInventoryRequest, dict]]):
                The request object. Request message for
                [ProductService.SetInventory][google.cloud.retail.v2beta.ProductService.SetInventory]
                method.
            inventory (:class:`google.cloud.retail_v2beta.types.Product`):
                Required. The inventory information to update. The
                allowable fields to update are:

                - [Product.price_info][google.cloud.retail.v2beta.Product.price_info]
                - [Product.availability][google.cloud.retail.v2beta.Product.availability]
                - [Product.available_quantity][google.cloud.retail.v2beta.Product.available_quantity]
                - [Product.fulfillment_info][google.cloud.retail.v2beta.Product.fulfillment_info]
                  The updated inventory fields must be specified in
                  [SetInventoryRequest.set_mask][google.cloud.retail.v2beta.SetInventoryRequest.set_mask].

                If
                [SetInventoryRequest.inventory.name][google.cloud.retail.v2beta.Product.name]
                is empty or invalid, an INVALID_ARGUMENT error is
                returned.

                If the caller does not have permission to update the
                [Product][google.cloud.retail.v2beta.Product] named in
                [Product.name][google.cloud.retail.v2beta.Product.name],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                If the [Product][google.cloud.retail.v2beta.Product] to
                update does not have existing inventory information, the
                provided inventory information will be inserted.

                If the [Product][google.cloud.retail.v2beta.Product] to
                update has existing inventory information, the provided
                inventory information will be merged while respecting
                the last update time for each inventory field, using the
                provided or default value for
                [SetInventoryRequest.set_time][google.cloud.retail.v2beta.SetInventoryRequest.set_time].

                The caller can replace place IDs for a subset of
                fulfillment types in the following ways:

                - Adds "fulfillment_info" in
                  [SetInventoryRequest.set_mask][google.cloud.retail.v2beta.SetInventoryRequest.set_mask]
                - Specifies only the desired fulfillment types and
                  corresponding place IDs to update in
                  [SetInventoryRequest.inventory.fulfillment_info][google.cloud.retail.v2beta.Product.fulfillment_info]

                The caller can clear all place IDs from a subset of
                fulfillment types in the following ways:

                - Adds "fulfillment_info" in
                  [SetInventoryRequest.set_mask][google.cloud.retail.v2beta.SetInventoryRequest.set_mask]
                - Specifies only the desired fulfillment types to clear
                  in
                  [SetInventoryRequest.inventory.fulfillment_info][google.cloud.retail.v2beta.Product.fulfillment_info]
                - Checks that only the desired fulfillment info types
                  have empty
                  [SetInventoryRequest.inventory.fulfillment_info.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids]

                The last update time is recorded for the following
                inventory fields:

                - [Product.price_info][google.cloud.retail.v2beta.Product.price_info]
                - [Product.availability][google.cloud.retail.v2beta.Product.availability]
                - [Product.available_quantity][google.cloud.retail.v2beta.Product.available_quantity]
                - [Product.fulfillment_info][google.cloud.retail.v2beta.Product.fulfillment_info]

                If a full overwrite of inventory information while
                ignoring timestamps is needed,
                [ProductService.UpdateProduct][google.cloud.retail.v2beta.ProductService.UpdateProduct]
                should be invoked instead.

                This corresponds to the ``inventory`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            set_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which inventory fields in the provided
                [Product][google.cloud.retail.v2beta.Product] to update.

                At least one field must be provided.

                If an unsupported or unknown field is provided, an
                INVALID_ARGUMENT error is returned and the entire update
                will be ignored.

                This corresponds to the ``set_mask`` field
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.SetInventoryResponse` Response of the SetInventoryRequest. Currently empty because
                   there is no meaningful response populated from the
                   [ProductService.SetInventory][google.cloud.retail.v2beta.ProductService.SetInventory]
                   method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [inventory, set_mask]
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
        if not isinstance(request, product_service.SetInventoryRequest):
            request = product_service.SetInventoryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if inventory is not None:
            request.inventory = inventory
        if set_mask is not None:
            request.set_mask = set_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.set_inventory
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("inventory.name", request.inventory.name),)
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
            product_service.SetInventoryResponse,
            metadata_type=product_service.SetInventoryMetadata,
        )

        # Done; return the response.
        return response

    async def add_fulfillment_places(
        self,
        request: Optional[
            Union[product_service.AddFulfillmentPlacesRequest, dict]
        ] = None,
        *,
        product: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""We recommend that you use the
        [ProductService.AddLocalInventories][google.cloud.retail.v2beta.ProductService.AddLocalInventories]
        method instead of the
        [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces]
        method.
        [ProductService.AddLocalInventories][google.cloud.retail.v2beta.ProductService.AddLocalInventories]
        achieves the same results but provides more fine-grained control
        over ingesting local inventory data.

        Incrementally adds place IDs to
        [Product.fulfillment_info.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids].

        This process is asynchronous and does not require the
        [Product][google.cloud.retail.v2beta.Product] to exist before
        updating fulfillment information. If the request is valid, the
        update will be enqueued and processed downstream. As a
        consequence, when a response is returned, the added place IDs
        are not immediately manifested in the
        [Product][google.cloud.retail.v2beta.Product] queried by
        [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct]
        or
        [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts].

        The returned [Operation][google.longrunning.Operation]s will be
        obsolete after 1 day, and
        [GetOperation][google.longrunning.Operations.GetOperation] API
        will return NOT_FOUND afterwards.

        If conflicting updates are issued, the
        [Operation][google.longrunning.Operation]s associated with the
        stale updates will not be marked as
        [done][google.longrunning.Operation.done] until being obsolete.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_add_fulfillment_places():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.AddFulfillmentPlacesRequest(
                    product="product_value",
                    type_="type__value",
                    place_ids=['place_ids_value1', 'place_ids_value2'],
                )

                # Make the request
                operation = await client.add_fulfillment_places(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.AddFulfillmentPlacesRequest, dict]]):
                The request object. Request message for
                [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces]
                method.
            product (:class:`str`):
                Required. Full resource name of
                [Product][google.cloud.retail.v2beta.Product], such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

                If the caller does not have permission to access the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                This corresponds to the ``product`` field
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.AddFulfillmentPlacesResponse` Response of the AddFulfillmentPlacesRequest. Currently empty because
                   there is no meaningful response populated from the
                   [ProductService.AddFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.AddFulfillmentPlaces]
                   method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [product]
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
        if not isinstance(request, product_service.AddFulfillmentPlacesRequest):
            request = product_service.AddFulfillmentPlacesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if product is not None:
            request.product = product

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_fulfillment_places
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("product", request.product),)),
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
            product_service.AddFulfillmentPlacesResponse,
            metadata_type=product_service.AddFulfillmentPlacesMetadata,
        )

        # Done; return the response.
        return response

    async def remove_fulfillment_places(
        self,
        request: Optional[
            Union[product_service.RemoveFulfillmentPlacesRequest, dict]
        ] = None,
        *,
        product: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""We recommend that you use the
        [ProductService.RemoveLocalInventories][google.cloud.retail.v2beta.ProductService.RemoveLocalInventories]
        method instead of the
        [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.RemoveFulfillmentPlaces]
        method.
        [ProductService.RemoveLocalInventories][google.cloud.retail.v2beta.ProductService.RemoveLocalInventories]
        achieves the same results but provides more fine-grained control
        over ingesting local inventory data.

        Incrementally removes place IDs from a
        [Product.fulfillment_info.place_ids][google.cloud.retail.v2beta.FulfillmentInfo.place_ids].

        This process is asynchronous and does not require the
        [Product][google.cloud.retail.v2beta.Product] to exist before
        updating fulfillment information. If the request is valid, the
        update will be enqueued and processed downstream. As a
        consequence, when a response is returned, the removed place IDs
        are not immediately manifested in the
        [Product][google.cloud.retail.v2beta.Product] queried by
        [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct]
        or
        [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts].

        The returned [Operation][google.longrunning.Operation]s will be
        obsolete after 1 day, and
        [GetOperation][google.longrunning.Operations.GetOperation] API
        will return NOT_FOUND afterwards.

        If conflicting updates are issued, the
        [Operation][google.longrunning.Operation]s associated with the
        stale updates will not be marked as
        [done][google.longrunning.Operation.done] until being obsolete.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_remove_fulfillment_places():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.RemoveFulfillmentPlacesRequest(
                    product="product_value",
                    type_="type__value",
                    place_ids=['place_ids_value1', 'place_ids_value2'],
                )

                # Make the request
                operation = await client.remove_fulfillment_places(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.RemoveFulfillmentPlacesRequest, dict]]):
                The request object. Request message for
                [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.RemoveFulfillmentPlaces]
                method.
            product (:class:`str`):
                Required. Full resource name of
                [Product][google.cloud.retail.v2beta.Product], such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

                If the caller does not have permission to access the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                This corresponds to the ``product`` field
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.RemoveFulfillmentPlacesResponse` Response of the RemoveFulfillmentPlacesRequest. Currently empty because there
                   is no meaningful response populated from the
                   [ProductService.RemoveFulfillmentPlaces][google.cloud.retail.v2beta.ProductService.RemoveFulfillmentPlaces]
                   method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [product]
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
        if not isinstance(request, product_service.RemoveFulfillmentPlacesRequest):
            request = product_service.RemoveFulfillmentPlacesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if product is not None:
            request.product = product

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_fulfillment_places
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("product", request.product),)),
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
            product_service.RemoveFulfillmentPlacesResponse,
            metadata_type=product_service.RemoveFulfillmentPlacesMetadata,
        )

        # Done; return the response.
        return response

    async def add_local_inventories(
        self,
        request: Optional[
            Union[product_service.AddLocalInventoriesRequest, dict]
        ] = None,
        *,
        product: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates local inventory information for a
        [Product][google.cloud.retail.v2beta.Product] at a list of
        places, while respecting the last update timestamps of each
        inventory field.

        This process is asynchronous and does not require the
        [Product][google.cloud.retail.v2beta.Product] to exist before
        updating inventory information. If the request is valid, the
        update will be enqueued and processed downstream. As a
        consequence, when a response is returned, updates are not
        immediately manifested in the
        [Product][google.cloud.retail.v2beta.Product] queried by
        [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct]
        or
        [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts].

        Local inventory information can only be modified using this
        method.
        [ProductService.CreateProduct][google.cloud.retail.v2beta.ProductService.CreateProduct]
        and
        [ProductService.UpdateProduct][google.cloud.retail.v2beta.ProductService.UpdateProduct]
        has no effect on local inventories.

        The returned [Operation][google.longrunning.Operation]s will be
        obsolete after 1 day, and
        [GetOperation][google.longrunning.Operations.GetOperation] API
        will return NOT_FOUND afterwards.

        If conflicting updates are issued, the
        [Operation][google.longrunning.Operation]s associated with the
        stale updates will not be marked as
        [done][google.longrunning.Operation.done] until being obsolete.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_add_local_inventories():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.AddLocalInventoriesRequest(
                    product="product_value",
                )

                # Make the request
                operation = await client.add_local_inventories(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.AddLocalInventoriesRequest, dict]]):
                The request object. Request message for
                [ProductService.AddLocalInventories][google.cloud.retail.v2beta.ProductService.AddLocalInventories]
                method.
            product (:class:`str`):
                Required. Full resource name of
                [Product][google.cloud.retail.v2beta.Product], such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

                If the caller does not have permission to access the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                This corresponds to the ``product`` field
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.AddLocalInventoriesResponse` Response of the
                   [ProductService.AddLocalInventories][google.cloud.retail.v2beta.ProductService.AddLocalInventories]
                   API. Currently empty because there is no meaningful
                   response populated from the
                   [ProductService.AddLocalInventories][google.cloud.retail.v2beta.ProductService.AddLocalInventories]
                   method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [product]
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
        if not isinstance(request, product_service.AddLocalInventoriesRequest):
            request = product_service.AddLocalInventoriesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if product is not None:
            request.product = product

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_local_inventories
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("product", request.product),)),
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
            product_service.AddLocalInventoriesResponse,
            metadata_type=product_service.AddLocalInventoriesMetadata,
        )

        # Done; return the response.
        return response

    async def remove_local_inventories(
        self,
        request: Optional[
            Union[product_service.RemoveLocalInventoriesRequest, dict]
        ] = None,
        *,
        product: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Remove local inventory information for a
        [Product][google.cloud.retail.v2beta.Product] at a list of
        places at a removal timestamp.

        This process is asynchronous. If the request is valid, the
        removal will be enqueued and processed downstream. As a
        consequence, when a response is returned, removals are not
        immediately manifested in the
        [Product][google.cloud.retail.v2beta.Product] queried by
        [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct]
        or
        [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts].

        Local inventory information can only be removed using this
        method.
        [ProductService.CreateProduct][google.cloud.retail.v2beta.ProductService.CreateProduct]
        and
        [ProductService.UpdateProduct][google.cloud.retail.v2beta.ProductService.UpdateProduct]
        has no effect on local inventories.

        The returned [Operation][google.longrunning.Operation]s will be
        obsolete after 1 day, and
        [GetOperation][google.longrunning.Operations.GetOperation] API
        will return NOT_FOUND afterwards.

        If conflicting updates are issued, the
        [Operation][google.longrunning.Operation]s associated with the
        stale updates will not be marked as
        [done][google.longrunning.Operation.done] until being obsolete.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_remove_local_inventories():
                # Create a client
                client = retail_v2beta.ProductServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.RemoveLocalInventoriesRequest(
                    product="product_value",
                    place_ids=['place_ids_value1', 'place_ids_value2'],
                )

                # Make the request
                operation = await client.remove_local_inventories(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.RemoveLocalInventoriesRequest, dict]]):
                The request object. Request message for
                [ProductService.RemoveLocalInventories][google.cloud.retail.v2beta.ProductService.RemoveLocalInventories]
                method.
            product (:class:`str`):
                Required. Full resource name of
                [Product][google.cloud.retail.v2beta.Product], such as
                ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/some_product_id``.

                If the caller does not have permission to access the
                [Product][google.cloud.retail.v2beta.Product],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                This corresponds to the ``product`` field
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

                The result type for the operation will be :class:`google.cloud.retail_v2beta.types.RemoveLocalInventoriesResponse` Response of the
                   [ProductService.RemoveLocalInventories][google.cloud.retail.v2beta.ProductService.RemoveLocalInventories]
                   API. Currently empty because there is no meaningful
                   response populated from the
                   [ProductService.RemoveLocalInventories][google.cloud.retail.v2beta.ProductService.RemoveLocalInventories]
                   method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [product]
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
        if not isinstance(request, product_service.RemoveLocalInventoriesRequest):
            request = product_service.RemoveLocalInventoriesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if product is not None:
            request.product = product

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_local_inventories
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("product", request.product),)),
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
            product_service.RemoveLocalInventoriesResponse,
            metadata_type=product_service.RemoveLocalInventoriesMetadata,
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

    async def __aenter__(self) -> "ProductServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ProductServiceAsyncClient",)
