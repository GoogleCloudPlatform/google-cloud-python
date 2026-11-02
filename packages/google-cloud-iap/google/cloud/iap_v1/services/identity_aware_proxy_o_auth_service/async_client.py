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

from google.cloud.iap_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.iap_v1.services.identity_aware_proxy_o_auth_service import pagers
from google.cloud.iap_v1.types import service

from .client import IdentityAwareProxyOAuthServiceClient
from .transports.base import (
    DEFAULT_CLIENT_INFO,
    IdentityAwareProxyOAuthServiceTransport,
)
from .transports.grpc_asyncio import IdentityAwareProxyOAuthServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class IdentityAwareProxyOAuthServiceAsyncClient:
    """API to programmatically create, list and retrieve Identity
    Aware Proxy (IAP) OAuth brands; and create, retrieve, delete and
    reset-secret of IAP OAuth clients.
    """

    _client: IdentityAwareProxyOAuthServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = IdentityAwareProxyOAuthServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = IdentityAwareProxyOAuthServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        IdentityAwareProxyOAuthServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = IdentityAwareProxyOAuthServiceClient._DEFAULT_UNIVERSE

    common_billing_account_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_location_path
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
            IdentityAwareProxyOAuthServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            IdentityAwareProxyOAuthServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(
            IdentityAwareProxyOAuthServiceAsyncClient, info, *args, **kwargs
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
            IdentityAwareProxyOAuthServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            IdentityAwareProxyOAuthServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            IdentityAwareProxyOAuthServiceAsyncClient, filename, *args, **kwargs
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
        return IdentityAwareProxyOAuthServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> IdentityAwareProxyOAuthServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            IdentityAwareProxyOAuthServiceTransport: The transport used by the client instance.
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

    get_transport_class = IdentityAwareProxyOAuthServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                IdentityAwareProxyOAuthServiceTransport,
                Callable[..., IdentityAwareProxyOAuthServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the identity aware proxy o auth service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,IdentityAwareProxyOAuthServiceTransport,Callable[..., IdentityAwareProxyOAuthServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the IdentityAwareProxyOAuthServiceTransport constructor.
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
        self._client = IdentityAwareProxyOAuthServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.iap_v1.IdentityAwareProxyOAuthServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
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
                    "serviceName": "google.cloud.iap.v1.IdentityAwareProxyOAuthService",
                    "credentialsType": None,
                },
            )

    async def list_brands(
        self,
        request: Optional[Union[service.ListBrandsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.ListBrandsResponse:
        r"""Lists the existing brands for the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_list_brands():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.ListBrandsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_brands(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.ListBrandsRequest, dict]]):
                The request object. The request sent to ListBrands.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.iap_v1.types.ListBrandsResponse:
                Response message for ListBrands.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.ListBrandsRequest):
            request = service.ListBrandsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_brands
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

    async def create_brand(
        self,
        request: Optional[Union[service.CreateBrandRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.Brand:
        r"""Constructs a new OAuth brand for the project if one
        does not exist. The created brand is "internal only",
        meaning that OAuth clients created under it only accept
        requests from users who belong to the same Google
        Workspace organization as the project. The brand is
        created in an un-reviewed status. NOTE: The "internal
        only" status can be manually changed in the Google Cloud
        Console. Requires that a brand does not already exist
        for the project, and that the specified support email is
        owned by the caller.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_create_brand():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.CreateBrandRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_brand(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.CreateBrandRequest, dict]]):
                The request object. The request sent to CreateBrand.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.iap_v1.types.Brand:
                OAuth brand data.
                NOTE: Only contains a portion of the
                data that describes a brand.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.CreateBrandRequest):
            request = service.CreateBrandRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_brand
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

    async def get_brand(
        self,
        request: Optional[Union[service.GetBrandRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.Brand:
        r"""Retrieves the OAuth brand of the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_get_brand():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.GetBrandRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_brand(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.GetBrandRequest, dict]]):
                The request object. The request sent to GetBrand.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.iap_v1.types.Brand:
                OAuth brand data.
                NOTE: Only contains a portion of the
                data that describes a brand.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.GetBrandRequest):
            request = service.GetBrandRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_brand
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

    async def create_identity_aware_proxy_client(
        self,
        request: Optional[
            Union[service.CreateIdentityAwareProxyClientRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.IdentityAwareProxyClient:
        r"""Creates an Identity Aware Proxy (IAP) OAuth client.
        The client is owned by IAP. Requires that the brand for
        the project exists and that it is set for internal-only
        use.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_create_identity_aware_proxy_client():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.CreateIdentityAwareProxyClientRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_identity_aware_proxy_client(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.CreateIdentityAwareProxyClientRequest, dict]]):
                The request object. The request sent to
                CreateIdentityAwareProxyClient.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.iap_v1.types.IdentityAwareProxyClient:
                Contains the data that describes an
                Identity Aware Proxy owned client.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.CreateIdentityAwareProxyClientRequest):
            request = service.CreateIdentityAwareProxyClientRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_identity_aware_proxy_client
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

    async def list_identity_aware_proxy_clients(
        self,
        request: Optional[
            Union[service.ListIdentityAwareProxyClientsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListIdentityAwareProxyClientsAsyncPager:
        r"""Lists the existing clients for the brand.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_list_identity_aware_proxy_clients():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.ListIdentityAwareProxyClientsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_identity_aware_proxy_clients(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.ListIdentityAwareProxyClientsRequest, dict]]):
                The request object. The request sent to
                ListIdentityAwareProxyClients.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.iap_v1.services.identity_aware_proxy_o_auth_service.pagers.ListIdentityAwareProxyClientsAsyncPager:
                Response message for
                ListIdentityAwareProxyClients.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.ListIdentityAwareProxyClientsRequest):
            request = service.ListIdentityAwareProxyClientsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_identity_aware_proxy_clients
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
        response = pagers.ListIdentityAwareProxyClientsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_identity_aware_proxy_client(
        self,
        request: Optional[
            Union[service.GetIdentityAwareProxyClientRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.IdentityAwareProxyClient:
        r"""Retrieves an Identity Aware Proxy (IAP) OAuth client.
        Requires that the client is owned by IAP.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_get_identity_aware_proxy_client():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.GetIdentityAwareProxyClientRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_identity_aware_proxy_client(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.GetIdentityAwareProxyClientRequest, dict]]):
                The request object. The request sent to
                GetIdentityAwareProxyClient.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.iap_v1.types.IdentityAwareProxyClient:
                Contains the data that describes an
                Identity Aware Proxy owned client.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.GetIdentityAwareProxyClientRequest):
            request = service.GetIdentityAwareProxyClientRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_identity_aware_proxy_client
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

    async def reset_identity_aware_proxy_client_secret(
        self,
        request: Optional[
            Union[service.ResetIdentityAwareProxyClientSecretRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> service.IdentityAwareProxyClient:
        r"""Resets an Identity Aware Proxy (IAP) OAuth client
        secret. Useful if the secret was compromised. Requires
        that the client is owned by IAP.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_reset_identity_aware_proxy_client_secret():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.ResetIdentityAwareProxyClientSecretRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.reset_identity_aware_proxy_client_secret(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.ResetIdentityAwareProxyClientSecretRequest, dict]]):
                The request object. The request sent to
                ResetIdentityAwareProxyClientSecret.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.iap_v1.types.IdentityAwareProxyClient:
                Contains the data that describes an
                Identity Aware Proxy owned client.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, service.ResetIdentityAwareProxyClientSecretRequest):
            request = service.ResetIdentityAwareProxyClientSecretRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reset_identity_aware_proxy_client_secret
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

    async def delete_identity_aware_proxy_client(
        self,
        request: Optional[
            Union[service.DeleteIdentityAwareProxyClientRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an Identity Aware Proxy (IAP) OAuth client.
        Useful for removing obsolete clients, managing the
        number of clients in a given project, and cleaning up
        after tests. Requires that the client is owned by IAP.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import iap_v1

            async def sample_delete_identity_aware_proxy_client():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.DeleteIdentityAwareProxyClientRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_identity_aware_proxy_client(request=request)

        Args:
            request (Optional[Union[google.cloud.iap_v1.types.DeleteIdentityAwareProxyClientRequest, dict]]):
                The request object. The request sent to
                DeleteIdentityAwareProxyClient.
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
        if not isinstance(request, service.DeleteIdentityAwareProxyClientRequest):
            request = service.DeleteIdentityAwareProxyClientRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_identity_aware_proxy_client
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

    async def __aenter__(self) -> "IdentityAwareProxyOAuthServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("IdentityAwareProxyOAuthServiceAsyncClient",)
