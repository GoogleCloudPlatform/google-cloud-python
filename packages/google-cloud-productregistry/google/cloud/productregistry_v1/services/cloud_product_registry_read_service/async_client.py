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

from google.cloud.productregistry_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.productregistry_v1.services.cloud_product_registry_read_service import (
    pagers,
)
from google.cloud.productregistry_v1.types import (
    cloud_product_registry_read_service,
    lifecycle_state,
    logical_product,
    logical_product_variant,
    product_suite,
)

from .client import CloudProductRegistryReadServiceClient
from .transports.base import (
    DEFAULT_CLIENT_INFO,
    CloudProductRegistryReadServiceTransport,
)
from .transports.grpc_asyncio import CloudProductRegistryReadServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class CloudProductRegistryReadServiceAsyncClient:
    """Cloud Product Registry Read Service provides capabilities to
    access all first and third party Google Cloud products.
    """

    _client: CloudProductRegistryReadServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = CloudProductRegistryReadServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CloudProductRegistryReadServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        CloudProductRegistryReadServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = CloudProductRegistryReadServiceClient._DEFAULT_UNIVERSE

    logical_product_path = staticmethod(
        CloudProductRegistryReadServiceClient.logical_product_path
    )
    parse_logical_product_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_logical_product_path
    )
    logical_product_variant_path = staticmethod(
        CloudProductRegistryReadServiceClient.logical_product_variant_path
    )
    parse_logical_product_variant_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_logical_product_variant_path
    )
    product_suite_path = staticmethod(
        CloudProductRegistryReadServiceClient.product_suite_path
    )
    parse_product_suite_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_product_suite_path
    )
    common_billing_account_path = staticmethod(
        CloudProductRegistryReadServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        CloudProductRegistryReadServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        CloudProductRegistryReadServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        CloudProductRegistryReadServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        CloudProductRegistryReadServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        CloudProductRegistryReadServiceClient.parse_common_location_path
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
            CloudProductRegistryReadServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            CloudProductRegistryReadServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(
            CloudProductRegistryReadServiceAsyncClient, info, *args, **kwargs
        )

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
            CloudProductRegistryReadServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            CloudProductRegistryReadServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            CloudProductRegistryReadServiceAsyncClient, filename, *args, **kwargs
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
        return CloudProductRegistryReadServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> CloudProductRegistryReadServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudProductRegistryReadServiceTransport: The transport used by the client instance.
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

    get_transport_class = CloudProductRegistryReadServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                CloudProductRegistryReadServiceTransport,
                Callable[..., CloudProductRegistryReadServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud product registry read service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CloudProductRegistryReadServiceTransport,Callable[..., CloudProductRegistryReadServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CloudProductRegistryReadServiceTransport constructor.
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
        self._client = CloudProductRegistryReadServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.productregistry_v1.CloudProductRegistryReadServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
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
                    "serviceName": "google.cloud.productregistry.v1.CloudProductRegistryReadService",
                    "credentialsType": None,
                },
            )

    async def get_product_suite(
        self,
        request: Optional[
            Union[cloud_product_registry_read_service.GetProductSuiteRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> product_suite.ProductSuite:
        r"""Get details of a ProductSuite.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import productregistry_v1

            async def sample_get_product_suite():
                # Create a client
                client = productregistry_v1.CloudProductRegistryReadServiceAsyncClient()

                # Initialize request argument(s)
                request = productregistry_v1.GetProductSuiteRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_product_suite(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.productregistry_v1.types.GetProductSuiteRequest, dict]]):
                The request object. Request message for GetProductSuite.
            name (:class:`str`):
                Required. The name of the ProductSuite to retrieve.
                Format: productSuites/{product_suite}

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
            google.cloud.productregistry_v1.types.ProductSuite:
                Represents a unified grouping of
                products sharing a common brand and
                market positioning.

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
            request, cloud_product_registry_read_service.GetProductSuiteRequest
        ):
            request = cloud_product_registry_read_service.GetProductSuiteRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_product_suite
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

    async def list_product_suites(
        self,
        request: Optional[
            Union[cloud_product_registry_read_service.ListProductSuitesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListProductSuitesAsyncPager:
        r"""Lists ProductSuites.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import productregistry_v1

            async def sample_list_product_suites():
                # Create a client
                client = productregistry_v1.CloudProductRegistryReadServiceAsyncClient()

                # Initialize request argument(s)
                request = productregistry_v1.ListProductSuitesRequest(
                )

                # Make the request
                page_result = client.list_product_suites(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.productregistry_v1.types.ListProductSuitesRequest, dict]]):
                The request object. Request message for
                ListProductSuites.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListProductSuitesAsyncPager:
                Response message for
                ListProductSuites.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_product_registry_read_service.ListProductSuitesRequest
        ):
            request = cloud_product_registry_read_service.ListProductSuitesRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_product_suites
        ]

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
        response = pagers.ListProductSuitesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_logical_product(
        self,
        request: Optional[
            Union[cloud_product_registry_read_service.GetLogicalProductRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> logical_product.LogicalProduct:
        r"""Gets details of a LogicalProduct.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import productregistry_v1

            async def sample_get_logical_product():
                # Create a client
                client = productregistry_v1.CloudProductRegistryReadServiceAsyncClient()

                # Initialize request argument(s)
                request = productregistry_v1.GetLogicalProductRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_logical_product(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.productregistry_v1.types.GetLogicalProductRequest, dict]]):
                The request object. Request message for
                GetLogicalProduct.
            name (:class:`str`):
                Required. The name of the LogicalProduct to retrieve.
                Format: logicalProducts/{logical_product}

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
            google.cloud.productregistry_v1.types.LogicalProduct:
                Represents an independent service
                offering that can be provisioned by a
                customer.

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
            request, cloud_product_registry_read_service.GetLogicalProductRequest
        ):
            request = cloud_product_registry_read_service.GetLogicalProductRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_logical_product
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

    async def list_logical_products(
        self,
        request: Optional[
            Union[cloud_product_registry_read_service.ListLogicalProductsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListLogicalProductsAsyncPager:
        r"""Lists LogicalProducts matching given criteria.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import productregistry_v1

            async def sample_list_logical_products():
                # Create a client
                client = productregistry_v1.CloudProductRegistryReadServiceAsyncClient()

                # Initialize request argument(s)
                request = productregistry_v1.ListLogicalProductsRequest(
                )

                # Make the request
                page_result = client.list_logical_products(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.productregistry_v1.types.ListLogicalProductsRequest, dict]]):
                The request object. Request message for
                ListLogicalProducts.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductsAsyncPager:
                Response message for
                ListLogicalProducts.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_product_registry_read_service.ListLogicalProductsRequest
        ):
            request = cloud_product_registry_read_service.ListLogicalProductsRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_logical_products
        ]

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
        response = pagers.ListLogicalProductsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_logical_product_variant(
        self,
        request: Optional[
            Union[
                cloud_product_registry_read_service.GetLogicalProductVariantRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> logical_product_variant.LogicalProductVariant:
        r"""Get details of a LogicalProductVariant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import productregistry_v1

            async def sample_get_logical_product_variant():
                # Create a client
                client = productregistry_v1.CloudProductRegistryReadServiceAsyncClient()

                # Initialize request argument(s)
                request = productregistry_v1.GetLogicalProductVariantRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_logical_product_variant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.productregistry_v1.types.GetLogicalProductVariantRequest, dict]]):
                The request object. Request message for
                GetLogicalProductVariant.
            name (:class:`str`):
                Required. The name of the LogicalProductVariant to
                retrieve. Format:
                logicalProducts/{logical_product}/variants/{variant}

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
            google.cloud.productregistry_v1.types.LogicalProductVariant:
                Represents a distinct offering
                derived from a primary product that
                retains core functionalities but offers
                specialized features for a specific
                market segment.

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
            request, cloud_product_registry_read_service.GetLogicalProductVariantRequest
        ):
            request = (
                cloud_product_registry_read_service.GetLogicalProductVariantRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_logical_product_variant
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

    async def list_logical_product_variants(
        self,
        request: Optional[
            Union[
                cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListLogicalProductVariantsAsyncPager:
        r"""Lists LogicalProductVariants matching given criteria.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import productregistry_v1

            async def sample_list_logical_product_variants():
                # Create a client
                client = productregistry_v1.CloudProductRegistryReadServiceAsyncClient()

                # Initialize request argument(s)
                request = productregistry_v1.ListLogicalProductVariantsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_logical_product_variants(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.productregistry_v1.types.ListLogicalProductVariantsRequest, dict]]):
                The request object. Request message for
                ListLogicalProductVariants.
            parent (:class:`str`):
                Required. Parent logical product id. Format:
                logicalProducts/{logical_product}

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
            google.cloud.productregistry_v1.services.cloud_product_registry_read_service.pagers.ListLogicalProductVariantsAsyncPager:
                Response message for
                ListLogicalProductVariants.
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
        if not isinstance(
            request,
            cloud_product_registry_read_service.ListLogicalProductVariantsRequest,
        ):
            request = (
                cloud_product_registry_read_service.ListLogicalProductVariantsRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_logical_product_variants
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
        response = pagers.ListLogicalProductVariantsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def lookup_entity(
        self,
        request: Optional[
            Union[cloud_product_registry_read_service.LookupEntityRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_product_registry_read_service.LookupEntityResponse:
        r"""Look up entities.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import productregistry_v1

            async def sample_lookup_entity():
                # Create a client
                client = productregistry_v1.CloudProductRegistryReadServiceAsyncClient()

                # Initialize request argument(s)
                request = productregistry_v1.LookupEntityRequest(
                    lookup_uri="lookup_uri_value",
                )

                # Make the request
                response = await client.lookup_entity(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.productregistry_v1.types.LookupEntityRequest, dict]]):
                The request object. Request message for LookupEntity.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.productregistry_v1.types.LookupEntityResponse:
                Response message for LookupEntity.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, cloud_product_registry_read_service.LookupEntityRequest
        ):
            request = cloud_product_registry_read_service.LookupEntityRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.lookup_entity
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("lookup_uri", request.lookup_uri),)
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

    async def __aenter__(self) -> "CloudProductRegistryReadServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("CloudProductRegistryReadServiceAsyncClient",)
