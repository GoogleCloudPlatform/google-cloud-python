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

from google.shopping.merchant_inventories_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.shopping.merchant_inventories_v1.services.regional_inventory_service import (
    pagers,
)
from google.shopping.merchant_inventories_v1.types import (
    inventories_common,
    regionalinventory,
)

from .client import RegionalInventoryServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, RegionalInventoryServiceTransport
from .transports.grpc_asyncio import RegionalInventoryServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class RegionalInventoryServiceAsyncClient:
    """Service to manage regional inventory for products. There is also
    separate ``regions`` resource and API to manage regions definitions.
    """

    _client: RegionalInventoryServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = RegionalInventoryServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = RegionalInventoryServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        RegionalInventoryServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = RegionalInventoryServiceClient._DEFAULT_UNIVERSE

    regional_inventory_path = staticmethod(
        RegionalInventoryServiceClient.regional_inventory_path
    )
    parse_regional_inventory_path = staticmethod(
        RegionalInventoryServiceClient.parse_regional_inventory_path
    )
    common_billing_account_path = staticmethod(
        RegionalInventoryServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        RegionalInventoryServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(RegionalInventoryServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        RegionalInventoryServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        RegionalInventoryServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        RegionalInventoryServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        RegionalInventoryServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        RegionalInventoryServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        RegionalInventoryServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        RegionalInventoryServiceClient.parse_common_location_path
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
            RegionalInventoryServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            RegionalInventoryServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(RegionalInventoryServiceAsyncClient, info, *args, **kwargs)

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
            RegionalInventoryServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            RegionalInventoryServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            RegionalInventoryServiceAsyncClient, filename, *args, **kwargs
        )

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
        return RegionalInventoryServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> RegionalInventoryServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            RegionalInventoryServiceTransport: The transport used by the client instance.
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

    get_transport_class = RegionalInventoryServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                RegionalInventoryServiceTransport,
                Callable[..., RegionalInventoryServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the regional inventory service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,RegionalInventoryServiceTransport,Callable[..., RegionalInventoryServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the RegionalInventoryServiceTransport constructor.
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
        self._client = RegionalInventoryServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.inventories_v1.RegionalInventoryServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.inventories.v1.RegionalInventoryService",
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
                    "serviceName": "google.shopping.merchant.inventories.v1.RegionalInventoryService",
                    "credentialsType": None,
                },
            )

    async def list_regional_inventories(
        self,
        request: Optional[
            Union[regionalinventory.ListRegionalInventoriesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRegionalInventoriesAsyncPager:
        r"""Lists the ``RegionalInventory`` resources for the given product
        in your merchant account. The response might contain fewer items
        than specified by ``pageSize``. If ``pageToken`` was returned in
        previous request, it can be used to obtain additional results.

        ``RegionalInventory`` resources are listed per product for a
        given account.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_inventories_v1

            async def sample_list_regional_inventories():
                # Create a client
                client = merchant_inventories_v1.RegionalInventoryServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_inventories_v1.ListRegionalInventoriesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_regional_inventories(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_inventories_v1.types.ListRegionalInventoriesRequest, dict]]):
                The request object. Request message for the ``ListRegionalInventories``
                method.
            parent (:class:`str`):
                Required. The ``name`` of the parent product to list
                ``RegionalInventory`` resources for. Format:
                ``accounts/{account}/products/{product}``

                The ``{product}`` segment is a unique identifier for the
                product. This identifier must be unique within a
                merchant account and generally follows the structure:
                ``content_language~feed_label~offer_id``. Example:
                ``en~US~sku123`` For legacy local products, the
                structure is:
                ``local~content_language~feed_label~offer_id``. Example:
                ``local~en~US~sku123``

                The format of the ``{product}`` segment in the URL is
                automatically detected by the server, supporting two
                options:

                1. **Encoded Format**: The ``{product}`` segment is an
                   **unpadded base64url** encoded string (RFC 4648
                   Section 5). The decoded string must result in the
                   ``content_language~feed_label~offer_id`` structure.
                   This encoding MUST be used if any part of the product
                   identifier (like ``offer_id``) contains characters
                   such as ``/``, ``%``, or ``~``.

                   - Example: To represent the product ID
                     ``en~US~sku/123``, the ``{product}`` segment must
                     be the unpadded base64url encoding of this string,
                     which is ``ZW5-VVN-c2t1LzEyMw``. The full resource
                     name for the product would be
                     ``accounts/123/products/ZW5-VVN-c2t1LzEyMw``.

                2. **Plain Format**: The ``{product}`` segment is the
                   tilde-separated string
                   ``content_language~feed_label~offer_id``. This format
                   is suitable only when ``content_language``,
                   ``feed_label``, and ``offer_id`` do not contain
                   URL-problematic characters like ``/``, ``%``, or
                   ``~``.

                We recommend using the **Encoded Format** for all
                product IDs to ensure correct parsing, especially those
                containing special characters. The presence of tilde
                (``~``) characters in the ``{product}`` segment is used
                to differentiate between the two formats.

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
            google.shopping.merchant_inventories_v1.services.regional_inventory_service.pagers.ListRegionalInventoriesAsyncPager:
                Response message for the ListRegionalInventories method.

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
        if not isinstance(request, regionalinventory.ListRegionalInventoriesRequest):
            request = regionalinventory.ListRegionalInventoriesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_regional_inventories
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
        response = pagers.ListRegionalInventoriesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def insert_regional_inventory(
        self,
        request: Optional[
            Union[regionalinventory.InsertRegionalInventoryRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> regionalinventory.RegionalInventory:
        r"""Inserts a ``RegionalInventory`` to a given product in your
        merchant account.

        Replaces the full ``RegionalInventory`` resource if an entry
        with the same
        [``region``][google.shopping.merchant.inventories.v1.RegionalInventory.region]
        already exists for the product.

        It might take up to 30 minutes for the new or updated
        ``RegionalInventory`` resource to appear in products.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_inventories_v1

            async def sample_insert_regional_inventory():
                # Create a client
                client = merchant_inventories_v1.RegionalInventoryServiceAsyncClient()

                # Initialize request argument(s)
                regional_inventory = merchant_inventories_v1.RegionalInventory()
                regional_inventory.region = "region_value"

                request = merchant_inventories_v1.InsertRegionalInventoryRequest(
                    parent="parent_value",
                    regional_inventory=regional_inventory,
                )

                # Make the request
                response = await client.insert_regional_inventory(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_inventories_v1.types.InsertRegionalInventoryRequest, dict]]):
                The request object. Request message for the ``InsertRegionalInventory``
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.shopping.merchant_inventories_v1.types.RegionalInventory:
                Regional inventory information for the product. Represents specific
                   information like price and availability for a given
                   product in a specific
                   [region][google.shopping.merchant.inventories.v1.RegionalInventory.region].
                   For a list of all accepted attribute values, see the
                   [regional product inventory data
                   specification](https://support.google.com/merchants/answer/9698880).

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, regionalinventory.InsertRegionalInventoryRequest):
            request = regionalinventory.InsertRegionalInventoryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.insert_regional_inventory
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

    async def delete_regional_inventory(
        self,
        request: Optional[
            Union[regionalinventory.DeleteRegionalInventoryRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the specified ``RegionalInventory`` resource from the
        given product in your merchant account. It might take up to an
        hour for the ``RegionalInventory`` to be deleted from the
        specific product. Once you have received a successful delete
        response, wait for that period before attempting a delete again.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_inventories_v1

            async def sample_delete_regional_inventory():
                # Create a client
                client = merchant_inventories_v1.RegionalInventoryServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_inventories_v1.DeleteRegionalInventoryRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_regional_inventory(request=request)

        Args:
            request (Optional[Union[google.shopping.merchant_inventories_v1.types.DeleteRegionalInventoryRequest, dict]]):
                The request object. Request message for the ``DeleteRegionalInventory``
                method.
            name (:class:`str`):
                Required. The name of the ``RegionalInventory`` resource
                to delete. Format:
                ``accounts/{account}/products/{product}/regionalInventories/{region}``

                The ``{product}`` segment is a unique identifier for the
                product. This identifier must be unique within a
                merchant account and generally follows the structure:
                ``content_language~feed_label~offer_id``. Example:
                ``en~US~sku123`` For legacy local products, the
                structure is:
                ``local~content_language~feed_label~offer_id``. Example:
                ``local~en~US~sku123``

                The format of the ``{product}`` segment in the URL is
                automatically detected by the server, supporting two
                options:

                1. **Encoded Format**: The ``{product}`` segment is an
                   **unpadded base64url** encoded string (RFC 4648
                   Section 5). The decoded string must result in the
                   ``content_language~feed_label~offer_id`` structure.
                   This encoding MUST be used if any part of the product
                   identifier (like ``offer_id``) contains characters
                   such as ``/``, ``%``, or ``~``.

                   - Example: To represent the product ID
                     ``en~US~sku/123`` for ``region`` "region123", the
                     ``{product}`` segment must be the unpadded
                     base64url encoding of this string, which is
                     ``ZW5-VVN-c2t1LzEyMw``. The full resource name for
                     the regional inventory would be
                     ``accounts/123/products/ZW5-VVN-c2t1LzEyMw/regionalInventories/region123``.

                2. **Plain Format**: The ``{product}`` segment is the
                   tilde-separated string
                   ``content_language~feed_label~offer_id``. This format
                   is suitable only when ``content_language``,
                   ``feed_label``, and ``offer_id`` do not contain
                   URL-problematic characters like ``/``, ``%``, or
                   ``~``.

                We recommend using the **Encoded Format** for all
                product IDs to ensure correct parsing, especially those
                containing special characters. The presence of tilde
                (``~``) characters in the ``{product}`` segment is used
                to differentiate between the two formats.

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
        if not isinstance(request, regionalinventory.DeleteRegionalInventoryRequest):
            request = regionalinventory.DeleteRegionalInventoryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_regional_inventory
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

    async def __aenter__(self) -> "RegionalInventoryServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("RegionalInventoryServiceAsyncClient",)
