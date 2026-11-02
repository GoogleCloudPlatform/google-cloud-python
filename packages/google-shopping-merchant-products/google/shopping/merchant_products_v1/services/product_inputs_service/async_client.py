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

from google.shopping.merchant_products_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
from google.shopping.type.types import types

from google.shopping.merchant_products_v1.types import productinputs, products_common

from .client import ProductInputsServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, ProductInputsServiceTransport
from .transports.grpc_asyncio import ProductInputsServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ProductInputsServiceAsyncClient:
    """Service to use ProductInput resource."""

    _client: ProductInputsServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ProductInputsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ProductInputsServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = ProductInputsServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = ProductInputsServiceClient._DEFAULT_UNIVERSE

    product_path = staticmethod(ProductInputsServiceClient.product_path)
    parse_product_path = staticmethod(ProductInputsServiceClient.parse_product_path)
    product_input_path = staticmethod(ProductInputsServiceClient.product_input_path)
    parse_product_input_path = staticmethod(
        ProductInputsServiceClient.parse_product_input_path
    )
    common_billing_account_path = staticmethod(
        ProductInputsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ProductInputsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ProductInputsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ProductInputsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ProductInputsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ProductInputsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ProductInputsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        ProductInputsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(ProductInputsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        ProductInputsServiceClient.parse_common_location_path
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
            ProductInputsServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            ProductInputsServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(ProductInputsServiceAsyncClient, info, *args, **kwargs)

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
            ProductInputsServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            ProductInputsServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(ProductInputsServiceAsyncClient, filename, *args, **kwargs)

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
        return ProductInputsServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> ProductInputsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ProductInputsServiceTransport: The transport used by the client instance.
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

    get_transport_class = ProductInputsServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                ProductInputsServiceTransport,
                Callable[..., ProductInputsServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the product inputs service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ProductInputsServiceTransport,Callable[..., ProductInputsServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ProductInputsServiceTransport constructor.
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
        self._client = ProductInputsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.products_v1.ProductInputsServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.products.v1.ProductInputsService",
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
                    "serviceName": "google.shopping.merchant.products.v1.ProductInputsService",
                    "credentialsType": None,
                },
            )

    async def insert_product_input(
        self,
        request: Optional[Union[productinputs.InsertProductInputRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> productinputs.ProductInput:
        r"""`Uploads a product input to your Merchant Center
        account </merchant/api/guides/products/add-manage#add_a_product>`__.
        You must have a products `data
        source </merchant/api/guides/data-sources/api-sources#create-primary-data-source>`__
        to be able to insert a product. The unique identifier of the
        data source is passed as a query parameter in the request URL.

        If a product input with the same contentLanguage, offerId, and
        dataSource already exists, then the product input inserted by
        this method replaces that entry.

        After inserting, updating, or deleting a product input, it may
        take several minutes before the processed product can be
        retrieved.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_products_v1

            async def sample_insert_product_input():
                # Create a client
                client = merchant_products_v1.ProductInputsServiceAsyncClient()

                # Initialize request argument(s)
                product_input = merchant_products_v1.ProductInput()
                product_input.offer_id = "offer_id_value"
                product_input.content_language = "content_language_value"
                product_input.feed_label = "feed_label_value"

                request = merchant_products_v1.InsertProductInputRequest(
                    parent="parent_value",
                    product_input=product_input,
                    data_source="data_source_value",
                )

                # Make the request
                response = await client.insert_product_input(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_products_v1.types.InsertProductInputRequest, dict]]):
                The request object. Request message for the
                InsertProductInput method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.shopping.merchant_products_v1.types.ProductInput:
                This resource represents input data you submit for a product, not the
                   processed product that you see in Merchant Center, in
                   Shopping ads, or across Google surfaces. Product
                   inputs, rules and supplemental data source data are
                   combined to create the processed
                   [Product][google.shopping.merchant.products.v1.Product].
                   For more information, see [Manage
                   products](/merchant/api/guides/products/overview).

                   Required product input attributes to pass data
                   validation checks are primarily defined in the
                   [Products Data
                   Specification](https://support.google.com/merchants/answer/188494).

                   The following attributes are required:
                   [feedLabel][google.shopping.merchant.products.v1.Product.feed_label],
                   [contentLanguage][google.shopping.merchant.products.v1.Product.content_language]
                   and
                   [offerId][google.shopping.merchant.products.v1.Product.offer_id].

                   After inserting, updating, or deleting a product
                   input, it may take several minutes before the
                   processed product can be retrieved.

                   All fields in the product input and its sub-messages
                   match the English name of their corresponding
                   attribute in the [Products Data
                   Specification](https://support.google.com/merchants/answer/188494)
                   with [some
                   exceptions](https://support.google.com/merchants/answer/7052112).
                   The following reference documentation lists the field
                   names in the **camelCase** casing style while the
                   Products Data Specification lists the names in the
                   **snake_case** casing style.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, productinputs.InsertProductInputRequest):
            request = productinputs.InsertProductInputRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.insert_product_input
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

    async def update_product_input(
        self,
        request: Optional[Union[productinputs.UpdateProductInputRequest, dict]] = None,
        *,
        product_input: Optional[productinputs.ProductInput] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> productinputs.ProductInput:
        r"""Updates the existing product input in your Merchant Center
        account. The name of the product input to update is taken from
        the ``name`` field within the ``ProductInput`` resource.

        After inserting, updating, or deleting a product input, it may
        take several minutes before the processed product can be
        retrieved.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_products_v1

            async def sample_update_product_input():
                # Create a client
                client = merchant_products_v1.ProductInputsServiceAsyncClient()

                # Initialize request argument(s)
                product_input = merchant_products_v1.ProductInput()
                product_input.offer_id = "offer_id_value"
                product_input.content_language = "content_language_value"
                product_input.feed_label = "feed_label_value"

                request = merchant_products_v1.UpdateProductInputRequest(
                    product_input=product_input,
                    data_source="data_source_value",
                )

                # Make the request
                response = await client.update_product_input(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_products_v1.types.UpdateProductInputRequest, dict]]):
                The request object. Request message for the
                UpdateProductInput method. The product
                (primary input) must exist for the
                update to succeed. If the update is for
                a primary product input, the existing
                primary product input must be from the
                same data source.
            product_input (:class:`google.shopping.merchant_products_v1.types.ProductInput`):
                Required. The product input resource to update.
                Information you submit will be applied to the processed
                product as well. The ``name`` field within this resource
                identifies the product input to be updated.

                This corresponds to the ``product_input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of product attributes to be updated.

                If the update mask is omitted, then it is treated as
                implied field mask equivalent to all fields that are
                populated (have a non-empty value).

                Attributes specified in the update mask without a value
                specified in the body will be deleted from the product.

                Update mask can only be specified for top level fields
                in attributes and custom attributes.

                To specify the update mask for custom attributes you
                need to add the ``custom_attribute.`` prefix.

                Providing special "\*" value for full product
                replacement is not supported.

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
            google.shopping.merchant_products_v1.types.ProductInput:
                This resource represents input data you submit for a product, not the
                   processed product that you see in Merchant Center, in
                   Shopping ads, or across Google surfaces. Product
                   inputs, rules and supplemental data source data are
                   combined to create the processed
                   [Product][google.shopping.merchant.products.v1.Product].
                   For more information, see [Manage
                   products](/merchant/api/guides/products/overview).

                   Required product input attributes to pass data
                   validation checks are primarily defined in the
                   [Products Data
                   Specification](https://support.google.com/merchants/answer/188494).

                   The following attributes are required:
                   [feedLabel][google.shopping.merchant.products.v1.Product.feed_label],
                   [contentLanguage][google.shopping.merchant.products.v1.Product.content_language]
                   and
                   [offerId][google.shopping.merchant.products.v1.Product.offer_id].

                   After inserting, updating, or deleting a product
                   input, it may take several minutes before the
                   processed product can be retrieved.

                   All fields in the product input and its sub-messages
                   match the English name of their corresponding
                   attribute in the [Products Data
                   Specification](https://support.google.com/merchants/answer/188494)
                   with [some
                   exceptions](https://support.google.com/merchants/answer/7052112).
                   The following reference documentation lists the field
                   names in the **camelCase** casing style while the
                   Products Data Specification lists the names in the
                   **snake_case** casing style.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [product_input, update_mask]
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
        if not isinstance(request, productinputs.UpdateProductInputRequest):
            request = productinputs.UpdateProductInputRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if product_input is not None:
            request.product_input = product_input
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_product_input
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("product_input.name", request.product_input.name),)
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

    async def delete_product_input(
        self,
        request: Optional[Union[productinputs.DeleteProductInputRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a product input from your Merchant Center
        account.
        After inserting, updating, or deleting a product input,
        it may take several minutes before the processed product
        can be retrieved.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_products_v1

            async def sample_delete_product_input():
                # Create a client
                client = merchant_products_v1.ProductInputsServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_products_v1.DeleteProductInputRequest(
                    name="name_value",
                    data_source="data_source_value",
                )

                # Make the request
                await client.delete_product_input(request=request)

        Args:
            request (Optional[Union[google.shopping.merchant_products_v1.types.DeleteProductInputRequest, dict]]):
                The request object. Request message for the
                DeleteProductInput method.
            name (:class:`str`):
                Required. The name of the product input to delete.
                Format:
                ``accounts/{account}/productInputs/{productInput}``

                The {productInput} segment is a unique identifier for
                the product. This identifier must be unique within a
                merchant account and generally follows the structure:
                ``content_language~feed_label~offer_id``. Example:
                ``en~US~sku123`` For legacy local products, the
                structure is:
                ``local~content_language~feed_label~offer_id``. Example:
                ``local~en~US~sku123``

                The format of the {productInput} segment in the URL is
                automatically detected by the server, supporting two
                options:

                1. **Encoded Format**: The ``{productInput}`` segment is
                   an unpadded base64url encoded string (RFC 4648
                   Section 5). The decoded string must result in the
                   ``content_language~feed_label~offer_id`` structure.
                   This encoding MUST be used if any part of the product
                   identifier (like ``offer_id``) contains characters
                   such as ``/``, ``%``, or ``~``.

                   - Example: To represent the product ID
                     ``en~US~sku/123``, the ``{productInput}`` segment
                     must be the unpadded base64url encoding of this
                     string, which is ``ZW5-VVN-c2t1LzEyMw``. The full
                     resource name for the product would be
                     ``accounts/123/productInputs/ZW5-VVN-c2t1LzEyMw``.

                2. **Plain Format**: The ``{productInput}`` segment is
                   the tilde-separated string
                   ``content_language~feed_label~offer_id``. This format
                   is suitable only when ``content_language``,
                   ``feed_label``, and ``offer_id`` do not contain
                   URL-problematic characters like ``/``, ``%``, or
                   ``~``.

                We recommend using the **Encoded Format** for all
                product IDs to ensure correct parsing, especially those
                containing special characters. The presence of tilde
                (``~``) characters in the ``{productInput}`` segment is
                used to differentiate between the two formats.

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
        if not isinstance(request, productinputs.DeleteProductInputRequest):
            request = productinputs.DeleteProductInputRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_product_input
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

    async def __aenter__(self) -> "ProductInputsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ProductInputsServiceAsyncClient",)
