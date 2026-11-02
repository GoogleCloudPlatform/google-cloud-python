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

from google.cloud.asset_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.expr_pb2 as expr_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.asset_v1.services.asset_service import pagers
from google.cloud.asset_v1.types import asset_service, assets

from .client import AssetServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, AssetServiceTransport
from .transports.grpc_asyncio import AssetServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AssetServiceAsyncClient:
    """Asset service definition."""

    _client: AssetServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AssetServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AssetServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AssetServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AssetServiceClient._DEFAULT_UNIVERSE

    access_level_path = staticmethod(AssetServiceClient.access_level_path)
    parse_access_level_path = staticmethod(AssetServiceClient.parse_access_level_path)
    access_policy_path = staticmethod(AssetServiceClient.access_policy_path)
    parse_access_policy_path = staticmethod(AssetServiceClient.parse_access_policy_path)
    asset_path = staticmethod(AssetServiceClient.asset_path)
    parse_asset_path = staticmethod(AssetServiceClient.parse_asset_path)
    feed_path = staticmethod(AssetServiceClient.feed_path)
    parse_feed_path = staticmethod(AssetServiceClient.parse_feed_path)
    inventory_path = staticmethod(AssetServiceClient.inventory_path)
    parse_inventory_path = staticmethod(AssetServiceClient.parse_inventory_path)
    saved_query_path = staticmethod(AssetServiceClient.saved_query_path)
    parse_saved_query_path = staticmethod(AssetServiceClient.parse_saved_query_path)
    service_perimeter_path = staticmethod(AssetServiceClient.service_perimeter_path)
    parse_service_perimeter_path = staticmethod(
        AssetServiceClient.parse_service_perimeter_path
    )
    common_billing_account_path = staticmethod(
        AssetServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AssetServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AssetServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(AssetServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(AssetServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        AssetServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AssetServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        AssetServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(AssetServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        AssetServiceClient.parse_common_location_path
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
            AssetServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            AssetServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AssetServiceAsyncClient, info, *args, **kwargs)

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
            AssetServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            AssetServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(AssetServiceAsyncClient, filename, *args, **kwargs)

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
        return AssetServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AssetServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            AssetServiceTransport: The transport used by the client instance.
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

    get_transport_class = AssetServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, AssetServiceTransport, Callable[..., AssetServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the asset service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AssetServiceTransport,Callable[..., AssetServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AssetServiceTransport constructor.
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
        self._client = AssetServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.asset_v1.AssetServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.asset.v1.AssetService",
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
                    "serviceName": "google.cloud.asset.v1.AssetService",
                    "credentialsType": None,
                },
            )

    async def export_assets(
        self,
        request: Optional[Union[asset_service.ExportAssetsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports assets with time and resource types to a given Cloud
        Storage location/BigQuery table. For Cloud Storage location
        destinations, the output format is newline-delimited JSON. Each
        line represents a
        [google.cloud.asset.v1.Asset][google.cloud.asset.v1.Asset] in
        the JSON format; for BigQuery table destinations, the output
        table stores the fields in asset Protobuf as columns. This API
        implements the
        [google.longrunning.Operation][google.longrunning.Operation]
        API, which allows you to keep track of the export. We recommend
        intervals of at least 2 seconds with exponential retry to poll
        the export operation result. For regular-size resource parent,
        the export operation usually finishes within 5 minutes.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_export_assets():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                output_config = asset_v1.OutputConfig()
                output_config.gcs_destination.uri = "uri_value"

                request = asset_v1.ExportAssetsRequest(
                    parent="parent_value",
                    output_config=output_config,
                )

                # Make the request
                operation = await client.export_assets(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.ExportAssetsRequest, dict]]):
                The request object. Export asset request.
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

                The result type for the operation will be :class:`google.cloud.asset_v1.types.ExportAssetsResponse` The export asset response. This message is returned by the
                   [google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]
                   method in the returned
                   [google.longrunning.Operation.response][google.longrunning.Operation.response]
                   field.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, asset_service.ExportAssetsRequest):
            request = asset_service.ExportAssetsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_assets
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
            asset_service.ExportAssetsResponse,
            metadata_type=asset_service.ExportAssetsRequest,
        )

        # Done; return the response.
        return response

    async def list_assets(
        self,
        request: Optional[Union[asset_service.ListAssetsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAssetsAsyncPager:
        r"""Lists assets with time and resource types and returns
        paged results in response.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_list_assets():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.ListAssetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_assets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.ListAssetsRequest, dict]]):
                The request object. ListAssets request.
            parent (:class:`str`):
                Required. Name of the organization, folder, or project
                the assets belong to. Format:
                "organizations/[organization-number]" (such as
                "organizations/123"), "projects/[project-id]" (such as
                "projects/my-project-id"), "projects/[project-number]"
                (such as "projects/12345"), or "folders/[folder-number]"
                (such as "folders/12345").

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
            google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager:
                ListAssets response.

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
        if not isinstance(request, asset_service.ListAssetsRequest):
            request = asset_service.ListAssetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_assets
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
        response = pagers.ListAssetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def batch_get_assets_history(
        self,
        request: Optional[
            Union[asset_service.BatchGetAssetsHistoryRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.BatchGetAssetsHistoryResponse:
        r"""Batch gets the update history of assets that overlap a time
        window. For IAM_POLICY content, this API outputs history when
        the asset and its attached IAM POLICY both exist. This can
        create gaps in the output history. Otherwise, this API outputs
        history with asset in both non-delete or deleted status. If a
        specified asset does not exist, this API returns an
        INVALID_ARGUMENT error.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_batch_get_assets_history():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.BatchGetAssetsHistoryRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.batch_get_assets_history(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.BatchGetAssetsHistoryRequest, dict]]):
                The request object. Batch get assets history request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.asset_v1.types.BatchGetAssetsHistoryResponse:
                Batch get assets history response.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, asset_service.BatchGetAssetsHistoryRequest):
            request = asset_service.BatchGetAssetsHistoryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_get_assets_history
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

    async def create_feed(
        self,
        request: Optional[Union[asset_service.CreateFeedRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.Feed:
        r"""Creates a feed in a parent
        project/folder/organization to listen to its asset
        updates.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_create_feed():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                feed = asset_v1.Feed()
                feed.name = "name_value"

                request = asset_v1.CreateFeedRequest(
                    parent="parent_value",
                    feed_id="feed_id_value",
                    feed=feed,
                )

                # Make the request
                response = await client.create_feed(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.CreateFeedRequest, dict]]):
                The request object. Create asset feed request.
            parent (:class:`str`):
                Required. The name of the
                project/folder/organization where this
                feed should be created in. It can only
                be an organization number (such as
                "organizations/123"), a folder number
                (such as "folders/123"), a project ID
                (such as "projects/my-project-id"), or a
                project number (such as
                "projects/12345").

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
            google.cloud.asset_v1.types.Feed:
                An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:

                Pub/Sub topics.

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
        if not isinstance(request, asset_service.CreateFeedRequest):
            request = asset_service.CreateFeedRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_feed
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

    async def get_feed(
        self,
        request: Optional[Union[asset_service.GetFeedRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.Feed:
        r"""Gets details about an asset feed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_get_feed():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.GetFeedRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_feed(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.GetFeedRequest, dict]]):
                The request object. Get asset feed request.
            name (:class:`str`):
                Required. The name of the Feed and it must be in the
                format of: projects/project_number/feeds/feed_id
                folders/folder_number/feeds/feed_id
                organizations/organization_number/feeds/feed_id

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
            google.cloud.asset_v1.types.Feed:
                An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:

                Pub/Sub topics.

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
        if not isinstance(request, asset_service.GetFeedRequest):
            request = asset_service.GetFeedRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_feed]

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

    async def list_feeds(
        self,
        request: Optional[Union[asset_service.ListFeedsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.ListFeedsResponse:
        r"""Lists all asset feeds in a parent
        project/folder/organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_list_feeds():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.ListFeedsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.list_feeds(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.ListFeedsRequest, dict]]):
                The request object. List asset feeds request.
            parent (:class:`str`):
                Required. The parent
                project/folder/organization whose feeds
                are to be listed. It can only be using
                project/folder/organization number (such
                as "folders/12345")", or a project ID
                (such as "projects/my-project-id").

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
            google.cloud.asset_v1.types.ListFeedsResponse:

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
        if not isinstance(request, asset_service.ListFeedsRequest):
            request = asset_service.ListFeedsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_feeds
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

    async def update_feed(
        self,
        request: Optional[Union[asset_service.UpdateFeedRequest, dict]] = None,
        *,
        feed: Optional[asset_service.Feed] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.Feed:
        r"""Updates an asset feed configuration.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_update_feed():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                feed = asset_v1.Feed()
                feed.name = "name_value"

                request = asset_v1.UpdateFeedRequest(
                    feed=feed,
                )

                # Make the request
                response = await client.update_feed(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.UpdateFeedRequest, dict]]):
                The request object. Update asset feed request.
            feed (:class:`google.cloud.asset_v1.types.Feed`):
                Required. The new values of feed details. It must match
                an existing feed and the field ``name`` must be in the
                format of: projects/project_number/feeds/feed_id or
                folders/folder_number/feeds/feed_id or
                organizations/organization_number/feeds/feed_id.

                This corresponds to the ``feed`` field
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
            google.cloud.asset_v1.types.Feed:
                An asset feed used to export asset
                updates to a destinations. An asset feed
                filter controls what updates are
                exported. The asset feed must be created
                within a project, organization, or
                folder. Supported destinations are:

                Pub/Sub topics.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [feed]
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
        if not isinstance(request, asset_service.UpdateFeedRequest):
            request = asset_service.UpdateFeedRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if feed is not None:
            request.feed = feed

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_feed
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("feed.name", request.feed.name),)
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

    async def delete_feed(
        self,
        request: Optional[Union[asset_service.DeleteFeedRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an asset feed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_delete_feed():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.DeleteFeedRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_feed(request=request)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.DeleteFeedRequest, dict]]):
                The request object.
            name (:class:`str`):
                Required. The name of the feed and it must be in the
                format of: projects/project_number/feeds/feed_id
                folders/folder_number/feeds/feed_id
                organizations/organization_number/feeds/feed_id

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
        if not isinstance(request, asset_service.DeleteFeedRequest):
            request = asset_service.DeleteFeedRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_feed
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

    async def search_all_resources(
        self,
        request: Optional[Union[asset_service.SearchAllResourcesRequest, dict]] = None,
        *,
        scope: Optional[str] = None,
        query: Optional[str] = None,
        asset_types: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchAllResourcesAsyncPager:
        r"""Searches all Google Cloud resources within the specified scope,
        such as a project, folder, or organization. The caller must be
        granted the ``cloudasset.assets.searchAllResources`` permission
        on the desired scope, otherwise the request will be rejected.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_search_all_resources():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.SearchAllResourcesRequest(
                    scope="scope_value",
                )

                # Make the request
                page_result = client.search_all_resources(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.SearchAllResourcesRequest, dict]]):
                The request object. Search all resources request.
            scope (:class:`str`):
                Required. A scope can be a project, a folder, or an
                organization. The search is limited to the resources
                within the ``scope``. The caller must be granted the
                ```cloudasset.assets.searchAllResources`` <https://cloud.google.com/asset-inventory/docs/access-control#required_permissions>`__
                permission on the desired scope.

                The allowed values are:

                - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
                - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
                - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
                - organizations/{ORGANIZATION_NUMBER} (e.g.,
                  "organizations/123456")

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`str`):
                Optional. The query statement. See `how to construct a
                query <https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query>`__
                for more information. If not specified or empty, it will
                search all the resources within the specified ``scope``.

                Examples:

                - ``name:Important`` to find Google Cloud resources
                  whose name contains ``Important`` as a word.
                - ``name=Important`` to find the Google Cloud resource
                  whose name is exactly ``Important``.
                - ``displayName:Impor*`` to find Google Cloud resources
                  whose display name contains ``Impor`` as a prefix of
                  any word in the field.
                - ``location:us-west*`` to find Google Cloud resources
                  whose location contains both ``us`` and ``west`` as
                  prefixes.
                - ``labels:prod`` to find Google Cloud resources whose
                  labels contain ``prod`` as a key or value.
                - ``labels.env:prod`` to find Google Cloud resources
                  that have a label ``env`` and its value is ``prod``.
                - ``labels.env:*`` to find Google Cloud resources that
                  have a label ``env``.
                - ``tagKeys:env`` to find Google Cloud resources that
                  have directly attached tags where the
                  ```TagKey.namespacedName`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey>`__
                  contains ``env``.
                - ``tagValues:prod*`` to find Google Cloud resources
                  that have directly attached tags where the
                  ```TagValue.namespacedName`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue>`__
                  contains a word prefixed by ``prod``.
                - ``tagValueIds=tagValues/123`` to find Google Cloud
                  resources that have directly attached tags where the
                  ```TagValue.name`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue>`__
                  is exactly ``tagValues/123``.
                - ``effectiveTagKeys:env`` to find Google Cloud
                  resources that have directly attached or inherited
                  tags where the
                  ```TagKey.namespacedName`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey>`__
                  contains ``env``.
                - ``effectiveTagValues:prod*`` to find Google Cloud
                  resources that have directly attached or inherited
                  tags where the
                  ```TagValue.namespacedName`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue>`__
                  contains a word prefixed by ``prod``.
                - ``effectiveTagValueIds=tagValues/123`` to find Google
                  Cloud resources that have directly attached or
                  inherited tags where the
                  ```TagValue.name`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue>`__
                  is exactly ``tagValues/123``.
                - ``kmsKey:key`` to find Google Cloud resources
                  encrypted with a customer-managed encryption key whose
                  name contains ``key`` as a word. This field is
                  deprecated. Use the ``kmsKeys`` field to retrieve
                  Cloud KMS key information.
                - ``kmsKeys:key`` to find Google Cloud resources
                  encrypted with customer-managed encryption keys whose
                  name contains the word ``key``.
                - ``relationships:instance-group-1`` to find Google
                  Cloud resources that have relationships with
                  ``instance-group-1`` in the related resource name.
                - ``relationships:INSTANCE_TO_INSTANCEGROUP`` to find
                  Compute Engine instances that have relationships of
                  type ``INSTANCE_TO_INSTANCEGROUP``.
                - ``relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1``
                  to find Compute Engine instances that have
                  relationships with ``instance-group-1`` in the Compute
                  Engine instance group resource name, for relationship
                  type ``INSTANCE_TO_INSTANCEGROUP``.
                - ``sccSecurityMarks.key=value`` to find Cloud resources
                  that are attached with security marks whose key is
                  ``key`` and value is ``value``.
                - ``sccSecurityMarks.key:*`` to find Cloud resources
                  that are attached with security marks whose key is
                  ``key``.
                - ``state:ACTIVE`` to find Google Cloud resources whose
                  state contains ``ACTIVE`` as a word.
                - ``NOT state:ACTIVE`` to find Google Cloud resources
                  whose state doesn't contain ``ACTIVE`` as a word.
                - ``createTime<1609459200`` to find Google Cloud
                  resources that were created before
                  ``2021-01-01 00:00:00 UTC``. ``1609459200`` is the
                  epoch timestamp of ``2021-01-01 00:00:00 UTC`` in
                  seconds.
                - ``updateTime>1609459200`` to find Google Cloud
                  resources that were updated after
                  ``2021-01-01 00:00:00 UTC``. ``1609459200`` is the
                  epoch timestamp of ``2021-01-01 00:00:00 UTC`` in
                  seconds.
                - ``Important`` to find Google Cloud resources that
                  contain ``Important`` as a word in any of the
                  searchable fields.
                - ``Impor*`` to find Google Cloud resources that contain
                  ``Impor`` as a prefix of any word in any of the
                  searchable fields.
                - ``Important location:(us-west1 OR global)`` to find
                  Google Cloud resources that contain ``Important`` as a
                  word in any of the searchable fields and are also
                  located in the ``us-west1`` region or the ``global``
                  location.

                This corresponds to the ``query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            asset_types (:class:`MutableSequence[str]`):
                Optional. A list of asset types that this request
                searches for. If empty, it will search all the asset
                types `supported by search
                APIs <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__.

                Regular expressions are also supported. For example:

                - "compute.googleapis.com.\*" snapshots resources whose
                  asset type starts with "compute.googleapis.com".
                - ".*Instance" snapshots resources whose asset type ends
                  with "Instance".
                - ".\ *Instance.*" snapshots resources whose asset type
                  contains "Instance".

                See `RE2 <https://github.com/google/re2/wiki/Syntax>`__
                for all supported regular expression syntax. If the
                regular expression does not match any supported asset
                type, an INVALID_ARGUMENT error will be returned.

                This corresponds to the ``asset_types`` field
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
            google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager:
                Search all resources response.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, query, asset_types]
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
        if not isinstance(request, asset_service.SearchAllResourcesRequest):
            request = asset_service.SearchAllResourcesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if query is not None:
            request.query = query
        if asset_types:
            request.asset_types.extend(asset_types)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_all_resources
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
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
        response = pagers.SearchAllResourcesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_all_iam_policies(
        self,
        request: Optional[
            Union[asset_service.SearchAllIamPoliciesRequest, dict]
        ] = None,
        *,
        scope: Optional[str] = None,
        query: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchAllIamPoliciesAsyncPager:
        r"""Searches all IAM policies within the specified scope, such as a
        project, folder, or organization. The caller must be granted the
        ``cloudasset.assets.searchAllIamPolicies`` permission on the
        desired scope, otherwise the request will be rejected.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_search_all_iam_policies():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.SearchAllIamPoliciesRequest(
                    scope="scope_value",
                )

                # Make the request
                page_result = client.search_all_iam_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.SearchAllIamPoliciesRequest, dict]]):
                The request object. Search all IAM policies request.
            scope (:class:`str`):
                Required. A scope can be a project, a folder, or an
                organization. The search is limited to the IAM policies
                within the ``scope``. The caller must be granted the
                ```cloudasset.assets.searchAllIamPolicies`` <https://cloud.google.com/asset-inventory/docs/access-control#required_permissions>`__
                permission on the desired scope.

                The allowed values are:

                - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
                - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
                - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
                - organizations/{ORGANIZATION_NUMBER} (e.g.,
                  "organizations/123456")

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`str`):
                Optional. The query statement. See `how to construct a
                query <https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query>`__
                for more information. If not specified or empty, it will
                search all the IAM policies within the specified
                ``scope``. Note that the query string is compared
                against each IAM policy binding, including its
                principals, roles, and IAM conditions. The returned IAM
                policies will only contain the bindings that match your
                query. To learn more about the IAM policy structure, see
                the `IAM policy
                documentation <https://cloud.google.com/iam/help/allow-policies/structure>`__.

                Examples:

                - ``policy:amy@gmail.com`` to find IAM policy bindings
                  that specify user "amy@gmail.com".
                - ``policy:roles/compute.admin`` to find IAM policy
                  bindings that specify the Compute Admin role.
                - ``policy:comp*`` to find IAM policy bindings that
                  contain "comp" as a prefix of any word in the binding.
                - ``policy.role.permissions:storage.buckets.update`` to
                  find IAM policy bindings that specify a role
                  containing "storage.buckets.update" permission. Note
                  that if callers don't have ``iam.roles.get`` access to
                  a role's included permissions, policy bindings that
                  specify this role will be dropped from the search
                  results.
                - ``policy.role.permissions:upd*`` to find IAM policy
                  bindings that specify a role containing "upd" as a
                  prefix of any word in the role permission. Note that
                  if callers don't have ``iam.roles.get`` access to a
                  role's included permissions, policy bindings that
                  specify this role will be dropped from the search
                  results.
                - ``resource:organizations/123456`` to find IAM policy
                  bindings that are set on "organizations/123456".
                - ``resource=//cloudresourcemanager.googleapis.com/projects/myproject``
                  to find IAM policy bindings that are set on the
                  project named "myproject".
                - ``Important`` to find IAM policy bindings that contain
                  "Important" as a word in any of the searchable fields
                  (except for the included permissions).
                - ``resource:(instance1 OR instance2) policy:amy`` to
                  find IAM policy bindings that are set on resources
                  "instance1" or "instance2" and also specify user
                  "amy".
                - ``roles:roles/compute.admin`` to find IAM policy
                  bindings that specify the Compute Admin role.
                - ``memberTypes:user`` to find IAM policy bindings that
                  contain the principal type "user".

                This corresponds to the ``query`` field
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
            google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager:
                Search all IAM policies response.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, query]
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
        if not isinstance(request, asset_service.SearchAllIamPoliciesRequest):
            request = asset_service.SearchAllIamPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if query is not None:
            request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_all_iam_policies
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
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
        response = pagers.SearchAllIamPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def analyze_iam_policy(
        self,
        request: Optional[Union[asset_service.AnalyzeIamPolicyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.AnalyzeIamPolicyResponse:
        r"""Analyzes IAM policies to answer which identities have
        what accesses on which resources.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_analyze_iam_policy():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                analysis_query = asset_v1.IamPolicyAnalysisQuery()
                analysis_query.scope = "scope_value"

                request = asset_v1.AnalyzeIamPolicyRequest(
                    analysis_query=analysis_query,
                )

                # Make the request
                response = await client.analyze_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.AnalyzeIamPolicyRequest, dict]]):
                The request object. A request message for
                [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.asset_v1.types.AnalyzeIamPolicyResponse:
                A response message for
                   [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, asset_service.AnalyzeIamPolicyRequest):
            request = asset_service.AnalyzeIamPolicyRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.analyze_iam_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("analysis_query.scope", request.analysis_query.scope),)
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

    async def analyze_iam_policy_longrunning(
        self,
        request: Optional[
            Union[asset_service.AnalyzeIamPolicyLongrunningRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Analyzes IAM policies asynchronously to answer which identities
        have what accesses on which resources, and writes the analysis
        results to a Google Cloud Storage or a BigQuery destination. For
        Cloud Storage destination, the output format is the JSON format
        that represents a
        [AnalyzeIamPolicyResponse][google.cloud.asset.v1.AnalyzeIamPolicyResponse].
        This method implements the
        [google.longrunning.Operation][google.longrunning.Operation],
        which allows you to track the operation status. We recommend
        intervals of at least 2 seconds with exponential backoff retry
        to poll the operation result. The metadata contains the metadata
        for the long-running operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_analyze_iam_policy_longrunning():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                analysis_query = asset_v1.IamPolicyAnalysisQuery()
                analysis_query.scope = "scope_value"

                output_config = asset_v1.IamPolicyAnalysisOutputConfig()
                output_config.gcs_destination.uri = "uri_value"

                request = asset_v1.AnalyzeIamPolicyLongrunningRequest(
                    analysis_query=analysis_query,
                    output_config=output_config,
                )

                # Make the request
                operation = await client.analyze_iam_policy_longrunning(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningRequest, dict]]):
                The request object. A request message for
                [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning].
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

                The result type for the operation will be :class:`google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningResponse` A response message for
                   [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, asset_service.AnalyzeIamPolicyLongrunningRequest):
            request = asset_service.AnalyzeIamPolicyLongrunningRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.analyze_iam_policy_longrunning
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("analysis_query.scope", request.analysis_query.scope),)
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
            asset_service.AnalyzeIamPolicyLongrunningResponse,
            metadata_type=asset_service.AnalyzeIamPolicyLongrunningMetadata,
        )

        # Done; return the response.
        return response

    async def analyze_move(
        self,
        request: Optional[Union[asset_service.AnalyzeMoveRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.AnalyzeMoveResponse:
        r"""Analyze moving a resource to a specified destination
        without kicking off the actual move. The analysis is
        best effort depending on the user's permissions of
        viewing different hierarchical policies and
        configurations. The policies and configuration are
        subject to change before the actual resource migration
        takes place.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_analyze_move():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.AnalyzeMoveRequest(
                    resource="resource_value",
                    destination_parent="destination_parent_value",
                )

                # Make the request
                response = await client.analyze_move(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.AnalyzeMoveRequest, dict]]):
                The request object. The request message for performing
                resource move analysis.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.asset_v1.types.AnalyzeMoveResponse:
                The response message for resource
                move analysis.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, asset_service.AnalyzeMoveRequest):
            request = asset_service.AnalyzeMoveRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.analyze_move
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

        # Done; return the response.
        return response

    async def query_assets(
        self,
        request: Optional[Union[asset_service.QueryAssetsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.QueryAssetsResponse:
        r"""Issue a job that queries assets using a SQL statement compatible
        with `BigQuery
        SQL <https://cloud.google.com/bigquery/docs/introduction-sql>`__.

        If the query execution finishes within timeout and there's no
        pagination, the full query results will be returned in the
        ``QueryAssetsResponse``.

        Otherwise, full query results can be obtained by issuing extra
        requests with the ``job_reference`` from the a previous
        ``QueryAssets`` call.

        Note, the query result has approximately 10 GB limitation
        enforced by
        `BigQuery <https://cloud.google.com/bigquery/docs/best-practices-performance-output>`__.
        Queries return larger results will result in errors.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_query_assets():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.QueryAssetsRequest(
                    statement="statement_value",
                    parent="parent_value",
                )

                # Make the request
                response = await client.query_assets(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.QueryAssetsRequest, dict]]):
                The request object. QueryAssets request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.asset_v1.types.QueryAssetsResponse:
                QueryAssets response.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, asset_service.QueryAssetsRequest):
            request = asset_service.QueryAssetsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.query_assets
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

    async def create_saved_query(
        self,
        request: Optional[Union[asset_service.CreateSavedQueryRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        saved_query: Optional[asset_service.SavedQuery] = None,
        saved_query_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.SavedQuery:
        r"""Creates a saved query in a parent
        project/folder/organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_create_saved_query():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.CreateSavedQueryRequest(
                    parent="parent_value",
                    saved_query_id="saved_query_id_value",
                )

                # Make the request
                response = await client.create_saved_query(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.CreateSavedQueryRequest, dict]]):
                The request object. Request to create a saved query.
            parent (:class:`str`):
                Required. The name of the project/folder/organization
                where this saved_query should be created in. It can only
                be an organization number (such as "organizations/123"),
                a folder number (such as "folders/123"), a project ID
                (such as "projects/my-project-id"), or a project number
                (such as "projects/12345").

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            saved_query (:class:`google.cloud.asset_v1.types.SavedQuery`):
                Required. The saved_query details. The ``name`` field
                must be empty as it will be generated based on the
                parent and saved_query_id.

                This corresponds to the ``saved_query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            saved_query_id (:class:`str`):
                Required. The ID to use for the saved query, which must
                be unique in the specified parent. It will become the
                final component of the saved query's resource name.

                This value should be 4-63 characters, and valid
                characters are ``[a-z][0-9]-``.

                Notice that this field is required in the saved query
                creation, and the ``name`` field of the ``saved_query``
                will be ignored.

                This corresponds to the ``saved_query_id`` field
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
            google.cloud.asset_v1.types.SavedQuery:
                A saved query which can be shared
                with others or used later.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, saved_query, saved_query_id]
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
        if not isinstance(request, asset_service.CreateSavedQueryRequest):
            request = asset_service.CreateSavedQueryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if saved_query is not None:
            request.saved_query = saved_query
        if saved_query_id is not None:
            request.saved_query_id = saved_query_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_saved_query
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

    async def get_saved_query(
        self,
        request: Optional[Union[asset_service.GetSavedQueryRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.SavedQuery:
        r"""Gets details about a saved query.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_get_saved_query():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.GetSavedQueryRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_saved_query(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.GetSavedQueryRequest, dict]]):
                The request object. Request to get a saved query.
            name (:class:`str`):
                Required. The name of the saved query and it must be in
                the format of:

                - projects/project_number/savedQueries/saved_query_id
                - folders/folder_number/savedQueries/saved_query_id
                - organizations/organization_number/savedQueries/saved_query_id

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
            google.cloud.asset_v1.types.SavedQuery:
                A saved query which can be shared
                with others or used later.

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
        if not isinstance(request, asset_service.GetSavedQueryRequest):
            request = asset_service.GetSavedQueryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_saved_query
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

    async def list_saved_queries(
        self,
        request: Optional[Union[asset_service.ListSavedQueriesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSavedQueriesAsyncPager:
        r"""Lists all saved queries in a parent
        project/folder/organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_list_saved_queries():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.ListSavedQueriesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_saved_queries(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.ListSavedQueriesRequest, dict]]):
                The request object. Request to list saved queries.
            parent (:class:`str`):
                Required. The parent
                project/folder/organization whose
                savedQueries are to be listed. It can
                only be using
                project/folder/organization number (such
                as "folders/12345")", or a project ID
                (such as "projects/my-project-id").

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
            google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager:
                Response of listing saved queries.

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
        if not isinstance(request, asset_service.ListSavedQueriesRequest):
            request = asset_service.ListSavedQueriesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_saved_queries
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
        response = pagers.ListSavedQueriesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_saved_query(
        self,
        request: Optional[Union[asset_service.UpdateSavedQueryRequest, dict]] = None,
        *,
        saved_query: Optional[asset_service.SavedQuery] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.SavedQuery:
        r"""Updates a saved query.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_update_saved_query():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.UpdateSavedQueryRequest(
                )

                # Make the request
                response = await client.update_saved_query(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.UpdateSavedQueryRequest, dict]]):
                The request object. Request to update a saved query.
            saved_query (:class:`google.cloud.asset_v1.types.SavedQuery`):
                Required. The saved query to update.

                The saved query's ``name`` field is used to identify the
                one to update, which has format as below:

                - projects/project_number/savedQueries/saved_query_id
                - folders/folder_number/savedQueries/saved_query_id
                - organizations/organization_number/savedQueries/saved_query_id

                This corresponds to the ``saved_query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to
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
            google.cloud.asset_v1.types.SavedQuery:
                A saved query which can be shared
                with others or used later.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [saved_query, update_mask]
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
        if not isinstance(request, asset_service.UpdateSavedQueryRequest):
            request = asset_service.UpdateSavedQueryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if saved_query is not None:
            request.saved_query = saved_query
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_saved_query
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("saved_query.name", request.saved_query.name),)
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

    async def delete_saved_query(
        self,
        request: Optional[Union[asset_service.DeleteSavedQueryRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a saved query.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_delete_saved_query():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.DeleteSavedQueryRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_saved_query(request=request)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.DeleteSavedQueryRequest, dict]]):
                The request object. Request to delete a saved query.
            name (:class:`str`):
                Required. The name of the saved query to delete. It must
                be in the format of:

                - projects/project_number/savedQueries/saved_query_id
                - folders/folder_number/savedQueries/saved_query_id
                - organizations/organization_number/savedQueries/saved_query_id

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
        if not isinstance(request, asset_service.DeleteSavedQueryRequest):
            request = asset_service.DeleteSavedQueryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_saved_query
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

    async def batch_get_effective_iam_policies(
        self,
        request: Optional[
            Union[asset_service.BatchGetEffectiveIamPoliciesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> asset_service.BatchGetEffectiveIamPoliciesResponse:
        r"""Gets effective IAM policies for a batch of resources.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_batch_get_effective_iam_policies():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.BatchGetEffectiveIamPoliciesRequest(
                    scope="scope_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = await client.batch_get_effective_iam_policies(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesRequest, dict]]):
                The request object. A request message for
                [AssetService.BatchGetEffectiveIamPolicies][google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesResponse:
                A response message for
                   [AssetService.BatchGetEffectiveIamPolicies][google.cloud.asset.v1.AssetService.BatchGetEffectiveIamPolicies].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, asset_service.BatchGetEffectiveIamPoliciesRequest):
            request = asset_service.BatchGetEffectiveIamPoliciesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_get_effective_iam_policies
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
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

    async def analyze_org_policies(
        self,
        request: Optional[Union[asset_service.AnalyzeOrgPoliciesRequest, dict]] = None,
        *,
        scope: Optional[str] = None,
        constraint: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.AnalyzeOrgPoliciesAsyncPager:
        r"""Analyzes organization policies under a scope.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_analyze_org_policies():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.AnalyzeOrgPoliciesRequest(
                    scope="scope_value",
                    constraint="constraint_value",
                )

                # Make the request
                page_result = client.analyze_org_policies(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.AnalyzeOrgPoliciesRequest, dict]]):
                The request object. A request message for
                [AssetService.AnalyzeOrgPolicies][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies].
            scope (:class:`str`):
                Required. The organization to scope the request. Only
                organization policies within the scope will be analyzed.

                - organizations/{ORGANIZATION_NUMBER} (e.g.,
                  "organizations/123456")

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            constraint (:class:`str`):
                Required. The name of the constraint
                to analyze organization policies for.
                The response only contains analyzed
                organization policies for the provided
                constraint.

                This corresponds to the ``constraint`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                The expression to filter
                [AnalyzeOrgPoliciesResponse.org_policy_results][google.cloud.asset.v1.AnalyzeOrgPoliciesResponse.org_policy_results].
                Filtering is currently available for bare literal values
                and the following fields:

                - consolidated_policy.attached_resource
                - consolidated_policy.rules.enforce

                When filtering by a specific field, the only supported
                operator is ``=``. For example, filtering by
                consolidated_policy.attached_resource="//cloudresourcemanager.googleapis.com/folders/001"
                will return all the Organization Policy results attached
                to "folders/001".

                This corresponds to the ``filter`` field
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
            google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager:
                The response message for
                   [AssetService.AnalyzeOrgPolicies][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicies].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, constraint, filter]
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
        if not isinstance(request, asset_service.AnalyzeOrgPoliciesRequest):
            request = asset_service.AnalyzeOrgPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if constraint is not None:
            request.constraint = constraint
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.analyze_org_policies
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
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
        response = pagers.AnalyzeOrgPoliciesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def analyze_org_policy_governed_containers(
        self,
        request: Optional[
            Union[asset_service.AnalyzeOrgPolicyGovernedContainersRequest, dict]
        ] = None,
        *,
        scope: Optional[str] = None,
        constraint: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager:
        r"""Analyzes organization policies governed containers
        (projects, folders or organization) under a scope.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_analyze_org_policy_governed_containers():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.AnalyzeOrgPolicyGovernedContainersRequest(
                    scope="scope_value",
                    constraint="constraint_value",
                )

                # Make the request
                page_result = client.analyze_org_policy_governed_containers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersRequest, dict]]):
                The request object. A request message for
                [AssetService.AnalyzeOrgPolicyGovernedContainers][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers].
            scope (:class:`str`):
                Required. The organization to scope the request. Only
                organization policies within the scope will be analyzed.
                The output containers will also be limited to the ones
                governed by those in-scope organization policies.

                - organizations/{ORGANIZATION_NUMBER} (e.g.,
                  "organizations/123456")

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            constraint (:class:`str`):
                Required. The name of the constraint
                to analyze governed containers for. The
                analysis only contains organization
                policies for the provided constraint.

                This corresponds to the ``constraint`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                The expression to filter
                [AnalyzeOrgPolicyGovernedContainersResponse.governed_containers][google.cloud.asset.v1.AnalyzeOrgPolicyGovernedContainersResponse.governed_containers].
                Filtering is currently available for bare literal values
                and the following fields:

                - parent
                - consolidated_policy.rules.enforce

                When filtering by a specific field, the only supported
                operator is ``=``. For example, filtering by
                parent="//cloudresourcemanager.googleapis.com/folders/001"
                will return all the containers under "folders/001".

                This corresponds to the ``filter`` field
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
            google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager:
                The response message for
                   [AssetService.AnalyzeOrgPolicyGovernedContainers][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedContainers].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, constraint, filter]
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
            request, asset_service.AnalyzeOrgPolicyGovernedContainersRequest
        ):
            request = asset_service.AnalyzeOrgPolicyGovernedContainersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if constraint is not None:
            request.constraint = constraint
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.analyze_org_policy_governed_containers
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
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
        response = pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def analyze_org_policy_governed_assets(
        self,
        request: Optional[
            Union[asset_service.AnalyzeOrgPolicyGovernedAssetsRequest, dict]
        ] = None,
        *,
        scope: Optional[str] = None,
        constraint: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager:
        r"""Analyzes organization policies governed assets (Google Cloud
        resources or policies) under a scope. This RPC supports custom
        constraints and the following canned constraints:

        - constraints/ainotebooks.accessMode
        - constraints/ainotebooks.disableFileDownloads
        - constraints/ainotebooks.disableRootAccess
        - constraints/ainotebooks.disableTerminal
        - constraints/ainotebooks.environmentOptions
        - constraints/ainotebooks.requireAutoUpgradeSchedule
        - constraints/ainotebooks.restrictVpcNetworks
        - constraints/compute.disableGuestAttributesAccess
        - constraints/compute.disableInstanceDataAccessApis
        - constraints/compute.disableNestedVirtualization
        - constraints/compute.disableSerialPortAccess
        - constraints/compute.disableSerialPortLogging
        - constraints/compute.disableVpcExternalIpv6
        - constraints/compute.requireOsLogin
        - constraints/compute.requireShieldedVm
        - constraints/compute.restrictLoadBalancerCreationForTypes
        - constraints/compute.restrictProtocolForwardingCreationForTypes
        - constraints/compute.restrictXpnProjectLienRemoval
        - constraints/compute.setNewProjectDefaultToZonalDNSOnly
        - constraints/compute.skipDefaultNetworkCreation
        - constraints/compute.trustedImageProjects
        - constraints/compute.vmCanIpForward
        - constraints/compute.vmExternalIpAccess
        - constraints/gcp.detailedAuditLoggingMode
        - constraints/gcp.resourceLocations
        - constraints/iam.allowedPolicyMemberDomains
        - constraints/iam.automaticIamGrantsForDefaultServiceAccounts
        - constraints/iam.disableServiceAccountCreation
        - constraints/iam.disableServiceAccountKeyCreation
        - constraints/iam.disableServiceAccountKeyUpload
        - constraints/iam.restrictCrossProjectServiceAccountLienRemoval
        - constraints/iam.serviceAccountKeyExpiryHours
        - constraints/resourcemanager.accessBoundaries
        - constraints/resourcemanager.allowedExportDestinations
        - constraints/sql.restrictAuthorizedNetworks
        - constraints/sql.restrictNoncompliantDiagnosticDataAccess
        - constraints/sql.restrictNoncompliantResourceCreation
        - constraints/sql.restrictPublicIp
        - constraints/storage.publicAccessPrevention
        - constraints/storage.restrictAuthTypes
        - constraints/storage.uniformBucketLevelAccess

        This RPC only returns either resources of types `supported by
        search
        APIs <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
        or IAM policies.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import asset_v1

            async def sample_analyze_org_policy_governed_assets():
                # Create a client
                client = asset_v1.AssetServiceAsyncClient()

                # Initialize request argument(s)
                request = asset_v1.AnalyzeOrgPolicyGovernedAssetsRequest(
                    scope="scope_value",
                    constraint="constraint_value",
                )

                # Make the request
                page_result = client.analyze_org_policy_governed_assets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsRequest, dict]]):
                The request object. A request message for
                [AssetService.AnalyzeOrgPolicyGovernedAssets][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets].
            scope (:class:`str`):
                Required. The organization to scope the request. Only
                organization policies within the scope will be analyzed.
                The output assets will also be limited to the ones
                governed by those in-scope organization policies.

                - organizations/{ORGANIZATION_NUMBER} (e.g.,
                  "organizations/123456")

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            constraint (:class:`str`):
                Required. The name of the constraint
                to analyze governed assets for. The
                analysis only contains analyzed
                organization policies for the provided
                constraint.

                This corresponds to the ``constraint`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                The expression to filter
                [AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets][google.cloud.asset.v1.AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets].

                For governed resources, filtering is currently available
                for bare literal values and the following fields:

                - governed_resource.project
                - governed_resource.folders
                - consolidated_policy.rules.enforce When filtering by
                  ``governed_resource.project`` or
                  ``consolidated_policy.rules.enforce``, the only
                  supported operator is ``=``. When filtering by
                  ``governed_resource.folders``, the supported operators
                  are ``=`` and ``:``. For example, filtering by
                  ``governed_resource.project="projects/12345678"`` will
                  return all the governed resources under
                  "projects/12345678", including the project itself if
                  applicable.

                For governed IAM policies, filtering is currently
                available for bare literal values and the following
                fields:

                - governed_iam_policy.project
                - governed_iam_policy.folders
                - consolidated_policy.rules.enforce When filtering by
                  ``governed_iam_policy.project`` or
                  ``consolidated_policy.rules.enforce``, the only
                  supported operator is ``=``. When filtering by
                  ``governed_iam_policy.folders``, the supported
                  operators are ``=`` and ``:``. For example, filtering
                  by ``governed_iam_policy.folders:"folders/12345678"``
                  will return all the governed IAM policies under
                  "folders/001".

                This corresponds to the ``filter`` field
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
            google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager:
                The response message for
                   [AssetService.AnalyzeOrgPolicyGovernedAssets][google.cloud.asset.v1.AssetService.AnalyzeOrgPolicyGovernedAssets].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, constraint, filter]
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
        if not isinstance(request, asset_service.AnalyzeOrgPolicyGovernedAssetsRequest):
            request = asset_service.AnalyzeOrgPolicyGovernedAssetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if constraint is not None:
            request.constraint = constraint
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.analyze_org_policy_governed_assets
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
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
        response = pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
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

    async def __aenter__(self) -> "AssetServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AssetServiceAsyncClient",)
