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

from google.cloud.privatecatalog_v1beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.privatecatalog_v1beta1.services.private_catalog import pagers
from google.cloud.privatecatalog_v1beta1.types import private_catalog

from .client import PrivateCatalogClient
from .transports.base import DEFAULT_CLIENT_INFO, PrivateCatalogTransport
from .transports.grpc_asyncio import PrivateCatalogGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class PrivateCatalogAsyncClient:
    """``PrivateCatalog`` allows catalog consumers to retrieve ``Catalog``,
    ``Product`` and ``Version`` resources under a target resource
    context.

    ``Catalog`` is computed based on the [Association][]s linked to the
    target resource and its ancestors. Each association's
    [google.cloud.privatecatalogproducer.v1beta.Catalog][] is
    transformed into a ``Catalog``. If multiple associations have the
    same parent [google.cloud.privatecatalogproducer.v1beta.Catalog][],
    they are de-duplicated into one ``Catalog``. Users must have
    ``cloudprivatecatalog.catalogTargets.get`` IAM permission on the
    resource context in order to access catalogs. ``Catalog`` contains
    the resource name and a subset of data of the original
    [google.cloud.privatecatalogproducer.v1beta.Catalog][].

    ``Product`` is child resource of the catalog. A ``Product`` contains
    the resource name and a subset of the data of the original
    [google.cloud.privatecatalogproducer.v1beta.Product][].

    ``Version`` is child resource of the product. A ``Version`` contains
    the resource name and a subset of the data of the original
    [google.cloud.privatecatalogproducer.v1beta.Version][].
    """

    _client: PrivateCatalogClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = PrivateCatalogClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PrivateCatalogClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = PrivateCatalogClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = PrivateCatalogClient._DEFAULT_UNIVERSE

    catalog_path = staticmethod(PrivateCatalogClient.catalog_path)
    parse_catalog_path = staticmethod(PrivateCatalogClient.parse_catalog_path)
    product_path = staticmethod(PrivateCatalogClient.product_path)
    parse_product_path = staticmethod(PrivateCatalogClient.parse_product_path)
    version_path = staticmethod(PrivateCatalogClient.version_path)
    parse_version_path = staticmethod(PrivateCatalogClient.parse_version_path)
    common_billing_account_path = staticmethod(
        PrivateCatalogClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PrivateCatalogClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(PrivateCatalogClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        PrivateCatalogClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        PrivateCatalogClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        PrivateCatalogClient.parse_common_organization_path
    )
    common_project_path = staticmethod(PrivateCatalogClient.common_project_path)
    parse_common_project_path = staticmethod(
        PrivateCatalogClient.parse_common_project_path
    )
    common_location_path = staticmethod(PrivateCatalogClient.common_location_path)
    parse_common_location_path = staticmethod(
        PrivateCatalogClient.parse_common_location_path
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
            PrivateCatalogAsyncClient: The constructed client.
        """
        sa_info_func = (
            PrivateCatalogClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(PrivateCatalogAsyncClient, info, *args, **kwargs)

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
            PrivateCatalogAsyncClient: The constructed client.
        """
        sa_file_func = (
            PrivateCatalogClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(PrivateCatalogAsyncClient, filename, *args, **kwargs)

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
        return PrivateCatalogClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> PrivateCatalogTransport:
        """Returns the transport used by the client instance.

        Returns:
            PrivateCatalogTransport: The transport used by the client instance.
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

    get_transport_class = PrivateCatalogClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, PrivateCatalogTransport, Callable[..., PrivateCatalogTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the private catalog async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,PrivateCatalogTransport,Callable[..., PrivateCatalogTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the PrivateCatalogTransport constructor.
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
        self._client = PrivateCatalogClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.privatecatalog_v1beta1.PrivateCatalogAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.privatecatalog.v1beta1.PrivateCatalog",
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
                    "serviceName": "google.cloud.privatecatalog.v1beta1.PrivateCatalog",
                    "credentialsType": None,
                },
            )

    async def search_catalogs(
        self,
        request: Optional[Union[private_catalog.SearchCatalogsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchCatalogsAsyncPager:
        r"""Search [Catalog][google.cloud.privatecatalog.v1beta1.Catalog]
        resources that consumers have access to, within the scope of the
        consumer cloud resource hierarchy context.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import privatecatalog_v1beta1

            async def sample_search_catalogs():
                # Create a client
                client = privatecatalog_v1beta1.PrivateCatalogAsyncClient()

                # Initialize request argument(s)
                request = privatecatalog_v1beta1.SearchCatalogsRequest(
                    resource="resource_value",
                )

                # Make the request
                page_result = client.search_catalogs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.privatecatalog_v1beta1.types.SearchCatalogsRequest, dict]]):
                The request object. Request message for
                [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.privatecatalog_v1beta1.services.private_catalog.pagers.SearchCatalogsAsyncPager:
                Response message for
                [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, private_catalog.SearchCatalogsRequest):
            request = private_catalog.SearchCatalogsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_catalogs
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
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
        response = pagers.SearchCatalogsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_products(
        self,
        request: Optional[Union[private_catalog.SearchProductsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchProductsAsyncPager:
        r"""Search [Product][google.cloud.privatecatalog.v1beta1.Product]
        resources that consumers have access to, within the scope of the
        consumer cloud resource hierarchy context.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import privatecatalog_v1beta1

            async def sample_search_products():
                # Create a client
                client = privatecatalog_v1beta1.PrivateCatalogAsyncClient()

                # Initialize request argument(s)
                request = privatecatalog_v1beta1.SearchProductsRequest(
                    resource="resource_value",
                )

                # Make the request
                page_result = client.search_products(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.privatecatalog_v1beta1.types.SearchProductsRequest, dict]]):
                The request object. Request message for
                [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.privatecatalog_v1beta1.services.private_catalog.pagers.SearchProductsAsyncPager:
                Response message for
                [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, private_catalog.SearchProductsRequest):
            request = private_catalog.SearchProductsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_products
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
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
        response = pagers.SearchProductsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_versions(
        self,
        request: Optional[Union[private_catalog.SearchVersionsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchVersionsAsyncPager:
        r"""Search [Version][google.cloud.privatecatalog.v1beta1.Version]
        resources that consumers have access to, within the scope of the
        consumer cloud resource hierarchy context.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import privatecatalog_v1beta1

            async def sample_search_versions():
                # Create a client
                client = privatecatalog_v1beta1.PrivateCatalogAsyncClient()

                # Initialize request argument(s)
                request = privatecatalog_v1beta1.SearchVersionsRequest(
                    resource="resource_value",
                    query="query_value",
                )

                # Make the request
                page_result = client.search_versions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.privatecatalog_v1beta1.types.SearchVersionsRequest, dict]]):
                The request object. Request message for
                [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.privatecatalog_v1beta1.services.private_catalog.pagers.SearchVersionsAsyncPager:
                Response message for
                [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, private_catalog.SearchVersionsRequest):
            request = private_catalog.SearchVersionsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_versions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
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
        response = pagers.SearchVersionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "PrivateCatalogAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("PrivateCatalogAsyncClient",)
