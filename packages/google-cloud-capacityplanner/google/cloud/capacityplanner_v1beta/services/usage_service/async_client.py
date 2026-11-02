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

from google.cloud.capacityplanner_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore

from google.cloud.capacityplanner_v1beta.types import usage_service

from .client import UsageServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, UsageServiceTransport
from .transports.grpc_asyncio import UsageServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class UsageServiceAsyncClient:
    """Provides access to historical and forecasted usage data."""

    _client: UsageServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = UsageServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = UsageServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = UsageServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = UsageServiceClient._DEFAULT_UNIVERSE

    forecast_path = staticmethod(UsageServiceClient.forecast_path)
    parse_forecast_path = staticmethod(UsageServiceClient.parse_forecast_path)
    reservation_path = staticmethod(UsageServiceClient.reservation_path)
    parse_reservation_path = staticmethod(UsageServiceClient.parse_reservation_path)
    common_billing_account_path = staticmethod(
        UsageServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        UsageServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(UsageServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(UsageServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(UsageServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        UsageServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(UsageServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        UsageServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(UsageServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        UsageServiceClient.parse_common_location_path
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
            UsageServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            UsageServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(UsageServiceAsyncClient, info, *args, **kwargs)

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
            UsageServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            UsageServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(UsageServiceAsyncClient, filename, *args, **kwargs)

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
        return UsageServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> UsageServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            UsageServiceTransport: The transport used by the client instance.
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

    get_transport_class = UsageServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, UsageServiceTransport, Callable[..., UsageServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the usage service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,UsageServiceTransport,Callable[..., UsageServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the UsageServiceTransport constructor.
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
        self._client = UsageServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.capacityplanner_v1beta.UsageServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
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
                    "serviceName": "google.cloud.capacityplanner.v1beta.UsageService",
                    "credentialsType": None,
                },
            )

    async def query_usage_histories(
        self,
        request: Optional[Union[usage_service.QueryUsageHistoriesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> usage_service.QueryUsageHistoriesResponse:
        r"""Returns a list of the usage histories that are in the
        parent parameter and match your specified filters.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import capacityplanner_v1beta

            async def sample_query_usage_histories():
                # Create a client
                client = capacityplanner_v1beta.UsageServiceAsyncClient()

                # Initialize request argument(s)
                request = capacityplanner_v1beta.QueryUsageHistoriesRequest(
                    parent="parent_value",
                    cloud_resource_type="cloud_resource_type_value",
                )

                # Make the request
                response = await client.query_usage_histories(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.capacityplanner_v1beta.types.QueryUsageHistoriesRequest, dict]]):
                The request object. The ``QueryUsageHistories`` request. Next : 16
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.capacityplanner_v1beta.types.QueryUsageHistoriesResponse:
                The QueryUsageHistories response.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, usage_service.QueryUsageHistoriesRequest):
            request = usage_service.QueryUsageHistoriesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.query_usage_histories
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

    async def query_forecasts(
        self,
        request: Optional[Union[usage_service.QueryForecastsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> usage_service.QueryForecastsResponse:
        r"""Returns a list of the forecasts that are in the
        parent parameter and match your specified filters.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import capacityplanner_v1beta

            async def sample_query_forecasts():
                # Create a client
                client = capacityplanner_v1beta.UsageServiceAsyncClient()

                # Initialize request argument(s)
                request = capacityplanner_v1beta.QueryForecastsRequest(
                    parent="parent_value",
                    cloud_resource_type="cloud_resource_type_value",
                )

                # Make the request
                response = await client.query_forecasts(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.capacityplanner_v1beta.types.QueryForecastsRequest, dict]]):
                The request object. The ``QueryForecasts`` request. Next : 14
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.capacityplanner_v1beta.types.QueryForecastsResponse:
                The QueryForecasts response.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, usage_service.QueryForecastsRequest):
            request = usage_service.QueryForecastsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.query_forecasts
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

    async def query_reservations(
        self,
        request: Optional[Union[usage_service.QueryReservationsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> usage_service.QueryReservationsResponse:
        r"""Returns a list of the reservations that are in the
        parent parameter and match your specified filters.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import capacityplanner_v1beta

            async def sample_query_reservations():
                # Create a client
                client = capacityplanner_v1beta.UsageServiceAsyncClient()

                # Initialize request argument(s)
                request = capacityplanner_v1beta.QueryReservationsRequest(
                    parent="parent_value",
                    cloud_resource_type="cloud_resource_type_value",
                    reservation_type="RESERVATION_TYPE_ALL",
                    reservation_data_level="RESERVATION_DATA_LEVEL_PER_RESERVATION",
                )

                # Make the request
                response = await client.query_reservations(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.capacityplanner_v1beta.types.QueryReservationsRequest, dict]]):
                The request object. The ``QueryReservations`` request.
            parent (:class:`str`):
                Required. The compute engine resource
                and location for the time series values
                to return. The format is:

                projects/{project}/locations/{location}
                or
                organizations/{organization}/locations/{location}
                or folders/{folder}/locations/{location}

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
            google.cloud.capacityplanner_v1beta.types.QueryReservationsResponse:
                The QueryReservations response.
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
        if not isinstance(request, usage_service.QueryReservationsRequest):
            request = usage_service.QueryReservationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.query_reservations
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

    async def export_usage_histories(
        self,
        request: Optional[
            Union[usage_service.ExportUsageHistoriesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports historical usage data requested by user into
        either an existing Cloud Storage bucket or a BigQuery
        table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import capacityplanner_v1beta

            async def sample_export_usage_histories():
                # Create a client
                client = capacityplanner_v1beta.UsageServiceAsyncClient()

                # Initialize request argument(s)
                output_config = capacityplanner_v1beta.OutputConfig()
                output_config.gcs_destination.bucket = "bucket_value"
                output_config.gcs_destination.object_ = "object__value"

                request = capacityplanner_v1beta.ExportUsageHistoriesRequest(
                    parent="parent_value",
                    resource_type="resource_type_value",
                    output_config=output_config,
                )

                # Make the request
                operation = await client.export_usage_histories(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.capacityplanner_v1beta.types.ExportUsageHistoriesRequest, dict]]):
                The request object. The ``ExportUsageHistories`` request Next : 12
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

                The result type for the operation will be
                :class:`google.cloud.capacityplanner_v1beta.types.ExportUsageHistoriesResponse`
                A response message for
                [UsageService.ExportUsageHistories].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, usage_service.ExportUsageHistoriesRequest):
            request = usage_service.ExportUsageHistoriesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_usage_histories
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
            usage_service.ExportUsageHistoriesResponse,
            metadata_type=usage_service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def export_forecasts(
        self,
        request: Optional[Union[usage_service.ExportForecastsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports forecasted usage data requested by user into
        either an existing Cloud Storage bucket or a BigQuery
        table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import capacityplanner_v1beta

            async def sample_export_forecasts():
                # Create a client
                client = capacityplanner_v1beta.UsageServiceAsyncClient()

                # Initialize request argument(s)
                output_config = capacityplanner_v1beta.OutputConfig()
                output_config.gcs_destination.bucket = "bucket_value"
                output_config.gcs_destination.object_ = "object__value"

                request = capacityplanner_v1beta.ExportForecastsRequest(
                    parent="parent_value",
                    resource_type="resource_type_value",
                    output_config=output_config,
                )

                # Make the request
                operation = await client.export_forecasts(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.capacityplanner_v1beta.types.ExportForecastsRequest, dict]]):
                The request object. The ``ExportForecasts`` request Next : 13
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

                The result type for the operation will be
                :class:`google.cloud.capacityplanner_v1beta.types.ExportForecastsResponse`
                A response message for [UsageService.ExportForecasts].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, usage_service.ExportForecastsRequest):
            request = usage_service.ExportForecastsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_forecasts
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
            usage_service.ExportForecastsResponse,
            metadata_type=usage_service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def export_reservations_usage(
        self,
        request: Optional[
            Union[usage_service.ExportReservationsUsageRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports reservations usage data requested by user
        into either an existing Cloud Storage bucket or a
        new/existing BigQuery table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import capacityplanner_v1beta

            async def sample_export_reservations_usage():
                # Create a client
                client = capacityplanner_v1beta.UsageServiceAsyncClient()

                # Initialize request argument(s)
                output_config = capacityplanner_v1beta.OutputConfig()
                output_config.gcs_destination.bucket = "bucket_value"
                output_config.gcs_destination.object_ = "object__value"

                request = capacityplanner_v1beta.ExportReservationsUsageRequest(
                    machine_family="machine_family_value",
                    parent="parent_value",
                    cloud_resource_type="cloud_resource_type_value",
                    usage_aggregation_method="P99",
                    output_config=output_config,
                )

                # Make the request
                operation = await client.export_reservations_usage(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.capacityplanner_v1beta.types.ExportReservationsUsageRequest, dict]]):
                The request object. The ``ExportReservationsUsage`` request
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

                The result type for the operation will be
                :class:`google.cloud.capacityplanner_v1beta.types.ExportReservationsUsageResponse`
                A response message for
                [UsageService.ExportReservationsUsage].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, usage_service.ExportReservationsUsageRequest):
            request = usage_service.ExportReservationsUsageRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_reservations_usage
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
            usage_service.ExportReservationsUsageResponse,
            metadata_type=usage_service.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "UsageServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("UsageServiceAsyncClient",)
