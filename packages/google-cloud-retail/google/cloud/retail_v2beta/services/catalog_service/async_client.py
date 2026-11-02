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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.retail_v2beta.services.catalog_service import pagers
from google.cloud.retail_v2beta.types import (
    catalog,
    catalog_service,
    common,
    import_config,
)
from google.cloud.retail_v2beta.types import catalog as gcr_catalog

from .client import CatalogServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, CatalogServiceTransport
from .transports.grpc_asyncio import CatalogServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class CatalogServiceAsyncClient:
    """Service for managing catalog configuration."""

    _client: CatalogServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = CatalogServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CatalogServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = CatalogServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = CatalogServiceClient._DEFAULT_UNIVERSE

    attributes_config_path = staticmethod(CatalogServiceClient.attributes_config_path)
    parse_attributes_config_path = staticmethod(
        CatalogServiceClient.parse_attributes_config_path
    )
    branch_path = staticmethod(CatalogServiceClient.branch_path)
    parse_branch_path = staticmethod(CatalogServiceClient.parse_branch_path)
    catalog_path = staticmethod(CatalogServiceClient.catalog_path)
    parse_catalog_path = staticmethod(CatalogServiceClient.parse_catalog_path)
    completion_config_path = staticmethod(CatalogServiceClient.completion_config_path)
    parse_completion_config_path = staticmethod(
        CatalogServiceClient.parse_completion_config_path
    )
    common_billing_account_path = staticmethod(
        CatalogServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CatalogServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(CatalogServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        CatalogServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        CatalogServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        CatalogServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(CatalogServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        CatalogServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(CatalogServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        CatalogServiceClient.parse_common_location_path
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
            CatalogServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            CatalogServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(CatalogServiceAsyncClient, info, *args, **kwargs)

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
            CatalogServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            CatalogServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(CatalogServiceAsyncClient, filename, *args, **kwargs)

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
        return CatalogServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CatalogServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CatalogServiceTransport: The transport used by the client instance.
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

    get_transport_class = CatalogServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, CatalogServiceTransport, Callable[..., CatalogServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the catalog service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CatalogServiceTransport,Callable[..., CatalogServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CatalogServiceTransport constructor.
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
        self._client = CatalogServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.retail_v2beta.CatalogServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.retail.v2beta.CatalogService",
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
                    "serviceName": "google.cloud.retail.v2beta.CatalogService",
                    "credentialsType": None,
                },
            )

    async def list_catalogs(
        self,
        request: Optional[Union[catalog_service.ListCatalogsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCatalogsAsyncPager:
        r"""Lists all the [Catalog][google.cloud.retail.v2beta.Catalog]s
        associated with the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_list_catalogs():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.ListCatalogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_catalogs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.ListCatalogsRequest, dict]]):
                The request object. Request for
                [CatalogService.ListCatalogs][google.cloud.retail.v2beta.CatalogService.ListCatalogs]
                method.
            parent (:class:`str`):
                Required. The account resource name with an associated
                location.

                If the caller does not have permission to list
                [Catalog][google.cloud.retail.v2beta.Catalog]s under
                this location, regardless of whether or not this
                location exists, a PERMISSION_DENIED error is returned.

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
            google.cloud.retail_v2beta.services.catalog_service.pagers.ListCatalogsAsyncPager:
                Response for
                   [CatalogService.ListCatalogs][google.cloud.retail.v2beta.CatalogService.ListCatalogs]
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
        if not isinstance(request, catalog_service.ListCatalogsRequest):
            request = catalog_service.ListCatalogsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_catalogs
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
        response = pagers.ListCatalogsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_catalog(
        self,
        request: Optional[Union[catalog_service.UpdateCatalogRequest, dict]] = None,
        *,
        catalog: Optional[gcr_catalog.Catalog] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcr_catalog.Catalog:
        r"""Updates the [Catalog][google.cloud.retail.v2beta.Catalog]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_update_catalog():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                catalog = retail_v2beta.Catalog()
                catalog.name = "name_value"
                catalog.display_name = "display_name_value"

                request = retail_v2beta.UpdateCatalogRequest(
                    catalog=catalog,
                )

                # Make the request
                response = await client.update_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.UpdateCatalogRequest, dict]]):
                The request object. Request for
                [CatalogService.UpdateCatalog][google.cloud.retail.v2beta.CatalogService.UpdateCatalog]
                method.
            catalog (:class:`google.cloud.retail_v2beta.types.Catalog`):
                Required. The
                [Catalog][google.cloud.retail.v2beta.Catalog] to update.

                If the caller does not have permission to update the
                [Catalog][google.cloud.retail.v2beta.Catalog],
                regardless of whether or not it exists, a
                PERMISSION_DENIED error is returned.

                If the [Catalog][google.cloud.retail.v2beta.Catalog] to
                update does not exist, a NOT_FOUND error is returned.

                This corresponds to the ``catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which fields in the provided
                [Catalog][google.cloud.retail.v2beta.Catalog] to update.

                If an unsupported or unknown field is provided, an
                INVALID_ARGUMENT error is returned.

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
            google.cloud.retail_v2beta.types.Catalog:
                The catalog configuration.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [catalog, update_mask]
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
        if not isinstance(request, catalog_service.UpdateCatalogRequest):
            request = catalog_service.UpdateCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if catalog is not None:
            request.catalog = catalog
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_catalog
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("catalog.name", request.catalog.name),)
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

    async def set_default_branch(
        self,
        request: Optional[Union[catalog_service.SetDefaultBranchRequest, dict]] = None,
        *,
        catalog: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Set a specified branch id as default branch. API methods such as
        [SearchService.Search][google.cloud.retail.v2beta.SearchService.Search],
        [ProductService.GetProduct][google.cloud.retail.v2beta.ProductService.GetProduct],
        [ProductService.ListProducts][google.cloud.retail.v2beta.ProductService.ListProducts]
        will treat requests using "default_branch" to the actual branch
        id set as default.

        For example, if ``projects/*/locations/*/catalogs/*/branches/1``
        is set as default, setting
        [SearchRequest.branch][google.cloud.retail.v2beta.SearchRequest.branch]
        to ``projects/*/locations/*/catalogs/*/branches/default_branch``
        is equivalent to setting
        [SearchRequest.branch][google.cloud.retail.v2beta.SearchRequest.branch]
        to ``projects/*/locations/*/catalogs/*/branches/1``.

        Using multiple branches can be useful when developers would like
        to have a staging branch to test and verify for future usage.
        When it becomes ready, developers switch on the staging branch
        using this API while keeping using
        ``projects/*/locations/*/catalogs/*/branches/default_branch`` as
        [SearchRequest.branch][google.cloud.retail.v2beta.SearchRequest.branch]
        to route the traffic to this staging branch.

        CAUTION: If you have live predict/search traffic, switching the
        default branch could potentially cause outages if the ID space
        of the new branch is very different from the old one.

        More specifically:

        - PredictionService will only return product IDs from branch
          {newBranch}.
        - SearchService will only return product IDs from branch
          {newBranch} (if branch is not explicitly set).
        - UserEventService will only join events with products from
          branch {newBranch}.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_set_default_branch():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.SetDefaultBranchRequest(
                )

                # Make the request
                await client.set_default_branch(request=request)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.SetDefaultBranchRequest, dict]]):
                The request object. Request message to set a specified branch as new
                default_branch.
            catalog (:class:`str`):
                Full resource name of the catalog, such as
                ``projects/*/locations/global/catalogs/default_catalog``.

                This corresponds to the ``catalog`` field
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
        flattened_params = [catalog]
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
        if not isinstance(request, catalog_service.SetDefaultBranchRequest):
            request = catalog_service.SetDefaultBranchRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if catalog is not None:
            request.catalog = catalog

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.set_default_branch
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("catalog", request.catalog),)),
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

    async def get_default_branch(
        self,
        request: Optional[Union[catalog_service.GetDefaultBranchRequest, dict]] = None,
        *,
        catalog: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_service.GetDefaultBranchResponse:
        r"""Get which branch is currently default branch set by
        [CatalogService.SetDefaultBranch][google.cloud.retail.v2beta.CatalogService.SetDefaultBranch]
        method under a specified parent catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_get_default_branch():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.GetDefaultBranchRequest(
                )

                # Make the request
                response = await client.get_default_branch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.GetDefaultBranchRequest, dict]]):
                The request object. Request message to show which branch
                is currently the default branch.
            catalog (:class:`str`):
                The parent catalog resource name, such as
                ``projects/*/locations/global/catalogs/default_catalog``.

                This corresponds to the ``catalog`` field
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
            google.cloud.retail_v2beta.types.GetDefaultBranchResponse:
                Response message of
                   [CatalogService.GetDefaultBranch][google.cloud.retail.v2beta.CatalogService.GetDefaultBranch].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [catalog]
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
        if not isinstance(request, catalog_service.GetDefaultBranchRequest):
            request = catalog_service.GetDefaultBranchRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if catalog is not None:
            request.catalog = catalog

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_default_branch
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("catalog", request.catalog),)),
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

    async def get_completion_config(
        self,
        request: Optional[
            Union[catalog_service.GetCompletionConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog.CompletionConfig:
        r"""Gets a
        [CompletionConfig][google.cloud.retail.v2beta.CompletionConfig].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_get_completion_config():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.GetCompletionConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_completion_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.GetCompletionConfigRequest, dict]]):
                The request object. Request for
                [CatalogService.GetCompletionConfig][google.cloud.retail.v2beta.CatalogService.GetCompletionConfig]
                method.
            name (:class:`str`):
                Required. Full CompletionConfig resource name. Format:
                ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/completionConfig``

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
            google.cloud.retail_v2beta.types.CompletionConfig:
                Catalog level autocomplete config for
                customers to customize autocomplete
                feature's settings.

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
        if not isinstance(request, catalog_service.GetCompletionConfigRequest):
            request = catalog_service.GetCompletionConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_completion_config
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

    async def update_completion_config(
        self,
        request: Optional[
            Union[catalog_service.UpdateCompletionConfigRequest, dict]
        ] = None,
        *,
        completion_config: Optional[catalog.CompletionConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog.CompletionConfig:
        r"""Updates the
        [CompletionConfig][google.cloud.retail.v2beta.CompletionConfig]s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_update_completion_config():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                completion_config = retail_v2beta.CompletionConfig()
                completion_config.name = "name_value"

                request = retail_v2beta.UpdateCompletionConfigRequest(
                    completion_config=completion_config,
                )

                # Make the request
                response = await client.update_completion_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.UpdateCompletionConfigRequest, dict]]):
                The request object. Request for
                [CatalogService.UpdateCompletionConfig][google.cloud.retail.v2beta.CatalogService.UpdateCompletionConfig]
                method.
            completion_config (:class:`google.cloud.retail_v2beta.types.CompletionConfig`):
                Required. The
                [CompletionConfig][google.cloud.retail.v2beta.CompletionConfig]
                to update.

                If the caller does not have permission to update the
                [CompletionConfig][google.cloud.retail.v2beta.CompletionConfig],
                then a PERMISSION_DENIED error is returned.

                If the
                [CompletionConfig][google.cloud.retail.v2beta.CompletionConfig]
                to update does not exist, a NOT_FOUND error is returned.

                This corresponds to the ``completion_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which fields in the provided
                [CompletionConfig][google.cloud.retail.v2beta.CompletionConfig]
                to update. The following are the only supported fields:

                - [CompletionConfig.matching_order][google.cloud.retail.v2beta.CompletionConfig.matching_order]
                - [CompletionConfig.max_suggestions][google.cloud.retail.v2beta.CompletionConfig.max_suggestions]
                - [CompletionConfig.min_prefix_length][google.cloud.retail.v2beta.CompletionConfig.min_prefix_length]
                - [CompletionConfig.auto_learning][google.cloud.retail.v2beta.CompletionConfig.auto_learning]

                If not set, all supported fields are updated.

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
            google.cloud.retail_v2beta.types.CompletionConfig:
                Catalog level autocomplete config for
                customers to customize autocomplete
                feature's settings.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [completion_config, update_mask]
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
        if not isinstance(request, catalog_service.UpdateCompletionConfigRequest):
            request = catalog_service.UpdateCompletionConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if completion_config is not None:
            request.completion_config = completion_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_completion_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("completion_config.name", request.completion_config.name),)
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

    async def get_attributes_config(
        self,
        request: Optional[
            Union[catalog_service.GetAttributesConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog.AttributesConfig:
        r"""Gets an
        [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_get_attributes_config():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.GetAttributesConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_attributes_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.GetAttributesConfigRequest, dict]]):
                The request object. Request for
                [CatalogService.GetAttributesConfig][google.cloud.retail.v2beta.CatalogService.GetAttributesConfig]
                method.
            name (:class:`str`):
                Required. Full AttributesConfig resource name. Format:
                ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/attributesConfig``

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
            google.cloud.retail_v2beta.types.AttributesConfig:
                Catalog level attribute config.
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
        if not isinstance(request, catalog_service.GetAttributesConfigRequest):
            request = catalog_service.GetAttributesConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_attributes_config
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

    async def update_attributes_config(
        self,
        request: Optional[
            Union[catalog_service.UpdateAttributesConfigRequest, dict]
        ] = None,
        *,
        attributes_config: Optional[catalog.AttributesConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog.AttributesConfig:
        r"""Updates the
        [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig].

        The catalog attributes in the request will be updated in the
        catalog, or inserted if they do not exist. Existing catalog
        attributes not included in the request will remain unchanged.
        Attributes that are assigned to products, but do not exist at
        the catalog level, are always included in the response. The
        product attribute is assigned default values for missing catalog
        attribute fields, e.g., searchable and dynamic facetable
        options.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_update_attributes_config():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                attributes_config = retail_v2beta.AttributesConfig()
                attributes_config.name = "name_value"

                request = retail_v2beta.UpdateAttributesConfigRequest(
                    attributes_config=attributes_config,
                )

                # Make the request
                response = await client.update_attributes_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.UpdateAttributesConfigRequest, dict]]):
                The request object. Request for
                [CatalogService.UpdateAttributesConfig][google.cloud.retail.v2beta.CatalogService.UpdateAttributesConfig]
                method.
            attributes_config (:class:`google.cloud.retail_v2beta.types.AttributesConfig`):
                Required. The
                [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig]
                to update.

                This corresponds to the ``attributes_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which fields in the provided
                [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig]
                to update. The following is the only supported field:

                - [AttributesConfig.catalog_attributes][google.cloud.retail.v2beta.AttributesConfig.catalog_attributes]

                If not set, all supported fields are updated.

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
            google.cloud.retail_v2beta.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [attributes_config, update_mask]
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
        if not isinstance(request, catalog_service.UpdateAttributesConfigRequest):
            request = catalog_service.UpdateAttributesConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if attributes_config is not None:
            request.attributes_config = attributes_config
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_attributes_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("attributes_config.name", request.attributes_config.name),)
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

    async def add_catalog_attribute(
        self,
        request: Optional[
            Union[catalog_service.AddCatalogAttributeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog.AttributesConfig:
        r"""Adds the specified
        [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]
        to the
        [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig].

        If the
        [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]
        to add already exists, an ALREADY_EXISTS error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_add_catalog_attribute():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                catalog_attribute = retail_v2beta.CatalogAttribute()
                catalog_attribute.key = "key_value"

                request = retail_v2beta.AddCatalogAttributeRequest(
                    attributes_config="attributes_config_value",
                    catalog_attribute=catalog_attribute,
                )

                # Make the request
                response = await client.add_catalog_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.AddCatalogAttributeRequest, dict]]):
                The request object. Request for
                [CatalogService.AddCatalogAttribute][google.cloud.retail.v2beta.CatalogService.AddCatalogAttribute]
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.retail_v2beta.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, catalog_service.AddCatalogAttributeRequest):
            request = catalog_service.AddCatalogAttributeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.add_catalog_attribute
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("attributes_config", request.attributes_config),)
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

    async def remove_catalog_attribute(
        self,
        request: Optional[
            Union[catalog_service.RemoveCatalogAttributeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog.AttributesConfig:
        r"""Removes the specified
        [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]
        from the
        [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig].

        If the
        [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]
        to remove does not exist, a NOT_FOUND error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_remove_catalog_attribute():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.RemoveCatalogAttributeRequest(
                    attributes_config="attributes_config_value",
                    key="key_value",
                )

                # Make the request
                response = await client.remove_catalog_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.RemoveCatalogAttributeRequest, dict]]):
                The request object. Request for
                [CatalogService.RemoveCatalogAttribute][google.cloud.retail.v2beta.CatalogService.RemoveCatalogAttribute]
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.retail_v2beta.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, catalog_service.RemoveCatalogAttributeRequest):
            request = catalog_service.RemoveCatalogAttributeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.remove_catalog_attribute
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("attributes_config", request.attributes_config),)
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

    async def batch_remove_catalog_attributes(
        self,
        request: Optional[
            Union[catalog_service.BatchRemoveCatalogAttributesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_service.BatchRemoveCatalogAttributesResponse:
        r"""Removes all specified
        [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]s
        from the
        [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_batch_remove_catalog_attributes():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                request = retail_v2beta.BatchRemoveCatalogAttributesRequest(
                    attributes_config="attributes_config_value",
                    attribute_keys=['attribute_keys_value1', 'attribute_keys_value2'],
                )

                # Make the request
                response = await client.batch_remove_catalog_attributes(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.BatchRemoveCatalogAttributesRequest, dict]]):
                The request object. Request for
                [CatalogService.BatchRemoveCatalogAttributes][google.cloud.retail.v2beta.CatalogService.BatchRemoveCatalogAttributes]
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.retail_v2beta.types.BatchRemoveCatalogAttributesResponse:
                Response of the
                   [CatalogService.BatchRemoveCatalogAttributes][google.cloud.retail.v2beta.CatalogService.BatchRemoveCatalogAttributes].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, catalog_service.BatchRemoveCatalogAttributesRequest):
            request = catalog_service.BatchRemoveCatalogAttributesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_remove_catalog_attributes
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("attributes_config", request.attributes_config),)
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

    async def replace_catalog_attribute(
        self,
        request: Optional[
            Union[catalog_service.ReplaceCatalogAttributeRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog.AttributesConfig:
        r"""Replaces the specified
        [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]
        in the
        [AttributesConfig][google.cloud.retail.v2beta.AttributesConfig]
        by updating the catalog attribute with the same
        [CatalogAttribute.key][google.cloud.retail.v2beta.CatalogAttribute.key].

        If the
        [CatalogAttribute][google.cloud.retail.v2beta.CatalogAttribute]
        to replace does not exist, a NOT_FOUND error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import retail_v2beta

            async def sample_replace_catalog_attribute():
                # Create a client
                client = retail_v2beta.CatalogServiceAsyncClient()

                # Initialize request argument(s)
                catalog_attribute = retail_v2beta.CatalogAttribute()
                catalog_attribute.key = "key_value"

                request = retail_v2beta.ReplaceCatalogAttributeRequest(
                    attributes_config="attributes_config_value",
                    catalog_attribute=catalog_attribute,
                )

                # Make the request
                response = await client.replace_catalog_attribute(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.retail_v2beta.types.ReplaceCatalogAttributeRequest, dict]]):
                The request object. Request for
                [CatalogService.ReplaceCatalogAttribute][google.cloud.retail.v2beta.CatalogService.ReplaceCatalogAttribute]
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.retail_v2beta.types.AttributesConfig:
                Catalog level attribute config.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, catalog_service.ReplaceCatalogAttributeRequest):
            request = catalog_service.ReplaceCatalogAttributeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.replace_catalog_attribute
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("attributes_config", request.attributes_config),)
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

    async def __aenter__(self) -> "CatalogServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("CatalogServiceAsyncClient",)
