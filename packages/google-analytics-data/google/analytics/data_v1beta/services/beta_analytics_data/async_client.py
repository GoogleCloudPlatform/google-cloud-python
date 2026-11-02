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

from google.analytics.data_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.analytics.data_v1beta.services.beta_analytics_data import pagers
from google.analytics.data_v1beta.types import analytics_data_api, data

from .client import BetaAnalyticsDataClient
from .transports.base import DEFAULT_CLIENT_INFO, BetaAnalyticsDataTransport
from .transports.grpc_asyncio import BetaAnalyticsDataGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class BetaAnalyticsDataAsyncClient:
    """Google Analytics reporting data service."""

    _client: BetaAnalyticsDataClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = BetaAnalyticsDataClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = BetaAnalyticsDataClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = BetaAnalyticsDataClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = BetaAnalyticsDataClient._DEFAULT_UNIVERSE

    audience_export_path = staticmethod(BetaAnalyticsDataClient.audience_export_path)
    parse_audience_export_path = staticmethod(
        BetaAnalyticsDataClient.parse_audience_export_path
    )
    metadata_path = staticmethod(BetaAnalyticsDataClient.metadata_path)
    parse_metadata_path = staticmethod(BetaAnalyticsDataClient.parse_metadata_path)
    common_billing_account_path = staticmethod(
        BetaAnalyticsDataClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(BetaAnalyticsDataClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        BetaAnalyticsDataClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_organization_path
    )
    common_project_path = staticmethod(BetaAnalyticsDataClient.common_project_path)
    parse_common_project_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_project_path
    )
    common_location_path = staticmethod(BetaAnalyticsDataClient.common_location_path)
    parse_common_location_path = staticmethod(
        BetaAnalyticsDataClient.parse_common_location_path
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
            BetaAnalyticsDataAsyncClient: The constructed client.
        """
        sa_info_func = (
            BetaAnalyticsDataClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(BetaAnalyticsDataAsyncClient, info, *args, **kwargs)

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
            BetaAnalyticsDataAsyncClient: The constructed client.
        """
        sa_file_func = (
            BetaAnalyticsDataClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(BetaAnalyticsDataAsyncClient, filename, *args, **kwargs)

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
        return BetaAnalyticsDataClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> BetaAnalyticsDataTransport:
        """Returns the transport used by the client instance.

        Returns:
            BetaAnalyticsDataTransport: The transport used by the client instance.
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

    get_transport_class = BetaAnalyticsDataClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                BetaAnalyticsDataTransport,
                Callable[..., BetaAnalyticsDataTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the beta analytics data async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,BetaAnalyticsDataTransport,Callable[..., BetaAnalyticsDataTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the BetaAnalyticsDataTransport constructor.
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
        self._client = BetaAnalyticsDataClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.analytics.data_v1beta.BetaAnalyticsDataAsyncClient`.",
                extra={
                    "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
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
                    "serviceName": "google.analytics.data.v1beta.BetaAnalyticsData",
                    "credentialsType": None,
                },
            )

    async def run_report(
        self,
        request: Optional[Union[analytics_data_api.RunReportRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RunReportResponse:
        r"""Returns a customized report of your Google Analytics event data.
        Reports contain statistics derived from data collected by the
        Google Analytics tracking code. The data returned from the API
        is as a table with columns for the requested dimensions and
        metrics. Metrics are individual measurements of user activity on
        your property, such as active users or event count. Dimensions
        break down metrics across some common criteria, such as country
        or event name.

        For a guide to constructing requests & understanding responses,
        see `Creating a
        Report <https://developers.google.com/analytics/devguides/reporting/data/v1/basics>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_run_report():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.RunReportRequest(
                )

                # Make the request
                response = await client.run_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.RunReportRequest, dict]]):
                The request object. The request to generate a report.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1beta.types.RunReportResponse:
                The response report table
                corresponding to a request.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.RunReportRequest):
            request = analytics_data_api.RunReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
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

    async def run_pivot_report(
        self,
        request: Optional[Union[analytics_data_api.RunPivotReportRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RunPivotReportResponse:
        r"""Returns a customized pivot report of your Google
        Analytics event data. Pivot reports are more advanced
        and expressive formats than regular reports. In a pivot
        report, dimensions are only visible if they are included
        in a pivot. Multiple pivots can be specified to further
        dissect your data.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_run_pivot_report():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.RunPivotReportRequest(
                )

                # Make the request
                response = await client.run_pivot_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.RunPivotReportRequest, dict]]):
                The request object. The request to generate a pivot
                report.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1beta.types.RunPivotReportResponse:
                The response pivot report table
                corresponding to a pivot request.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.RunPivotReportRequest):
            request = analytics_data_api.RunPivotReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_pivot_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
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

    async def batch_run_reports(
        self,
        request: Optional[
            Union[analytics_data_api.BatchRunReportsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.BatchRunReportsResponse:
        r"""Returns multiple reports in a batch. All reports must
        be for the same Google Analytics property.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_batch_run_reports():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.BatchRunReportsRequest(
                )

                # Make the request
                response = await client.batch_run_reports(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.BatchRunReportsRequest, dict]]):
                The request object. The batch request containing multiple
                report requests.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1beta.types.BatchRunReportsResponse:
                The batch response containing
                multiple reports.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.BatchRunReportsRequest):
            request = analytics_data_api.BatchRunReportsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_run_reports
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
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

    async def batch_run_pivot_reports(
        self,
        request: Optional[
            Union[analytics_data_api.BatchRunPivotReportsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.BatchRunPivotReportsResponse:
        r"""Returns multiple pivot reports in a batch. All
        reports must be for the same Google Analytics property.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_batch_run_pivot_reports():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.BatchRunPivotReportsRequest(
                )

                # Make the request
                response = await client.batch_run_pivot_reports(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.BatchRunPivotReportsRequest, dict]]):
                The request object. The batch request containing multiple
                pivot report requests.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1beta.types.BatchRunPivotReportsResponse:
                The batch response containing
                multiple pivot reports.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.BatchRunPivotReportsRequest):
            request = analytics_data_api.BatchRunPivotReportsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.batch_run_pivot_reports
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
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

    async def get_metadata(
        self,
        request: Optional[Union[analytics_data_api.GetMetadataRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.Metadata:
        r"""Returns metadata for dimensions and metrics available in
        reporting methods. Used to explore the dimensions and metrics.
        In this method, a Google Analytics property identifier is
        specified in the request, and the metadata response includes
        Custom dimensions and metrics as well as Universal metadata.

        For example if a custom metric with parameter name
        ``levels_unlocked`` is registered to a property, the Metadata
        response will contain ``customEvent:levels_unlocked``. Universal
        metadata are dimensions and metrics applicable to any property
        such as ``country`` and ``totalUsers``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_get_metadata():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.GetMetadataRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_metadata(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.GetMetadataRequest, dict]]):
                The request object. Request for a property's dimension
                and metric metadata.
            name (:class:`str`):
                Required. The resource name of the metadata to retrieve.
                This name field is specified in the URL path and not URL
                parameters. Property is a numeric Google Analytics
                property identifier. To learn more, see `where to find
                your Property
                ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.

                Example: properties/1234/metadata

                Set the Property ID to 0 for dimensions and metrics
                common to all properties. In this special mode, this
                method will not return custom dimensions and metrics.

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
            google.analytics.data_v1beta.types.Metadata:
                The dimensions, metrics and
                comparisons currently accepted in
                reporting methods.

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
        if not isinstance(request, analytics_data_api.GetMetadataRequest):
            request = analytics_data_api.GetMetadataRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_metadata
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

    async def run_realtime_report(
        self,
        request: Optional[
            Union[analytics_data_api.RunRealtimeReportRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RunRealtimeReportResponse:
        r"""Returns a customized report of realtime event data for your
        property. Events appear in realtime reports seconds after they
        have been sent to the Google Analytics. Realtime reports show
        events and usage data for the periods of time ranging from the
        present moment to 30 minutes ago (up to 60 minutes for Google
        Analytics 360 properties).

        For a guide to constructing realtime requests & understanding
        responses, see `Creating a Realtime
        Report <https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-basics>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_run_realtime_report():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.RunRealtimeReportRequest(
                )

                # Make the request
                response = await client.run_realtime_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.RunRealtimeReportRequest, dict]]):
                The request object. The request to generate a realtime
                report.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1beta.types.RunRealtimeReportResponse:
                The response realtime report table
                corresponding to a request.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.RunRealtimeReportRequest):
            request = analytics_data_api.RunRealtimeReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_realtime_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
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

    async def check_compatibility(
        self,
        request: Optional[
            Union[analytics_data_api.CheckCompatibilityRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.CheckCompatibilityResponse:
        r"""This compatibility method lists dimensions and
        metrics that can be added to a report request and
        maintain compatibility. This method fails if the
        request's dimensions and metrics are incompatible.

        In Google Analytics, reports fail if they request
        incompatible dimensions and/or metrics; in that case,
        you will need to remove dimensions and/or metrics from
        the incompatible report until the report is compatible.

        The Realtime and Core reports have different
        compatibility rules. This method checks compatibility
        for Core reports.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_check_compatibility():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.CheckCompatibilityRequest(
                )

                # Make the request
                response = await client.check_compatibility(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.CheckCompatibilityRequest, dict]]):
                The request object. The request for compatibility information for a report's
                dimensions and metrics. Check compatibility provides a
                preview of the compatibility of a report; fields shared
                with the ``runReport`` request should be the same values
                as in your ``runReport`` request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1beta.types.CheckCompatibilityResponse:
                The compatibility response with the
                compatibility of each dimension &
                metric.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.CheckCompatibilityRequest):
            request = analytics_data_api.CheckCompatibilityRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.check_compatibility
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
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

    async def create_audience_export(
        self,
        request: Optional[
            Union[analytics_data_api.CreateAudienceExportRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        audience_export: Optional[analytics_data_api.AudienceExport] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates an audience export for later retrieval. This method
        quickly returns the audience export's resource name and
        initiates a long running asynchronous request to form an
        audience export. To export the users in an audience export,
        first create the audience export through this method and then
        send the audience resource name to the ``QueryAudienceExport``
        method.

        See `Creating an Audience
        Export <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Exports with examples.

        An audience export is a snapshot of the users currently in the
        audience at the time of audience export creation. Creating
        audience exports for one audience on different days will return
        different results as users enter and exit the audience.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.
        Audience exports contain the users in each audience.

        Audience Export APIs have some methods at alpha and other
        methods at beta stability. The intention is to advance methods
        to beta stability after some feedback and adoption. To give your
        feedback on this API, complete the `Google Analytics Audience
        Export API Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__
        form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_create_audience_export():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                audience_export = data_v1beta.AudienceExport()
                audience_export.audience = "audience_value"

                request = data_v1beta.CreateAudienceExportRequest(
                    parent="parent_value",
                    audience_export=audience_export,
                )

                # Make the request
                operation = await client.create_audience_export(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.CreateAudienceExportRequest, dict]]):
                The request object. A request to create a new audience
                export.
            parent (:class:`str`):
                Required. The parent resource where this audience export
                will be created. Format: ``properties/{property}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audience_export (:class:`google.analytics.data_v1beta.types.AudienceExport`):
                Required. The audience export to
                create.

                This corresponds to the ``audience_export`` field
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

                The result type for the operation will be :class:`google.analytics.data_v1beta.types.AudienceExport` An audience export is a list of users in an audience at the time of the
                   list's creation. One audience may have multiple
                   audience exports created for different days.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, audience_export]
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
        if not isinstance(request, analytics_data_api.CreateAudienceExportRequest):
            request = analytics_data_api.CreateAudienceExportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if audience_export is not None:
            request.audience_export = audience_export

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_audience_export
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
            analytics_data_api.AudienceExport,
            metadata_type=analytics_data_api.AudienceExportMetadata,
        )

        # Done; return the response.
        return response

    async def query_audience_export(
        self,
        request: Optional[
            Union[analytics_data_api.QueryAudienceExportRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.QueryAudienceExportResponse:
        r"""Retrieves an audience export of users. After creating an
        audience, the users are not immediately available for exporting.
        First, a request to ``CreateAudienceExport`` is necessary to
        create an audience export of users, and then second, this method
        is used to retrieve the users in the audience export.

        See `Creating an Audience
        Export <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Exports with examples.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.

        Audience Export APIs have some methods at alpha and other
        methods at beta stability. The intention is to advance methods
        to beta stability after some feedback and adoption. To give your
        feedback on this API, complete the `Google Analytics Audience
        Export API Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__
        form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_query_audience_export():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.QueryAudienceExportRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.query_audience_export(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.QueryAudienceExportRequest, dict]]):
                The request object. A request to list users in an
                audience export.
            name (:class:`str`):
                Required. The name of the audience export to retrieve
                users from. Format:
                ``properties/{property}/audienceExports/{audience_export}``

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
            google.analytics.data_v1beta.types.QueryAudienceExportResponse:
                A list of users in an audience
                export.

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
        if not isinstance(request, analytics_data_api.QueryAudienceExportRequest):
            request = analytics_data_api.QueryAudienceExportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.query_audience_export
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

    async def get_audience_export(
        self,
        request: Optional[
            Union[analytics_data_api.GetAudienceExportRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.AudienceExport:
        r"""Gets configuration metadata about a specific audience export.
        This method can be used to understand an audience export after
        it has been created.

        See `Creating an Audience
        Export <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Exports with examples.

        Audience Export APIs have some methods at alpha and other
        methods at beta stability. The intention is to advance methods
        to beta stability after some feedback and adoption. To give your
        feedback on this API, complete the `Google Analytics Audience
        Export API Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__
        form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_get_audience_export():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.GetAudienceExportRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_audience_export(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.GetAudienceExportRequest, dict]]):
                The request object. A request to retrieve configuration
                metadata about a specific audience
                export.
            name (:class:`str`):
                Required. The audience export resource name. Format:
                ``properties/{property}/audienceExports/{audience_export}``

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
            google.analytics.data_v1beta.types.AudienceExport:
                An audience export is a list of users
                in an audience at the time of the list's
                creation. One audience may have multiple
                audience exports created for different
                days.

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
        if not isinstance(request, analytics_data_api.GetAudienceExportRequest):
            request = analytics_data_api.GetAudienceExportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_audience_export
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

    async def list_audience_exports(
        self,
        request: Optional[
            Union[analytics_data_api.ListAudienceExportsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAudienceExportsAsyncPager:
        r"""Lists all audience exports for a property. This method can be
        used for you to find and reuse existing audience exports rather
        than creating unnecessary new audience exports. The same
        audience can have multiple audience exports that represent the
        export of users that were in an audience on different days.

        See `Creating an Audience
        Export <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Exports with examples.

        Audience Export APIs have some methods at alpha and other
        methods at beta stability. The intention is to advance methods
        to beta stability after some feedback and adoption. To give your
        feedback on this API, complete the `Google Analytics Audience
        Export API Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__
        form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1beta

            async def sample_list_audience_exports():
                # Create a client
                client = data_v1beta.BetaAnalyticsDataAsyncClient()

                # Initialize request argument(s)
                request = data_v1beta.ListAudienceExportsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_audience_exports(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.analytics.data_v1beta.types.ListAudienceExportsRequest, dict]]):
                The request object. A request to list all audience
                exports for a property.
            parent (:class:`str`):
                Required. All audience exports for this property will be
                listed in the response. Format:
                ``properties/{property}``

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
            google.analytics.data_v1beta.services.beta_analytics_data.pagers.ListAudienceExportsAsyncPager:
                A list of all audience exports for a
                property.
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
        if not isinstance(request, analytics_data_api.ListAudienceExportsRequest):
            request = analytics_data_api.ListAudienceExportsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_audience_exports
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
        response = pagers.ListAudienceExportsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "BetaAnalyticsDataAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("BetaAnalyticsDataAsyncClient",)
